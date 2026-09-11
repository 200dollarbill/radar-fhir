---
id: clinicalsummary-module
title: Clinical Summary Module
source_url: https://hl7.org/fhir/R4/clinicalsummary-module.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:49Z'
sha256: 0bdaf3dfaa88829cfdc73986b3a598a446ccb58cffecdde777793f15b3b1c21f
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/clinicalsummary-module.html) [R4B](http://hl7.org/fhir/R4B/clinicalsummary-module.html) **R4** [R3](http://hl7.org/fhir/STU3/clinicalsummary-module.html)

|  |  |
| --- | --- |
| Work Group [Patient Care](http://www.hl7.org/Special/committees/patientcare/index.cfm) | [Standards Status](versions.html#std-process): [Informative](versions.html#std-process) |

## 9.0 Clinical Module

### 9.0.1 Introduction

This Clinical Module focuses on the FHIR Resources that represent core clinical
information for a patient. The information contained in these Resources are those
frequently documented, created or retrieved by healthcare providers during the course
of clinical care. Resources generated during the course of diagnostic studies can be
found in the [Diagnostics Module](diagnostics-module.html), whereas the
Resources related to medication ordering and administration process can be found
in the [Medications Module](medications-module.html).

As an introduction to FHIR APIs and Resources, please see the
[Developer's Introduction](overview-dev.html) or
[Clinical Introduction](overview-clinical.html) in the
Overview section of the [Foundation Module](foundation-module.html).

### 9.0.2 Index

The Clinical Module covers the following resources:

|  |  |  |
| --- | --- | --- |
| - [AllergyIntolerance](allergyintolerance.html "Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.") - [Condition](condition.html "A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.") (Problem) - [Procedure](procedure.html "An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.") - [FamilyMemberHistory](familymemberhistory.html "Significant health conditions for a person related to the patient relevant in the context of care for the patient.") | - [CarePlan](careplan.html "Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.") - [Goal](goal.html "Describes the intended objective(s) for a patient, group or organization care, for example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, etc.") - [CareTeam](careteam.html "The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.") - [ClinicalImpression](clinicalimpression.html "A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow. This resource is called \"ClinicalImpression\" rather than \"ClinicalAssessment\" to avoid confusion with the recording of assessment tools such as Apgar score.") | - [AdverseEvent](adverseevent.html "Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.") - [DetectedIssue](detectedissue.html "Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.") - [RiskAssessment](riskassessment.html "An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.") |

FHIR Resources have a low, moderate or high levels of complexity with respect to the number
of primary and child elements as well as the number of referenced Resources, found in this
module and others. To better understand the relationships between Resources, we recommend
beginning with the lower complexity, core Resources such as
[Patient](patient.html),
[Condition](condition.html), and
[FamilyMemberHistory](familymemberhistory.html) before addressing a high
complexity Resource such as [CarePlan](careplan.html).

### 9.0.3 Security and Privacy

The clinical resources often represent patient-related data, and as such are
susceptible to data breaching. Necessary privacy and security provision must be
in place for searching and fetching this information. For more general considerations,
see the [Security and Privacy module](secpriv-module.html).

### 9.0.4 Common use Cases

- **Documenting a patient's condition** - The [Condition](condition.html) Resource
  is used extensively throughout FHIR Resources to associate information and activities with
  specific conditions. The [Condition](condition.html) Resource is broadly defined
  to include problems, diagnoses and health concerns.
- **Retrieving the patient's problems**
- **Documenting and retrieving the patient's allergies** - The [AllergyIntolerance](allergyintolerance.html) Resource
  is used to represent the patient's allergy or intolerance to a substance. There is vibrant debate within clinical community
  regarding what is appropriate to document as an allergy or intolerance. These terms are used both formally by the Allergy and
  Immunology community as well as informally by patients leading to confusion. Readers are referred to the Resource definition
  for the Scope and Usage of this resource. The AllergyIntolerance Resource also supports the documenting of the absence of an allergy.
- **Family History** - The [FamilyMemberHistory](familymemberhistory.html) Resource can be used to document known conditions of family members and support
  the creation of pedigrees.
- **Care Plans** - The [CarePlan](careplan.html) resource supports a problem based care plan with references
  to other Resources including [CareTeam](careteam.html), [Condition](condition.html), [Goal](goal.html),
  and activities such as [ServiceRequest](servicerequest.html)

### 9.0.5 Developmental Roadmap

Over the next 18 months, we will continue to advance the resources through the [Maturity Levels](versions.html#maturity)
through the process of development and testing of the Resources. We anticipate more widespread implementation of core Resources such as Condition.
Complex Resources such as CarePlan are dependent on the maturation of its referred Resources and are expected to mature more gradually.
The clinical community will need to develop use cases to test and further mature the
[ServiceRequest](servicerequest.html) Resource at opportunities such as the
[Clinicians on FHIR sessions ![](external.png)](https://confluence.hl7.org/display/FHIR/Clinicians+on+FHIR) at the HL7 Working Group Meetings.
