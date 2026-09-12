---
id: procedure
title: Procedure
source_url: https://hl7.org/fhir/R4/procedure.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:14Z'
sha256: 3521567c7788924467ebe86604a53cfc093fc7b8ba502f619f4ddf5dc3d23c9c
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/procedure.html) [R4B](http://hl7.org/fhir/R4B/procedure.html) **R4** [R3](http://hl7.org/fhir/STU3/procedure.html) [R2](http://hl7.org/fhir/DSTU2/procedure.html)

- [Content](#)
- [Examples](procedure-examples.html)
- [Detailed Descriptions](procedure-definitions.html)
- [Mappings](procedure-mappings.html)
- [Profiles & Extensions](procedure-profiles.html)
- [R3 Conversions](procedure-version-maps.html)

# 9.3 Resource Procedure - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Care](http://www.hl7.org/Special/committees/patientcare/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) |

An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.

## 9.3.1 Scope and Usage

Procedure is one of the [event](workflow.html#event) resources in the FHIR [workflow](workflow.html) specification.

This resource is used to record the details of current and historical procedures performed on or for a patient. A procedure is an activity
that is performed on, with, or for a patient as part of the provision of care. Examples include surgical
procedures, diagnostic procedures, endoscopic procedures, biopsies, counseling, physiotherapy, personal support services, adult day care services, non-emergency transportation, home modification, exercise, etc.
Procedures may be performed by a healthcare professional, a service provider, a friend or relative or in some cases by the patient
themselves.

This resource provides summary information about the occurrence of the procedure and is not intended to
provide real-time snapshots of a procedure as it unfolds, though for long-running procedures such as psychotherapy,
it could represent summary level information about overall progress. The creation of a resource to support detailed
real-time procedure information awaits the identification of a specific implementation use-case to share such information.

## 9.3.2 Boundaries and Relationships

The Procedure resource should not be used to capture an event if a more specific resource already exists - i.e.
[immunizations](immunization.html), [drug administrations](medicationadministration.html)
and [communications](communication.html). The boundary between determining whether an action is a Procedure
(training or counseling) as opposed to a Communication is based on whether
there's a specific intent to change the mind-set of the patient. Mere disclosure of information would be considered
a Communication. A process that involves verification of the patient's comprehension or to change the patient's
mental state would be a Procedure.

Note that many diagnostic processes are procedures that generate [Observations](observation.html) and
[DiagnosticReports](diagnosticreport.html). In many cases,
such an observation does not require an explicit representation of the procedure used to create the
observation, but where there are details of interest about how the diagnostic procedure was performed,
the Procedure resource is used to describe the activity.

Some diagnostic procedures might not have a Procedure record. The Procedure record is only necessary when
there is a need to capture information about the physical intervention that was performed to capture the diagnostic
information (e.g. anesthetic, incision, scope size, etc.)

A [Task](task.html) is a workflow step such as cancelling an order, fulfilling an order, signing an order, merging a set of records, admitting a patient.
Procedures are actions that are intended to result in a physical or mental change to or for the subject (e.g. surgery, physiotherapy, training, counseling).
A [Task](task.html) resource often exists in parallel with clinical resources. For example, a [Task](task.html) might request fulfillment of a [ServiceRequest](servicerequest.html) ordering a Procedure.

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [Appointment](appointment.html#Appointment), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [Encounter](encounter.html#Encounter), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [ImagingStudy](imagingstudy.html#ImagingStudy), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationStatement](medicationstatement.html#MedicationStatement), [Observation](observation.html#Observation), itself and [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)

## 9.3.3 Resource Content

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
| .. [Procedure](procedure-definitions.html#Procedure "Procedure : An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | An action that is being or was performed on a patient Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](procedure-definitions.html#Procedure.identifier "Procedure.identifier : Business identifiers assigned to this procedure by the performer or other systems which remain constant as the resource is updated and is propagated from server to server.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | External Identifiers for this procedure |
| ... [instantiatesCanonical](procedure-definitions.html#Procedure.instantiatesCanonical "Procedure.instantiatesCanonical : The URL pointing to a FHIR-defined protocol, guideline, order set or other definition that is adhered to in whole or in part by this Procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html) | [ActivityDefinition](activitydefinition.html) | [Measure](measure.html) | [OperationDefinition](operationdefinition.html) | [Questionnaire](questionnaire.html)) | Instantiates FHIR protocol or definition |
| ... [instantiatesUri](procedure-definitions.html#Procedure.instantiatesUri "Procedure.instantiatesUri : The URL pointing to an externally maintained protocol, guideline, order set or other definition that is adhered to in whole or in part by this Procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [uri](datatypes.html#uri) | Instantiates external protocol or definition |
| ... [basedOn](procedure-definitions.html#Procedure.basedOn "Procedure.basedOn : A reference to a resource that contains details of the request for this procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([CarePlan](careplan.html) | [ServiceRequest](servicerequest.html)) | A request for this procedure |
| ... [partOf](procedure-definitions.html#Procedure.partOf "Procedure.partOf : A larger event of which this particular procedure is a component or step.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Procedure](procedure.html) | [Observation](observation.html) | [MedicationAdministration](medicationadministration.html)) | Part of referenced event |
| ... [status](procedure-definitions.html#Procedure.status "Procedure.status : A code specifying the state of the procedure. Generally, this will be the in-progress or completed state.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown [EventStatus](valueset-event-status.html "A code specifying the state of the procedure.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [statusReason](procedure-definitions.html#Procedure.statusReason "Procedure.statusReason : Captures the reason for the current state of the procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status [Procedure Not Performed Reason (SNOMED-CT)](valueset-procedure-not-performed-reason.html "A code that identifies the reason a procedure was not performed.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [category](procedure-definitions.html#Procedure.category "Procedure.category : A code that classifies the procedure for searching, sorting and display purposes (e.g. \"Surgical Procedure\").") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of the procedure [Procedure Category Codes (SNOMED CT)](valueset-procedure-category.html "A code that classifies a procedure for searching, sorting and display purposes.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [code](procedure-definitions.html#Procedure.code "Procedure.code : The specific procedure that is performed. Use text if the exact nature of the procedure cannot be coded (e.g. \"Laparoscopic Appendectomy\").") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Identification of the procedure [Procedure Codes (SNOMED CT)](valueset-procedure-code.html "A code to identify a specific procedure .") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](procedure-definitions.html#Procedure.subject "Procedure.subject : The person, animal or group on which the procedure was performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who the procedure was performed on |
| ... [encounter](procedure-definitions.html#Procedure.encounter "Procedure.encounter : The Encounter during which this Procedure was created or performed or to which the creation of this record is tightly associated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of |
| ... [performed[x]](procedure-definitions.html#Procedure.performed_x_ "Procedure.performed[x] : Estimated or actual date, date-time, period, or age when the procedure was performed.  Allows a period to support complex procedures that span more than one date, and also allows for the length of the procedure to be captured.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | When the procedure was performed |
| .... performedDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... performedPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... performedString |  |  | [string](datatypes.html#string) |  |
| .... performedAge |  |  | [Age](datatypes.html#Age) |  |
| .... performedRange |  |  | [Range](datatypes.html#Range) |  |
| ... [recorder](procedure-definitions.html#Procedure.recorder "Procedure.recorder : Individual who recorded the record and takes responsibility for its content.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Who recorded the procedure |
| ... [asserter](procedure-definitions.html#Procedure.asserter "Procedure.asserter : Individual who is making the procedure statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Person who asserts this procedure |
| ... [performer](procedure-definitions.html#Procedure.performer "Procedure.performer : Limited to \"real\" people rather than equipment.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | The people who performed the procedure |
| .... [function](procedure-definitions.html#Procedure.performer.function "Procedure.performer.function : Distinguishes the type of involvement of the performer in the procedure. For example, surgeon, anaesthetist, endoscopist.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of performance [Procedure Performer Role Codes](valueset-performer-role.html "A code that identifies the role of a performer of the procedure.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [actor](procedure-definitions.html#Procedure.performer.actor "Procedure.performer.actor : The practitioner who was involved in the procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Device](device.html)) | The reference to the practitioner |
| .... [onBehalfOf](procedure-definitions.html#Procedure.performer.onBehalfOf "Procedure.performer.onBehalfOf : The organization the device or practitioner was acting on behalf of.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization the device or practitioner was acting for |
| ... [location](procedure-definitions.html#Procedure.location "Procedure.location : The location where the procedure actually happened.  E.g. a newborn at home, a tracheostomy at a restaurant.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Where the procedure happened |
| ... [reasonCode](procedure-definitions.html#Procedure.reasonCode "Procedure.reasonCode : The coded reason why the procedure was performed. This may be a coded entity of some type, or may simply be present as text.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason procedure performed [Procedure Reason Codes](valueset-procedure-reason.html "A code that identifies the reason a procedure is  required.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [reasonReference](procedure-definitions.html#Procedure.reasonReference "Procedure.reasonReference : The justification of why the procedure was performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [Procedure](procedure.html) | [DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html)) | The justification that the procedure was performed |
| ... [bodySite](procedure-definitions.html#Procedure.bodySite "Procedure.bodySite : Detailed and structured anatomical location information. Multiple locations are allowed - e.g. multiple punch biopsies of a lesion.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Target body sites [SNOMED CT Body Structures](valueset-body-site.html "Codes describing anatomical locations. May include laterality.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [outcome](procedure-definitions.html#Procedure.outcome "Procedure.outcome : The outcome of the procedure - did it resolve the reasons for the procedure being performed?") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The result of procedure [Procedure Outcome Codes (SNOMED CT)](valueset-procedure-outcome.html "An outcome of a procedure - whether it was resolved or otherwise.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [report](procedure-definitions.html#Procedure.report "Procedure.report : This could be a histology result, pathology report, surgical report, etc.") |  | 0..\* | [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html) | [Composition](composition.html)) | Any report resulting from the procedure |
| ... [complication](procedure-definitions.html#Procedure.complication "Procedure.complication : Any complications that occurred during the procedure, or in the immediate post-performance period. These are generally tracked separately from the notes, which will typically describe the procedure itself rather than any 'post procedure' issues.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Complication following the procedure [Condition/Problem/Diagnosis Codes](valueset-condition-code.html "Codes describing complications that resulted from a procedure.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [complicationDetail](procedure-definitions.html#Procedure.complicationDetail "Procedure.complicationDetail : Any complications that occurred during the procedure, or in the immediate post-performance period.") |  | 0..\* | [Reference](references.html#Reference)([Condition](condition.html)) | A condition that is a result of the procedure |
| ... [followUp](procedure-definitions.html#Procedure.followUp "Procedure.followUp : If the procedure required specific follow up - e.g. removal of sutures. The follow up may be represented as a simple note or could potentially be more complex, in which case the CarePlan resource can be used.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Instructions for follow up [Procedure Follow up Codes (SNOMED CT)](valueset-procedure-followup.html "Specific follow up required for a procedure e.g. removal of sutures.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [note](procedure-definitions.html#Procedure.note "Procedure.note : Any other notes and comments about the procedure.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Additional information about the procedure |
| ... [focalDevice](procedure-definitions.html#Procedure.focalDevice "Procedure.focalDevice : A device that is implanted, removed or otherwise manipulated (calibration, battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a focal portion of the Procedure.") |  | 0..\* | [BackboneElement](backboneelement.html) | Manipulated, implanted, or removed device |
| .... [action](procedure-definitions.html#Procedure.focalDevice.action "Procedure.focalDevice.action : The kind of change that happened to the device during the procedure.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of change to device [Procedure Device Action Codes](valueset-device-action.html "A kind of change that happened to the device during the procedure.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [manipulated](procedure-definitions.html#Procedure.focalDevice.manipulated "Procedure.focalDevice.manipulated : The device that was manipulated (changed) during the procedure.") |  | 1..1 | [Reference](references.html#Reference)([Device](device.html)) | Device that was changed |
| ... [usedReference](procedure-definitions.html#Procedure.usedReference "Procedure.usedReference : Identifies medications, devices and any other substance used as part of the procedure.") |  | 0..\* | [Reference](references.html#Reference)([Device](device.html) | [Medication](medication.html) | [Substance](substance.html)) | Items used during procedure |
| ... [usedCode](procedure-definitions.html#Procedure.usedCode "Procedure.usedCode : Identifies coded items that were used as part of the procedure.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded items used during the procedure [FHIR Device Types](valueset-device-kind.html "Codes describing items used during a procedure.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Procedure xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier External Identifiers for this procedure --></identifier>
 <instantiatesCanonical><!-- 0..* canonical(PlanDefinition|ActivityDefinition|
   Measure|OperationDefinition|Questionnaire) Instantiates FHIR protocol or definition --></instantiatesCanonical>
 <instantiatesUri value="[uri]"/><!-- 0..* Instantiates external protocol or definition -->
 <basedOn><!-- 0..* Reference(CarePlan|ServiceRequest) A request for this procedure --></basedOn>
 <partOf><!-- 0..* Reference(Procedure|Observation|MedicationAdministration) Part of referenced event --></partOf>
 <status value="[code]"/><!-- 1..1 preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown -->
 <statusReason><!-- 0..1 CodeableConcept Reason for current status --></statusReason>
 <category><!-- 0..1 CodeableConcept Classification of the procedure --></category>
 <code><!-- 0..1 CodeableConcept Identification of the procedure --></code>
 <subject><!-- 1..1 Reference(Patient|Group) Who the procedure was performed on --></subject>
 <encounter><!-- 0..1 Reference(Encounter) Encounter created as part of --></encounter>
 <performed[x]><!-- 0..1 dateTime|Period|string|Age|Range When the procedure was performed --></performed[x]>
 <recorder><!-- 0..1 Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) Who recorded the procedure --></recorder>
 <asserter><!-- 0..1 Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) Person who asserts this procedure --></asserter>
 <performer>  <!-- 0..* The people who performed the procedure -->
  <function><!-- 0..1 CodeableConcept Type of performance --></function>
  <actor><!-- 1..1 Reference(Practitioner|PractitionerRole|Organization|Patient|
    RelatedPerson|Device) The reference to the practitioner --></actor>
  <onBehalfOf><!-- 0..1 Reference(Organization) Organization the device or practitioner was acting for --></onBehalfOf>
 </performer>
 <location><!-- 0..1 Reference(Location) Where the procedure happened --></location>
 <reasonCode><!-- 0..* CodeableConcept Coded reason procedure performed --></reasonCode>
 <reasonReference><!-- 0..* Reference(Condition|Observation|Procedure|
   DiagnosticReport|DocumentReference) The justification that the procedure was performed --></reasonReference>
 <bodySite><!-- 0..* CodeableConcept Target body sites --></bodySite>
 <outcome><!-- 0..1 CodeableConcept The result of procedure --></outcome>
 <report><!-- 0..* Reference(DiagnosticReport|DocumentReference|Composition) Any report resulting from the procedure --></report>
 <complication><!-- 0..* CodeableConcept Complication following the procedure --></complication>
 <complicationDetail><!-- 0..* Reference(Condition) A condition that is a result of the procedure --></complicationDetail>
 <followUp><!-- 0..* CodeableConcept Instructions for follow up --></followUp>
 <note><!-- 0..* Annotation Additional information about the procedure --></note>
 <focalDevice>  <!-- 0..* Manipulated, implanted, or removed device -->
  <action><!-- 0..1 CodeableConcept Kind of change to device --></action>
  <manipulated><!-- 1..1 Reference(Device) Device that was changed --></manipulated>
 </focalDevice>
 <usedReference><!-- 0..* Reference(Device|Medication|Substance) Items used during procedure --></usedReference>
 <usedCode><!-- 0..* CodeableConcept Coded items used during the procedure --></usedCode>
</Procedure>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Procedure",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // External Identifiers for this procedure
  "instantiatesCanonical" : [{ canonical(PlanDefinition|ActivityDefinition|
   Measure|OperationDefinition|Questionnaire) }], // Instantiates FHIR protocol or definition
  "instantiatesUri" : ["<uri>"], // Instantiates external protocol or definition
  "basedOn" : [{ Reference(CarePlan|ServiceRequest) }], // A request for this procedure
  "partOf" : [{ Reference(Procedure|Observation|MedicationAdministration) }], // Part of referenced event
  "status" : "<code>", // R!  preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
  "statusReason" : { CodeableConcept }, // Reason for current status
  "category" : { CodeableConcept }, // Classification of the procedure
  "code" : { CodeableConcept }, // Identification of the procedure
  "subject" : { Reference(Patient|Group) }, // R!  Who the procedure was performed on
  "encounter" : { Reference(Encounter) }, // Encounter created as part of
  // performed[x]: When the procedure was performed. One of these 5:
  "performedDateTime" : "<dateTime>",
  "performedPeriod" : { Period },
  "performedString" : "<string>",
  "performedAge" : { Age },
  "performedRange" : { Range },
  "recorder" : { Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) }, // Who recorded the procedure
  "asserter" : { Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) }, // Person who asserts this procedure
  "performer" : [{ // The people who performed the procedure
    "function" : { CodeableConcept }, // Type of performance
    "actor" : { Reference(Practitioner|PractitionerRole|Organization|Patient|
    RelatedPerson|Device) }, // R!  The reference to the practitioner
    "onBehalfOf" : { Reference(Organization) } // Organization the device or practitioner was acting for
  }],
  "location" : { Reference(Location) }, // Where the procedure happened
  "reasonCode" : [{ CodeableConcept }], // Coded reason procedure performed
  "reasonReference" : [{ Reference(Condition|Observation|Procedure|
   DiagnosticReport|DocumentReference) }], // The justification that the procedure was performed
  "bodySite" : [{ CodeableConcept }], // Target body sites
  "outcome" : { CodeableConcept }, // The result of procedure
  "report" : [{ Reference(DiagnosticReport|DocumentReference|Composition) }], // Any report resulting from the procedure
  "complication" : [{ CodeableConcept }], // Complication following the procedure
  "complicationDetail" : [{ Reference(Condition) }], // A condition that is a result of the procedure
  "followUp" : [{ CodeableConcept }], // Instructions for follow up
  "note" : [{ Annotation }], // Additional information about the procedure
  "focalDevice" : [{ // Manipulated, implanted, or removed device
    "action" : { CodeableConcept }, // Kind of change to device
    "manipulated" : { Reference(Device) } // R!  Device that was changed
  }],
  "usedReference" : [{ Reference(Device|Medication|Substance) }], // Items used during procedure
  "usedCode" : [{ CodeableConcept }] // Coded items used during the procedure
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Procedure;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Procedure.identifier [ Identifier ], ... ; # 0..* External Identifiers for this procedure
  fhir:Procedure.instantiatesCanonical [ canonical(PlanDefinition|ActivityDefinition|Measure|OperationDefinition|Questionnaire) ], ... ; # 0..* Instantiates FHIR protocol or definition
  fhir:Procedure.instantiatesUri [ uri ], ... ; # 0..* Instantiates external protocol or definition
  fhir:Procedure.basedOn [ Reference(CarePlan|ServiceRequest) ], ... ; # 0..* A request for this procedure
  fhir:Procedure.partOf [ Reference(Procedure|Observation|MedicationAdministration) ], ... ; # 0..* Part of referenced event
  fhir:Procedure.status [ code ]; # 1..1 preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
  fhir:Procedure.statusReason [ CodeableConcept ]; # 0..1 Reason for current status
  fhir:Procedure.category [ CodeableConcept ]; # 0..1 Classification of the procedure
  fhir:Procedure.code [ CodeableConcept ]; # 0..1 Identification of the procedure
  fhir:Procedure.subject [ Reference(Patient|Group) ]; # 1..1 Who the procedure was performed on
  fhir:Procedure.encounter [ Reference(Encounter) ]; # 0..1 Encounter created as part of
  # Procedure.performed[x] : 0..1 When the procedure was performed. One of these 5
    fhir:Procedure.performedDateTime [ dateTime ]
    fhir:Procedure.performedPeriod [ Period ]
    fhir:Procedure.performedString [ string ]
    fhir:Procedure.performedAge [ Age ]
    fhir:Procedure.performedRange [ Range ]
  fhir:Procedure.recorder [ Reference(Patient|RelatedPerson|Practitioner|PractitionerRole) ]; # 0..1 Who recorded the procedure
  fhir:Procedure.asserter [ Reference(Patient|RelatedPerson|Practitioner|PractitionerRole) ]; # 0..1 Person who asserts this procedure
  fhir:Procedure.performer [ # 0..* The people who performed the procedure
    fhir:Procedure.performer.function [ CodeableConcept ]; # 0..1 Type of performance
    fhir:Procedure.performer.actor [ Reference(Practitioner|PractitionerRole|Organization|Patient|RelatedPerson|Device) ]; # 1..1 The reference to the practitioner
    fhir:Procedure.performer.onBehalfOf [ Reference(Organization) ]; # 0..1 Organization the device or practitioner was acting for
  ], ...;
  fhir:Procedure.location [ Reference(Location) ]; # 0..1 Where the procedure happened
  fhir:Procedure.reasonCode [ CodeableConcept ], ... ; # 0..* Coded reason procedure performed
  fhir:Procedure.reasonReference [ Reference(Condition|Observation|Procedure|DiagnosticReport|DocumentReference) ], ... ; # 0..* The justification that the procedure was performed
  fhir:Procedure.bodySite [ CodeableConcept ], ... ; # 0..* Target body sites
  fhir:Procedure.outcome [ CodeableConcept ]; # 0..1 The result of procedure
  fhir:Procedure.report [ Reference(DiagnosticReport|DocumentReference|Composition) ], ... ; # 0..* Any report resulting from the procedure
  fhir:Procedure.complication [ CodeableConcept ], ... ; # 0..* Complication following the procedure
  fhir:Procedure.complicationDetail [ Reference(Condition) ], ... ; # 0..* A condition that is a result of the procedure
  fhir:Procedure.followUp [ CodeableConcept ], ... ; # 0..* Instructions for follow up
  fhir:Procedure.note [ Annotation ], ... ; # 0..* Additional information about the procedure
  fhir:Procedure.focalDevice [ # 0..* Manipulated, implanted, or removed device
    fhir:Procedure.focalDevice.action [ CodeableConcept ]; # 0..1 Kind of change to device
    fhir:Procedure.focalDevice.manipulated [ Reference(Device) ]; # 1..1 Device that was changed
  ], ...;
  fhir:Procedure.usedReference [ Reference(Device|Medication|Substance) ], ... ; # 0..* Items used during procedure
  fhir:Procedure.usedCode [ CodeableConcept ], ... ; # 0..* Coded items used during the procedure
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Procedure](procedure.html#Procedure) |  |
| Procedure.instantiatesCanonical | - Added Element |
| Procedure.instantiatesUri | - Added Element |
| Procedure.basedOn | - Type Reference: Added Target Type ServiceRequest - Type Reference: Removed Target Types ProcedureRequest, ReferralRequest |
| Procedure.status | - Change value set from http://hl7.org/fhir/ValueSet/event-status to http://hl7.org/fhir/ValueSet/event-status|4.0.1 |
| Procedure.statusReason | - Added Element |
| Procedure.encounter | - Added Element |
| Procedure.performed[x] | - Add Types string, Age, Range |
| Procedure.recorder | - Added Element |
| Procedure.asserter | - Added Element |
| Procedure.performer.function | - Added Element |
| Procedure.performer.actor | - Type Reference: Added Target Type PractitionerRole |
| Procedure.reasonReference | - Type Reference: Added Target Types Procedure, DiagnosticReport, DocumentReference |
| Procedure.report | - Type Reference: Added Target Types DocumentReference, Composition |
| Procedure.definition | - deleted |
| Procedure.notDone | - deleted |
| Procedure.notDoneReason | - deleted |
| Procedure.context | - deleted |
| Procedure.performer.role | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](procedure.diff.xml) or [JSON](procedure.diff.json).

See [R3 <--> R4 Conversion Maps](procedure-version-maps.html) (status = 15 tests that all execute ok. 3 fail round-trip testing and 1 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Procedure](procedure-definitions.html#Procedure "Procedure : An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | An action that is being or was performed on a patient Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](procedure-definitions.html#Procedure.identifier "Procedure.identifier : Business identifiers assigned to this procedure by the performer or other systems which remain constant as the resource is updated and is propagated from server to server.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | External Identifiers for this procedure |
| ... [instantiatesCanonical](procedure-definitions.html#Procedure.instantiatesCanonical "Procedure.instantiatesCanonical : The URL pointing to a FHIR-defined protocol, guideline, order set or other definition that is adhered to in whole or in part by this Procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html) | [ActivityDefinition](activitydefinition.html) | [Measure](measure.html) | [OperationDefinition](operationdefinition.html) | [Questionnaire](questionnaire.html)) | Instantiates FHIR protocol or definition |
| ... [instantiatesUri](procedure-definitions.html#Procedure.instantiatesUri "Procedure.instantiatesUri : The URL pointing to an externally maintained protocol, guideline, order set or other definition that is adhered to in whole or in part by this Procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [uri](datatypes.html#uri) | Instantiates external protocol or definition |
| ... [basedOn](procedure-definitions.html#Procedure.basedOn "Procedure.basedOn : A reference to a resource that contains details of the request for this procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([CarePlan](careplan.html) | [ServiceRequest](servicerequest.html)) | A request for this procedure |
| ... [partOf](procedure-definitions.html#Procedure.partOf "Procedure.partOf : A larger event of which this particular procedure is a component or step.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Procedure](procedure.html) | [Observation](observation.html) | [MedicationAdministration](medicationadministration.html)) | Part of referenced event |
| ... [status](procedure-definitions.html#Procedure.status "Procedure.status : A code specifying the state of the procedure. Generally, this will be the in-progress or completed state.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown [EventStatus](valueset-event-status.html "A code specifying the state of the procedure.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [statusReason](procedure-definitions.html#Procedure.statusReason "Procedure.statusReason : Captures the reason for the current state of the procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status [Procedure Not Performed Reason (SNOMED-CT)](valueset-procedure-not-performed-reason.html "A code that identifies the reason a procedure was not performed.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [category](procedure-definitions.html#Procedure.category "Procedure.category : A code that classifies the procedure for searching, sorting and display purposes (e.g. \"Surgical Procedure\").") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of the procedure [Procedure Category Codes (SNOMED CT)](valueset-procedure-category.html "A code that classifies a procedure for searching, sorting and display purposes.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [code](procedure-definitions.html#Procedure.code "Procedure.code : The specific procedure that is performed. Use text if the exact nature of the procedure cannot be coded (e.g. \"Laparoscopic Appendectomy\").") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Identification of the procedure [Procedure Codes (SNOMED CT)](valueset-procedure-code.html "A code to identify a specific procedure .") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](procedure-definitions.html#Procedure.subject "Procedure.subject : The person, animal or group on which the procedure was performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who the procedure was performed on |
| ... [encounter](procedure-definitions.html#Procedure.encounter "Procedure.encounter : The Encounter during which this Procedure was created or performed or to which the creation of this record is tightly associated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of |
| ... [performed[x]](procedure-definitions.html#Procedure.performed_x_ "Procedure.performed[x] : Estimated or actual date, date-time, period, or age when the procedure was performed.  Allows a period to support complex procedures that span more than one date, and also allows for the length of the procedure to be captured.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | When the procedure was performed |
| .... performedDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... performedPeriod |  |  | [Period](datatypes.html#Period) |  |
| .... performedString |  |  | [string](datatypes.html#string) |  |
| .... performedAge |  |  | [Age](datatypes.html#Age) |  |
| .... performedRange |  |  | [Range](datatypes.html#Range) |  |
| ... [recorder](procedure-definitions.html#Procedure.recorder "Procedure.recorder : Individual who recorded the record and takes responsibility for its content.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Who recorded the procedure |
| ... [asserter](procedure-definitions.html#Procedure.asserter "Procedure.asserter : Individual who is making the procedure statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Person who asserts this procedure |
| ... [performer](procedure-definitions.html#Procedure.performer "Procedure.performer : Limited to \"real\" people rather than equipment.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | The people who performed the procedure |
| .... [function](procedure-definitions.html#Procedure.performer.function "Procedure.performer.function : Distinguishes the type of involvement of the performer in the procedure. For example, surgeon, anaesthetist, endoscopist.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of performance [Procedure Performer Role Codes](valueset-performer-role.html "A code that identifies the role of a performer of the procedure.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [actor](procedure-definitions.html#Procedure.performer.actor "Procedure.performer.actor : The practitioner who was involved in the procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Device](device.html)) | The reference to the practitioner |
| .... [onBehalfOf](procedure-definitions.html#Procedure.performer.onBehalfOf "Procedure.performer.onBehalfOf : The organization the device or practitioner was acting on behalf of.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization the device or practitioner was acting for |
| ... [location](procedure-definitions.html#Procedure.location "Procedure.location : The location where the procedure actually happened.  E.g. a newborn at home, a tracheostomy at a restaurant.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Where the procedure happened |
| ... [reasonCode](procedure-definitions.html#Procedure.reasonCode "Procedure.reasonCode : The coded reason why the procedure was performed. This may be a coded entity of some type, or may simply be present as text.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason procedure performed [Procedure Reason Codes](valueset-procedure-reason.html "A code that identifies the reason a procedure is  required.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [reasonReference](procedure-definitions.html#Procedure.reasonReference "Procedure.reasonReference : The justification of why the procedure was performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [Procedure](procedure.html) | [DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html)) | The justification that the procedure was performed |
| ... [bodySite](procedure-definitions.html#Procedure.bodySite "Procedure.bodySite : Detailed and structured anatomical location information. Multiple locations are allowed - e.g. multiple punch biopsies of a lesion.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Target body sites [SNOMED CT Body Structures](valueset-body-site.html "Codes describing anatomical locations. May include laterality.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [outcome](procedure-definitions.html#Procedure.outcome "Procedure.outcome : The outcome of the procedure - did it resolve the reasons for the procedure being performed?") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The result of procedure [Procedure Outcome Codes (SNOMED CT)](valueset-procedure-outcome.html "An outcome of a procedure - whether it was resolved or otherwise.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [report](procedure-definitions.html#Procedure.report "Procedure.report : This could be a histology result, pathology report, surgical report, etc.") |  | 0..\* | [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html) | [Composition](composition.html)) | Any report resulting from the procedure |
| ... [complication](procedure-definitions.html#Procedure.complication "Procedure.complication : Any complications that occurred during the procedure, or in the immediate post-performance period. These are generally tracked separately from the notes, which will typically describe the procedure itself rather than any 'post procedure' issues.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Complication following the procedure [Condition/Problem/Diagnosis Codes](valueset-condition-code.html "Codes describing complications that resulted from a procedure.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [complicationDetail](procedure-definitions.html#Procedure.complicationDetail "Procedure.complicationDetail : Any complications that occurred during the procedure, or in the immediate post-performance period.") |  | 0..\* | [Reference](references.html#Reference)([Condition](condition.html)) | A condition that is a result of the procedure |
| ... [followUp](procedure-definitions.html#Procedure.followUp "Procedure.followUp : If the procedure required specific follow up - e.g. removal of sutures. The follow up may be represented as a simple note or could potentially be more complex, in which case the CarePlan resource can be used.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Instructions for follow up [Procedure Follow up Codes (SNOMED CT)](valueset-procedure-followup.html "Specific follow up required for a procedure e.g. removal of sutures.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [note](procedure-definitions.html#Procedure.note "Procedure.note : Any other notes and comments about the procedure.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Additional information about the procedure |
| ... [focalDevice](procedure-definitions.html#Procedure.focalDevice "Procedure.focalDevice : A device that is implanted, removed or otherwise manipulated (calibration, battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a focal portion of the Procedure.") |  | 0..\* | [BackboneElement](backboneelement.html) | Manipulated, implanted, or removed device |
| .... [action](procedure-definitions.html#Procedure.focalDevice.action "Procedure.focalDevice.action : The kind of change that happened to the device during the procedure.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of change to device [Procedure Device Action Codes](valueset-device-action.html "A kind of change that happened to the device during the procedure.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [manipulated](procedure-definitions.html#Procedure.focalDevice.manipulated "Procedure.focalDevice.manipulated : The device that was manipulated (changed) during the procedure.") |  | 1..1 | [Reference](references.html#Reference)([Device](device.html)) | Device that was changed |
| ... [usedReference](procedure-definitions.html#Procedure.usedReference "Procedure.usedReference : Identifies medications, devices and any other substance used as part of the procedure.") |  | 0..\* | [Reference](references.html#Reference)([Device](device.html) | [Medication](medication.html) | [Substance](substance.html)) | Items used during procedure |
| ... [usedCode](procedure-definitions.html#Procedure.usedCode "Procedure.usedCode : Identifies coded items that were used as part of the procedure.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded items used during the procedure [FHIR Device Types](valueset-device-kind.html "Codes describing items used during a procedure.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Procedure xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier External Identifiers for this procedure --></identifier>
 <instantiatesCanonical><!-- 0..* canonical(PlanDefinition|ActivityDefinition|
   Measure|OperationDefinition|Questionnaire) Instantiates FHIR protocol or definition --></instantiatesCanonical>
 <instantiatesUri value="[uri]"/><!-- 0..* Instantiates external protocol or definition -->
 <basedOn><!-- 0..* Reference(CarePlan|ServiceRequest) A request for this procedure --></basedOn>
 <partOf><!-- 0..* Reference(Procedure|Observation|MedicationAdministration) Part of referenced event --></partOf>
 <status value="[code]"/><!-- 1..1 preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown -->
 <statusReason><!-- 0..1 CodeableConcept Reason for current status --></statusReason>
 <category><!-- 0..1 CodeableConcept Classification of the procedure --></category>
 <code><!-- 0..1 CodeableConcept Identification of the procedure --></code>
 <subject><!-- 1..1 Reference(Patient|Group) Who the procedure was performed on --></subject>
 <encounter><!-- 0..1 Reference(Encounter) Encounter created as part of --></encounter>
 <performed[x]><!-- 0..1 dateTime|Period|string|Age|Range When the procedure was performed --></performed[x]>
 <recorder><!-- 0..1 Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) Who recorded the procedure --></recorder>
 <asserter><!-- 0..1 Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) Person who asserts this procedure --></asserter>
 <performer>  <!-- 0..* The people who performed the procedure -->
  <function><!-- 0..1 CodeableConcept Type of performance --></function>
  <actor><!-- 1..1 Reference(Practitioner|PractitionerRole|Organization|Patient|
    RelatedPerson|Device) The reference to the practitioner --></actor>
  <onBehalfOf><!-- 0..1 Reference(Organization) Organization the device or practitioner was acting for --></onBehalfOf>
 </performer>
 <location><!-- 0..1 Reference(Location) Where the procedure happened --></location>
 <reasonCode><!-- 0..* CodeableConcept Coded reason procedure performed --></reasonCode>
 <reasonReference><!-- 0..* Reference(Condition|Observation|Procedure|
   DiagnosticReport|DocumentReference) The justification that the procedure was performed --></reasonReference>
 <bodySite><!-- 0..* CodeableConcept Target body sites --></bodySite>
 <outcome><!-- 0..1 CodeableConcept The result of procedure --></outcome>
 <report><!-- 0..* Reference(DiagnosticReport|DocumentReference|Composition) Any report resulting from the procedure --></report>
 <complication><!-- 0..* CodeableConcept Complication following the procedure --></complication>
 <complicationDetail><!-- 0..* Reference(Condition) A condition that is a result of the procedure --></complicationDetail>
 <followUp><!-- 0..* CodeableConcept Instructions for follow up --></followUp>
 <note><!-- 0..* Annotation Additional information about the procedure --></note>
 <focalDevice>  <!-- 0..* Manipulated, implanted, or removed device -->
  <action><!-- 0..1 CodeableConcept Kind of change to device --></action>
  <manipulated><!-- 1..1 Reference(Device) Device that was changed --></manipulated>
 </focalDevice>
 <usedReference><!-- 0..* Reference(Device|Medication|Substance) Items used during procedure --></usedReference>
 <usedCode><!-- 0..* CodeableConcept Coded items used during the procedure --></usedCode>
</Procedure>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Procedure",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // External Identifiers for this procedure
  "instantiatesCanonical" : [{ canonical(PlanDefinition|ActivityDefinition|
   Measure|OperationDefinition|Questionnaire) }], // Instantiates FHIR protocol or definition
  "instantiatesUri" : ["<uri>"], // Instantiates external protocol or definition
  "basedOn" : [{ Reference(CarePlan|ServiceRequest) }], // A request for this procedure
  "partOf" : [{ Reference(Procedure|Observation|MedicationAdministration) }], // Part of referenced event
  "status" : "<code>", // R!  preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
  "statusReason" : { CodeableConcept }, // Reason for current status
  "category" : { CodeableConcept }, // Classification of the procedure
  "code" : { CodeableConcept }, // Identification of the procedure
  "subject" : { Reference(Patient|Group) }, // R!  Who the procedure was performed on
  "encounter" : { Reference(Encounter) }, // Encounter created as part of
  // performed[x]: When the procedure was performed. One of these 5:
  "performedDateTime" : "<dateTime>",
  "performedPeriod" : { Period },
  "performedString" : "<string>",
  "performedAge" : { Age },
  "performedRange" : { Range },
  "recorder" : { Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) }, // Who recorded the procedure
  "asserter" : { Reference(Patient|RelatedPerson|Practitioner|
   PractitionerRole) }, // Person who asserts this procedure
  "performer" : [{ // The people who performed the procedure
    "function" : { CodeableConcept }, // Type of performance
    "actor" : { Reference(Practitioner|PractitionerRole|Organization|Patient|
    RelatedPerson|Device) }, // R!  The reference to the practitioner
    "onBehalfOf" : { Reference(Organization) } // Organization the device or practitioner was acting for
  }],
  "location" : { Reference(Location) }, // Where the procedure happened
  "reasonCode" : [{ CodeableConcept }], // Coded reason procedure performed
  "reasonReference" : [{ Reference(Condition|Observation|Procedure|
   DiagnosticReport|DocumentReference) }], // The justification that the procedure was performed
  "bodySite" : [{ CodeableConcept }], // Target body sites
  "outcome" : { CodeableConcept }, // The result of procedure
  "report" : [{ Reference(DiagnosticReport|DocumentReference|Composition) }], // Any report resulting from the procedure
  "complication" : [{ CodeableConcept }], // Complication following the procedure
  "complicationDetail" : [{ Reference(Condition) }], // A condition that is a result of the procedure
  "followUp" : [{ CodeableConcept }], // Instructions for follow up
  "note" : [{ Annotation }], // Additional information about the procedure
  "focalDevice" : [{ // Manipulated, implanted, or removed device
    "action" : { CodeableConcept }, // Kind of change to device
    "manipulated" : { Reference(Device) } // R!  Device that was changed
  }],
  "usedReference" : [{ Reference(Device|Medication|Substance) }], // Items used during procedure
  "usedCode" : [{ CodeableConcept }] // Coded items used during the procedure
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Procedure;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Procedure.identifier [ Identifier ], ... ; # 0..* External Identifiers for this procedure
  fhir:Procedure.instantiatesCanonical [ canonical(PlanDefinition|ActivityDefinition|Measure|OperationDefinition|Questionnaire) ], ... ; # 0..* Instantiates FHIR protocol or definition
  fhir:Procedure.instantiatesUri [ uri ], ... ; # 0..* Instantiates external protocol or definition
  fhir:Procedure.basedOn [ Reference(CarePlan|ServiceRequest) ], ... ; # 0..* A request for this procedure
  fhir:Procedure.partOf [ Reference(Procedure|Observation|MedicationAdministration) ], ... ; # 0..* Part of referenced event
  fhir:Procedure.status [ code ]; # 1..1 preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
  fhir:Procedure.statusReason [ CodeableConcept ]; # 0..1 Reason for current status
  fhir:Procedure.category [ CodeableConcept ]; # 0..1 Classification of the procedure
  fhir:Procedure.code [ CodeableConcept ]; # 0..1 Identification of the procedure
  fhir:Procedure.subject [ Reference(Patient|Group) ]; # 1..1 Who the procedure was performed on
  fhir:Procedure.encounter [ Reference(Encounter) ]; # 0..1 Encounter created as part of
  # Procedure.performed[x] : 0..1 When the procedure was performed. One of these 5
    fhir:Procedure.performedDateTime [ dateTime ]
    fhir:Procedure.performedPeriod [ Period ]
    fhir:Procedure.performedString [ string ]
    fhir:Procedure.performedAge [ Age ]
    fhir:Procedure.performedRange [ Range ]
  fhir:Procedure.recorder [ Reference(Patient|RelatedPerson|Practitioner|PractitionerRole) ]; # 0..1 Who recorded the procedure
  fhir:Procedure.asserter [ Reference(Patient|RelatedPerson|Practitioner|PractitionerRole) ]; # 0..1 Person who asserts this procedure
  fhir:Procedure.performer [ # 0..* The people who performed the procedure
    fhir:Procedure.performer.function [ CodeableConcept ]; # 0..1 Type of performance
    fhir:Procedure.performer.actor [ Reference(Practitioner|PractitionerRole|Organization|Patient|RelatedPerson|Device) ]; # 1..1 The reference to the practitioner
    fhir:Procedure.performer.onBehalfOf [ Reference(Organization) ]; # 0..1 Organization the device or practitioner was acting for
  ], ...;
  fhir:Procedure.location [ Reference(Location) ]; # 0..1 Where the procedure happened
  fhir:Procedure.reasonCode [ CodeableConcept ], ... ; # 0..* Coded reason procedure performed
  fhir:Procedure.reasonReference [ Reference(Condition|Observation|Procedure|DiagnosticReport|DocumentReference) ], ... ; # 0..* The justification that the procedure was performed
  fhir:Procedure.bodySite [ CodeableConcept ], ... ; # 0..* Target body sites
  fhir:Procedure.outcome [ CodeableConcept ]; # 0..1 The result of procedure
  fhir:Procedure.report [ Reference(DiagnosticReport|DocumentReference|Composition) ], ... ; # 0..* Any report resulting from the procedure
  fhir:Procedure.complication [ CodeableConcept ], ... ; # 0..* Complication following the procedure
  fhir:Procedure.complicationDetail [ Reference(Condition) ], ... ; # 0..* A condition that is a result of the procedure
  fhir:Procedure.followUp [ CodeableConcept ], ... ; # 0..* Instructions for follow up
  fhir:Procedure.note [ Annotation ], ... ; # 0..* Additional information about the procedure
  fhir:Procedure.focalDevice [ # 0..* Manipulated, implanted, or removed device
    fhir:Procedure.focalDevice.action [ CodeableConcept ]; # 0..1 Kind of change to device
    fhir:Procedure.focalDevice.manipulated [ Reference(Device) ]; # 1..1 Device that was changed
  ], ...;
  fhir:Procedure.usedReference [ Reference(Device|Medication|Substance) ], ... ; # 0..* Items used during procedure
  fhir:Procedure.usedCode [ CodeableConcept ], ... ; # 0..* Coded items used during the procedure
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Procedure](procedure.html#Procedure) |  |
| Procedure.instantiatesCanonical | - Added Element |
| Procedure.instantiatesUri | - Added Element |
| Procedure.basedOn | - Type Reference: Added Target Type ServiceRequest - Type Reference: Removed Target Types ProcedureRequest, ReferralRequest |
| Procedure.status | - Change value set from http://hl7.org/fhir/ValueSet/event-status to http://hl7.org/fhir/ValueSet/event-status|4.0.1 |
| Procedure.statusReason | - Added Element |
| Procedure.encounter | - Added Element |
| Procedure.performed[x] | - Add Types string, Age, Range |
| Procedure.recorder | - Added Element |
| Procedure.asserter | - Added Element |
| Procedure.performer.function | - Added Element |
| Procedure.performer.actor | - Type Reference: Added Target Type PractitionerRole |
| Procedure.reasonReference | - Type Reference: Added Target Types Procedure, DiagnosticReport, DocumentReference |
| Procedure.report | - Type Reference: Added Target Types DocumentReference, Composition |
| Procedure.definition | - deleted |
| Procedure.notDone | - deleted |
| Procedure.notDoneReason | - deleted |
| Procedure.context | - deleted |
| Procedure.performer.role | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](procedure.diff.xml) or [JSON](procedure.diff.json).

See [R3 <--> R4 Conversion Maps](procedure-version-maps.html) (status = 15 tests that all execute ok. 3 fail round-trip testing and 1 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](procedure-profiles.html) and the alternate definitions:
Master Definition [XML](procedure.profile.xml.html) + [JSON](procedure.profile.json.html),
[XML](xml.html) [Schema](procedure.xsd)/[Schematron](procedure.sch) + [JSON](json.html)
[Schema](procedure.schema.json.html), [ShEx](procedure.shex.html) (for [Turtle](rdf.html)) + [see the extensions](procedure-profiles.html) & the [dependency analysis](procedure-dependencies.html)

### 9.3.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Procedure.status | A code specifying the state of the procedure. | [Required](terminologies.html#required) | [EventStatus](valueset-event-status.html) |
| Procedure.statusReason | A code that identifies the reason a procedure was not performed. | [Example](terminologies.html#example) | [ProcedureNotPerformedReason(SNOMED-CT)](valueset-procedure-not-performed-reason.html) |
| Procedure.category | A code that classifies a procedure for searching, sorting and display purposes. | [Example](terminologies.html#example) | [ProcedureCategoryCodes(SNOMEDCT)](valueset-procedure-category.html) |
| Procedure.code | A code to identify a specific procedure . | [Example](terminologies.html#example) | [ProcedureCodes(SNOMEDCT)](valueset-procedure-code.html) |
| Procedure.performer.function | A code that identifies the role of a performer of the procedure. | [Example](terminologies.html#example) | [ProcedurePerformerRoleCodes](valueset-performer-role.html) |
| Procedure.reasonCode | A code that identifies the reason a procedure is required. | [Example](terminologies.html#example) | [ProcedureReasonCodes](valueset-procedure-reason.html) |
| Procedure.bodySite | Codes describing anatomical locations. May include laterality. | [Example](terminologies.html#example) | [SNOMEDCTBodyStructures](valueset-body-site.html) |
| Procedure.outcome | An outcome of a procedure - whether it was resolved or otherwise. | [Example](terminologies.html#example) | [ProcedureOutcomeCodes(SNOMEDCT)](valueset-procedure-outcome.html) |
| Procedure.complication | Codes describing complications that resulted from a procedure. | [Example](terminologies.html#example) | [Condition/Problem/DiagnosisCodes](valueset-condition-code.html) |
| Procedure.followUp | Specific follow up required for a procedure e.g. removal of sutures. | [Example](terminologies.html#example) | [ProcedureFollowUpCodes(SNOMEDCT)](valueset-procedure-followup.html) |
| Procedure.focalDevice.action | A kind of change that happened to the device during the procedure. | [Preferred](terminologies.html#preferred) | [ProcedureDeviceActionCodes](valueset-device-action.html) |
| Procedure.usedCode | Codes describing items used during a procedure. | [Example](terminologies.html#example) | [FHIRDeviceTypes](valueset-device-kind.html) |

### 9.3.3.2 Use of Procedure properties

Many of the elements of Procedure have inherent relationships and may be conveyed by the Procedure.code or in the text element
of the Procedure.code property. I.e. you may be able to infer category, bodySite and even indication.
Whether these other properties will be populated may vary by implementation.

Care should be taken to avoid nonsensical combinations/statements; e.g. "name=amputation, bodySite=heart".

### 9.3.3.3 Use of Procedure.used

For devices, these are devices that are incidental to / or used to perform the procedure - scalpels, gauze, endoscopes, etc.
Devices that are the focus of the procedure should appear in Procedure.device instead.

## 9.3.4 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| based-on | [reference](search.html#reference) | A request for this procedure | Procedure.basedOn ([CarePlan](careplan.html), [ServiceRequest](servicerequest.html)) |  |
| category | [token](search.html#token) | Classification of the procedure | Procedure.category |  |
| code | [token](search.html#token) | A code to identify a procedure | Procedure.code | [13 Resources](searchparameter-registry.html#clinical-code) |
| date | [date](search.html#date) | When the procedure was performed | Procedure.performed | [17 Resources](searchparameter-registry.html#clinical-date) |
| encounter | [reference](search.html#reference) | Encounter created as part of | Procedure.encounter ([Encounter](encounter.html)) | [12 Resources](searchparameter-registry.html#clinical-encounter) |
| identifier | [token](search.html#token) | A unique identifier for a procedure | Procedure.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) |
| instantiates-canonical | [reference](search.html#reference) | Instantiates FHIR protocol or definition | Procedure.instantiatesCanonical ([Questionnaire](questionnaire.html), [Measure](measure.html), [PlanDefinition](plandefinition.html), [OperationDefinition](operationdefinition.html), [ActivityDefinition](activitydefinition.html)) |  |
| instantiates-uri | [uri](search.html#uri) | Instantiates external protocol or definition | Procedure.instantiatesUri |  |
| location | [reference](search.html#reference) | Where the procedure happened | Procedure.location ([Location](location.html)) |  |
| part-of | [reference](search.html#reference) | Part of referenced event | Procedure.partOf ([Observation](observation.html), [Procedure](procedure.html), [MedicationAdministration](medicationadministration.html)) |  |
| patient | [reference](search.html#reference) | Search by subject - a patient | Procedure.subject.where(resolve() is Patient) ([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) |
| performer | [reference](search.html#reference) | The reference to the practitioner | Procedure.performer.actor ([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |  |
| reason-code | [token](search.html#token) | Coded reason procedure performed | Procedure.reasonCode |  |
| reason-reference | [reference](search.html#reference) | The justification that the procedure was performed | Procedure.reasonReference ([Condition](condition.html), [Observation](observation.html), [Procedure](procedure.html), [DiagnosticReport](diagnosticreport.html), [DocumentReference](documentreference.html)) |  |
| status | [token](search.html#token) | preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown | Procedure.status |  |
| subject | [reference](search.html#reference) | Search by subject | Procedure.subject ([Group](group.html), [Patient](patient.html)) |  |
