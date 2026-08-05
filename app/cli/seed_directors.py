from app.db import SessionLocal
from app.registries.directors import sync_director_registry


def main() -> None:
    with SessionLocal() as session:
        directors = sync_director_registry(session)
    print(f"Director Registry synchronized: {len(directors)} seats")


if __name__ == "__main__":
    main()
