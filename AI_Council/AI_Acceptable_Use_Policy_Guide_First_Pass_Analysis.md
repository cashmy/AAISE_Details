# AI Acceptable Use Policy Guide - First Pass Analysis

Author: Cash Myers  
Artifact reviewed: `AI General - AI Acceptable Use Policy Guide.pdf`  
Version/date visible in PDF: Version 1.0, approved 5/20/26  
Review date: 2026-06-24

## Executive Take

This is a solid Version 1.0 policy guide. It already contains many of the right institutional controls: tool approval, an approved-tool inventory, privacy/data protection warnings, human review requirements, limits on high-impact decisions, vendor controls, reporting duties, accessibility expectations, and recurring risk review.

The main opportunity is to make the guide more operational. Right now, it reads partly as a policy, partly as training guidance, and partly as a governance framework. The next version should clarify decision paths, approval criteria, risk tiers, data-use categories, monitoring boundaries, and academic-use implementation so employees and faculty can consistently answer: "Can I use this tool, with this data, for this purpose, under these conditions?"

## Major Strengths

1. **Broad institutional scope**
   The guide covers employees, students, vendors, consultants, volunteers, board members, contractors, guests, and other authorized users. That breadth is useful for a college environment where AI use crosses instruction, administration, student services, vendors, and public-facing communications.

2. **Tool approval and inventory are explicitly required**
   Sections 1.3 and 1.4 create a strong foundation: tools must be reviewed and approved before use with college, student, or employee data, and the college will maintain an approved inventory. This is one of the most important pieces to preserve.

3. **Data protection is treated as a core risk**
   The guide repeatedly warns against sharing confidential, restricted, proprietary, student, employee, donor, and credential/security data with unapproved AI systems. It also includes data minimization, masking/anonymization, no external model training without authorization, and vendor due diligence.

4. **Human judgment remains central**
   The policy says AI should enhance rather than replace human judgment, and it bars AI from serving as the sole decision-maker for grading, admissions, financial aid, discipline, employment, or other decisions that materially affect individuals.

5. **Academic implementation is acknowledged**
   Requiring each syllabus to state permitted and prohibited AI use is a practical bridge between institution-level policy and classroom reality.

6. **Governance responsibilities are named**
   The accountability table assigns ownership across the AI Council, ITS, HR, internal audit, data stewards, and supervisors. That gives the council a workable starting map.

## Key Concerns and Gaps

1. **The guide needs a clearer data-use matrix**
   The policy says Microsoft Copilot and Anthology Copilot Embedded AI are approved exceptions for confidential or proprietary Southwest Tech data, but later says AI tools may not be used with Restricted or Confidential data unless explicit written approval is granted. This can be reconciled, but employees need a simple matrix that distinguishes:
   - Public data
   - Internal data
   - Confidential data
   - Restricted data
   - Student education records/FERPA data
   - Employee records
   - PHI/HIPAA data
   - PCI/payment data
   - Credentials and security configurations

   Recommended improvement: add a table showing which data classes may be used in which approved tools, under which conditions, and who can approve exceptions.

2. **"Approved tool" is not enough by itself**
   A tool can be approved for one use case but inappropriate for another. For example, a tool might be acceptable for summarizing public web content but not acceptable for analyzing student advising notes.

   Recommended improvement: approve combinations of tool + data type + use case + user role, not just tool names.

3. **The approval workflow is not yet concrete**
   The guide says tools must be reviewed and approved by the AI Council, with Academic Council involvement for academic requests. It does not yet explain intake, review criteria, risk tiering, decision timelines, documentation, appeal/reconsideration, renewal, or emergency suspension communication.

   Recommended improvement: create an AI Tool Review Standard or intake checklist that includes data classification, purpose, user group, vendor terms, training/model use, retention, audit logging, accessibility, security review, contract status, and required training.

4. **Monitoring language needs privacy guardrails**
   The policy reserves the right to review and monitor AI usage, prompts, outputs, and communications. That may be necessary for security and compliance, but it needs boundaries: notice, role-based access, retention period, investigation threshold, student versus employee handling, and whether prompt/output logs become institutional records.

   Recommended improvement: define what is logged, who can see it, how long it is retained, and when it may be reviewed.

5. **Academic use needs more student-facing detail**
   The syllabus requirement is good, but the guide should also address whether students may be required to create accounts with external AI providers, what alternatives must exist, how AI use intersects with academic integrity, and how students can appeal or clarify ambiguous cases.

   Recommended improvement: pair the policy with a student-facing AI use standard and a faculty syllabus decision guide.

6. **The vendor controls should become contract clauses**
   The third-party section is directionally right, but it should specify minimum contract requirements. At minimum: no training on college data without explicit written authorization, data deletion/return, breach notification, subprocessors, data residency if relevant, audit/support evidence, model/version change notification, accessibility conformance, indemnity/IP terms, and incident response cooperation.

7. **"Validation" of AI output needs definition**
   The guide says users must review, validate, and accept responsibility for AI work product. That is correct, but vague. Validation should mean different things for a marketing draft, a code snippet, a policy summary, a financial calculation, or a student-facing advising recommendation.

   Recommended improvement: add role- or risk-based validation examples.

