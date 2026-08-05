# Legacy Hub Roadmap

## Legacy v1 release objective

Legacy v1 freezes the first production scope defined in [FOUNDATION.md](FOUNDATION.md): four seat-based Directors, four shared Specialist Agents, nine included workflows, Airtable as the structured-data source of truth, Google Drive for files, and Make-only Airtable-to-Jobber synchronization.

## Delivery order

| Phase | Objective | Exit criteria |
| --- | --- | --- |
| 0. Documentation baseline | Approve the authoritative v1 model and ownership matrix | No conflicting Director, specialist, system-ownership, or workflow descriptions remain |
| 1. Airtable foundation | Build the v1 entities, fields, links, task/red-flag patterns, and seat views | Directors can record and find v1 work in Airtable |
| 2. Director workflows | Manually validate the included workflows by seat | Each workflow has accountable ownership, clear handoffs, and no lost context |
| 3. Drive and communication discipline | Apply file linking and Gmail/Calendar recordkeeping | Files and material communication are traceable from Airtable |
| 4. Make–Jobber synchronization | Implement only approved field/status mappings | Mapped sync is tested, reconciled, and creates visible exceptions on failure |
| 5. Controlled specialist support | Add the four v1 agents after their request/result contracts are tested | Agents return useful structured results without taking workflow ownership |

## Future Releases

- Additional Directors, including Operations and Financial Intelligence Directors
- Additional specialist agents, including email, quote, invoice, website, maintenance-intelligence, and photo-library agents
- Invoice, deposit-to-project, material-readiness, final-walkthrough, warranty, customer-for-life, maintenance-intelligence, and advanced financial workflows
- Commercial/HOA expansion, advanced reporting/forecasting, and custom application evaluation

## Decision gates

- Do not add a Director or Specialist Agent without updating the authoritative v1/future-release scope.
- Do not automate a workflow until its manual version and Airtable ownership are stable.
- Do not put business logic, decisions, routing, or communication inside Make.
- Do not authorize unreviewed customer-facing or financial actions.

## Open decisions

- Airtable field/view/interface specifications: **TBD**
- Make–Jobber mapping inventory and reconciliation frequency: **TBD**
- Director permission and approval matrix: **TBD**
- Drive folder naming and retention policy: **TBD**
