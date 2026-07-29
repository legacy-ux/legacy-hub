# Legacy Hub Specialist Agents

## Purpose

Specialist agents perform narrowly defined work for a director or approved workflow. They use only the tools and data needed for that work, return structured results, and never assume authority to perform a customer-facing or financial action.

## Agent contract

Each agent definition must document:

- Purpose and bounded scope
- Permitted systems and data
- Required inputs
- Structured output
- Approval requirements
- Error, conflict, and missing-information behavior
- Recordkeeping location

## Current specialist roster

| Agent | Purpose | Permitted systems | Output | Status |
| --- | --- | --- | --- | --- |
| **Legacy Plant Library Builder** | Build and maintain plant/gallon-size knowledge records and asset completeness | Airtable, Google Drive, approved research sources | Plant record updates, missing-asset list, research draft | Planned |
| **Design Email Agent** | Draft design-related customer communications from approved context | Gmail/approved email workflow, Drive, Airtable | Draft email and review metadata | Planned |
| **Research Agent** | Gather and summarize approved research for operational, design, or business questions | Approved research sources, Drive/Airtable as needed | Cited research brief and recommendations | Planned |
| **Jobber Quote Agent** | Prepare quote and proposal drafts using approved customer, property, scope, and pricing information | Jobber, Drive, Airtable, approved templates | Quote/proposal draft and readiness status | Planned |

## Agent boundaries

| Agent | Must not do |
| --- | --- |
| Plant Library Builder | Treat unverified research as final plant guidance or overwrite approved records without change tracking |
| Design Email Agent | Send messages without the required approval |
| Research Agent | Make business commitments or represent research as a final decision without cited support |
| Jobber Quote Agent | Send a quote, create unapproved financial commitments, or override pricing/approval policy |

## Standard result schema

All agent results should be representable with the following fields:

| Field | Description |
| --- | --- |
| `request_id` | Source request or linked record |
| `status` | `complete`, `needs_review`, `blocked`, or `failed` |
| `summary` | Concise human-readable result |
| `outputs` | Links/IDs for drafts, records, files, or recommendations |
| `missing_information` | Required gaps that prevented completion |
| `red_flags` | Issues requiring visibility or escalation |
| `approval_required` | Whether a human must approve the next action |
| `next_owner` | Responsible director, agent, or human role |

## Future agents

| Candidate | Trigger to add | Status |
| --- | --- | --- |
| Invoice Agent | Invoice workflow is defined, tested, and approved | TBD |
| Financial Analysis Agent | Financial permissions, data source, and review controls are defined | TBD |
| Website Content Agent | Website content workflow and approvals are defined | TBD |
| Maintenance Intelligence Agent | Maintenance data capture and exception rules are stable | TBD |

## Open decisions

- Agent runtime/platform selection: **TBD**
- Evaluation and quality thresholds per agent: **TBD**
- Versioning and release process for agent instructions: **TBD**
- Human review interface and notification method: **TBD**
