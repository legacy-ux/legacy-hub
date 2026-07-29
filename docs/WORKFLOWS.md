# Legacy Hub Workflows

## Workflow standard

Every documented workflow should state the trigger, inputs, owner, required checks, outputs, approval point, system updates, exceptions, and completion criteria. Workflows should be tested manually before repeatable automation is enabled.

## Core workflow catalog

| Workflow | Trigger | Primary owner | Approval point | Status |
| --- | --- | --- | --- | --- |
| New customer intake and verification | New request or customer information | AI Director | Before creating a new customer/property | Defined at high level |
| Consultation capture | Consultation/site visit complete | Sales & Design Director | Before proposal preparation | Defined at high level |
| Proposal readiness and quote drafting | Consultation information complete | Jobber Quote Agent | Before customer send | Defined at high level |
| Deposit-to-project setup | Approval/deposit received | Operations Director | Before scheduling/material order | Defined at high level |
| Material readiness and pre-start | Seven days before start / pre-start review | Operations Director | Before job start | Defined at high level |
| Daily production capture | Crew workday / job activity | Crew leader / Operations Director | N/A | Defined at high level |
| Final walkthrough and warranty activation | Work marked complete | Designer or Account Manager | Customer acceptance/payment verification | Defined at high level |
| Property evaluation and enhancement opportunities | Scheduled evaluation | Account Manager Director | Before customer recommendations/send | Planned |
| Plant library completion | Plant asset/research submitted | Plant Library Builder | Before approval/publish | Planned |
| Invoice routing | Invoice request | AI Director / future Invoice Agent | Before invoice creation/send | TBD |

## New customer intake and verification

1. Capture customer contact, property address, request type, source, and supplied files.
2. Search for matching customer and property records before creation.
3. If an existing record is found, route the information to that workspace.
4. If no match is confirmed, create the required draft/new record through the approved system workflow.
5. Assign the next owner and create any required follow-up or red flag.

**Completion:** a verified customer/property relationship exists or a visible exception explains why it cannot be verified.

## Consultation to proposal-ready package

1. Capture photos, voice notes, measurements/quantities, goals, budget, preferences, decision-maker status, and next step.
2. Store source files in Drive and link them to the consultation/project workspace.
3. Check proposal readiness: scope, measurements, budget, design/mood board needs, availability, pricing notes, and HOA/approval needs.
4. For work under $6,000, prepare an email proposal with a simple mood board as appropriate.
5. For work over $6,000, prepare a formal presentation with a full mood board, plant palette, and renders as applicable.
6. Send the complete approved package to the Jobber Quote Agent for draft preparation.

**Completion:** a quote/proposal draft is ready for authorized review, or missing requirements are visible and assigned.

## Deposit to project setup

1. Verify customer approval and deposit status in Jobber.
2. Confirm scope, latest proposal version, schedule estimate, crew assignment, material plan, and customer access notes.
3. Create/update project workspace, linked tasks, and relevant Drive folder references.
4. Record material ordering status; do not represent materials as ordered until that action is confirmed.
5. Surface readiness red flags to the responsible owner.

**Completion:** project is ready to schedule or a blocker is assigned and visible.

## Pre-start and production

### Pre-start checklist

- Final scope and latest proposal confirmed
- Customer start confirmation completed
- Access, gate, pets, HOA, and site constraints confirmed
- Materials confirmed
- Crew leader, layout, and special notes assigned

### Daily capture

Crew reporting records clock-in/out, completed work, percent complete, photos, customer communication notes, issues, and crew-leader notes.

**Completion:** workday information is attached to the project and exceptions have owners.

## Final walkthrough, warranty, and customer for life

1. Designer or Account Manager completes final walkthrough, photos, punch-list notes, acceptance, and satisfaction confirmation.
2. Verify final payment status and resolve any punch-list items.
3. Activate warranty only after final walkthrough and payment verification.
4. Schedule a seven-day thank-you/review/referral request and a 30-day enjoyment/referral follow-up.
5. Enroll the customer in the monthly customer-for-life communication process as applicable.

**Completion:** closeout artifacts, warranty status, follow-ups, and referral source tracking are complete.

## Exceptions and red flags

Red flags must include severity, description, linked entity, owner, created date, next action, and resolution status. Examples include missing consultation information, material not confirmed, customer not notified of schedule change, skipped visit not rescheduled, unverified deposit, and incomplete final closeout.

## Workflow details still to define

- Invoice workflow and handoff rules
- Schedule-change notification workflow
- Change-order hard stop and owner override record
- Maintenance onboarding and service-time intelligence
- Financial review and approval workflow
- SLA targets, escalation timing, and notification channels
