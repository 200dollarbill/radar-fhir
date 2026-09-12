---
id: condition
title: Condition
source_url: https://hl7.org/fhir/R4/condition.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:05Z'
sha256: c5d6188a8de09d6d7434385ac835e81f2129d8bdcc433393dea894ca88be215e
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/condition.html) [R4B](http://hl7.org/fhir/R4B/condition.html) **R4** [R3](http://hl7.org/fhir/STU3/condition.html) [R2](http://hl7.org/fhir/DSTU2/condition.html)

- [Content](#)
- [Examples](condition-examples.html)
- [Detailed Descriptions](condition-definitions.html)
- [Mappings](condition-mappings.html)
- [Profiles & Extensions](condition-profiles.html)
- [R3 Conversions](condition-version-maps.html)

# 9.2 Resource Condition - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Care](http://www.hl7.org/Special/committees/patientcare/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) |

A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.

## 9.2.1 Scope and Usage

Condition is one of the [event](workflow.html#event) resources in the FHIR [workflow](workflow.html) specification.

This resource is used to record detailed information about a condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern. The condition could be a point in time diagnosis in context of an encounter, it could be an item on the practitioner’s Problem List, or it could be a concern that doesn’t exist on the practitioner’s Problem List. Often times, a condition is about a clinician's assessment and assertion of a particular aspect of a patient's state of health. It can be used to record information about a disease/illness identified from application of clinical reasoning over the pathologic and pathophysiologic findings (diagnosis), or identification of health issues/situations that a practitioner considers harmful, potentially harmful and may be investigated and managed (problem), or other health issue/situation that may require ongoing monitoring and/or management (health issue/concern).

The condition resource may be used to record a certain health state of a patient which does not normally present a negative outcome, e.g. pregnancy. The condition resource may be used to record a condition following a procedure, such as the condition of Amputee-BKA following an amputation procedure.

While conditions are frequently a result of a clinician's assessment and assertion of a particular aspect of a patient's state of health, conditions can also be expressed by the patient, related person, or any care team member. A clinician may have a concern about a patient condition (e.g. anorexia) that the patient is not concerned about. Likewise, the patient may have a condition (e.g. hair loss) that does not rise to the level of importance such that it belongs on a practitioner’s Problem List.

For example, each of the following conditions could rise to the level of importance such that it belongs on a problem or concern list due to its direct or indirect impact on the patient’s health. These examples may also be represented using other resources, such as [FamilyMemberHistory](familymemberhistory.html), [Observation](observation.html), or [Procedure](procedure.html).

- Unemployed
- Without transportation (or other barriers)
- Susceptibility to falls
- Exposure to communicable disease
- Family History of cardiovascular disease
- Fear of cancer
- Cardiac pacemaker
- Amputee-BKA
- Risk of Zika virus following travel to a country
- Former smoker
- Travel to a country planned (that warrants immunizations)
- Motor Vehicle Accident
- Patient has had coronary bypass graft

## 9.2.2 Boundaries and Relationships

The condition resource may be referenced by other resources as "reasons" for an action (e.g. [MedicationRequest](medicationrequest.html),
[Procedure](procedure.html), [ServiceRequest](servicerequest.html), etc.)

This resource is not typically used to record information about subjective and objective information that might lead to the recording of a Condition resource. Such signs and symptoms are typically captured using the [Observation](observation.html) resource;
although in some cases a persistent symptom, e.g. fever, headache may be captured as a condition before a definitive diagnosis can be discerned by a clinician. By contrast, headache may be captured as an Observation when it contributes to the establishment of a meningitis Condition.

Use the [Observation](observation.html) resource when a symptom is resolved without long term management, tracking, or when a symptom contributes to the establishment of a condition.

Use Condition when a symptom requires long term management, tracking, or is used as a proxy for a diagnosis or problem that is not yet determined.

When the diagnosis is related to an allergy or intolerance, the Condition and [AllergyIntolerance](allergyintolerance.html) resources can both be used. However, to be actionable for decision support, using Condition alone is not sufficient as the allergy or intolerance condition needs to be represented as an [AllergyIntolerance](allergyintolerance.html).

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [Appointment](appointment.html#Appointment), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [Claim](claim.html#Claim), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Contract](contract.html#Contract), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [Encounter](encounter.html#Encounter), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory), [Goal](goal.html#Goal), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [Procedure](procedure.html#Procedure), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [ServiceRequest](servicerequest.html#ServiceRequest) and [SupplyRequest](supplyrequest.html#SupplyRequest)

## 9.2.3 Resource Content

- [Structure](#tabs-struc)
- [UML](#tabs-uml)
- [XML](#tabs-xml)
- [JSON](#tabs-json)
- [Turtle](#tabs-ttl)
- [R3 Diff](#tabs-diff)
- [All](#tabs-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Condition](condition-definitions.html#Condition "Condition : A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Detailed information about conditions, problems or diagnoses + Guideline: Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item + Rule: If condition is abated, then clinicalStatus must be either inactive, resolved, or remission + Rule: Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](condition-definitions.html#Condition.identifier "Condition.identifier : Business identifiers assigned to this condition by the performer or other systems which remain constant as the resource is updated and propagates from server to server.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | External Ids for this condition |
| ... [clinicalStatus](condition-definitions.html#Condition.clinicalStatus "Condition.clinicalStatus : The clinical status of the condition.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | active | recurrence | relapse | inactive | remission | resolved [Condition Clinical Status Codes](valueset-condition-clinical.html "The clinical status of the condition or diagnosis.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [verificationStatus](condition-definitions.html#Condition.verificationStatus "Condition.verificationStatus : The verification status to support the clinical status of the condition.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | unconfirmed | provisional | differential | confirmed | refuted | entered-in-error [ConditionVerificationStatus](valueset-condition-ver-status.html "The verification status to support or decline the clinical status of the condition or diagnosis.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [category](condition-definitions.html#Condition.category "Condition.category : A category assigned to the condition.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | problem-list-item | encounter-diagnosis [Condition Category Codes](valueset-condition-category.html "A category assigned to the condition.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [severity](condition-definitions.html#Condition.severity "Condition.severity : A subjective assessment of the severity of the condition as evaluated by the clinician.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Subjective severity of condition [Condition/Diagnosis Severity](valueset-condition-severity.html "A subjective assessment of the severity of the condition as evaluated by the clinician.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [code](condition-definitions.html#Condition.code "Condition.code : Identification of the condition, problem or diagnosis.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Identification of the condition, problem or diagnosis [Condition/Problem/Diagnosis Codes](valueset-condition-code.html "Identification of the condition or diagnosis.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [bodySite](condition-definitions.html#Condition.bodySite "Condition.bodySite : The anatomical location where this condition manifests itself.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location, if relevant [SNOMED CT Body Structures](valueset-body-site.html "Codes describing anatomical locations. May include laterality.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](condition-definitions.html#Condition.subject "Condition.subject : Indicates the patient or group who the condition record is associated with.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who has the condition? |
| ... [encounter](condition-definitions.html#Condition.encounter "Condition.encounter : The Encounter during which this Condition was created or to which the creation of this record is tightly associated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of |
| ... [onset[x]](condition-definitions.html#Condition.onset_x_ "Condition.onset[x] : Estimated or actual date or date-time  the condition began, in the opinion of the clinician.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Estimated or actual date, date-time, or age |
| .... onsetDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... onsetAge |  |  | [Age](datatypes.html#Age) |  |
| .... onsetPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... onsetRange |  |  | [Range](datatypes.html#Range) |  |
| .... onsetString |  |  | [string](datatypes.html#string) |  |
| ... [abatement[x]](condition-definitions.html#Condition.abatement_x_ "Condition.abatement[x] : The date or estimated date that the condition resolved or went into remission. This is called \"abatement\" because of the many overloaded connotations associated with \"remission\" or \"resolution\" - Conditions are never really resolved, but they can abate.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 |  | When in resolution/remission |
| .... abatementDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... abatementAge |  |  | [Age](datatypes.html#Age) |  |
| .... abatementPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... abatementRange |  |  | [Range](datatypes.html#Range) |  |
| .... abatementString |  |  | [string](datatypes.html#string) |  |
| ... [recordedDate](condition-definitions.html#Condition.recordedDate "Condition.recordedDate : The recordedDate represents when this particular Condition record was created in the system, which is often a system-generated date.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date record was first recorded |
| ... [recorder](condition-definitions.html#Condition.recorder "Condition.recorder : Individual who recorded the record and takes responsibility for its content.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who recorded the condition |
| ... [asserter](condition-definitions.html#Condition.asserter "Condition.asserter : Individual who is making the condition statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Person who asserts this condition |
| ... [stage](condition-definitions.html#Condition.stage "Condition.stage : Clinical stage or grade of a condition. May include formal severity assessments.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Stage/grade, usually assessed formally + Rule: Stage SHALL have summary or assessment |
| .... [summary](condition-definitions.html#Condition.stage.summary "Condition.stage.summary : A simple summary of the stage such as \"Stage 3\". The determination of the stage is disease-specific.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Simple summary (disease specific) [Condition Stage](valueset-condition-stage.html "Codes describing condition stages (e.g. Cancer stages).") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [assessment](condition-definitions.html#Condition.stage.assessment "Condition.stage.assessment : Reference to a formal record of the evidence on which the staging assessment is based.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html) | [DiagnosticReport](diagnosticreport.html) | [Observation](observation.html)) | Formal record of assessment |
| .... [type](condition-definitions.html#Condition.stage.type "Condition.stage.type : The kind of staging, such as pathological or clinical staging.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of staging [Condition Stage Type](valueset-condition-stage-type.html "Codes describing the kind of condition staging (e.g. clinical or pathological).") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [evidence](condition-definitions.html#Condition.evidence "Condition.evidence : Supporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the condition.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Supporting evidence + Rule: evidence SHALL have code or details |
| .... [code](condition-definitions.html#Condition.evidence.code "Condition.evidence.code : A manifestation or symptom that led to the recording of this condition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Manifestation/symptom [Manifestation and Symptom Codes](valueset-manifestation-or-symptom.html "Codes that describe the manifestation or symptoms of a condition.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [detail](condition-definitions.html#Condition.evidence.detail "Condition.evidence.detail : Links to other relevant information, including pathology reports.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Supporting information found elsewhere |
| ... [note](condition-definitions.html#Condition.note "Condition.note : Additional information about the Condition. This is a general notes/comments entry  for description of the Condition, its diagnosis and prognosis.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Additional information about the Condition |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Condition xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier External Ids for this condition --></identifier>
 <clinicalStatus><!-- ![??](lock.png) 0..1 CodeableConcept active | recurrence | relapse | inactive | remission | resolved --></clinicalStatus>
 <verificationStatus><!-- ![??](lock.png) 0..1 CodeableConcept unconfirmed | provisional | differential | confirmed | refuted | entered-in-error --></verificationStatus>
 <category><!-- 0..* CodeableConcept problem-list-item | encounter-diagnosis --></category>
 <severity><!-- 0..1 CodeableConcept Subjective severity of condition --></severity>
 <code><!-- 0..1 CodeableConcept Identification of the condition, problem or diagnosis --></code>
 <bodySite><!-- 0..* CodeableConcept Anatomical location, if relevant --></bodySite>
 <subject><!-- 1..1 Reference(Patient|Group) Who has the condition? --></subject>
 <encounter><!-- 0..1 Reference(Encounter) Encounter created as part of --></encounter>
 <onset[x]><!-- 0..1 dateTime|Age|Period|Range|string Estimated or actual date,  date-time, or age --></onset[x]>
 <abatement[x]><!-- ![??](lock.png) 0..1 dateTime|Age|Period|Range|string When in resolution/remission --></abatement[x]>
 <recordedDate value="[dateTime]"/><!-- 0..1 Date record was first recorded -->
 <recorder><!-- 0..1 Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) Who recorded the condition --></recorder>
 <asserter><!-- 0..1 Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) Person who asserts this condition --></asserter>
 <stage>  <!-- 0..* Stage/grade, usually assessed formally -->
  <summary><!-- ![??](lock.png) 0..1 CodeableConcept Simple summary (disease specific) --></summary>
  <assessment><!-- ![??](lock.png) 0..* Reference(ClinicalImpression|DiagnosticReport|Observation) Formal record of assessment --></assessment>
  <type><!-- 0..1 CodeableConcept Kind of staging --></type>
 </stage>
 <evidence>  <!-- 0..* Supporting evidence -->
  <code><!-- ![??](lock.png) 0..* CodeableConcept Manifestation/symptom --></code>
  <detail><!-- ![??](lock.png) 0..* Reference(Any) Supporting information found elsewhere --></detail>
 </evidence>
 <note><!-- 0..* Annotation Additional information about the Condition --></note>
</Condition>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Condition",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // External Ids for this condition
  "clinicalStatus" : { CodeableConcept }, // C? active | recurrence | relapse | inactive | remission | resolved
  "verificationStatus" : { CodeableConcept }, // C? unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
  "category" : [{ CodeableConcept }], // problem-list-item | encounter-diagnosis
  "severity" : { CodeableConcept }, // Subjective severity of condition
  "code" : { CodeableConcept }, // Identification of the condition, problem or diagnosis
  "bodySite" : [{ CodeableConcept }], // Anatomical location, if relevant
  "subject" : { Reference(Patient|Group) }, // R!  Who has the condition?
  "encounter" : { Reference(Encounter) }, // Encounter created as part of
  // onset[x]: Estimated or actual date,  date-time, or age. One of these 5:
  "onsetDateTime" : "<dateTime>",
  "onsetAge" : { Age },
  "onsetPeriod" : { Period },
  "onsetRange" : { Range },
  "onsetString" : "<string>",
  // abatement[x]: When in resolution/remission. One of these 5:
  "abatementDateTime" : "<dateTime>",
  "abatementAge" : { Age },
  "abatementPeriod" : { Period },
  "abatementRange" : { Range },
  "abatementString" : "<string>",
  "recordedDate" : "<dateTime>", // Date record was first recorded
  "recorder" : { Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) }, // Who recorded the condition
  "asserter" : { Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) }, // Person who asserts this condition
  "stage" : [{ // Stage/grade, usually assessed formally
    "summary" : { CodeableConcept }, // C? Simple summary (disease specific)
    "assessment" : [{ Reference(ClinicalImpression|DiagnosticReport|Observation) }], // C? Formal record of assessment
    "type" : { CodeableConcept } // Kind of staging
  }],
  "evidence" : [{ // Supporting evidence
    "code" : [{ CodeableConcept }], // C? Manifestation/symptom
    "detail" : [{ Reference(Any) }] // C? Supporting information found elsewhere
  }],
  "note" : [{ Annotation }] // Additional information about the Condition
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Condition;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Condition.identifier [ Identifier ], ... ; # 0..* External Ids for this condition
  fhir:Condition.clinicalStatus [ CodeableConcept ]; # 0..1 active | recurrence | relapse | inactive | remission | resolved
  fhir:Condition.verificationStatus [ CodeableConcept ]; # 0..1 unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
  fhir:Condition.category [ CodeableConcept ], ... ; # 0..* problem-list-item | encounter-diagnosis
  fhir:Condition.severity [ CodeableConcept ]; # 0..1 Subjective severity of condition
  fhir:Condition.code [ CodeableConcept ]; # 0..1 Identification of the condition, problem or diagnosis
  fhir:Condition.bodySite [ CodeableConcept ], ... ; # 0..* Anatomical location, if relevant
  fhir:Condition.subject [ Reference(Patient|Group) ]; # 1..1 Who has the condition?
  fhir:Condition.encounter [ Reference(Encounter) ]; # 0..1 Encounter created as part of
  # Condition.onset[x] : 0..1 Estimated or actual date,  date-time, or age. One of these 5
    fhir:Condition.onsetDateTime [ dateTime ]
    fhir:Condition.onsetAge [ Age ]
    fhir:Condition.onsetPeriod [ Period ]
    fhir:Condition.onsetRange [ Range ]
    fhir:Condition.onsetString [ string ]
  # Condition.abatement[x] : 0..1 When in resolution/remission. One of these 5
    fhir:Condition.abatementDateTime [ dateTime ]
    fhir:Condition.abatementAge [ Age ]
    fhir:Condition.abatementPeriod [ Period ]
    fhir:Condition.abatementRange [ Range ]
    fhir:Condition.abatementString [ string ]
  fhir:Condition.recordedDate [ dateTime ]; # 0..1 Date record was first recorded
  fhir:Condition.recorder [ Reference(Practitioner|PractitionerRole|Patient|RelatedPerson) ]; # 0..1 Who recorded the condition
  fhir:Condition.asserter [ Reference(Practitioner|PractitionerRole|Patient|RelatedPerson) ]; # 0..1 Person who asserts this condition
  fhir:Condition.stage [ # 0..* Stage/grade, usually assessed formally
    fhir:Condition.stage.summary [ CodeableConcept ]; # 0..1 Simple summary (disease specific)
    fhir:Condition.stage.assessment [ Reference(ClinicalImpression|DiagnosticReport|Observation) ], ... ; # 0..* Formal record of assessment
    fhir:Condition.stage.type [ CodeableConcept ]; # 0..1 Kind of staging
  ], ...;
  fhir:Condition.evidence [ # 0..* Supporting evidence
    fhir:Condition.evidence.code [ CodeableConcept ], ... ; # 0..* Manifestation/symptom
    fhir:Condition.evidence.detail [ Reference(Any) ], ... ; # 0..* Supporting information found elsewhere
  ], ...;
  fhir:Condition.note [ Annotation ], ... ; # 0..* Additional information about the Condition
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Condition](condition.html#Condition) |  |
| Condition.clinicalStatus | - Type changed from code to CodeableConcept - Change value set from http://hl7.org/fhir/ValueSet/condition-clinical to http://hl7.org/fhir/ValueSet/condition-clinical|4.0.1 |
| Condition.verificationStatus | - Type changed from code to CodeableConcept - Change value set from http://hl7.org/fhir/ValueSet/condition-ver-status to http://hl7.org/fhir/ValueSet/condition-ver-status|4.0.1 - Default Value "unknown" removed |
| Condition.category | - Add Binding `http://hl7.org/fhir/ValueSet/condition-category` (extensible) |
| Condition.encounter | - Added Element |
| Condition.abatement[x] | - Remove Type boolean |
| Condition.recordedDate | - Renamed from assertedDate to recordedDate |
| Condition.recorder | - Added Element |
| Condition.asserter | - Type Reference: Added Target Type PractitionerRole |
| Condition.stage | - Max Cardinality changed from 1 to \* |
| Condition.stage.type | - Added Element |
| Condition.context | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](condition.diff.xml) or [JSON](condition.diff.json).

See [R3 <--> R4 Conversion Maps](condition-version-maps.html) (status = 12 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Condition](condition-definitions.html#Condition "Condition : A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Detailed information about conditions, problems or diagnoses + Guideline: Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item + Rule: If condition is abated, then clinicalStatus must be either inactive, resolved, or remission + Rule: Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](condition-definitions.html#Condition.identifier "Condition.identifier : Business identifiers assigned to this condition by the performer or other systems which remain constant as the resource is updated and propagates from server to server.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | External Ids for this condition |
| ... [clinicalStatus](condition-definitions.html#Condition.clinicalStatus "Condition.clinicalStatus : The clinical status of the condition.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | active | recurrence | relapse | inactive | remission | resolved [Condition Clinical Status Codes](valueset-condition-clinical.html "The clinical status of the condition or diagnosis.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [verificationStatus](condition-definitions.html#Condition.verificationStatus "Condition.verificationStatus : The verification status to support the clinical status of the condition.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | unconfirmed | provisional | differential | confirmed | refuted | entered-in-error [ConditionVerificationStatus](valueset-condition-ver-status.html "The verification status to support or decline the clinical status of the condition or diagnosis.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [category](condition-definitions.html#Condition.category "Condition.category : A category assigned to the condition.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | problem-list-item | encounter-diagnosis [Condition Category Codes](valueset-condition-category.html "A category assigned to the condition.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [severity](condition-definitions.html#Condition.severity "Condition.severity : A subjective assessment of the severity of the condition as evaluated by the clinician.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Subjective severity of condition [Condition/Diagnosis Severity](valueset-condition-severity.html "A subjective assessment of the severity of the condition as evaluated by the clinician.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [code](condition-definitions.html#Condition.code "Condition.code : Identification of the condition, problem or diagnosis.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Identification of the condition, problem or diagnosis [Condition/Problem/Diagnosis Codes](valueset-condition-code.html "Identification of the condition or diagnosis.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [bodySite](condition-definitions.html#Condition.bodySite "Condition.bodySite : The anatomical location where this condition manifests itself.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location, if relevant [SNOMED CT Body Structures](valueset-body-site.html "Codes describing anatomical locations. May include laterality.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](condition-definitions.html#Condition.subject "Condition.subject : Indicates the patient or group who the condition record is associated with.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who has the condition? |
| ... [encounter](condition-definitions.html#Condition.encounter "Condition.encounter : The Encounter during which this Condition was created or to which the creation of this record is tightly associated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of |
| ... [onset[x]](condition-definitions.html#Condition.onset_x_ "Condition.onset[x] : Estimated or actual date or date-time  the condition began, in the opinion of the clinician.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Estimated or actual date, date-time, or age |
| .... onsetDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... onsetAge |  |  | [Age](datatypes.html#Age) |  |
| .... onsetPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... onsetRange |  |  | [Range](datatypes.html#Range) |  |
| .... onsetString |  |  | [string](datatypes.html#string) |  |
| ... [abatement[x]](condition-definitions.html#Condition.abatement_x_ "Condition.abatement[x] : The date or estimated date that the condition resolved or went into remission. This is called \"abatement\" because of the many overloaded connotations associated with \"remission\" or \"resolution\" - Conditions are never really resolved, but they can abate.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 |  | When in resolution/remission |
| .... abatementDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... abatementAge |  |  | [Age](datatypes.html#Age) |  |
| .... abatementPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... abatementRange |  |  | [Range](datatypes.html#Range) |  |
| .... abatementString |  |  | [string](datatypes.html#string) |  |
| ... [recordedDate](condition-definitions.html#Condition.recordedDate "Condition.recordedDate : The recordedDate represents when this particular Condition record was created in the system, which is often a system-generated date.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date record was first recorded |
| ... [recorder](condition-definitions.html#Condition.recorder "Condition.recorder : Individual who recorded the record and takes responsibility for its content.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who recorded the condition |
| ... [asserter](condition-definitions.html#Condition.asserter "Condition.asserter : Individual who is making the condition statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Person who asserts this condition |
| ... [stage](condition-definitions.html#Condition.stage "Condition.stage : Clinical stage or grade of a condition. May include formal severity assessments.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Stage/grade, usually assessed formally + Rule: Stage SHALL have summary or assessment |
| .... [summary](condition-definitions.html#Condition.stage.summary "Condition.stage.summary : A simple summary of the stage such as \"Stage 3\". The determination of the stage is disease-specific.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Simple summary (disease specific) [Condition Stage](valueset-condition-stage.html "Codes describing condition stages (e.g. Cancer stages).") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [assessment](condition-definitions.html#Condition.stage.assessment "Condition.stage.assessment : Reference to a formal record of the evidence on which the staging assessment is based.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html) | [DiagnosticReport](diagnosticreport.html) | [Observation](observation.html)) | Formal record of assessment |
| .... [type](condition-definitions.html#Condition.stage.type "Condition.stage.type : The kind of staging, such as pathological or clinical staging.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of staging [Condition Stage Type](valueset-condition-stage-type.html "Codes describing the kind of condition staging (e.g. clinical or pathological).") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [evidence](condition-definitions.html#Condition.evidence "Condition.evidence : Supporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the condition.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Supporting evidence + Rule: evidence SHALL have code or details |
| .... [code](condition-definitions.html#Condition.evidence.code "Condition.evidence.code : A manifestation or symptom that led to the recording of this condition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Manifestation/symptom [Manifestation and Symptom Codes](valueset-manifestation-or-symptom.html "Codes that describe the manifestation or symptoms of a condition.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [detail](condition-definitions.html#Condition.evidence.detail "Condition.evidence.detail : Links to other relevant information, including pathology reports.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Supporting information found elsewhere |
| ... [note](condition-definitions.html#Condition.note "Condition.note : Additional information about the Condition. This is a general notes/comments entry  for description of the Condition, its diagnosis and prognosis.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Additional information about the Condition |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Condition xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier External Ids for this condition --></identifier>
 <clinicalStatus><!-- ![??](lock.png) 0..1 CodeableConcept active | recurrence | relapse | inactive | remission | resolved --></clinicalStatus>
 <verificationStatus><!-- ![??](lock.png) 0..1 CodeableConcept unconfirmed | provisional | differential | confirmed | refuted | entered-in-error --></verificationStatus>
 <category><!-- 0..* CodeableConcept problem-list-item | encounter-diagnosis --></category>
 <severity><!-- 0..1 CodeableConcept Subjective severity of condition --></severity>
 <code><!-- 0..1 CodeableConcept Identification of the condition, problem or diagnosis --></code>
 <bodySite><!-- 0..* CodeableConcept Anatomical location, if relevant --></bodySite>
 <subject><!-- 1..1 Reference(Patient|Group) Who has the condition? --></subject>
 <encounter><!-- 0..1 Reference(Encounter) Encounter created as part of --></encounter>
 <onset[x]><!-- 0..1 dateTime|Age|Period|Range|string Estimated or actual date,  date-time, or age --></onset[x]>
 <abatement[x]><!-- ![??](lock.png) 0..1 dateTime|Age|Period|Range|string When in resolution/remission --></abatement[x]>
 <recordedDate value="[dateTime]"/><!-- 0..1 Date record was first recorded -->
 <recorder><!-- 0..1 Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) Who recorded the condition --></recorder>
 <asserter><!-- 0..1 Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) Person who asserts this condition --></asserter>
 <stage>  <!-- 0..* Stage/grade, usually assessed formally -->
  <summary><!-- ![??](lock.png) 0..1 CodeableConcept Simple summary (disease specific) --></summary>
  <assessment><!-- ![??](lock.png) 0..* Reference(ClinicalImpression|DiagnosticReport|Observation) Formal record of assessment --></assessment>
  <type><!-- 0..1 CodeableConcept Kind of staging --></type>
 </stage>
 <evidence>  <!-- 0..* Supporting evidence -->
  <code><!-- ![??](lock.png) 0..* CodeableConcept Manifestation/symptom --></code>
  <detail><!-- ![??](lock.png) 0..* Reference(Any) Supporting information found elsewhere --></detail>
 </evidence>
 <note><!-- 0..* Annotation Additional information about the Condition --></note>
</Condition>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Condition",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // External Ids for this condition
  "clinicalStatus" : { CodeableConcept }, // C? active | recurrence | relapse | inactive | remission | resolved
  "verificationStatus" : { CodeableConcept }, // C? unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
  "category" : [{ CodeableConcept }], // problem-list-item | encounter-diagnosis
  "severity" : { CodeableConcept }, // Subjective severity of condition
  "code" : { CodeableConcept }, // Identification of the condition, problem or diagnosis
  "bodySite" : [{ CodeableConcept }], // Anatomical location, if relevant
  "subject" : { Reference(Patient|Group) }, // R!  Who has the condition?
  "encounter" : { Reference(Encounter) }, // Encounter created as part of
  // onset[x]: Estimated or actual date,  date-time, or age. One of these 5:
  "onsetDateTime" : "<dateTime>",
  "onsetAge" : { Age },
  "onsetPeriod" : { Period },
  "onsetRange" : { Range },
  "onsetString" : "<string>",
  // abatement[x]: When in resolution/remission. One of these 5:
  "abatementDateTime" : "<dateTime>",
  "abatementAge" : { Age },
  "abatementPeriod" : { Period },
  "abatementRange" : { Range },
  "abatementString" : "<string>",
  "recordedDate" : "<dateTime>", // Date record was first recorded
  "recorder" : { Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) }, // Who recorded the condition
  "asserter" : { Reference(Practitioner|PractitionerRole|Patient|
   RelatedPerson) }, // Person who asserts this condition
  "stage" : [{ // Stage/grade, usually assessed formally
    "summary" : { CodeableConcept }, // C? Simple summary (disease specific)
    "assessment" : [{ Reference(ClinicalImpression|DiagnosticReport|Observation) }], // C? Formal record of assessment
    "type" : { CodeableConcept } // Kind of staging
  }],
  "evidence" : [{ // Supporting evidence
    "code" : [{ CodeableConcept }], // C? Manifestation/symptom
    "detail" : [{ Reference(Any) }] // C? Supporting information found elsewhere
  }],
  "note" : [{ Annotation }] // Additional information about the Condition
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Condition;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Condition.identifier [ Identifier ], ... ; # 0..* External Ids for this condition
  fhir:Condition.clinicalStatus [ CodeableConcept ]; # 0..1 active | recurrence | relapse | inactive | remission | resolved
  fhir:Condition.verificationStatus [ CodeableConcept ]; # 0..1 unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
  fhir:Condition.category [ CodeableConcept ], ... ; # 0..* problem-list-item | encounter-diagnosis
  fhir:Condition.severity [ CodeableConcept ]; # 0..1 Subjective severity of condition
  fhir:Condition.code [ CodeableConcept ]; # 0..1 Identification of the condition, problem or diagnosis
  fhir:Condition.bodySite [ CodeableConcept ], ... ; # 0..* Anatomical location, if relevant
  fhir:Condition.subject [ Reference(Patient|Group) ]; # 1..1 Who has the condition?
  fhir:Condition.encounter [ Reference(Encounter) ]; # 0..1 Encounter created as part of
  # Condition.onset[x] : 0..1 Estimated or actual date,  date-time, or age. One of these 5
    fhir:Condition.onsetDateTime [ dateTime ]
    fhir:Condition.onsetAge [ Age ]
    fhir:Condition.onsetPeriod [ Period ]
    fhir:Condition.onsetRange [ Range ]
    fhir:Condition.onsetString [ string ]
  # Condition.abatement[x] : 0..1 When in resolution/remission. One of these 5
    fhir:Condition.abatementDateTime [ dateTime ]
    fhir:Condition.abatementAge [ Age ]
    fhir:Condition.abatementPeriod [ Period ]
    fhir:Condition.abatementRange [ Range ]
    fhir:Condition.abatementString [ string ]
  fhir:Condition.recordedDate [ dateTime ]; # 0..1 Date record was first recorded
  fhir:Condition.recorder [ Reference(Practitioner|PractitionerRole|Patient|RelatedPerson) ]; # 0..1 Who recorded the condition
  fhir:Condition.asserter [ Reference(Practitioner|PractitionerRole|Patient|RelatedPerson) ]; # 0..1 Person who asserts this condition
  fhir:Condition.stage [ # 0..* Stage/grade, usually assessed formally
    fhir:Condition.stage.summary [ CodeableConcept ]; # 0..1 Simple summary (disease specific)
    fhir:Condition.stage.assessment [ Reference(ClinicalImpression|DiagnosticReport|Observation) ], ... ; # 0..* Formal record of assessment
    fhir:Condition.stage.type [ CodeableConcept ]; # 0..1 Kind of staging
  ], ...;
  fhir:Condition.evidence [ # 0..* Supporting evidence
    fhir:Condition.evidence.code [ CodeableConcept ], ... ; # 0..* Manifestation/symptom
    fhir:Condition.evidence.detail [ Reference(Any) ], ... ; # 0..* Supporting information found elsewhere
  ], ...;
  fhir:Condition.note [ Annotation ], ... ; # 0..* Additional information about the Condition
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Condition](condition.html#Condition) |  |
| Condition.clinicalStatus | - Type changed from code to CodeableConcept - Change value set from http://hl7.org/fhir/ValueSet/condition-clinical to http://hl7.org/fhir/ValueSet/condition-clinical|4.0.1 |
| Condition.verificationStatus | - Type changed from code to CodeableConcept - Change value set from http://hl7.org/fhir/ValueSet/condition-ver-status to http://hl7.org/fhir/ValueSet/condition-ver-status|4.0.1 - Default Value "unknown" removed |
| Condition.category | - Add Binding `http://hl7.org/fhir/ValueSet/condition-category` (extensible) |
| Condition.encounter | - Added Element |
| Condition.abatement[x] | - Remove Type boolean |
| Condition.recordedDate | - Renamed from assertedDate to recordedDate |
| Condition.recorder | - Added Element |
| Condition.asserter | - Type Reference: Added Target Type PractitionerRole |
| Condition.stage | - Max Cardinality changed from 1 to \* |
| Condition.stage.type | - Added Element |
| Condition.context | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](condition.diff.xml) or [JSON](condition.diff.json).

See [R3 <--> R4 Conversion Maps](condition-version-maps.html) (status = 12 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](condition-profiles.html) and the alternate definitions:
Master Definition [XML](condition.profile.xml.html) + [JSON](condition.profile.json.html),
[XML](xml.html) [Schema](condition.xsd)/[Schematron](condition.sch) + [JSON](json.html)
[Schema](condition.schema.json.html), [ShEx](condition.shex.html) (for [Turtle](rdf.html)) + [see the extensions](condition-profiles.html) & the [dependency analysis](condition-dependencies.html)

### 9.2.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Condition.clinicalStatus | The clinical status of the condition or diagnosis. | [Required](terminologies.html#required) | [ConditionClinicalStatusCodes](valueset-condition-clinical.html) |
| Condition.verificationStatus | The verification status to support or decline the clinical status of the condition or diagnosis. | [Required](terminologies.html#required) | [ConditionVerificationStatus](valueset-condition-ver-status.html) |
| Condition.category | A category assigned to the condition. | [Extensible](terminologies.html#extensible) | [ConditionCategoryCodes](valueset-condition-category.html) |
| Condition.severity | A subjective assessment of the severity of the condition as evaluated by the clinician. | [Preferred](terminologies.html#preferred) | [Condition/DiagnosisSeverity](valueset-condition-severity.html) |
| Condition.code | Identification of the condition or diagnosis. | [Example](terminologies.html#example) | [Condition/Problem/DiagnosisCodes](valueset-condition-code.html) |
| Condition.bodySite | Codes describing anatomical locations. May include laterality. | [Example](terminologies.html#example) | [SNOMEDCTBodyStructures](valueset-body-site.html) |
| Condition.stage.summary | Codes describing condition stages (e.g. Cancer stages). | [Example](terminologies.html#example) | [ConditionStage](valueset-condition-stage.html) |
| Condition.stage.type | Codes describing the kind of condition staging (e.g. clinical or pathological). | [Example](terminologies.html#example) | [ConditionStageType](valueset-condition-stage-type.html) |
| Condition.evidence.code | Codes that describe the manifestation or symptoms of a condition. | [Example](terminologies.html#example) | [ManifestationAndSymptomCodes](valueset-manifestation-or-symptom.html) |

### 9.2.3.2 Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **con-1** | [Rule](conformance-rules.html#rule) | Condition.stage | Stage SHALL have summary or assessment | summary.exists() or assessment.exists() |
| **con-2** | [Rule](conformance-rules.html#rule) | Condition.evidence | evidence SHALL have code or details | code.exists() or detail.exists() |
| **con-3** | [Guideline](conformance-rules.html#best-practice) | (base) | Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item | clinicalStatus.exists() or verificationStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-ver-status' and code = 'entered-in-error').exists() or category.select($this='problem-list-item').empty() This is (only) a best practice guideline because: Most systems will expect a clinicalStatus to be valued for problem-list-items that are managed over time, but might not need a clinicalStatus for point in time encounter-diagnosis. |
| **con-4** | [Rule](conformance-rules.html#rule) | (base) | If condition is abated, then clinicalStatus must be either inactive, resolved, or remission | abatement.empty() or clinicalStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-clinical' and (code='resolved' or code='remission' or code='inactive')).exists() |
| **con-5** | [Rule](conformance-rules.html#rule) | (base) | Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error | verificationStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-ver-status' and code='entered-in-error').empty() or clinicalStatus.empty() |

### 9.2.3.3 Use of Condition.code

Many of the code systems used for coding conditions will provide codes that define not only the condition itself, but may
also specify a particular stage, location, or causality as part of the code. This is particularly true if
SNOMED CT is used for the condition, and especially if expressions are allowed.

The Condition.code may also include such concepts as "history of X" and "good health", where it is useful or appropriate to make such assertions.
It can also be used to capture "risk of" and "fear of", in addition to physical conditions, as well as "no known problems" or "negated" conditions (e.g., "no X" or "no history of X" - see the following section for "No Known Problems" and Negated Conditions).

When the Condition.code specifies additional properties of the condition, the other properties are not given
a value - instead, the value must be understood from the Condition.code.

### 9.2.3.4 "No Known Problems" and Negated Conditions

**Conditions/Problems Not Reviewed, Not Asked**

When a sending system does not have any information about conditions/problems being reviewed or the statement is about conditions/problems not yet being asked, then the [List](list.html) resource should be used to indicate the List.emptyReason.code="notasked".

**Conditions/Problems Reviewed, None Identified**

Systems may use the List.emptyReason when a statement is about the full scope of the list (i.e. the patient has no conditions/problems of any type). However, it may be preferred to use a code for "no known problems" (e.g., SNOMED CT: 160245001 |No current problems or disability (situation)|), so that all condition/problem data will be available and queryable from Condition resource instances.

Also note that care should be used when adding new Condition resources to a list to ensure that any negation statements that are voided by the addition of a new record are removed from the list. E.g. If the list contains a "no known problems" record and you add a "diabetes" condition record, then be sure that you remove the "no known problems" record.

> **Trial-Use Note:**
> There are two primary ways of reporting "no known problems" in the current specification: using the CodeableConcept,
> as described above, or using the [List](list.html) resource with emptyReason. During the STU period, [feedback ![](external.png)](http://hl7.org/fhir-issues) is sought regarding the preferred approach.
>
> Provide feedback [here ![](external.png)](http://hl7.org/fhir-issues).

**Patient Denies Condition**

When the patient denies a condition, that can be annotated in the Condition.note element.

### 9.2.3.5 Assertions of Condition Absence

Generally, electronic records do not contain assertions of conditions that a patient does not have. There are however two exceptions:

- It is appropriate to capture a "refuted" Condition record if the patient or anyone else had reason to believe that a patient did have a condition for a period of time and subsequent evidence has demonstrated that belief was mistaken. In this case, a concrete statement acknowledging the belief as well as the refutation of it is useful.
- It is common as part of checklists prior to admission, surgery, enrollment in trials, etc. to ask questions such as "are you pregnant", "do you have a history of hypertension", etc. This information should NOT be captured using the Condition resource but should instead be captured using QuestionnaireResponse or Observation. In this case, the combination of the question and answer would convey that a particular condition was not present.

### 9.2.3.6 Use of Condition.evidence

The Condition.evidence provides the basis for whatever is present in Condition.code.

### 9.2.3.7 Use of Condition.abatementRange

A range is used to communicate age period of subject at time of abatement.

### 9.2.3.8 Use of Condition.asserter

If the data enterer is different from the asserter and needs to be known, this could be captured using a Provenance instance pointing to the Condition.
For example, it is possible that a nurse records the condition on behalf of a physician. The physician is taking responsibility, despite the nurse entering it into the medical record.

### 9.2.3.9 Use of Condition.clinicalStatus

The Condition.stage and Condition.clinicalStatus may have interdependencies. For example, some "stages" of cancer, etc. will be different for a remission than for the initial occurrence.

### 9.2.3.10 Diagnosis Role and Rank within an Encounter

To represent the role of the diagnosis within an encounter, such as admission diagnosis or discharge diagnosis, use [Encounter.diagnosis.role](encounter-definitions.html#Encounter.diagnosis.role).

To represent the numeric ranking of the diagnosis within an encounter, such as primary, secondary, or tertiary, use [Encounter.diagnosis.rank](encounter-definitions.html#Encounter.diagnosis.rank).

### 9.2.3.11 Known Issue

A known issue exists with circular references between Condition and ClinicalImpression, which is due to the low maturity level of ClinicalImpression. The Patient Care work group intends to address this issue when ClinicalImpression is considered substantially complete and ready for implementation.

## 9.2.4 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| abatement-age | [quantity](search.html#quantity) | Abatement as age or age range | Condition.abatement.as(Age) | Condition.abatement.as(Range) |  |
| abatement-date | [date](search.html#date) | Date-related abatements (dateTime and period) | Condition.abatement.as(dateTime) | Condition.abatement.as(Period) |  |
| abatement-string | [string](search.html#string) | Abatement as a string | Condition.abatement.as(string) |  |
| asserter | [reference](search.html#reference) | Person who asserts this condition | Condition.asserter ([Practitioner](practitioner.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |  |
| body-site | [token](search.html#token) | Anatomical location, if relevant | Condition.bodySite |  |
| category | [token](search.html#token) | The category of the condition | Condition.category |  |
| clinical-status | [token](search.html#token) | The clinical status of the condition | Condition.clinicalStatus |  |
| code | [token](search.html#token) | Code for the condition | Condition.code | [13 Resources](searchparameter-registry.html#clinical-code) |
| encounter | [reference](search.html#reference) | Encounter created as part of | Condition.encounter ([Encounter](encounter.html)) |  |
| evidence | [token](search.html#token) | Manifestation/symptom | Condition.evidence.code |  |
| evidence-detail | [reference](search.html#reference) | Supporting information found elsewhere | Condition.evidence.detail (Any) |  |
| identifier | [token](search.html#token) | A unique identifier of the condition record | Condition.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) |
| onset-age | [quantity](search.html#quantity) | Onsets as age or age range | Condition.onset.as(Age) | Condition.onset.as(Range) |  |
| onset-date | [date](search.html#date) | Date related onsets (dateTime and Period) | Condition.onset.as(dateTime) | Condition.onset.as(Period) |  |
| onset-info | [string](search.html#string) | Onsets as a string | Condition.onset.as(string) |  |
| patient | [reference](search.html#reference) | Who has the condition? | Condition.subject.where(resolve() is Patient) ([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) |
| recorded-date | [date](search.html#date) | Date record was first recorded | Condition.recordedDate |  |
| severity | [token](search.html#token) | The severity of the condition | Condition.severity |  |
| stage | [token](search.html#token) | Simple summary (disease specific) | Condition.stage.summary |  |
| subject | [reference](search.html#reference) | Who has the condition? | Condition.subject ([Group](group.html), [Patient](patient.html)) |  |
| verification-status | [token](search.html#token) | unconfirmed | provisional | differential | confirmed | refuted | entered-in-error | Condition.verificationStatus |  |
