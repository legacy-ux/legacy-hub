# Legacy Hub Foundation

## Purpose

Legacy Hub is the AI operating system for All Landscape. It gives every employee one role-focused AI Director that understands the employee's seat, manages its complete workflow, and uses shared expertise when needed.

Its job is to make the right information available to the right person at the right time—without replacing human judgment, customer relationships, or required approvals.

## Founding principles

### 1. One employee seat = one Director

Legacy Hub is organized around business seats. Every employee has exactly one AI Director. That Director is the employee's front door for requests, information, and work.

Initial seats include Owner, Sales & Design, Account Management, and Crew Leadership. Final employee-to-seat assignments and backup coverage are **TBD**.

### 2. Directors own the complete seat workflow

The Director remains accountable for its seat's customer relationships, communication, scheduling, calendar, tasks, role-specific decisions, Airtable updates, Google Drive organization, and specialist coordination. Directors perform work directly whenever possible; a Specialist Agent is added only when distinct shared expertise is genuinely required.

### 3. Specialist Agents are shared services

Specialist Agents provide narrow, reusable expertise to a requesting Director. They never communicate directly with employees, own a workflow, or own a customer. They return structured results to the requesting Director, which decides and completes the next business action.

### 4. Airtable is the structured-data source of truth

All structured business information lives in Airtable: customers, properties, tasks, workflow status, quotes, evaluations, plant-library records, decisions, red flags, and dashboard data. Airtable also holds references and metadata for related Google Drive files and Jobber records.

### 5. Google Drive stores company files

Google Drive stores photos, designs, documents, contracts, reports, mood boards, voice files, and other durable artifacts. Airtable stores the links and metadata that make those files usable in the workflow.

### 6. Directors use the connected applications directly

Every Director has direct access to Airtable, Google Drive, Gmail, and Google Calendar. Their specific actions remain governed by role permissions and workflow approval rules.

### 7. Make and Jobber are the only external systems

Make has one purpose: synchronize defined structured Airtable data with Jobber. It contains no business logic, makes no decisions, does not communicate with employees or customers, and does not own workflows. Jobber is the external service system receiving and providing the synchronized data.

### 8. Every workflow produces structured data

Free-form conversation is for people. Directors and Specialist Agents exchange structured records, links, statuses, and results so work remains traceable and reusable.

### 9. Simplicity first

Legacy must remain understandable. Build the smallest dependable workflow first, validate it manually, and expand only when the value, ownership, and need for specialized expertise are clear.

## Product principles

1. **Capture once, use many times.** Photos, voice notes, documents, and decisions are saved before they are interpreted or routed.
2. **Systems have clear ownership.** Airtable is the structured-data source of truth; Google Drive is file storage; Make only synchronizes Airtable data with Jobber.
3. **Draft first; approve before external action.** Customer communications, proposals, transactions, and financial actions stay in draft or review status until an authorized person approves them.
4. **The dashboard shows attention; the workspace tells the full story.** Users should see what needs action without losing access to the underlying customer, property, project, and history.
5. **Use specialists with limited scope.** Directors route and oversee bounded specialist work while retaining workflow and customer accountability.
6. **Keep tools replaceable.** Legacy owns the process, Airtable data model, and knowledge structure. Supporting tools may change without changing the operating model.
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
- Dashboards, red flags, tasks, reports, and approved Airtable-to-Jobber synchronization

### Out of scope for the initial release

- Fully autonomous customer or financial actions
- Business logic inside Make
- A custom application before Airtable Interfaces no longer meet the operational need

## Product vocabulary

| Term | Meaning |
| --- | --- |
| **Legacy Hub** | The overall business operating system and its documented processes. |
| **Business seat** | The defined work role held by one employee and served by one Director. |
| **Director** | The AI front door for one employee seat. It owns the seat workflow, makes role-appropriate decisions, and coordinates specialist work. |
| **Specialist Agent** | A shared, bounded service that returns structured results to a requesting Director. |
| **Workspace** | The detailed operational view for a customer, property, project, or work area. |
| **Dashboard** | A role-specific attention view showing priorities, exceptions, and next actions. |
| **Red flag** | A condition requiring visibility, ownership, and resolution tracking. |
| **System of record** | The authoritative system for a defined kind of data; Airtable is the structured business-data source of truth. |

## Success measures

| Measure | Initial target | Owner |
| --- | --- | --- |
| Consultation capture completeness | TBD | Sales & Design Director |
| Proposal first-pass accuracy | TBD | Sales & Design Director |
| Time from consultation to proposal-ready package | TBD | Sales & Design Director |
| Jobs started with material/readiness issues | TBD | Operations Director |
| Follow-ups completed on time | TBD | Account Manager Director |
| Missing plant-library assets by gallon size | TBD | Plant Library Agent |

## Assumptions and open decisions

- **Primary interface:** Airtable Interfaces for Legacy 1.0; reassess when requirements exceed its capabilities.
- **Synchronization layer:** Make synchronizes only the approved Airtable and Jobber fields. Exact field contract is TBD.
- **Initial rollout:** Manual/assisted workflows are validated before broad synchronization.
- **Identity and access model:** TBD.
- **Retention, backup, and disaster recovery policy:** TBD.

## Related documents

- [Architecture](ARCHITECTURE.md)
- [Directors](DIRECTORS.md)
- [Agents](AGENTS.md)
- [Data model](DATA_MODEL.md)
- [Workflows](WORKFLOWS.md)
- [Roadmap](ROADMAP.md)
