# Legacy Hub Foundation

## Purpose

Legacy Hub is the operating model for All Landscape. It gives each employee one AI Director for the employee's business seat, keeping work, decisions, communication, and structured records together.

The Director helps the employee complete work; it does not replace required human approvals, customer relationships, or business judgment.

## Legacy v1 — authoritative scope

This section is the source of truth for the first production release. A capability is not Legacy v1 unless it is listed here.

### Included Directors

1. Owner Director
2. Design & Sales Director
3. Account Manager Director
4. Crew Leader Director

Each employee business seat has exactly one Director. There is no central or super Director. Directors may coordinate with one another when work crosses seats, but an employee works only with the Director assigned to that employee's seat.

### Included Specialist Agents

- Plant Library Agent
- Research Agent
- Design Agent
- Financial Analysis Agent

Specialist Agents are shared, bounded services. They never communicate directly with employees, own a customer, own a workflow, or make the next business decision. They return structured results to the requesting Director.

### Included workflows

- New Customer Intake
- Existing Customer Lookup
- Property Management
- Proposal Workflow
- Customer Communication
- Scheduling
- Daily Crew Management
- Property Evaluation
- Plant Library Management

### Deferred functionality

- Additional Directors, including any Operations or Financial Intelligence Director
- A separate AI Director or central routing Director
- Email, quote, invoice, website, maintenance-intelligence, or other specialist agents not listed above
- Fully autonomous customer-facing, financial, or irreversible actions
- Custom application development beyond Airtable Interfaces
- Expanded commercial, HOA, advanced reporting, forecasting, and full financial-system workflows

Deferred items belong in **Future Releases** and must not be assumed available in Legacy v1.

## Founding principles

### 1. One business seat, one Director

Every employee has one Director, their front door for work. Directors own the complete workflow for their assigned seat.

### 2. Directors do the work and own the outcome

Directors work directly in Airtable, Google Drive, Gmail, and Google Calendar. They are responsible for customer communication, scheduling and calendar management, task management, role-appropriate business decisions, Airtable updates, Drive organization, and specialist coordination.

### 3. Specialists are shared expertise, not employees' assistants

Directors use a Specialist Agent only when reusable, bounded expertise is needed. The Director interprets the result, updates the record, communicates the outcome, and completes the workflow.

### 4. Airtable is the structured-data source of truth

All structured Legacy business information lives in Airtable. Google Drive stores files; Airtable stores the files' links and metadata. Jobber holds customer-facing transaction records where Jobber must perform the transaction, while Airtable remains the operational context and synchronization record.

### 5. Make has a narrow synchronization role

Make synchronizes approved structured Airtable data with Jobber. It does not own business logic, make business decisions, route Directors, or communicate with employees or customers.

### 6. Draft first and preserve accountability

Customer-facing, financial, and irreversible actions remain draft or review work until an authorized person approves them. The responsible Director records the owner, decision, source, timestamps, and outcome in Airtable.

### 7. Simplicity first

Build the smallest dependable workflow, prove it manually, then automate only the defined Airtable-to-Jobber synchronization that adds value.

## Product vocabulary

| Term | Meaning |
| --- | --- |
| **Legacy Hub** | The documented All Landscape operating model, its Airtable data/workflow layer, and its Director experiences. |
| **Business seat** | An employee role with one assigned Director and defined workflow ownership. |
| **Director** | The employee's front door and owner of the complete workflow for one business seat. |
| **Specialist Agent** | A shared, bounded service that returns structured expertise to a requesting Director. |
| **System of record** | The authoritative system for a specified record or artifact, defined in the ownership matrix. |
| **Task** | An Airtable record that assigns a next action and tracks its completion. |
| **Red flag** | An Airtable exception record requiring an owner and resolution. |

## Related documents

- [Architecture](ARCHITECTURE.md)
- [Directors](DIRECTORS.md)
- [Specialist Agents](AGENTS.md)
- [Data model and ownership matrix](DATA_MODEL.md)
- [Workflows](WORKFLOWS.md)
- [Roadmap](ROADMAP.md)
