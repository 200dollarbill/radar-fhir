---
id: encounter
title: Encounter
source_url: https://hl7.org/fhir/R4/encounter.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:47Z'
sha256: 94cc0a5d480415449ed0559b19c0056fbd5937b4eea95ccd7a2dd0f43bcc143b
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/encounter.html) [R4B](http://hl7.org/fhir/R4B/encounter.html) **R4** [R3](http://hl7.org/fhir/STU3/encounter.html) [R2](http://hl7.org/fhir/DSTU2/encounter.html)

- [Content](#)
- [Examples](encounter-examples.html)
- [Detailed Descriptions](encounter-definitions.html)
- [Mappings](encounter-mappings.html)
- [Profiles & Extensions](encounter-profiles.html)
- [Operations](encounter-operations.html)
- [R3 Conversions](encounter-version-maps.html)

# 8.11 Resource Encounter - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Administration](http://www.hl7.org/Special/committees/pafm/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) |

An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.

## 8.11.1 Scope and Usage

A patient encounter is further characterized by the setting in which it takes place. Amongst them are ambulatory,
emergency, home health, inpatient and virtual encounters. An Encounter encompasses the lifecycle from pre-admission,
the actual encounter (for ambulatory encounters), and admission, stay and discharge (for inpatient encounters).
During the encounter the patient may move from practitioner to practitioner and location to location.

Because of the broad scope of Encounter, not all elements will be relevant in all settings. For this reason,
admission/discharge related information is kept in a separate Hospitalization component within Encounter.
The *class* element is used to distinguish between these settings, which will guide further validation and
application of business rules.

There is also substantial variance from organization to organization (and between jurisdictions and countries)
on which business events translate to the start of a new Encounter, or what level of aggregation is used for Encounter. For example, each
single visit of a practitioner during a hospitalization may lead to a new instance of Encounter, but depending on
local practice and the systems involved, it may well be that this is aggregated to a single instance for a whole hospitalization.
Even more aggregation may occur where jurisdictions introduce groups of Encounters for financial or other reasons.
Encounters can be aggregated or grouped under other Encounters using the *partOf* element.
See [below](#examples) for examples.

Encounter instances may exist before the actual encounter takes place to convey pre-admission information, including
using Encounters elements to reflect the planned start date or planned encounter locations. In
this case the *status* element is set to 'planned'.

The Hospitalization component is intended to store the extended information relating to a hospitalization event.
It is always expected to be the same period as the encounter itself. Where the period is different, another
encounter instance should be used to capture this information as a partOf this encounter instance.

The Procedure and encounter have references to each other, and these should be to different procedures;
one for the procedure that was performed during the encounter (stored in Procedure.encounter), and another for cases
where an encounter is a result of another procedure (stored in Encounter.indication) such as a follow-up encounter to
resolve complications from an earlier procedure.

### 8.11.1.1 Status Management

During the life-cycle of an encounter it will pass through many statuses. Typically these are in order or the
organization's workflow: planned, in-progress, finished/cancelled.  
This status information is often used for other things, and often an analysis of the status history is required.
This could be done by scanning through all the versions of the encounter, checking the period of each,
and then doing some form of post processing. To ease the burden of this (or where a system doesn't support resource
histories) a status history component is included.

There is no direct indication purely by the status field as to whether an encounter is considered "admitted".  
The context of the encounter and business practices/policies/workflows/types can influence this definition.
(e.g., acute care facility, aged care center, outpatient clinic, emergency department, community-based clinic).  
Statuses of "arrived", "triaged" or "in progress" could be considered the start of the admission, and also have the
presence of the hospitalization sub-component entered.

The "on leave" status might or might not be a part of the admission, for example if the patient
was permitted to go home for a weekend or some other form of external event.  
The location is also likely to be filled in with a location status of "present".  
For other examples such as an outpatient visit (day procedure - colonoscopy), the patient could also be
considered to be admitted, hence the encounter doesn't have a fixed definition of admitted.
At a minimum, we do believe that a patient IS admitted when the status is in-progress.

## 8.11.2 Boundaries and Relationships

The Encounter resource is not to be used to store appointment information, the Appointment resource is intended to be used for that.
Note that in many systems outpatient encounters (which are in scope for Encounter) and Appointment are used
concurrently. In FHIR, Appointment is used for establishing a date for the encounter, while Encounter is
applicable to information about the actual Encounter, i.e., the patient showing up.  
As such, an encounter in the "planned" status is not identical to the appointment that scheduled it,
but it is the encounter prior to its actual occurrence, with the expectation that encounter will be
updated as it progresses to completion. Patient arrival at a location does not necessarily mean the
start of the encounter (e.g. a patient arrives an hour earlier than he is actually seen by a practitioner).

An appointment is normally used for the planning stage of an appointment, searching, locating an available time, then
making the appointment. Once this process is completed and the appointment is about to start, then the appointment
will be marked as fulfilled, and linked to the newly created encounter.  
This new encounter may start in an "arrived" status when they are admitted at a location of the facility, and then will
move to the ward where another part-of encounter may begin.

Communication resources are used for a simultaneous interaction between a practitioner and a patient where there is no
direct contact. Examples include a phone message, or transmission of some correspondence documentation.  
There is no duration recorded for a communication resource, but it could contain sent and received times.

Standard Extension: **Associated Encounter**  
This extension should be used to reference an encounter where there is no property that already defines this association on the resource.

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Condition](condition.html#Condition), [Contract](contract.html#Contract), [DeviceRequest](devicerequest.html#DeviceRequest), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentReference](documentreference.html#DocumentReference), itself, [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [List](list.html#List), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [NutritionOrder](nutritionorder.html#NutritionOrder), [Observation](observation.html#Observation), [Procedure](procedure.html#Procedure), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [ServiceRequest](servicerequest.html#ServiceRequest), [Task](task.html#Task) and [VisionPrescription](visionprescription.html#VisionPrescription)

## 8.11.3 Resource Content

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
| .. [Encounter](encounter-definitions.html#Encounter "Encounter : An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | An interaction during which services are provided to the patient Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](encounter-definitions.html#Encounter.identifier "Encounter.identifier : Identifier(s) by which this encounter is known.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Identifier(s) by which this encounter is known |
| ... [status](encounter-definitions.html#Encounter.status "Encounter.status : planned | arrived | triaged | in-progress | onleave | finished | cancelled +.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled + [EncounterStatus](valueset-encounter-status.html "Current state of the encounter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [statusHistory](encounter-definitions.html#Encounter.statusHistory "Encounter.statusHistory : The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store them.") |  | 0..\* | [BackboneElement](backboneelement.html) | List of past encounter statuses |
| .... [status](encounter-definitions.html#Encounter.statusHistory.status "Encounter.statusHistory.status : planned | arrived | triaged | in-progress | onleave | finished | cancelled +.") |  | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled + [EncounterStatus](valueset-encounter-status.html "Current state of the encounter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [period](encounter-definitions.html#Encounter.statusHistory.period "Encounter.statusHistory.period : The time that the episode was in the specified status.") |  | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified status |
| ... [class](encounter-definitions.html#Encounter.class "Encounter.class : Concepts representing classification of patient encounter such as ambulatory (outpatient), inpatient, emergency, home health or others due to local variations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Coding](datatypes.html#Coding) | Classification of patient encounter [V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html "Classification of the encounter.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [classHistory](encounter-definitions.html#Encounter.classHistory "Encounter.classHistory : The class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatient.") |  | 0..\* | [BackboneElement](backboneelement.html) | List of past encounter classes |
| .... [class](encounter-definitions.html#Encounter.classHistory.class "Encounter.classHistory.class : inpatient | outpatient | ambulatory | emergency +.") |  | 1..1 | [Coding](datatypes.html#Coding) | inpatient | outpatient | ambulatory | emergency + [V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html "Classification of the encounter.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [period](encounter-definitions.html#Encounter.classHistory.period "Encounter.classHistory.period : The time that the episode was in the specified class.") |  | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified class |
| ... [type](encounter-definitions.html#Encounter.type "Encounter.type : Specific type of encounter (e.g. e-mail consultation, surgical day-care, skilled nursing, rehabilitation).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of encounter [Encounter type](valueset-encounter-type.html "The type of encounter.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [serviceType](encounter-definitions.html#Encounter.serviceType "Encounter.serviceType : Broad categorization of the service that is to be provided (e.g. cardiology).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of service [Service type](valueset-service-type.html "Broad categorization of the service that is to be provided.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [priority](encounter-definitions.html#Encounter.priority "Encounter.priority : Indicates the urgency of the encounter.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Indicates the urgency of the encounter [v3 Code System ActPriority](v3/ActPriority/vs.html "Indicates the urgency of the encounter.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](encounter-definitions.html#Encounter.subject "Encounter.subject : The patient or group present at the encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | The patient or group present at the encounter |
| ... [episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare "Encounter.episodeOfCare : Where a specific encounter should be classified as a part of a specific episode(s) of care this field should be used. This association can facilitate grouping of related encounters together for a specific purpose, such as government reporting, issue tracking, association via a common problem.  The association is recorded on the encounter as these are typically created after the episode of care and grouped on entry rather than editing the episode of care to append another encounter to it (the episode of care could span years).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html)) | Episode(s) of care that this encounter should be recorded against |
| ... [basedOn](encounter-definitions.html#Encounter.basedOn "Encounter.basedOn : The request this encounter satisfies (e.g. incoming referral or procedure request).") |  | 0..\* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | The ServiceRequest that initiated this encounter |
| ... [participant](encounter-definitions.html#Encounter.participant "Encounter.participant : The list of people responsible for providing the service.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | List of participants involved in the encounter |
| .... [type](encounter-definitions.html#Encounter.participant.type "Encounter.participant.type : Role of participant in encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in encounter [Participant type](valueset-encounter-participant-type.html "Role of participant in encounter.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [period](encounter-definitions.html#Encounter.participant.period "Encounter.participant.period : The period of time that the specified participant participated in the encounter. These can overlap or be sub-sets of the overall encounter's period.") |  | 0..1 | [Period](datatypes.html#Period) | Period of time during the encounter that the participant participated |
| .... [individual](encounter-definitions.html#Encounter.participant.individual "Encounter.participant.individual : Persons involved in the encounter other than the patient.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html)) | Persons involved in the encounter other than the patient |
| ... [appointment](encounter-definitions.html#Encounter.appointment "Encounter.appointment : The appointment that scheduled this encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Appointment](appointment.html)) | The appointment that scheduled this encounter |
| ... [period](encounter-definitions.html#Encounter.period "Encounter.period : The start and end time of the encounter.") |  | 0..1 | [Period](datatypes.html#Period) | The start and end time of the encounter |
| ... [length](encounter-definitions.html#Encounter.length "Encounter.length : Quantity of time the encounter lasted. This excludes the time during leaves of absence.") |  | 0..1 | [Duration](datatypes.html#Duration) | Quantity of time the encounter lasted (less time absent) |
| ... [reasonCode](encounter-definitions.html#Encounter.reasonCode "Encounter.reasonCode : Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosis.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason the encounter takes place [Encounter Reason Codes](valueset-encounter-reason.html "Reason why the encounter takes place.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [reasonReference](encounter-definitions.html#Encounter.reasonReference "Encounter.reasonReference : Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosis.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html) | [Observation](observation.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | Reason the encounter takes place (reference) |
| ... [diagnosis](encounter-definitions.html#Encounter.diagnosis "Encounter.diagnosis : The list of diagnosis relevant to this encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | The list of diagnosis relevant to this encounter |
| .... [condition](encounter-definitions.html#Encounter.diagnosis.condition "Encounter.diagnosis.condition : Reason the encounter takes place, as specified using information from another resource. For admissions, this is the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a Procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html)) | The diagnosis or procedure relevant to the encounter |
| .... [use](encounter-definitions.html#Encounter.diagnosis.use "Encounter.diagnosis.use : Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …).") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …) [DiagnosisRole](valueset-diagnosis-role.html "The type of diagnosis this condition represents.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [rank](encounter-definitions.html#Encounter.diagnosis.rank "Encounter.diagnosis.rank : Ranking of the diagnosis (for each role type).") |  | 0..1 | [positiveInt](datatypes.html#positiveInt) | Ranking of the diagnosis (for each role type) |
| ... [account](encounter-definitions.html#Encounter.account "Encounter.account : The set of accounts that may be used for billing for this Encounter.") |  | 0..\* | [Reference](references.html#Reference)([Account](account.html)) | The set of accounts that may be used for billing for this Encounter |
| ... [hospitalization](encounter-definitions.html#Encounter.hospitalization "Encounter.hospitalization : Details about the admission to a healthcare service.") |  | 0..1 | [BackboneElement](backboneelement.html) | Details about the admission to a healthcare service |
| .... [preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier "Encounter.hospitalization.preAdmissionIdentifier : Pre-admission identifier.") |  | 0..1 | [Identifier](datatypes.html#Identifier) | Pre-admission identifier |
| .... [origin](encounter-definitions.html#Encounter.hospitalization.origin "Encounter.hospitalization.origin : The location/organization from which the patient came before admission.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | The location/organization from which the patient came before admission |
| .... [admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource "Encounter.hospitalization.admitSource : From where patient was admitted (physician referral, transfer).") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | From where patient was admitted (physician referral, transfer) [Admit source](valueset-encounter-admit-source.html "From where the patient was admitted.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission "Encounter.hospitalization.reAdmission : Whether this hospitalization is a readmission and why if known.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission [v2 RE-ADMISSION INDICATOR](v2/0092/index.html "The reason for re-admission of this hospitalization encounter.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference "Encounter.hospitalization.dietPreference : Diet preferences reported by the patient.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Diet preferences reported by the patient [Diet](valueset-encounter-diet.html "Medical, cultural or ethical food preferences to help with catering requirements.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy "Encounter.hospitalization.specialCourtesy : Special courtesies (VIP, board member).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Special courtesies (VIP, board member) [Special courtesy](valueset-encounter-special-courtesy.html "Special courtesies.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement "Encounter.hospitalization.specialArrangement : Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other things.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Wheelchair, translator, stretcher, etc. [Special arrangements](valueset-encounter-special-arrangements.html "Special arrangements.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [destination](encounter-definitions.html#Encounter.hospitalization.destination "Encounter.hospitalization.destination : Location/organization to which the patient is discharged.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | Location/organization to which the patient is discharged |
| .... [dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition "Encounter.hospitalization.dischargeDisposition : Category or kind of location after discharge.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category or kind of location after discharge [Discharge disposition](valueset-encounter-discharge-disposition.html "Discharge Disposition.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [location](encounter-definitions.html#Encounter.location "Encounter.location : List of locations where  the patient has been during this encounter.") |  | 0..\* | [BackboneElement](backboneelement.html) | List of locations where the patient has been |
| .... [location](encounter-definitions.html#Encounter.location.location "Encounter.location.location : The location where the encounter takes place.") |  | 1..1 | [Reference](references.html#Reference)([Location](location.html)) | Location the encounter takes place |
| .... [status](encounter-definitions.html#Encounter.location.status "Encounter.location.status : The status of the participants' presence at the specified location during the period specified. If the participant is no longer at the location, then the period will have an end date/time.") |  | 0..1 | [code](datatypes.html#code) | planned | active | reserved | completed [EncounterLocationStatus](valueset-encounter-location-status.html "The status of the location.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [physicalType](encounter-definitions.html#Encounter.location.physicalType "Encounter.location.physicalType : This will be used to specify the required levels (bed/ward/room/etc.) desired to be recorded to simplify either messaging or query.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The physical type of the location (usually the level in the location hierachy - bed room ward etc.) [Location type](valueset-location-physical-type.html "Physical form of the location.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [period](encounter-definitions.html#Encounter.location.period "Encounter.location.period : Time period during which the patient was present at the location.") |  | 0..1 | [Period](datatypes.html#Period) | Time period during which the patient was present at the location |
| ... [serviceProvider](encounter-definitions.html#Encounter.serviceProvider "Encounter.serviceProvider : The organization that is primarily responsible for this Encounter's services. This MAY be the same as the organization on the Patient record, however it could be different, such as if the actor performing the services was from an external organization (which may be billed seperately) for an external consultation.  Refer to the example bundle showing an abbreviated set of Encounters for a colonoscopy.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization (facility) responsible for this encounter |
| ... [partOf](encounter-definitions.html#Encounter.partOf "Encounter.partOf : Another Encounter of which this encounter is a part of (administratively or in time).") |  | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Another Encounter this encounter is part of |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Encounter xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Identifier(s) by which this encounter is known --></identifier>
 <status value="[code]"/><!-- 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled + -->
 <statusHistory>  <!-- 0..* List of past encounter statuses -->
  <status value="[code]"/><!-- 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled + -->
  <period><!-- 1..1 Period The time that the episode was in the specified status --></period>
 </statusHistory>
 <class><!-- 1..1 Coding Classification of patient encounter --></class>
 <classHistory>  <!-- 0..* List of past encounter classes -->
  <class><!-- 1..1 Coding inpatient | outpatient | ambulatory | emergency + --></class>
  <period><!-- 1..1 Period The time that the episode was in the specified class --></period>
 </classHistory>
 <type><!-- 0..* CodeableConcept Specific type of encounter --></type>
 <serviceType><!-- 0..1 CodeableConcept Specific type of service --></serviceType>
 <priority><!-- 0..1 CodeableConcept Indicates the urgency of the encounter --></priority>
 <subject><!-- 0..1 Reference(Patient|Group) The patient or group present at the encounter --></subject>
 <episodeOfCare><!-- 0..* Reference(EpisodeOfCare) Episode(s) of care that this encounter should be recorded against --></episodeOfCare>
 <basedOn><!-- 0..* Reference(ServiceRequest) The ServiceRequest that initiated this encounter --></basedOn>
 <participant>  <!-- 0..* List of participants involved in the encounter -->
  <type><!-- 0..* CodeableConcept Role of participant in encounter --></type>
  <period><!-- 0..1 Period Period of time during the encounter that the participant participated --></period>
  <individual><!-- 0..1 Reference(Practitioner|PractitionerRole|RelatedPerson) Persons involved in the encounter other than the patient --></individual>
 </participant>
 <appointment><!-- 0..* Reference(Appointment) The appointment that scheduled this encounter --></appointment>
 <period><!-- 0..1 Period The start and end time of the encounter --></period>
 <length><!-- 0..1 Duration Quantity of time the encounter lasted (less time absent) --></length>
 <reasonCode><!-- 0..* CodeableConcept Coded reason the encounter takes place --></reasonCode>
 <reasonReference><!-- 0..* Reference(Condition|Procedure|Observation|
   ImmunizationRecommendation) Reason the encounter takes place (reference) --></reasonReference>
 <diagnosis>  <!-- 0..* The list of diagnosis relevant to this encounter -->
  <condition><!-- 1..1 Reference(Condition|Procedure) The diagnosis or procedure relevant to the encounter --></condition>
  <use><!-- 0..1 CodeableConcept Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦) --></use>
  <rank value="[positiveInt]"/><!-- 0..1 Ranking of the diagnosis (for each role type) -->
 </diagnosis>
 <account><!-- 0..* Reference(Account) The set of accounts that may be used for billing for this Encounter --></account>
 <hospitalization>  <!-- 0..1 Details about the admission to a healthcare service -->
  <preAdmissionIdentifier><!-- 0..1 Identifier Pre-admission identifier --></preAdmissionIdentifier>
  <origin><!-- 0..1 Reference(Location|Organization) The location/organization from which the patient came before admission --></origin>
  <admitSource><!-- 0..1 CodeableConcept From where patient was admitted (physician referral, transfer) --></admitSource>
  <reAdmission><!-- 0..1 CodeableConcept The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission --></reAdmission>
  <dietPreference><!-- 0..* CodeableConcept Diet preferences reported by the patient --></dietPreference>
  <specialCourtesy><!-- 0..* CodeableConcept Special courtesies (VIP, board member) --></specialCourtesy>
  <specialArrangement><!-- 0..* CodeableConcept Wheelchair, translator, stretcher, etc. --></specialArrangement>
  <destination><!-- 0..1 Reference(Location|Organization) Location/organization to which the patient is discharged --></destination>
  <dischargeDisposition><!-- 0..1 CodeableConcept Category or kind of location after discharge --></dischargeDisposition>
 </hospitalization>
 <location>  <!-- 0..* List of locations where the patient has been -->
  <location><!-- 1..1 Reference(Location) Location the encounter takes place --></location>
  <status value="[code]"/><!-- 0..1 planned | active | reserved | completed -->
  <physicalType><!-- 0..1 CodeableConcept The physical type of the location (usually the level in the location hierachy - bed room ward etc.) --></physicalType>
  <period><!-- 0..1 Period Time period during which the patient was present at the location --></period>
 </location>
 <serviceProvider><!-- 0..1 Reference(Organization) The organization (facility) responsible for this encounter --></serviceProvider>
 <partOf><!-- 0..1 Reference(Encounter) Another Encounter this encounter is part of --></partOf>
</Encounter>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Encounter",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Identifier(s) by which this encounter is known
  "status" : "<code>", // R!  planned | arrived | triaged | in-progress | onleave | finished | cancelled +
  "statusHistory" : [{ // List of past encounter statuses
    "status" : "<code>", // R!  planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    "period" : { Period } // R!  The time that the episode was in the specified status
  }],
  "class" : { Coding }, // R!  Classification of patient encounter
  "classHistory" : [{ // List of past encounter classes
    "class" : { Coding }, // R!  inpatient | outpatient | ambulatory | emergency +
    "period" : { Period } // R!  The time that the episode was in the specified class
  }],
  "type" : [{ CodeableConcept }], // Specific type of encounter
  "serviceType" : { CodeableConcept }, // Specific type of service
  "priority" : { CodeableConcept }, // Indicates the urgency of the encounter
  "subject" : { Reference(Patient|Group) }, // The patient or group present at the encounter
  "episodeOfCare" : [{ Reference(EpisodeOfCare) }], // Episode(s) of care that this encounter should be recorded against
  "basedOn" : [{ Reference(ServiceRequest) }], // The ServiceRequest that initiated this encounter
  "participant" : [{ // List of participants involved in the encounter
    "type" : [{ CodeableConcept }], // Role of participant in encounter
    "period" : { Period }, // Period of time during the encounter that the participant participated
    "individual" : { Reference(Practitioner|PractitionerRole|RelatedPerson) } // Persons involved in the encounter other than the patient
  }],
  "appointment" : [{ Reference(Appointment) }], // The appointment that scheduled this encounter
  "period" : { Period }, // The start and end time of the encounter
  "length" : { Duration }, // Quantity of time the encounter lasted (less time absent)
  "reasonCode" : [{ CodeableConcept }], // Coded reason the encounter takes place
  "reasonReference" : [{ Reference(Condition|Procedure|Observation|
   ImmunizationRecommendation) }], // Reason the encounter takes place (reference)
  "diagnosis" : [{ // The list of diagnosis relevant to this encounter
    "condition" : { Reference(Condition|Procedure) }, // R!  The diagnosis or procedure relevant to the encounter
    "use" : { CodeableConcept }, // Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)
    "rank" : "<positiveInt>" // Ranking of the diagnosis (for each role type)
  }],
  "account" : [{ Reference(Account) }], // The set of accounts that may be used for billing for this Encounter
  "hospitalization" : { // Details about the admission to a healthcare service
    "preAdmissionIdentifier" : { Identifier }, // Pre-admission identifier
    "origin" : { Reference(Location|Organization) }, // The location/organization from which the patient came before admission
    "admitSource" : { CodeableConcept }, // From where patient was admitted (physician referral, transfer)
    "reAdmission" : { CodeableConcept }, // The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
    "dietPreference" : [{ CodeableConcept }], // Diet preferences reported by the patient
    "specialCourtesy" : [{ CodeableConcept }], // Special courtesies (VIP, board member)
    "specialArrangement" : [{ CodeableConcept }], // Wheelchair, translator, stretcher, etc.
    "destination" : { Reference(Location|Organization) }, // Location/organization to which the patient is discharged
    "dischargeDisposition" : { CodeableConcept } // Category or kind of location after discharge
  },
  "location" : [{ // List of locations where the patient has been
    "location" : { Reference(Location) }, // R!  Location the encounter takes place
    "status" : "<code>", // planned | active | reserved | completed
    "physicalType" : { CodeableConcept }, // The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    "period" : { Period } // Time period during which the patient was present at the location
  }],
  "serviceProvider" : { Reference(Organization) }, // The organization (facility) responsible for this encounter
  "partOf" : { Reference(Encounter) } // Another Encounter this encounter is part of
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Encounter;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Encounter.identifier [ Identifier ], ... ; # 0..* Identifier(s) by which this encounter is known
  fhir:Encounter.status [ code ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
  fhir:Encounter.statusHistory [ # 0..* List of past encounter statuses
    fhir:Encounter.statusHistory.status [ code ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    fhir:Encounter.statusHistory.period [ Period ]; # 1..1 The time that the episode was in the specified status
  ], ...;
  fhir:Encounter.class [ Coding ]; # 1..1 Classification of patient encounter
  fhir:Encounter.classHistory [ # 0..* List of past encounter classes
    fhir:Encounter.classHistory.class [ Coding ]; # 1..1 inpatient | outpatient | ambulatory | emergency +
    fhir:Encounter.classHistory.period [ Period ]; # 1..1 The time that the episode was in the specified class
  ], ...;
  fhir:Encounter.type [ CodeableConcept ], ... ; # 0..* Specific type of encounter
  fhir:Encounter.serviceType [ CodeableConcept ]; # 0..1 Specific type of service
  fhir:Encounter.priority [ CodeableConcept ]; # 0..1 Indicates the urgency of the encounter
  fhir:Encounter.subject [ Reference(Patient|Group) ]; # 0..1 The patient or group present at the encounter
  fhir:Encounter.episodeOfCare [ Reference(EpisodeOfCare) ], ... ; # 0..* Episode(s) of care that this encounter should be recorded against
  fhir:Encounter.basedOn [ Reference(ServiceRequest) ], ... ; # 0..* The ServiceRequest that initiated this encounter
  fhir:Encounter.participant [ # 0..* List of participants involved in the encounter
    fhir:Encounter.participant.type [ CodeableConcept ], ... ; # 0..* Role of participant in encounter
    fhir:Encounter.participant.period [ Period ]; # 0..1 Period of time during the encounter that the participant participated
    fhir:Encounter.participant.individual [ Reference(Practitioner|PractitionerRole|RelatedPerson) ]; # 0..1 Persons involved in the encounter other than the patient
  ], ...;
  fhir:Encounter.appointment [ Reference(Appointment) ], ... ; # 0..* The appointment that scheduled this encounter
  fhir:Encounter.period [ Period ]; # 0..1 The start and end time of the encounter
  fhir:Encounter.length [ Duration ]; # 0..1 Quantity of time the encounter lasted (less time absent)
  fhir:Encounter.reasonCode [ CodeableConcept ], ... ; # 0..* Coded reason the encounter takes place
  fhir:Encounter.reasonReference [ Reference(Condition|Procedure|Observation|ImmunizationRecommendation) ], ... ; # 0..* Reason the encounter takes place (reference)
  fhir:Encounter.diagnosis [ # 0..* The list of diagnosis relevant to this encounter
    fhir:Encounter.diagnosis.condition [ Reference(Condition|Procedure) ]; # 1..1 The diagnosis or procedure relevant to the encounter
    fhir:Encounter.diagnosis.use [ CodeableConcept ]; # 0..1 Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)
    fhir:Encounter.diagnosis.rank [ positiveInt ]; # 0..1 Ranking of the diagnosis (for each role type)
  ], ...;
  fhir:Encounter.account [ Reference(Account) ], ... ; # 0..* The set of accounts that may be used for billing for this Encounter
  fhir:Encounter.hospitalization [ # 0..1 Details about the admission to a healthcare service
    fhir:Encounter.hospitalization.preAdmissionIdentifier [ Identifier ]; # 0..1 Pre-admission identifier
    fhir:Encounter.hospitalization.origin [ Reference(Location|Organization) ]; # 0..1 The location/organization from which the patient came before admission
    fhir:Encounter.hospitalization.admitSource [ CodeableConcept ]; # 0..1 From where patient was admitted (physician referral, transfer)
    fhir:Encounter.hospitalization.reAdmission [ CodeableConcept ]; # 0..1 The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
    fhir:Encounter.hospitalization.dietPreference [ CodeableConcept ], ... ; # 0..* Diet preferences reported by the patient
    fhir:Encounter.hospitalization.specialCourtesy [ CodeableConcept ], ... ; # 0..* Special courtesies (VIP, board member)
    fhir:Encounter.hospitalization.specialArrangement [ CodeableConcept ], ... ; # 0..* Wheelchair, translator, stretcher, etc.
    fhir:Encounter.hospitalization.destination [ Reference(Location|Organization) ]; # 0..1 Location/organization to which the patient is discharged
    fhir:Encounter.hospitalization.dischargeDisposition [ CodeableConcept ]; # 0..1 Category or kind of location after discharge
  ];
  fhir:Encounter.location [ # 0..* List of locations where the patient has been
    fhir:Encounter.location.location [ Reference(Location) ]; # 1..1 Location the encounter takes place
    fhir:Encounter.location.status [ code ]; # 0..1 planned | active | reserved | completed
    fhir:Encounter.location.physicalType [ CodeableConcept ]; # 0..1 The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    fhir:Encounter.location.period [ Period ]; # 0..1 Time period during which the patient was present at the location
  ], ...;
  fhir:Encounter.serviceProvider [ Reference(Organization) ]; # 0..1 The organization (facility) responsible for this encounter
  fhir:Encounter.partOf [ Reference(Encounter) ]; # 0..1 Another Encounter this encounter is part of
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Encounter](encounter.html#Encounter) |  |
| Encounter.status | - Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1 |
| Encounter.statusHistory.status | - Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1 |
| Encounter.class | - Min Cardinality changed from 0 to 1 |
| Encounter.serviceType | - Added Element |
| Encounter.basedOn | - Renamed from incomingReferral to basedOn - Type Reference: Added Target Type ServiceRequest - Type Reference: Removed Target Type ReferralRequest |
| Encounter.participant.individual | - Type Reference: Added Target Type PractitionerRole |
| Encounter.appointment | - Max Cardinality changed from 1 to \* |
| Encounter.reasonCode | - Added Element |
| Encounter.reasonReference | - Added Element |
| Encounter.diagnosis.use | - Added Element |
| Encounter.hospitalization.origin | - Type Reference: Added Target Type Organization |
| Encounter.hospitalization.destination | - Type Reference: Added Target Type Organization |
| Encounter.location.status | - Change value set from http://hl7.org/fhir/ValueSet/encounter-location-status to http://hl7.org/fhir/ValueSet/encounter-location-status|4.0.1 |
| Encounter.location.physicalType | - Added Element |
| Encounter.reason | - deleted |
| Encounter.diagnosis.role | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](encounter.diff.xml) or [JSON](encounter.diff.json).

See [R3 <--> R4 Conversion Maps](encounter-version-maps.html) (status = 10 tests that all execute ok. All tests pass round-trip testing and 3 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Encounter](encounter-definitions.html#Encounter "Encounter : An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | An interaction during which services are provided to the patient Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](encounter-definitions.html#Encounter.identifier "Encounter.identifier : Identifier(s) by which this encounter is known.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Identifier(s) by which this encounter is known |
| ... [status](encounter-definitions.html#Encounter.status "Encounter.status : planned | arrived | triaged | in-progress | onleave | finished | cancelled +.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled + [EncounterStatus](valueset-encounter-status.html "Current state of the encounter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [statusHistory](encounter-definitions.html#Encounter.statusHistory "Encounter.statusHistory : The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store them.") |  | 0..\* | [BackboneElement](backboneelement.html) | List of past encounter statuses |
| .... [status](encounter-definitions.html#Encounter.statusHistory.status "Encounter.statusHistory.status : planned | arrived | triaged | in-progress | onleave | finished | cancelled +.") |  | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled + [EncounterStatus](valueset-encounter-status.html "Current state of the encounter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [period](encounter-definitions.html#Encounter.statusHistory.period "Encounter.statusHistory.period : The time that the episode was in the specified status.") |  | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified status |
| ... [class](encounter-definitions.html#Encounter.class "Encounter.class : Concepts representing classification of patient encounter such as ambulatory (outpatient), inpatient, emergency, home health or others due to local variations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Coding](datatypes.html#Coding) | Classification of patient encounter [V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html "Classification of the encounter.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [classHistory](encounter-definitions.html#Encounter.classHistory "Encounter.classHistory : The class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatient.") |  | 0..\* | [BackboneElement](backboneelement.html) | List of past encounter classes |
| .... [class](encounter-definitions.html#Encounter.classHistory.class "Encounter.classHistory.class : inpatient | outpatient | ambulatory | emergency +.") |  | 1..1 | [Coding](datatypes.html#Coding) | inpatient | outpatient | ambulatory | emergency + [V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html "Classification of the encounter.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [period](encounter-definitions.html#Encounter.classHistory.period "Encounter.classHistory.period : The time that the episode was in the specified class.") |  | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified class |
| ... [type](encounter-definitions.html#Encounter.type "Encounter.type : Specific type of encounter (e.g. e-mail consultation, surgical day-care, skilled nursing, rehabilitation).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of encounter [Encounter type](valueset-encounter-type.html "The type of encounter.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [serviceType](encounter-definitions.html#Encounter.serviceType "Encounter.serviceType : Broad categorization of the service that is to be provided (e.g. cardiology).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of service [Service type](valueset-service-type.html "Broad categorization of the service that is to be provided.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [priority](encounter-definitions.html#Encounter.priority "Encounter.priority : Indicates the urgency of the encounter.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Indicates the urgency of the encounter [v3 Code System ActPriority](v3/ActPriority/vs.html "Indicates the urgency of the encounter.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](encounter-definitions.html#Encounter.subject "Encounter.subject : The patient or group present at the encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | The patient or group present at the encounter |
| ... [episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare "Encounter.episodeOfCare : Where a specific encounter should be classified as a part of a specific episode(s) of care this field should be used. This association can facilitate grouping of related encounters together for a specific purpose, such as government reporting, issue tracking, association via a common problem.  The association is recorded on the encounter as these are typically created after the episode of care and grouped on entry rather than editing the episode of care to append another encounter to it (the episode of care could span years).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html)) | Episode(s) of care that this encounter should be recorded against |
| ... [basedOn](encounter-definitions.html#Encounter.basedOn "Encounter.basedOn : The request this encounter satisfies (e.g. incoming referral or procedure request).") |  | 0..\* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | The ServiceRequest that initiated this encounter |
| ... [participant](encounter-definitions.html#Encounter.participant "Encounter.participant : The list of people responsible for providing the service.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | List of participants involved in the encounter |
| .... [type](encounter-definitions.html#Encounter.participant.type "Encounter.participant.type : Role of participant in encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in encounter [Participant type](valueset-encounter-participant-type.html "Role of participant in encounter.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [period](encounter-definitions.html#Encounter.participant.period "Encounter.participant.period : The period of time that the specified participant participated in the encounter. These can overlap or be sub-sets of the overall encounter's period.") |  | 0..1 | [Period](datatypes.html#Period) | Period of time during the encounter that the participant participated |
| .... [individual](encounter-definitions.html#Encounter.participant.individual "Encounter.participant.individual : Persons involved in the encounter other than the patient.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html)) | Persons involved in the encounter other than the patient |
| ... [appointment](encounter-definitions.html#Encounter.appointment "Encounter.appointment : The appointment that scheduled this encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Appointment](appointment.html)) | The appointment that scheduled this encounter |
| ... [period](encounter-definitions.html#Encounter.period "Encounter.period : The start and end time of the encounter.") |  | 0..1 | [Period](datatypes.html#Period) | The start and end time of the encounter |
| ... [length](encounter-definitions.html#Encounter.length "Encounter.length : Quantity of time the encounter lasted. This excludes the time during leaves of absence.") |  | 0..1 | [Duration](datatypes.html#Duration) | Quantity of time the encounter lasted (less time absent) |
| ... [reasonCode](encounter-definitions.html#Encounter.reasonCode "Encounter.reasonCode : Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosis.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason the encounter takes place [Encounter Reason Codes](valueset-encounter-reason.html "Reason why the encounter takes place.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [reasonReference](encounter-definitions.html#Encounter.reasonReference "Encounter.reasonReference : Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosis.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html) | [Observation](observation.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | Reason the encounter takes place (reference) |
| ... [diagnosis](encounter-definitions.html#Encounter.diagnosis "Encounter.diagnosis : The list of diagnosis relevant to this encounter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | The list of diagnosis relevant to this encounter |
| .... [condition](encounter-definitions.html#Encounter.diagnosis.condition "Encounter.diagnosis.condition : Reason the encounter takes place, as specified using information from another resource. For admissions, this is the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a Procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html)) | The diagnosis or procedure relevant to the encounter |
| .... [use](encounter-definitions.html#Encounter.diagnosis.use "Encounter.diagnosis.use : Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …).") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …) [DiagnosisRole](valueset-diagnosis-role.html "The type of diagnosis this condition represents.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [rank](encounter-definitions.html#Encounter.diagnosis.rank "Encounter.diagnosis.rank : Ranking of the diagnosis (for each role type).") |  | 0..1 | [positiveInt](datatypes.html#positiveInt) | Ranking of the diagnosis (for each role type) |
| ... [account](encounter-definitions.html#Encounter.account "Encounter.account : The set of accounts that may be used for billing for this Encounter.") |  | 0..\* | [Reference](references.html#Reference)([Account](account.html)) | The set of accounts that may be used for billing for this Encounter |
| ... [hospitalization](encounter-definitions.html#Encounter.hospitalization "Encounter.hospitalization : Details about the admission to a healthcare service.") |  | 0..1 | [BackboneElement](backboneelement.html) | Details about the admission to a healthcare service |
| .... [preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier "Encounter.hospitalization.preAdmissionIdentifier : Pre-admission identifier.") |  | 0..1 | [Identifier](datatypes.html#Identifier) | Pre-admission identifier |
| .... [origin](encounter-definitions.html#Encounter.hospitalization.origin "Encounter.hospitalization.origin : The location/organization from which the patient came before admission.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | The location/organization from which the patient came before admission |
| .... [admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource "Encounter.hospitalization.admitSource : From where patient was admitted (physician referral, transfer).") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | From where patient was admitted (physician referral, transfer) [Admit source](valueset-encounter-admit-source.html "From where the patient was admitted.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission "Encounter.hospitalization.reAdmission : Whether this hospitalization is a readmission and why if known.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission [v2 RE-ADMISSION INDICATOR](v2/0092/index.html "The reason for re-admission of this hospitalization encounter.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference "Encounter.hospitalization.dietPreference : Diet preferences reported by the patient.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Diet preferences reported by the patient [Diet](valueset-encounter-diet.html "Medical, cultural or ethical food preferences to help with catering requirements.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy "Encounter.hospitalization.specialCourtesy : Special courtesies (VIP, board member).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Special courtesies (VIP, board member) [Special courtesy](valueset-encounter-special-courtesy.html "Special courtesies.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement "Encounter.hospitalization.specialArrangement : Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other things.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Wheelchair, translator, stretcher, etc. [Special arrangements](valueset-encounter-special-arrangements.html "Special arrangements.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [destination](encounter-definitions.html#Encounter.hospitalization.destination "Encounter.hospitalization.destination : Location/organization to which the patient is discharged.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | Location/organization to which the patient is discharged |
| .... [dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition "Encounter.hospitalization.dischargeDisposition : Category or kind of location after discharge.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category or kind of location after discharge [Discharge disposition](valueset-encounter-discharge-disposition.html "Discharge Disposition.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [location](encounter-definitions.html#Encounter.location "Encounter.location : List of locations where  the patient has been during this encounter.") |  | 0..\* | [BackboneElement](backboneelement.html) | List of locations where the patient has been |
| .... [location](encounter-definitions.html#Encounter.location.location "Encounter.location.location : The location where the encounter takes place.") |  | 1..1 | [Reference](references.html#Reference)([Location](location.html)) | Location the encounter takes place |
| .... [status](encounter-definitions.html#Encounter.location.status "Encounter.location.status : The status of the participants' presence at the specified location during the period specified. If the participant is no longer at the location, then the period will have an end date/time.") |  | 0..1 | [code](datatypes.html#code) | planned | active | reserved | completed [EncounterLocationStatus](valueset-encounter-location-status.html "The status of the location.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [physicalType](encounter-definitions.html#Encounter.location.physicalType "Encounter.location.physicalType : This will be used to specify the required levels (bed/ward/room/etc.) desired to be recorded to simplify either messaging or query.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The physical type of the location (usually the level in the location hierachy - bed room ward etc.) [Location type](valueset-location-physical-type.html "Physical form of the location.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [period](encounter-definitions.html#Encounter.location.period "Encounter.location.period : Time period during which the patient was present at the location.") |  | 0..1 | [Period](datatypes.html#Period) | Time period during which the patient was present at the location |
| ... [serviceProvider](encounter-definitions.html#Encounter.serviceProvider "Encounter.serviceProvider : The organization that is primarily responsible for this Encounter's services. This MAY be the same as the organization on the Patient record, however it could be different, such as if the actor performing the services was from an external organization (which may be billed seperately) for an external consultation.  Refer to the example bundle showing an abbreviated set of Encounters for a colonoscopy.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization (facility) responsible for this encounter |
| ... [partOf](encounter-definitions.html#Encounter.partOf "Encounter.partOf : Another Encounter of which this encounter is a part of (administratively or in time).") |  | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Another Encounter this encounter is part of |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Encounter xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Identifier(s) by which this encounter is known --></identifier>
 <status value="[code]"/><!-- 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled + -->
 <statusHistory>  <!-- 0..* List of past encounter statuses -->
  <status value="[code]"/><!-- 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled + -->
  <period><!-- 1..1 Period The time that the episode was in the specified status --></period>
 </statusHistory>
 <class><!-- 1..1 Coding Classification of patient encounter --></class>
 <classHistory>  <!-- 0..* List of past encounter classes -->
  <class><!-- 1..1 Coding inpatient | outpatient | ambulatory | emergency + --></class>
  <period><!-- 1..1 Period The time that the episode was in the specified class --></period>
 </classHistory>
 <type><!-- 0..* CodeableConcept Specific type of encounter --></type>
 <serviceType><!-- 0..1 CodeableConcept Specific type of service --></serviceType>
 <priority><!-- 0..1 CodeableConcept Indicates the urgency of the encounter --></priority>
 <subject><!-- 0..1 Reference(Patient|Group) The patient or group present at the encounter --></subject>
 <episodeOfCare><!-- 0..* Reference(EpisodeOfCare) Episode(s) of care that this encounter should be recorded against --></episodeOfCare>
 <basedOn><!-- 0..* Reference(ServiceRequest) The ServiceRequest that initiated this encounter --></basedOn>
 <participant>  <!-- 0..* List of participants involved in the encounter -->
  <type><!-- 0..* CodeableConcept Role of participant in encounter --></type>
  <period><!-- 0..1 Period Period of time during the encounter that the participant participated --></period>
  <individual><!-- 0..1 Reference(Practitioner|PractitionerRole|RelatedPerson) Persons involved in the encounter other than the patient --></individual>
 </participant>
 <appointment><!-- 0..* Reference(Appointment) The appointment that scheduled this encounter --></appointment>
 <period><!-- 0..1 Period The start and end time of the encounter --></period>
 <length><!-- 0..1 Duration Quantity of time the encounter lasted (less time absent) --></length>
 <reasonCode><!-- 0..* CodeableConcept Coded reason the encounter takes place --></reasonCode>
 <reasonReference><!-- 0..* Reference(Condition|Procedure|Observation|
   ImmunizationRecommendation) Reason the encounter takes place (reference) --></reasonReference>
 <diagnosis>  <!-- 0..* The list of diagnosis relevant to this encounter -->
  <condition><!-- 1..1 Reference(Condition|Procedure) The diagnosis or procedure relevant to the encounter --></condition>
  <use><!-- 0..1 CodeableConcept Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦) --></use>
  <rank value="[positiveInt]"/><!-- 0..1 Ranking of the diagnosis (for each role type) -->
 </diagnosis>
 <account><!-- 0..* Reference(Account) The set of accounts that may be used for billing for this Encounter --></account>
 <hospitalization>  <!-- 0..1 Details about the admission to a healthcare service -->
  <preAdmissionIdentifier><!-- 0..1 Identifier Pre-admission identifier --></preAdmissionIdentifier>
  <origin><!-- 0..1 Reference(Location|Organization) The location/organization from which the patient came before admission --></origin>
  <admitSource><!-- 0..1 CodeableConcept From where patient was admitted (physician referral, transfer) --></admitSource>
  <reAdmission><!-- 0..1 CodeableConcept The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission --></reAdmission>
  <dietPreference><!-- 0..* CodeableConcept Diet preferences reported by the patient --></dietPreference>
  <specialCourtesy><!-- 0..* CodeableConcept Special courtesies (VIP, board member) --></specialCourtesy>
  <specialArrangement><!-- 0..* CodeableConcept Wheelchair, translator, stretcher, etc. --></specialArrangement>
  <destination><!-- 0..1 Reference(Location|Organization) Location/organization to which the patient is discharged --></destination>
  <dischargeDisposition><!-- 0..1 CodeableConcept Category or kind of location after discharge --></dischargeDisposition>
 </hospitalization>
 <location>  <!-- 0..* List of locations where the patient has been -->
  <location><!-- 1..1 Reference(Location) Location the encounter takes place --></location>
  <status value="[code]"/><!-- 0..1 planned | active | reserved | completed -->
  <physicalType><!-- 0..1 CodeableConcept The physical type of the location (usually the level in the location hierachy - bed room ward etc.) --></physicalType>
  <period><!-- 0..1 Period Time period during which the patient was present at the location --></period>
 </location>
 <serviceProvider><!-- 0..1 Reference(Organization) The organization (facility) responsible for this encounter --></serviceProvider>
 <partOf><!-- 0..1 Reference(Encounter) Another Encounter this encounter is part of --></partOf>
</Encounter>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Encounter",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Identifier(s) by which this encounter is known
  "status" : "<code>", // R!  planned | arrived | triaged | in-progress | onleave | finished | cancelled +
  "statusHistory" : [{ // List of past encounter statuses
    "status" : "<code>", // R!  planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    "period" : { Period } // R!  The time that the episode was in the specified status
  }],
  "class" : { Coding }, // R!  Classification of patient encounter
  "classHistory" : [{ // List of past encounter classes
    "class" : { Coding }, // R!  inpatient | outpatient | ambulatory | emergency +
    "period" : { Period } // R!  The time that the episode was in the specified class
  }],
  "type" : [{ CodeableConcept }], // Specific type of encounter
  "serviceType" : { CodeableConcept }, // Specific type of service
  "priority" : { CodeableConcept }, // Indicates the urgency of the encounter
  "subject" : { Reference(Patient|Group) }, // The patient or group present at the encounter
  "episodeOfCare" : [{ Reference(EpisodeOfCare) }], // Episode(s) of care that this encounter should be recorded against
  "basedOn" : [{ Reference(ServiceRequest) }], // The ServiceRequest that initiated this encounter
  "participant" : [{ // List of participants involved in the encounter
    "type" : [{ CodeableConcept }], // Role of participant in encounter
    "period" : { Period }, // Period of time during the encounter that the participant participated
    "individual" : { Reference(Practitioner|PractitionerRole|RelatedPerson) } // Persons involved in the encounter other than the patient
  }],
  "appointment" : [{ Reference(Appointment) }], // The appointment that scheduled this encounter
  "period" : { Period }, // The start and end time of the encounter
  "length" : { Duration }, // Quantity of time the encounter lasted (less time absent)
  "reasonCode" : [{ CodeableConcept }], // Coded reason the encounter takes place
  "reasonReference" : [{ Reference(Condition|Procedure|Observation|
   ImmunizationRecommendation) }], // Reason the encounter takes place (reference)
  "diagnosis" : [{ // The list of diagnosis relevant to this encounter
    "condition" : { Reference(Condition|Procedure) }, // R!  The diagnosis or procedure relevant to the encounter
    "use" : { CodeableConcept }, // Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)
    "rank" : "<positiveInt>" // Ranking of the diagnosis (for each role type)
  }],
  "account" : [{ Reference(Account) }], // The set of accounts that may be used for billing for this Encounter
  "hospitalization" : { // Details about the admission to a healthcare service
    "preAdmissionIdentifier" : { Identifier }, // Pre-admission identifier
    "origin" : { Reference(Location|Organization) }, // The location/organization from which the patient came before admission
    "admitSource" : { CodeableConcept }, // From where patient was admitted (physician referral, transfer)
    "reAdmission" : { CodeableConcept }, // The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
    "dietPreference" : [{ CodeableConcept }], // Diet preferences reported by the patient
    "specialCourtesy" : [{ CodeableConcept }], // Special courtesies (VIP, board member)
    "specialArrangement" : [{ CodeableConcept }], // Wheelchair, translator, stretcher, etc.
    "destination" : { Reference(Location|Organization) }, // Location/organization to which the patient is discharged
    "dischargeDisposition" : { CodeableConcept } // Category or kind of location after discharge
  },
  "location" : [{ // List of locations where the patient has been
    "location" : { Reference(Location) }, // R!  Location the encounter takes place
    "status" : "<code>", // planned | active | reserved | completed
    "physicalType" : { CodeableConcept }, // The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    "period" : { Period } // Time period during which the patient was present at the location
  }],
  "serviceProvider" : { Reference(Organization) }, // The organization (facility) responsible for this encounter
  "partOf" : { Reference(Encounter) } // Another Encounter this encounter is part of
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Encounter;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Encounter.identifier [ Identifier ], ... ; # 0..* Identifier(s) by which this encounter is known
  fhir:Encounter.status [ code ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
  fhir:Encounter.statusHistory [ # 0..* List of past encounter statuses
    fhir:Encounter.statusHistory.status [ code ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
    fhir:Encounter.statusHistory.period [ Period ]; # 1..1 The time that the episode was in the specified status
  ], ...;
  fhir:Encounter.class [ Coding ]; # 1..1 Classification of patient encounter
  fhir:Encounter.classHistory [ # 0..* List of past encounter classes
    fhir:Encounter.classHistory.class [ Coding ]; # 1..1 inpatient | outpatient | ambulatory | emergency +
    fhir:Encounter.classHistory.period [ Period ]; # 1..1 The time that the episode was in the specified class
  ], ...;
  fhir:Encounter.type [ CodeableConcept ], ... ; # 0..* Specific type of encounter
  fhir:Encounter.serviceType [ CodeableConcept ]; # 0..1 Specific type of service
  fhir:Encounter.priority [ CodeableConcept ]; # 0..1 Indicates the urgency of the encounter
  fhir:Encounter.subject [ Reference(Patient|Group) ]; # 0..1 The patient or group present at the encounter
  fhir:Encounter.episodeOfCare [ Reference(EpisodeOfCare) ], ... ; # 0..* Episode(s) of care that this encounter should be recorded against
  fhir:Encounter.basedOn [ Reference(ServiceRequest) ], ... ; # 0..* The ServiceRequest that initiated this encounter
  fhir:Encounter.participant [ # 0..* List of participants involved in the encounter
    fhir:Encounter.participant.type [ CodeableConcept ], ... ; # 0..* Role of participant in encounter
    fhir:Encounter.participant.period [ Period ]; # 0..1 Period of time during the encounter that the participant participated
    fhir:Encounter.participant.individual [ Reference(Practitioner|PractitionerRole|RelatedPerson) ]; # 0..1 Persons involved in the encounter other than the patient
  ], ...;
  fhir:Encounter.appointment [ Reference(Appointment) ], ... ; # 0..* The appointment that scheduled this encounter
  fhir:Encounter.period [ Period ]; # 0..1 The start and end time of the encounter
  fhir:Encounter.length [ Duration ]; # 0..1 Quantity of time the encounter lasted (less time absent)
  fhir:Encounter.reasonCode [ CodeableConcept ], ... ; # 0..* Coded reason the encounter takes place
  fhir:Encounter.reasonReference [ Reference(Condition|Procedure|Observation|ImmunizationRecommendation) ], ... ; # 0..* Reason the encounter takes place (reference)
  fhir:Encounter.diagnosis [ # 0..* The list of diagnosis relevant to this encounter
    fhir:Encounter.diagnosis.condition [ Reference(Condition|Procedure) ]; # 1..1 The diagnosis or procedure relevant to the encounter
    fhir:Encounter.diagnosis.use [ CodeableConcept ]; # 0..1 Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)
    fhir:Encounter.diagnosis.rank [ positiveInt ]; # 0..1 Ranking of the diagnosis (for each role type)
  ], ...;
  fhir:Encounter.account [ Reference(Account) ], ... ; # 0..* The set of accounts that may be used for billing for this Encounter
  fhir:Encounter.hospitalization [ # 0..1 Details about the admission to a healthcare service
    fhir:Encounter.hospitalization.preAdmissionIdentifier [ Identifier ]; # 0..1 Pre-admission identifier
    fhir:Encounter.hospitalization.origin [ Reference(Location|Organization) ]; # 0..1 The location/organization from which the patient came before admission
    fhir:Encounter.hospitalization.admitSource [ CodeableConcept ]; # 0..1 From where patient was admitted (physician referral, transfer)
    fhir:Encounter.hospitalization.reAdmission [ CodeableConcept ]; # 0..1 The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
    fhir:Encounter.hospitalization.dietPreference [ CodeableConcept ], ... ; # 0..* Diet preferences reported by the patient
    fhir:Encounter.hospitalization.specialCourtesy [ CodeableConcept ], ... ; # 0..* Special courtesies (VIP, board member)
    fhir:Encounter.hospitalization.specialArrangement [ CodeableConcept ], ... ; # 0..* Wheelchair, translator, stretcher, etc.
    fhir:Encounter.hospitalization.destination [ Reference(Location|Organization) ]; # 0..1 Location/organization to which the patient is discharged
    fhir:Encounter.hospitalization.dischargeDisposition [ CodeableConcept ]; # 0..1 Category or kind of location after discharge
  ];
  fhir:Encounter.location [ # 0..* List of locations where the patient has been
    fhir:Encounter.location.location [ Reference(Location) ]; # 1..1 Location the encounter takes place
    fhir:Encounter.location.status [ code ]; # 0..1 planned | active | reserved | completed
    fhir:Encounter.location.physicalType [ CodeableConcept ]; # 0..1 The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
    fhir:Encounter.location.period [ Period ]; # 0..1 Time period during which the patient was present at the location
  ], ...;
  fhir:Encounter.serviceProvider [ Reference(Organization) ]; # 0..1 The organization (facility) responsible for this encounter
  fhir:Encounter.partOf [ Reference(Encounter) ]; # 0..1 Another Encounter this encounter is part of
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Encounter](encounter.html#Encounter) |  |
| Encounter.status | - Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1 |
| Encounter.statusHistory.status | - Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1 |
| Encounter.class | - Min Cardinality changed from 0 to 1 |
| Encounter.serviceType | - Added Element |
| Encounter.basedOn | - Renamed from incomingReferral to basedOn - Type Reference: Added Target Type ServiceRequest - Type Reference: Removed Target Type ReferralRequest |
| Encounter.participant.individual | - Type Reference: Added Target Type PractitionerRole |
| Encounter.appointment | - Max Cardinality changed from 1 to \* |
| Encounter.reasonCode | - Added Element |
| Encounter.reasonReference | - Added Element |
| Encounter.diagnosis.use | - Added Element |
| Encounter.hospitalization.origin | - Type Reference: Added Target Type Organization |
| Encounter.hospitalization.destination | - Type Reference: Added Target Type Organization |
| Encounter.location.status | - Change value set from http://hl7.org/fhir/ValueSet/encounter-location-status to http://hl7.org/fhir/ValueSet/encounter-location-status|4.0.1 |
| Encounter.location.physicalType | - Added Element |
| Encounter.reason | - deleted |
| Encounter.diagnosis.role | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](encounter.diff.xml) or [JSON](encounter.diff.json).

See [R3 <--> R4 Conversion Maps](encounter-version-maps.html) (status = 10 tests that all execute ok. All tests pass round-trip testing and 3 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](encounter-profiles.html) and the alternate definitions:
Master Definition [XML](encounter.profile.xml.html) + [JSON](encounter.profile.json.html),
[XML](xml.html) [Schema](encounter.xsd)/[Schematron](encounter.sch) + [JSON](json.html)
[Schema](encounter.schema.json.html), [ShEx](encounter.shex.html) (for [Turtle](rdf.html)) + [see the extensions](encounter-profiles.html) & the [dependency analysis](encounter-dependencies.html)

### 8.11.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Encounter.status Encounter.statusHistory.status | Current state of the encounter. | [Required](terminologies.html#required) | [EncounterStatus](valueset-encounter-status.html) |
| Encounter.class Encounter.classHistory.class | Classification of the encounter. | [Extensible](terminologies.html#extensible) | [v3.ActEncounterCode](v3/ActEncounterCode/vs.html) |
| Encounter.type | The type of encounter. | [Example](terminologies.html#example) | [EncounterType](valueset-encounter-type.html) |
| Encounter.serviceType | Broad categorization of the service that is to be provided. | [Example](terminologies.html#example) | [ServiceType](valueset-service-type.html) |
| Encounter.priority | Indicates the urgency of the encounter. | [Example](terminologies.html#example) | [v3.ActPriority](v3/ActPriority/vs.html) |
| Encounter.participant.type | Role of participant in encounter. | [Extensible](terminologies.html#extensible) | [ParticipantType](valueset-encounter-participant-type.html) |
| Encounter.reasonCode | Reason why the encounter takes place. | [Preferred](terminologies.html#preferred) | [EncounterReasonCodes](valueset-encounter-reason.html) |
| Encounter.diagnosis.use | The type of diagnosis this condition represents. | [Preferred](terminologies.html#preferred) | [DiagnosisRole](valueset-diagnosis-role.html) |
| Encounter.hospitalization.admitSource | From where the patient was admitted. | [Preferred](terminologies.html#preferred) | [AdmitSource](valueset-encounter-admit-source.html) |
| Encounter.hospitalization.reAdmission | The reason for re-admission of this hospitalization encounter. | [Example](terminologies.html#example) | [v2.0092](v2/0092/index.html) |
| Encounter.hospitalization.dietPreference | Medical, cultural or ethical food preferences to help with catering requirements. | [Example](terminologies.html#example) | [Diet](valueset-encounter-diet.html) |
| Encounter.hospitalization.specialCourtesy | Special courtesies. | [Preferred](terminologies.html#preferred) | [SpecialCourtesy](valueset-encounter-special-courtesy.html) |
| Encounter.hospitalization.specialArrangement | Special arrangements. | [Preferred](terminologies.html#preferred) | [SpecialArrangements](valueset-encounter-special-arrangements.html) |
| Encounter.hospitalization.dischargeDisposition | Discharge Disposition. | [Example](terminologies.html#example) | [DischargeDisposition](valueset-encounter-discharge-disposition.html) |
| Encounter.location.status | The status of the location. | [Required](terminologies.html#required) | [EncounterLocationStatus](valueset-encounter-location-status.html) |
| Encounter.location.physicalType | Physical form of the location. | [Example](terminologies.html#example) | [LocationType](valueset-location-physical-type.html) |

## 8.11.4 Notes

- The *class* element describes the setting (in/outpatient etc.) in which the Encounter took place. Since this is important for
  interpreting the context of the encounter, choosing the appropriate business rules to enforce and for the management of the process, this element
  is required.
- In future versions of FHIR, some kind of charge posting vehicle (e.g. Account) will be added.

## 8.11.5 Example usage

As stated, Encounter allows a flexible nesting of Encounters using the partOf element. For example:

- A patient is admitted for two weeks - This could be modeled using a single Encounter instance,
  in which the start and length are given for the duration of the whole stay. The admitting doctor and
  the responsible doctor during the stay are specified using the Participant component.
- During the encounter, the patient moves from the admitting department to the Intensive Care unit and back -
  Three more detailed additional Encounters can be created, one for each location in which the patient stayed.
  Each of these Encounters has a single location (twice the admitting department and once
  the Intensive Care unit) and one or more participants at that location. These Encounters may use the partOf
  relationship to indicate these movements occurred during the longer overarching Encounter.
- During the last part of the stay, the patient is visited by the members of the multi-disciplinary team that
  treated him for final evaluation - If relevant, for each of these short visits, an Encounter may be created
  with a single participant. Since these took place during the last part of the stay, the partOf element can be
  used to associate these short visits with either the third patient movement or the bigger overall encounter.

Exactly how the Encounter is used depends on information available in the source system, the relevance of exchange
of each level of Encounter and demands specific to the communicating partners. The expectation is that for each
domain of exchange, profiles are used to limit the flexibility of Encounter to meet the demands of the use case.

## 8.11.6 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| account | [reference](search.html#reference) | The set of accounts that may be used for billing for this Encounter | Encounter.account ([Account](account.html)) |  |
| appointment | [reference](search.html#reference) | The appointment that scheduled this encounter | Encounter.appointment ([Appointment](appointment.html)) |  |
| based-on | [reference](search.html#reference) | The ServiceRequest that initiated this encounter | Encounter.basedOn ([ServiceRequest](servicerequest.html)) |  |
| class | [token](search.html#token) | Classification of patient encounter | Encounter.class |  |
| date | [date](search.html#date) | A date within the period the Encounter lasted | Encounter.period | [17 Resources](searchparameter-registry.html#clinical-date) |
| diagnosis | [reference](search.html#reference) | The diagnosis or procedure relevant to the encounter | Encounter.diagnosis.condition ([Condition](condition.html), [Procedure](procedure.html)) |  |
| episode-of-care | [reference](search.html#reference) | Episode(s) of care that this encounter should be recorded against | Encounter.episodeOfCare ([EpisodeOfCare](episodeofcare.html)) |  |
| identifier | [token](search.html#token) | Identifier(s) by which this encounter is known | Encounter.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) |
| length | [quantity](search.html#quantity) | Length of encounter in days | Encounter.length |  |
| location | [reference](search.html#reference) | Location the encounter takes place | Encounter.location.location ([Location](location.html)) |  |
| location-period | [date](search.html#date) | Time period during which the patient was present at the location | Encounter.location.period |  |
| part-of | [reference](search.html#reference) | Another Encounter this encounter is part of | Encounter.partOf ([Encounter](encounter.html)) |  |
| participant | [reference](search.html#reference) | Persons involved in the encounter other than the patient | Encounter.participant.individual ([Practitioner](practitioner.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |  |
| participant-type | [token](search.html#token) | Role of participant in encounter | Encounter.participant.type |  |
| patient | [reference](search.html#reference) | The patient or group present at the encounter | Encounter.subject.where(resolve() is Patient) ([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) |
| practitioner | [reference](search.html#reference) | Persons involved in the encounter other than the patient | Encounter.participant.individual.where(resolve() is Practitioner) ([Practitioner](practitioner.html)) |  |
| reason-code | [token](search.html#token) | Coded reason the encounter takes place | Encounter.reasonCode |  |
| reason-reference | [reference](search.html#reference) | Reason the encounter takes place (reference) | Encounter.reasonReference ([Condition](condition.html), [Observation](observation.html), [Procedure](procedure.html), [ImmunizationRecommendation](immunizationrecommendation.html)) |  |
| service-provider | [reference](search.html#reference) | The organization (facility) responsible for this encounter | Encounter.serviceProvider ([Organization](organization.html)) |  |
| special-arrangement | [token](search.html#token) | Wheelchair, translator, stretcher, etc. | Encounter.hospitalization.specialArrangement |  |
| status | [token](search.html#token) | planned | arrived | triaged | in-progress | onleave | finished | cancelled + | Encounter.status |  |
| subject | [reference](search.html#reference) | The patient or group present at the encounter | Encounter.subject ([Group](group.html), [Patient](patient.html)) |  |
| type | [token](search.html#token) | Specific type of encounter | Encounter.type | [5 Resources](searchparameter-registry.html#clinical-type) |
