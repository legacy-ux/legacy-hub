# Legacy Hub Roadmap

## Delivery approach

Legacy Hub will be built in small, dependable increments. A workflow must work manually with clear ownership and records before it is automated or given broader system access.

## Phases

| Phase | Objective | Key deliverables | Exit criteria |
| --- | --- | --- | --- |
| **0. Foundation** | Establish shared operating model and documentation | This documentation set, terminology, system ownership, initial data model | Core decisions are documented and approved |
| **1. Manual pilot** | Prove the smallest high-value workflows | Intake, consultation capture, follow-ups, red flags, Drive/Airtable linking | Users complete pilot work consistently without lost context |
| **2. Quote foundation** | Make quote/proposal preparation repeatable | Customer/property verification, proposal readiness, Jobber Quote Agent draft flow | Draft quotes are accurate, traceable, and approval-controlled |
| **3. Project delivery** | Improve job handoff and closeout | Deposit-to-project setup, readiness, daily capture, final walkthrough/warranty | Jobs have visible readiness and complete closeout records |
| **4. Account management** | Manage customers and properties by exception | Evaluations, opportunity reports, maintenance visibility, customer-for-life follow-up | Account manager can prioritize work from a dashboard |
| **5. Intelligence and scale** | Add controlled analytical capability | Plant-library completeness, reporting, cost/profit insights, controlled financial intelligence | Quality, permissions, and review controls are proven |
| **6. Platform evolution** | Upgrade the interface only when justified | Evaluate custom application or alternative interface | Migration decision is supported by measured need |

## Near-term priorities

1. Approve the foundational documentation and terminology.
2. Define the Airtable pilot tables, fields, views, and interfaces.
3. Build and test the quote/proposal draft workflow before expanding integrations.
4. Define invoice routing separately from quote work.
5. Establish Drive folder conventions and file-linking rules.
6. Add automation only for a workflow that is manually stable.

## Planned milestones

| Milestone | Definition of done | Target date |
| --- | --- | --- |
| Documentation baseline approved | All seven documentation files reviewed and accepted | TBD |
| Airtable pilot live | Core pilot tables and role views usable | TBD |
| Quote draft pilot complete | Test quote drafts created and reviewed end to end | TBD |
| Project readiness pilot complete | Pre-start checklist and red flags tested on live work | TBD |
| Account manager evaluation pilot | Evaluation input produces internal and customer-ready reports | TBD |

## Decision gates

- Do not automate external writes until the manual workflow is stable and approved.
- Do not allow an agent to send customer communications without the specified human approval path.
- Do not expand financial access until a role/permission model and review process exist.
- Do not replace Airtable Interfaces with a custom application until measured workflow limits justify it.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Overbuilding before users adopt the process | Deliver one workflow at a time and validate manually |
| Duplicate customer/property data | Require verification before record creation |
| AI output treated as final without review | Draft-first policy and clear approver fields |
| Knowledge scattered across tools | Drive-first artifact storage with Airtable links and ownership rules |
| Automation failures hidden from users | Visible exceptions, retries, and reconciliation rules |

## Deferred decisions

- Custom application timing and technology
- Full financial-system integration
- Commercial/HOA-specific workflow expansion
- Advanced reporting and forecasting
- Formal agent evaluation suite and production release process