8. **The software vulnerability language should be reworded**
   The risk bullet that says AI tools may "provide vulnerabilities (ie, code, viruses, etc.)" is directionally understandable but technically imprecise. AI-generated code is not automatically a vulnerability, and the current wording could imply that code itself is equivalent to viruses or malware.

   Recommended replacement: "Introduction of technical vulnerabilities. AI-generated code may contain insecure patterns, unsafe dependencies, or other defects that could make systems susceptible to malware, unauthorized access, data exposure, or other security risks if used without proper review and testing."

9. **Intellectual property and copyright need more specificity**
   The executive summary names intellectual property protection as a goal, but the standards do not provide much practical guidance on copyrighted inputs, generated outputs, third-party training data uncertainty, licensing, or attribution.

   Recommended improvement: add guidance for copyrighted materials, course materials, generated images, publication, public communications, and attribution/citation expectations.

10. **Meeting recording guidance may need nuance**
   The guide says AI meeting recording agents may not be used and notes a five-year public record retention issue if a meeting is recorded. This is important, but it may need a more precise distinction among transcription, recording, accessibility accommodations, minutes, Teams/Zoom native transcription, public meetings, private personnel meetings, and student meetings.

11. **Accessibility standard should be reviewed**
   The guide references WCAG 2.1 AA. That remains meaningful, but W3C encourages use of the latest WCAG version, and WCAG 2.2 adds additional success criteria while maintaining backward compatibility with 2.1.

   Recommended improvement: either update to WCAG 2.2 AA or phrase the requirement as "WCAG 2.1 AA or the college's currently adopted digital accessibility standard, whichever is more current."

12. **Sustainability is named but not operationalized**
   The sustainability section is thoughtful, but it does not yet define how the college will decide whether a use is meaningful, non-frivolous, cost-justified, environmentally responsible, or aligned to institutional priorities.

   Recommended improvement: turn sustainability into review criteria for tool approval and renewal.

## Artifact and Formatting Issues

These are not policy problems, but they matter because this is likely to become a reference document:

- The table of contents appears to truncate "4.0 - Rapid Change and Emerging Risk Clause" as "Cl".
- The table of contents lists 3.0 as "Enforcement and Auditing," while the body uses "Accountability, Enforcement and Auditing."
- The table of contents does not show sections 1.3, 1.4, or 5.0 Sustainability.
- The accountability table has a formatting issue around "As needed (Single License Agreement Incident response workflow defined)," which appears to merge unrelated text.
- Some punctuation and dash styles are inconsistent.
- "Compliancy" should probably be "compliance."
- "Guidelines document" is sometimes singular/plural inconsistent.
- The document includes "Revision History" in the table of contents but the extracted text does not show a revision history section.

## Suggested AI Council Questions

1. What counts as an approved AI use: the tool itself, or the tool plus use case plus data type?
2. Who can approve exceptions for Confidential or Restricted data, and how is that approval documented?
3. What is the official data classification scheme, and does it map cleanly to this AI policy?
4. What is the process and timeline for reviewing a new AI tool request?
5. Will the approved tool inventory include approved use cases, data classes, version/model details, owner, renewal date, and known restrictions?
6. What logs are retained for approved AI tools, and who can review prompts and outputs?
7. How should faculty communicate AI expectations in syllabi without creating course-to-course inconsistency?
8. Can students be required to use external AI tools, or must alternatives be available?
9. What validation standard is required before AI output can be used in official college work?
10. What minimum contract language is required for vendors using or embedding AI?
11. How will the college handle AI-generated accessibility failures, hallucinated content, biased output, and citation errors?
12. What incident response path applies when confidential data is pasted into an unapproved tool?

## Priority Recommendations for Version 1.1

1. Add a data classification/use-case matrix.
2. Add an AI tool approval workflow with risk tiers.
3. Expand vendor contract minimums.
4. Clarify monitoring, logging, retention, and privacy boundaries.
5. Add student-facing and faculty-facing academic AI guidance.
6. Define output validation expectations by risk level.
7. Reword the software vulnerability risk to distinguish insecure generated code from malware or viruses.
8. Update accessibility language to account for WCAG 2.2 or the college's current adopted standard.
9. Clean up formatting, table of contents, and accountability table issues.

## External Reference Points

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST AI 600-1 Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) emphasize governance, risk mapping, measurement, and management for generative AI systems.
- [U.S. Department of Education AI guidance](https://www.ed.gov/about/news/press-release/us-department-of-education-issues-guidance-artificial-intelligence-use-schools-proposes-additional-supplemental-priority) emphasizes responsible AI use in education with attention to privacy, equity, transparency, human oversight, and statutory/regulatory compliance.
- The [U.S. Department of Education Student Privacy Policy Office](https://studentprivacy.ed.gov/) remains the authoritative federal source for FERPA-related student privacy guidance.
- [W3C's WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/) identifies WCAG 2.2 as the latest WCAG 2 version and notes that it is backward compatible with WCAG 2.1.
