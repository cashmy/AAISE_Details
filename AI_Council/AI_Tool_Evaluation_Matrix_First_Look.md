# AI Tool Evaluation Matrix - First Look

Author: Cash Myers  
Artifact reviewed: `AI_Evaluation_Scorecard_HigherEd Draft.xlsx`  
Review date: 2026-06-24

## Executive Take

The preliminary evaluation matrix is a good starting point. It already names many of the right review areas for higher education: strategic fit, academic integrity, privacy/security, accessibility/equity, pedagogical value, user experience, integration, vendor viability, cost effectiveness, and risk management.

However, the current workbook is more of a qualitative checklist than an operational approval tool. It has no formulas, no weighting, no threshold logic, no risk gating, no data classification review, and no distinction between pilot approval, limited approval, full approval, conditional approval, or rejection.

The next improvement should not simply be "more rows." The stronger move is to turn the matrix into a repeatable review process that connects tool evaluation to approval status, data use, ownership, monitoring, and renewal.

## What the Current Matrix Covers Well

1. **Institutional alignment**
   It asks whether the tool aligns with mission, academic goals, innovation, and efficiency.

2. **Academic integrity**
   It includes plagiarism/misuse controls and faculty oversight.

3. **Privacy and security**
   It references FERPA, GDPR, local privacy laws, data collection, ownership, hosting, and encryption.

4. **Accessibility and equity**
   It includes disability access and potential bias across student populations.

5. **Pedagogical value**
   It asks whether the tool supports critical thinking, creativity, personalization, active learning, or feedback.

6. **User experience**
   It considers ease of use and training/onboarding.

7. **Integration**
   It considers LMS and campus IT compatibility.

8. **Vendor and cost**
   It includes vendor reputation, support, roadmap, total cost, and scalability.

9. **Risk management**
   It includes legal/IP risk and accountability for AI-generated content.

## Main Gaps

### 1. No Data Classification Gate

The matrix does not yet ask what type of data the tool will process.

This should be a gating question, not just one scored criterion.

Recommended categories:

- Public data
- Internal data
- Confidential data
- Restricted data
- Student education records / FERPA data
- Employee records
- PHI / HIPAA data
- PCI/payment data
- Authentication credentials, tokens, or security configurations

If a tool will process confidential or restricted data, the review should automatically require a higher level of scrutiny.

### 2. No Use-Case Definition

The matrix evaluates the tool in general, but AI tools should be approved by use case.

A tool may be acceptable for:

- drafting public communications
- creating synthetic lesson examples
- summarizing public documents
- supporting internal brainstorming

The same tool may not be acceptable for:

- processing student records
- making admissions or employment recommendations
- evaluating student conduct
- analyzing confidential HR matters
- integrating with enterprise systems

Recommended improvement: evaluate tool + use case + data type + user group together.

### 3. No Risk Tier

The matrix currently produces a general recommendation range, but it does not classify risk.

Recommended risk tiers:

- Low risk: public data, no system integration, no high-impact decisions
- Moderate risk: internal data, limited users, no confidential data, limited integration
- High risk: confidential data, student records, employee records, vendor-hosted processing, LMS/SSO integration
- Critical risk: restricted data, high-impact decisions, PHI/HIPAA, PCI, credentials/security data, automated decisions affecting individuals

Risk tier should determine the required approval path.

### 4. No Approval Outcome Categories

The scoring guide includes adoption recommendations, but the approval statuses should map to the AI tool inventory.

Suggested approval statuses:

- Approved
- Approved for Pilot
- Approved with Conditions
- Approved for Limited Use
- Academic Review Required
- ITS/Security Review Required
- Legal/Contract Review Required
- Rejected
- Suspended
- Retired

### 5. No Required Evidence Standard

The matrix includes a comments/evidence column, but it does not define what evidence is expected.

Evidence may include:

- vendor security documentation
- privacy policy
- data processing agreement
- terms of service
- accessibility conformance report or VPAT
- contract language
- support/SLA documentation
- AI/model training policy
- data retention/deletion terms
- subprocessor list
- integration documentation
- pilot results
- user training plan

### 6. No Weighting or Gating Logic

All criteria appear equal. In practice, privacy/security, data classification, accessibility, vendor terms, and high-impact decision risk should carry more weight than general ease of use.

