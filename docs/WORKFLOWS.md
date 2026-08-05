# Legacy Hub Workflows

## Legacy v1 workflow rules

Each workflow has one accountable Director for its primary seat. Directors may coordinate directly when work crosses seats, but no central Director, Operations Director, or Specialist Agent owns the workflow.

Every workflow records its request, linked customer/property, owner, task(s), workflow state, source files, approval state, exception(s), and completion in Airtable. Directors store files in Google Drive and link them back to Airtable. Make only synchronizes approved structured Airtable data with Jobber.

## Included workflow catalog

| Workflow | Accountable Director | Completion |
| --- | --- | --- |
| New Customer Intake | Owner Director or Design & Sales Director, based on receiving seat | Verified customer/property record or a visible verification exception |
| Existing Customer Lookup | Director receiving the request | Existing linked record identified and routed to the accountable seat |
| Property Management | Account Manager Director | Updated property profile, tasks, and history are complete |
| Proposal Workflow | Design & Sales Director | Customer-facing Jobber quote is ready for required review/send, with Airtable context complete |
| Customer Communication | Account Manager Director or the Director accountable for the active workflow | Message outcome and follow-up are recorded |
| Scheduling | Account Manager Director, coordinating with Crew Leader Director as needed | Readiness, schedule state, and notification status are recorded |
| Daily Crew Management | Crew Leader Director | Daily capture and exceptions are linked to the project/property |
| Property Evaluation | Account Manager Director | Evaluation, photos, scoring, report/recommendations, and follow-up tasks are complete |
| Plant Library Management | Owner Director, using Plant Library Agent as needed | Plant/gallon-size record and completeness state are updated |

## New Customer Intake

1. The receiving Director captures contact details, property address, request type, source, and supplied files.
2. The Director performs Existing Customer Lookup before any new record is created.
3. If a matching customer/property exists, the Director links the request to the existing Airtable records and routes it to the accountable Director.
4. If no match exists, the Director creates the Airtable customer, property, contact, intake, and next task records under the approved data rules.
5. If Jobber needs the customer/property for a later transaction, Make synchronizes only the approved mapped fields after the Airtable records are verified.

## Existing Customer Lookup

1. Search Airtable by customer name, phone, email, property address, and known Jobber ID.
2. Confirm the correct customer/property relationship before adding information or creating a duplicate.
3. Link the request, files, and new task to the verified record.
4. Create a red flag when a possible duplicate or conflicting identity cannot be resolved.

## Property Management

The Account Manager Director maintains the property profile: access, gate/pets, irrigation notes, maintenance/service context, property history, customer preferences, Drive links, open tasks, and red flags. It coordinates with other Directors through linked tasks when a sales, crew, or owner decision is required.

## Proposal Workflow

1. Design & Sales Director captures consultation information, photos, voice notes, measurements, goals, budget, preferences, decision-maker status, and next step.
2. The Director stores source files in Drive and links them to Airtable.
3. The Director verifies proposal readiness: scope, measurements, budget, design/mood-board needs, availability, pricing notes, and HOA requirements.
4. The Director performs proposal and customer-communication work directly, using the Design Agent or Research Agent only for bounded support.
5. The Director prepares the required customer-facing quote/proposal in Jobber under the approved transaction rule. Make may synchronize the approved mapped Airtable data and returned Jobber ID/status.
6. For work under $6,000, use an email proposal and simple mood board when appropriate; for work over $6,000, use a formal presentation with full supporting materials as applicable.

## Customer Communication

The accountable Director drafts, sends/receives, and records customer communication in Gmail. The Director links material messages, decisions, and required follow-up tasks to Airtable. Customer-facing messages remain subject to the applicable approval rule.

## Scheduling

1. Account Manager Director verifies the approved scope, readiness, customer constraints, and responsible crew before scheduling.
2. The Director records internal schedule information, notification status, and readiness in Airtable.
3. Where Jobber is used for a customer-facing scheduled transaction, Make synchronizes only the approved mapped schedule data and returns status to Airtable.
4. Crew Leader Director receives the relevant job, access, layout, and special notes through its assigned workflow.
5. Schedule changes record the reason, who changed it, who was notified, and any red flag.

## Daily Crew Management

Crew Leader Director records clock-in/out, completed work, percent complete, photos, customer communication notes, issues, and crew-leader notes. It links daily capture to the Airtable project/property record and escalates customer-impacting issues to Account Manager Director and approval decisions to Owner Director when required.

## Property Evaluation

Account Manager Director captures structured questions, scoring, photos, observations, maintenance concerns, and enhancement opportunities. It stores source files in Drive, links them in Airtable, creates the appropriate internal/customer-ready report, and assigns follow-up tasks. The Design Agent or Research Agent may provide bounded supporting material.

## Plant Library Management

Owner Director maintains the plant-library workflow and may request the Plant Library Agent to prepare research, asset-completeness, or proposed-record results. Each plant/gallon-size record is reviewed and updated in Airtable; associated photos and documents remain in Drive.

## Exceptions and red flags

Every red flag includes severity, description, linked record, accountable Director, created date, next action, and resolution state. Examples: possible duplicate customer, missing proposal input, material/readiness issue, uncommunicated schedule change, incomplete daily capture, or unresolved property-evaluation recommendation.

## Future Releases

- Invoice workflow
- Deposit-to-project setup and formal material-readiness workflow
- Final walkthrough, warranty, and customer-for-life workflow
- Change-order hard stop and owner override record
- Maintenance onboarding and service-time intelligence
- Detailed financial review/approval workflow
