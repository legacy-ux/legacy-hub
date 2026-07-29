# Legacy Hub Data Model

## Modeling principles

- Airtable is the source of truth for structured Legacy business information.
- Google Drive stores documents, photos, voice notes, designs, and other files; Airtable stores their links and metadata.
- Use one Airtable record per business entity and link records rather than duplicating information.
- Track owner, workflow state, source, timestamps, approval state, and external IDs for meaningful work.
- Make synchronizes only approved, mapped structured Airtable data with Jobber and records the synchronization outcome.

## System ownership matrix

| Information area | System of record | Airtable responsibility | Other-system responsibility | Synchronization responsibility |
| --- | --- | --- | --- | --- |
| Customers | **Airtable** | Authoritative customer record, ownership, workflow context, and linked Jobber ID | Jobber uses the mapped customer transaction record when required | Make creates/updates mapped Jobber data from approved Airtable fields and returns Jobber ID/status to Airtable |
| Properties | **Airtable** | Authoritative property profile, service knowledge, Drive links, and linked Jobber ID | Jobber uses mapped service-location data where required | Make synchronizes approved mapped property fields and reconciliation IDs/status |
| Contacts | **Airtable** | Authoritative contact, role, preferences, consent/communication context, and linked Jobber ID | Jobber receives mapped contacts for transactions | Make synchronizes approved contact fields and IDs/status |
| Tasks | **Airtable** | Authoritative assignment, due date, next action, and completion state | No separate task system in v1 | No Make synchronization unless explicitly added in a future release |
| Workflow state | **Airtable** | Authoritative stage, owner, approval state, red flags, and audit trail | Jobber transaction status is referenced, not the workflow owner | Make returns mapped Jobber transaction status; Director resolves conflicts in Airtable |
| Documents | **Google Drive** | Stores file link, category, owner, related record, and metadata | Drive stores the file and its native version history | No Make synchronization; Directors link Drive files in Airtable |
| Photos | **Google Drive** | Stores photo links, category, capture context, related record, and metadata | Drive stores the original asset | No Make synchronization; Directors link Drive photos in Airtable |
| Quotes | **Jobber for customer-facing quote transaction; Airtable for workflow context** | Proposal readiness, approval state, project relationship, Jobber quote ID, and transaction status | Jobber creates/holds the customer-facing quote and its transaction history | Make synchronizes only approved quote fields/statuses and returns IDs/statuses to Airtable |
| Scheduling | **Airtable for internal workflow schedule; Jobber for customer-facing scheduled transaction** | Assigned owner, readiness, internal dates, customer-notification state, and Jobber schedule ID/status | Jobber holds the customer-facing scheduled job/visit where used | Make synchronizes approved schedule fields/statuses; Director owns conflict resolution |
| Invoices | **Jobber for customer-facing invoice transaction; Airtable for workflow context** | Invoice request, approval state, linked Jobber invoice ID, status, and follow-up tasks | Jobber creates/holds the customer-facing invoice and payment history | Make synchronizes only approved invoice fields/statuses and returns IDs/statuses to Airtable |

## Core Airtable entities

| Entity | Purpose | Key relationships |
| --- | --- | --- |
| Customer | Business relationship and customer-level context | Has properties, contacts, opportunities, tasks, and Jobber reference |
| Property | Service location and property-specific history | Belongs to customer; has evaluations, projects, files, and schedule context |
| Contact | Person associated with a customer/property | Belongs to customer; may be decision maker or billing contact |
| Intake | New request and initial qualification | Resolves to existing customer/property or creates verified records |
| Opportunity / Project | Sales and delivery container for a service scope | Links consultation, proposal, tasks, files, schedule, and Jobber references |
| Proposal | Airtable workflow record for a quote/proposal | Links project, Design & Sales Director, Drive artifacts, approval, and Jobber quote ID |
| Schedule record | Internal readiness and scheduling context | Links project, crew, dates, customer-notification state, and Jobber schedule ID |
| Invoice request | Internal approval/follow-up record | Links project, customer, and Jobber invoice ID/status |
| Task | Assigned next action | Links to any entity and a responsible Director/human |
| Red flag | Exception requiring owner and resolution | Links to affected entity and workflow |
| File asset | Airtable metadata/reference for a Drive file | Links to Drive URL and business entities |
| Plant catalog item | One plant and gallon-size knowledge record | Links assets, research, completeness state, and approvals |
| Property evaluation | Structured inspection, scoring, and opportunity assessment | Belongs to property; links files, tasks, reports, and opportunities |

## Required common fields

| Field | Purpose |
| --- | --- |
| `legacy_id` | Stable Airtable/Legacy identifier |
| `jobber_id` | Linked Jobber identifier when applicable |
| `status` | Current workflow or entity state |
| `owner_director` | Director accountable for the next action |
| `source` | Originating person, system, or input |
| `approval_status` | Draft, pending review, approved, rejected, or not required |
| `drive_urls` | Links to the related Drive files/folders |
| `sync_status` / `synced_at` | Latest Make synchronization result and time |
| `created_at` / `updated_at` | Audit timestamps |

## Plant library minimum record

Each plant and gallon size is a separate Airtable record.

| Field group | Minimum fields |
| --- | --- |
| Identity | Botanical name, common name, gallon size, supplier item reference (TBD) |
| Knowledge | Approved description, care guidance, design uses, research status |
| Assets | Photo status, Drive links, care-guide status, document links |
| Completeness | Overall status, missing items, reviewer, last updated |

## Data integrity rules

- Verify existing customer and property records before creating a new record.
- A customer may have multiple properties and contacts; a property belongs to one customer at a time.
- A project may have multiple proposal revisions but identifies one current proposal.
- Tasks and red flags always have an owner and resolution state.
- Jobber IDs never replace the Airtable `legacy_id`; both are retained for traceability.
- Synchronization conflicts and failures are recorded in Airtable for the responsible Director.

## Controlled lists to define

- Service types: **TBD**
- Workflow and proposal statuses: **TBD**
- Red-flag categories/severity: **TBD**
- Approval roles/thresholds: **TBD**
- File categories and Drive folder naming: **TBD**