Some items should be non-negotiable gates. For example:

- Tool cannot meet FERPA obligations when student records are involved.
- Tool uses college/student/employee data to train external models without approval.
- Tool lacks acceptable security or contract terms for the requested use.
- Tool cannot meet accessibility expectations and no reasonable alternative or mitigation exists.
- Tool makes or materially influences high-impact decisions without human review.

### 7. No Lifecycle Review

The matrix does not yet account for renewal or monitoring.

AI tools change quickly. Approval should expire or require periodic review.

Recommended fields:

- approval date
- approving body
- owner/sponsor
- approved use cases
- approved data classes
- conditions/restrictions
- review cadence
- renewal date
- trigger events for re-review
- incident history
- current status

### 8. No Implementation Readiness Review

A tool might be acceptable in principle but not ready for rollout.

Recommended review areas:

- training plan
- support owner
- communication plan
- documentation location
- user onboarding
- opt-in/opt-out expectations
- accessibility remediation plan
- pilot success criteria
- retirement/exit plan

## Recommended Matrix Structure

The evaluation process should likely have more than one tab or section.

### 1. Intake Summary

Purpose: capture what is being requested.

Fields:

- tool name
- vendor
- requestor
- sponsor/owner
- academic or administrative use
- proposed user group
- proposed use case
- requested approval type
- data types involved
- integrations requested
- whether students are required to use it
- whether cost/licensing is involved

### 2. Gating Questions

Purpose: identify automatic escalation or rejection conditions.

Examples:

- Will the tool process student education records?
- Will the tool process employee records?
- Will the tool process confidential or restricted data?
- Will the vendor use submitted data to train external models?
- Does the tool integrate with SSO, LMS, SIS, HR, finance, or other enterprise systems?
- Will the tool influence grades, admissions, employment, financial aid, discipline, or accommodations?
- Are students required to create accounts with an external vendor?
- Does the tool have accessibility documentation?

### 3. Scored Evaluation

Purpose: compare tools and document quality.

Categories:

- Strategic fit
- Educational/pedagogical value
- Administrative value
- Privacy and data protection
- Security and technical controls
- Accessibility and equity
- Academic integrity and human oversight
- Vendor viability and contract terms
- Integration and support readiness
- Cost and sustainability
- Legal/IP risk
- Training and implementation readiness

### 4. Decision Summary

Purpose: document the review outcome.

Fields:

- overall risk tier
- total score
- required approval bodies
- decision
- approved use cases
- prohibited use cases
- approved data classes
- restrictions/conditions
- training requirements
- renewal/review date
- escalation notes

### 5. Ongoing Monitoring

Purpose: keep approval current.

Fields:

- renewal date
- vendor/model update notices
- incidents
- user feedback
- accessibility issues
- security changes
- contract changes
- status changes

## Immediate Recommendations Before Today's Review

If the AI Council is reviewing GitHub and Figma today, the current matrix can still be useful, but it should be supplemented with a few quick questions:

1. What exact use case is being reviewed?
2. Who will use the tool?
3. What data will users enter into the tool?
4. Will student, employee, confidential, or restricted data be involved?
5. Will the tool integrate with college systems?
6. Will students be required to create external accounts?
7. Does the vendor use prompts, files, outputs, or usage data for model training?
8. What contract or license terms govern the tool?
9. Is there accessibility documentation?
10. Is this a pilot, limited approval, or full adoption request?
11. Who owns training, support, monitoring, and renewal?
12. What conditions or restrictions should be recorded in the approved AI tool inventory?

## Suggested Short-Term Position

For now, the matrix should be treated as an evaluation discussion aid, not a final approval mechanism.

The Council can use it to structure conversation, but final approval should also document:

- approved use case
- approved user group
- approved data class
- risk tier
- required conditions
- review/renewal date
- responsible owner

## Bottom Line

The current matrix is a good February-era starting point, but the AI policy work now needs a stronger process model.

The better next version should evaluate not just "Is this a good tool?" but:

- "Is this tool appropriate for this use case?"
- "With what data?"
- "For which users?"
- "Under what conditions?"
- "With what monitoring?"
- "For how long before re-review?"

That shift would make the evaluation process much more defensible, repeatable, and aligned with the emerging AI governance framework.

