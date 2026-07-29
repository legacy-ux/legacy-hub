# Legacy Hub Foundation

## Purpose

Legacy Hub is the AI operating system for All Landscape. It gives every employee a role-focused AI Director that understands their work, helps with daily decisions, and coordinates specialist capabilities while preserving structured business data.

Its job is to make the right information available to the right person at the right time—without replacing human judgment, customer relationships, or required approvals.

## Founding principles

### 1. One seat = one Director

Every business seat has exactly one Director. Employees communicate with their Director; the Director is the front door.

Initial seats include Owner, Design / Sales, Account Manager, and Crew Leader. Final seat coverage is **TBD**.

### 2. Directors own the business workflow

Directors coordinate business decisions, workflow, customer communication, tasks, scheduling, quotes, invoices, connected applications, and specialist delegation for their seat. They retain the complete workflow context and follow the approval rules defined for that workflow.

### 3. Specialist Agents provide shared expertise

Specialists do not own a business seat or communicate directly with employees. They provide narrow, reusable expertise and return structured results to the requesting Director. Any authorized Director may use an approved specialist.

### 4. Airtable is the structured-data source of truth

Customers, properties, tasks, workflow status, quotes, evaluations, plant-library records, and dashboard data are managed as structured Airtable records. Where Jobber is required for a customer-facing transaction, Legacy records the linked Jobber reference and transaction status in Airtable.

### 5. Google Drive stores company files

Google Drive stores photos, designs, documents, contracts, reports, mood boards, and other durable artifacts. Airtable stores the links and metadata that make those files usable in the workflow.

### 6. Directors use approved connected apps

Directors use approved connected applications directly, initially including Airtable, Google Drive, Gmail, and Google Calendar. Exact permissions are defined by role and workflow.

### 7. Make and Jobber are external systems

Make coordinates approved Jobber synchronization and other repeatable external-system work. Business policy stays in Legacy; Make executes defined scenarios. Jobber remains the customer-facing system for its supported transactions.

### 8. Every workflow produces structured data

Free-form conversation is for people. Legacy Directors and Agents exchange structured records, links, statuses, and results so work remains traceable and reusable.

### 9. Simplicity first

Legacy must remain understandable. Build the smallest dependable workflow first, validate it manually, and expand only when the value and ownership are clear.

## Product principles

1. **Capture once, use many times.** Photos, voice notes, documents, and decisions are saved before they are interpreted or routed.
2. **Systems have clear ownership.** Google Drive is the company knowledge vault; Airtable is the data, workflow, and attention layer; Jobber is the customer-facing transaction system.
3. **Draft first; approve before external action.** Customer communications, proposals, transactions, and financial actions stay in draft or review status until an authorized person approves them.
4. **The dashboard shows attention; the workspace tells the full story.** Users should see what needs action without losing access to the underlying customer, property, project, and history.
5. **Use specialists with limited scope.** Directors route and oversee work; specialist agents perform bounded tasks with the minimum permissions required.
6. **Keep tools replaceable.** Legacy owns the process, data model, and knowledge structure. AI models and supporting tools may change without changing the operating model.
7. **Build the smallest dependable version first.** Validate a workflow manually before automating or expanding it.

## Core business outcomes

- Faster, more complete capture after consultations, site visits, and crew activity.
- More accurate and consistent proposals, customer follow-up, and project handoffs.
- Clear visibility into approvals, deposits, scheduling, job readiness, red flags, and warranty obligations.
- A durable company memory for plant knowledge, property history, customer preferences, and operating decisions.
- Better owner visibility into sales, production, maintenance, financial performance, and opportunities.

## Scope

### In scope

- Customer and property information routing
- Sales, design, quote, proposal, and invoice workflows
- Project delivery, maintenance, warranty, and customer-for-life workflows
- Plant library and property knowledge management
- Dashboards, red flags, tasks, reports, and approved automations

### Out of scope for the initial release

- Replacing Jobber as the system of record for customer-facing quotes, approvals, scheduling, and invoices
- Fully autonomous customer or financial actions
- A custom application before Airtable Interfaces no longer meet the operational need

## Product vocabulary

| Term | Meaning |
| --- | --- |
| **Legacy Hub** | The overall business operating system and its documented processes. |
| **Director** | A role-focused coordinator that receives requests, applies policy, and routes approved work to specialists. |
| **Agent** | A bounded specialist that performs a defined task and returns structured results. |
| **Workspace** | The detailed operational view for a customer, property, project, or work area. |
| **Dashboard** | A role-specific attention view showing priorities, exceptions, and next actions. |
| **Red flag** | A condition requiring visibility, ownership, and resolution tracking. |
| **System of record** | The authoritative system for a particular kind of data or transaction. |

## Success measures

| Measure | Initial target | Owner |
| --- | --- | --- |
| Consultation capture completeness | TBD | Sales / Design Director |
| Proposal first-pass accuracy | TBD | Quote Agent |
| Time from consultation to proposal-ready package | TBD | Sales / Design Director |
| Jobs started with material/readiness issues | TBD | Operations Director |
| Follow-ups completed on time | TBD | Account Manager Director |
| Missing plant-library assets by gallon size | TBD | Plant Library Builder |

## Assumptions and open decisions

- **Primary interface:** Airtable Interfaces for Legacy 1.0; reassess when requirements exceed its capabilities.
- **Automation layer:** Make is the planned repeatable-workflow coordinator. Exact scenario inventory is TBD.
- **Initial rollout:** Manual/assisted workflows are validated before broad integrations and automation.
- **Identity and access model:** TBD.
- **Retention, backup, and disaster recovery policy:** TBD.

## Related documents

- [Architecture](ARCHITECTURE.md)
- [Directors](DIRECTORS.md)
- [Agents](AGENTS.md)
- [Data model](DATA_MODEL.md)
- [Workflows](WORKFLOWS.md)
- [Roadmap](ROADMAP.md)
