import os
from datetime import datetime, timedelta, timezone

import jwt
import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, inspect, text


DATABASE_URL = os.getenv("DATABASE_URL")
AUTH_SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
pytestmark = pytest.mark.skipif(
    not DATABASE_URL or not AUTH_SECRET_KEY,
    reason="PostgreSQL integration environment is not configured.",
)


def _token(director: str, *, subject: str, human: bool = True) -> str:
    assert AUTH_SECRET_KEY is not None
    now = datetime.now(timezone.utc)
    return jwt.encode(
        {
            "sub": subject,
            "director": director,
            "human": human,
            "iat": now,
            "exp": now + timedelta(minutes=10),
            "iss": "legacy-hub",
            "aud": "legacy-hub-api",
        },
        AUTH_SECRET_KEY,
        algorithm="HS256",
    )


def _headers(director: str, *, subject: str, human: bool = True) -> dict[str, str]:
    return {"Authorization": f"Bearer {_token(director, subject=subject, human=human)}"}


@pytest.fixture(scope="module")
def migrated_database():
    assert DATABASE_URL is not None
    config = Config("alembic.ini")
    command.downgrade(config, "base")
    command.upgrade(config, "head")

    engine = create_engine(DATABASE_URL)
    expected_tables = {
        "alembic_version",
        "approvals",
        "audits",
        "directors",
        "messages",
        "specialists",
        "tasks",
    }
    assert expected_tables <= set(inspect(engine).get_table_names())
    yield engine

    command.downgrade(config, "base")
    assert not (expected_tables - {"alembic_version"}) & set(inspect(engine).get_table_names())
    command.upgrade(config, "head")
    engine.dispose()


def test_complete_legacy_hub_workflow(migrated_database) -> None:
    from app.main import app

    owner_headers = _headers("owner", subject="lu-owner")
    crew_headers = _headers("crew_leader", subject="crew-reviewer")

    with TestClient(app) as client:
        assert client.get("/").json()["status"] == "running"
        assert client.get("/health").json() == {
            "status": "healthy",
            "service": "legacy-hub",
        }
        assert client.get("/api/v1/directors").status_code == 401

        sync = client.post("/api/v1/directors/actions/sync", headers=owner_headers)
        assert sync.status_code == 200, sync.text
        directors = sync.json()
        assert {director["key"] for director in directors} == {
            "owner",
            "design_sales",
            "account_manager",
            "crew_leader",
        }
        owner_id = next(item["id"] for item in directors if item["key"] == "owner")

        task_response = client.post(
            "/api/v1/tasks",
            headers=owner_headers,
            json={
                "director_id": owner_id,
                "title": "PostgreSQL integration workflow",
                "description": "Verify the secured Legacy Hub workflow end to end.",
                "priority": "high",
            },
        )
        assert task_response.status_code == 201, task_response.text
        task = task_response.json()
        task_id = task["id"]
        assert task["status"] == "pending"

        transition = client.post(
            f"/api/v1/tasks/{task_id}/actions/transition",
            headers=owner_headers,
            json={"status": "in_progress"},
        )
        assert transition.status_code == 200, transition.text
        assert transition.json()["status"] == "in_progress"

        message_response = client.post(
            f"/api/v1/messages/tasks/{task_id}",
            headers=owner_headers,
            json={
                "director_id": owner_id,
                "direction": "internal",
                "content": "Integration workflow reached the approval gate.",
                "channel": "legacy_hub",
            },
        )
        assert message_response.status_code == 201, message_response.text

        approval_response = client.post(
            f"/api/v1/approvals/tasks/{task_id}",
            headers=owner_headers,
            json={
                "director_id": owner_id,
                "action": "owner.override",
                "request_details": "Integration test decision gate.",
            },
        )
        assert approval_response.status_code == 201, approval_response.text
        approval_id = approval_response.json()["id"]

        forbidden = client.post(
            f"/api/v1/approvals/{approval_id}/actions/decide",
            headers=crew_headers,
            json={"status": "approved", "decision_notes": "Must be rejected."},
        )
        assert forbidden.status_code == 403

        decision = client.post(
            f"/api/v1/approvals/{approval_id}/actions/decide",
            headers=owner_headers,
            json={"status": "approved", "decision_notes": "Verified by integration test."},
        )
        assert decision.status_code == 200, decision.text
        assert decision.json()["reviewed_by"] == "lu-owner"

        completed = client.post(
            f"/api/v1/tasks/{task_id}/actions/transition",
            headers=owner_headers,
            json={"status": "completed"},
        )
        assert completed.status_code == 200, completed.text
        assert completed.json()["completed_at"] is not None

        audits = client.get(
            "/api/v1/audits",
            headers=owner_headers,
            params={"task_id": task_id},
        )
        assert audits.status_code == 200, audits.text
        assert {item["event_type"] for item in audits.json()} >= {
            "message.created",
            "approval.requested",
            "approval.decided",
        }

    with migrated_database.connect() as connection:
        assert connection.execute(text("select count(*) from directors")).scalar_one() == 4
        assert connection.execute(text("select count(*) from tasks")).scalar_one() == 1
        assert connection.execute(text("select count(*) from messages")).scalar_one() == 1
        assert connection.execute(text("select count(*) from approvals")).scalar_one() == 1
        assert connection.execute(text("select count(*) from audits")).scalar_one() == 3
