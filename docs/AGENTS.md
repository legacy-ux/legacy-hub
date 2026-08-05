# Legacy Hub Specialist Agents

## Legacy v1 Specialist Agents

Specialist Agents are shared, reusable services for Directors. They never communicate directly with employees, own a workflow, own a customer, or make the next business decision.

Directors perform work directly whenever possible. A Specialist Agent exists only when a bounded, reusable expertise improves the work across one or more business seats.

| Specialist Agent | Bounded purpose | Structured result to requesting Director |
| --- | --- | --- |
| **Plant Library Agent** | Build and maintain plant-by-gallon-size knowledge and completeness records | Proposed Airtable updates, source links, completeness status, missing-asset list, and review flags |
| **Research Agent** | Gather and summarize approved research for an operational, design, or business question | Cited research brief, findings, limitations, and recommendations |
| **Design Agent** | Produce design-support materials from approved property, scope, and preference context | Design concept, mood-board/plant-palette recommendations, asset links, assumptions, and review flags |
| **Financial Analysis Agent** | Analyze approved financial data for visibility and decision support | Analysis, source period, assumptions, risks, and recommendations; never a financial action |

## Request contract

A Director's request must include the Airtable record or request ID, applicable Drive links, desired outcome, constraints, and approval context. The specialist returns only the defined result and identifies missing information, red flags, and any required review.

| Field | Description |
| --- | --- |
| `request_id` | Linked Airtable record or unique request ID |
| `status` | `complete`, `needs_review`, `blocked`, or `failed` |
| `summary` | Concise result for the Director |
| `outputs` | Links/IDs for proposed records, files, drafts, or recommendations |
| `sources` | Source links and citations used |
| `missing_information` | Gaps preventing a reliable result |
| `red_flags` | Risks or exceptions requiring visibility |
| `approval_required` | Whether the Director must seek human approval before the next action |
| `next_owner` | The requesting Director or an explicitly named human role; never the Specialist Agent |

## Boundaries

| Specialist Agent | Must not do |
| --- | --- |
| Plant Library Agent | Publish unverified plant guidance as approved or overwrite approved records without review |
| Research Agent | Make commitments or present research as a final business decision |
| Design Agent | Communicate directly with employees/customers, approve scope/pricing, or own proposal workflow |
| Financial Analysis Agent | Access unapproved financial data, initiate transactions, or make financial decisions |

The Design Email Agent and Jobber Quote Agent are not Legacy v1 agents. Their former responsibilities belong to the appropriate Director, primarily the Design & Sales Director, using the normal proposal and customer-communication workflows.

## Future Releases

Any additional specialist—such as an Invoice, Website Content, Maintenance Intelligence, or Photo Library Agent—requires a defined repeatable service, permission boundary, structured result, and approved addition to Legacy v1 scope or a future-release plan.

## Open decisions

- Specialist runtime/platform selection: **TBD**
- Evaluation thresholds and release process: **TBD**
- Per-agent permission grants: **TBD**
