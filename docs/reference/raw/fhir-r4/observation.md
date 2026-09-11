---
id: observation
title: Observation
source_url: https://hl7.org/fhir/R4/observation.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:50Z'
sha256: ac4dfb923be5eef2f9184b6bcd61e3de1b4b8e3117d433a1b213a2caaa3647ba
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/observation.html) [R4B](http://hl7.org/fhir/R4B/observation.html) **R4** [R3](http://hl7.org/fhir/STU3/observation.html) [R2](http://hl7.org/fhir/DSTU2/observation.html)

- [Content](#)
- [Examples](observation-examples.html)
- [Detailed Descriptions](observation-definitions.html)
- [Mappings](observation-mappings.html)
- [Profiles & Extensions](observation-profiles.html)
- [Operations](observation-operations.html)
- [R3 Conversions](observation-version-maps.html)

# 10.1 Resource Observation - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Orders and Observations](http://www.hl7.org/Special/committees/orders/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) | [Normative](versions.html#std-process "Standard Status") (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Observation](ansi-observation.html) Package for further details. |

Measurements and simple assertions made about a patient, device or other subject.

## 10.1.1 Scope and Usage

This resource is an [*event resource*](workflow.html#event) from a FHIR workflow perspective - see [Workflow](workflow.html).

Observations are a central element in healthcare, used to support diagnosis, monitor progress, determine baselines and patterns and even capture demographic characteristics. Most observations are simple name/value pair assertions with some metadata, but some observations group other observations together logically, or even are multi-component observations. Note that the [DiagnosticReport](diagnosticreport.html) resource provides a clinical or workflow context for a set of observations and the Observation resource is referenced by DiagnosticReport to represent laboratory, imaging, and other clinical and diagnostic data to form a complete report.

Uses for the Observation resource include:

- Vital signs such as [body weight](observation-example.html), [blood pressure](observation-example-bloodpressure.html), and [temperature](observation-example-f202-temperature.html)
- Laboratory Data like [blood glucose](observation-example-f001-glucose.html), or an [estimated GFR](observation-example-f205-egfr.html)
- Imaging results like [bone density](observation-example-bmd.html) or fetal measurements
- Clinical Findings\* such as [abdominal tenderness](observation-example-abdo-tender.html)
- Device measurements such as [EKG data](observation-example-sample-data.html) or [Pulse Oximetry data](observation-example-satO2.html)
- Clinical assessment tools such as [APGAR](observation-example-5minute-apgar-score.html) or a [Glasgow Coma Score](observation-example-glasgow.html)
- Personal characteristics: such as [eye-color](observation-example-eye-color.html)
- Social history like tobacco use, family support, or cognitive status
- Core characteristics like pregnancy status, or a death assertion

\*The boundaries between clinical findings and disorders remains a challenge in medical ontology. Refer the [Boundaries](#bnr) section below and in [Condition](condition.html#bnr) for general guidance. These boundaries can be clarified by profiling Observation for a particular use case.

### 10.1.1.1 Core Profiles for Observation [Trial Use](versions.html#std-process "Standards Status = Trial Use")

The following core [profiles](profiling.html) for the Observation resource have been defined as well. If implementations use this Resource when expressing the profile-specific concepts as structured data, they **SHALL** conform to the following profiles:

| Profile | Description |
| --- | --- |
| [Vital signs](observation-vitalsigns.html) | The FHIR Vital Signs profile sets minimum expectations for the Observation Resource to record, search and fetch the vital signs (e.g. temperature, blood pressure, respiration rate, etc.) associated with a patient |

## 10.1.2 Boundaries and Relationships

At its core, Observation allows expressing a name-value pair or structured collection of name-value pairs. As such, it can support conveying any type of information desired. However, that is not its intent. Observation is intended for capturing measurements and subjective point-in-time assessments. It is not intended to be used for those specific contexts and use cases already covered by other FHIR resources. For example, the [AllergyIntolerance](allergyintolerance.html) resource represents a patient allergies, [MedicationStatement](medicationstatement.html) resource: medications taken by a patient,  [FamilyMemberHistory](familymemberhistory.html) resource: a patient's family history, [Procedure](procedure.html) resource: information about a procedure, and [QuestionnaireResponse](questionnaireresponse.html) resource: a set of answers to a set of questions. The Observation resource should not be used to record clinical diagnosis about a patient or subject that are typically captured in the [Condition](condition.html) resource or the ClinicalImpression resource. The Observation resource is often referenced by the Condition resource to provide specific subjective and objective data to support its assertions. There will however be situations of overlap. For example, a response to a question of "have you ever taken illicit drugs" could in principle be represented using MedicationStatement, but most systems would treat such an assertion as an Observation. In some cases, such as when source data is coming from an [HL7 v2 ![](external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) feed, a system might not have information that allows it to distinguish diagnosis, allergy and other "specialized" types of observations from laboratory, vital sign and other observation types intended to be conveyed with this resource. In those circumstances, such specialized observations may also appear using this resource. Adhering to such convention is an appropriate use of Observation. If implementers are uncertain whether a proposed use of Observation is appropriate, they're encouraged to consult with implementers on  [chat.fhir.org implementer's stream ![](external.png)](https://chat.fhir.org/)

The [Media](media.html) resource captures a specific type of observation whose value is audio, video or image data. This resource is used instead of Observation to represent such forms of information as it exposes the metadata relevant for interpreting the information. See Media's [boundaries section](media.html#bnr) to see how Media (and Observation) differs from [ImagingStudy](imagingstudy.html) and [DocumentReference](documentreference.html).

In contrast to the Observation resource, the [DiagnosticReport](diagnosticreport.html) resource typically includes additional clinical context and some mix of atomic results, images, imaging reports, textual and coded interpretation, and formatted representations. Laboratory reports, pathology reports, and imaging reports should be represented using the DiagnosticReport resource. The Observation resource is referenced by the DiagnosticReport to provide the atomic results for a particular investigation. "Laboratories routinely have a variable that is summative across a series of discrete variables - these are usually called 'impressions' or 'interpretations'. Sometimes they are algorithmically specified and sometimes they have the imprimatur of pathologists and they are conveyed in Observation or DiagnosticReport instead of the [Clinical Impression](clinicalimpression.html) resource. The Observation resource should not be used to record clinical diagnosis about a patient or subject as discussed above.

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [Appointment](appointment.html#Appointment), [CarePlan](careplan.html#CarePlan), [ChargeItem](chargeitem.html#ChargeItem), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Condition](condition.html#Condition), [Contract](contract.html#Contract), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [Encounter](encounter.html#Encounter), [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory), [Goal](goal.html#Goal), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MolecularSequence](molecularsequence.html#MolecularSequence), itself, [Procedure](procedure.html#Procedure), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [ServiceRequest](servicerequest.html#ServiceRequest) and [SupplyRequest](supplyrequest.html#SupplyRequest)

## 10.1.3 Resource Content

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
| .. [Observation](observation-definitions.html#Observation "Observation : Measurements and simple assertions made about a patient, device or other subject.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | Measurements and simple assertions + Rule: dataAbsentReason SHALL only be present if Observation.value[x] is not present + Rule: If Observation.code is the same as an Observation.component.code then the value element associated with the code SHALL NOT be present Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](observation-definitions.html#Observation.identifier "Observation.identifier : A unique identifier assigned to this observation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Business Identifier for observation |
| ... [basedOn](observation-definitions.html#Observation.basedOn "Observation.basedOn : A plan, proposal or order that is fulfilled in whole or in part by this event.  For example, a MedicationRequest may require a patient to have laboratory test performed before  it is dispensed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([CarePlan](careplan.html) | [DeviceRequest](devicerequest.html) | [ImmunizationRecommendation](immunizationrecommendation.html) | [MedicationRequest](medicationrequest.html) | [NutritionOrder](nutritionorder.html) | [ServiceRequest](servicerequest.html)) | Fulfills plan, proposal or order |
| ... [partOf](observation-definitions.html#Observation.partOf "Observation.partOf : A larger event of which this particular Observation is a component or step.  For example,  an observation as part of a procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([MedicationAdministration](medicationadministration.html) | [MedicationDispense](medicationdispense.html) | [MedicationStatement](medicationstatement.html) | [Procedure](procedure.html) | [Immunization](immunization.html) | [ImagingStudy](imagingstudy.html)) | Part of referenced event |
| ... [status](observation-definitions.html#Observation.status "Observation.status : The status of the result value.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | registered | preliminary | final | amended + [ObservationStatus](valueset-observation-status.html "Codes providing the status of an observation.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [category](observation-definitions.html#Observation.category "Observation.category : A code that classifies the general type of observation being made.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of type of observation [Observation Category Codes](valueset-observation-category.html "Codes for high level observation categories.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [code](observation-definitions.html#Observation.code "Observation.code : Describes what was observed. Sometimes this is called the observation \"name\".") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of observation (code / type) [LOINC Codes](valueset-observation-codes.html "Codes identifying names of simple observations.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](observation-definitions.html#Observation.subject "Observation.subject : The patient, or group of patients, location, or device this observation is about and into whose record the observation is placed. If the actual focus of the observation is different from the subject (or a sample of, part, or region of the subject), the `focus` element or the `code` itself specifies the actual focus of the observation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html) | [Device](device.html) | [Location](location.html)) | Who and/or what the observation is about |
| ... [focus](observation-definitions.html#Observation.focus "Observation.focus : The actual focus of an observation when it is not the patient of record representing something or someone associated with the patient such as a spouse, parent, fetus, or donor. For example, fetus observations in a mother's record.  The focus of an observation could also be an existing condition,  an intervention, the subject's diet,  another observation of the subject,  or a body structure such as tumor or implanted device.   An example use case would be using the Observation resource to capture whether the mother is trained to change her child's tracheostomy tube. In this example, the child is the patient of record and the mother is the focus.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [Reference](references.html#Reference)([Any](resourcelist.html)) | What the observation is about, when it is not about the subject of record |
| ... [encounter](observation-definitions.html#Observation.encounter "Observation.encounter : The healthcare event  (e.g. a patient and healthcare provider interaction) during which this observation is made.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Healthcare event during which this observation is made |
| ... [effective[x]](observation-definitions.html#Observation.effective_x_ "Observation.effective[x] : The time or time-period the observed value is asserted as being true. For biological subjects - e.g. human patients - this is usually called the \"physiologically relevant time\". This is usually either the time of the procedure or of specimen collection, but very often the source of the date/time is not known, only the date/time itself.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Clinically relevant time/time-period for observation |
| .... effectiveDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... effectivePeriod |  |  | [Period](datatypes.html#Period) |  |
| .... effectiveTiming |  |  | [Timing](datatypes.html#Timing) |  |
| .... effectiveInstant |  |  | [instant](datatypes.html#instant) |  |
| ... [issued](observation-definitions.html#Observation.issued "Observation.issued : The date and time this version of the observation was made available to providers, typically after the results have been reviewed and verified.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [instant](datatypes.html#instant) | Date/Time this version was made available |
| ... [performer](observation-definitions.html#Observation.performer "Observation.performer : Who was responsible for asserting the observed value as \"true\".") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [CareTeam](careteam.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who is responsible for the observation |
| ... [value[x]](observation-definitions.html#Observation.value_x_ "Observation.value[x] : The information determined as a result of making the observation, if the information has a simple value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 |  | Actual result |
| .... valueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| .... valueCodeableConcept |  |  | [CodeableConcept](datatypes.html#CodeableConcept) |  |
| .... valueString |  |  | [string](datatypes.html#string) |  |
| .... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| .... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| .... valueRange |  |  | [Range](datatypes.html#Range) |  |
| .... valueRatio |  |  | [Ratio](datatypes.html#Ratio) |  |
| .... valueSampledData |  |  | [SampledData](datatypes.html#SampledData) |  |
| .... valueTime |  |  | [time](datatypes.html#time) |  |
| .... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... valuePeriod |  |  | [Period](datatypes.html#Period) |  |
| ... [dataAbsentReason](observation-definitions.html#Observation.dataAbsentReason "Observation.dataAbsentReason : Provides a reason why the expected value in the element Observation.value[x] is missing.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the result is missing [DataAbsentReason](valueset-data-absent-reason.html "Codes specifying why the result (`Observation.value[x]`) is missing.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [interpretation](observation-definitions.html#Observation.interpretation "Observation.interpretation : A categorical assessment of an observation value.  For example, high, low, normal.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | High, low, normal, etc. [Observation Interpretation Codes](valueset-observation-interpretation.html "Codes identifying interpretations of observations.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [note](observation-definitions.html#Observation.note "Observation.note : Comments about the observation or the results.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Comments about the observation |
| ... [bodySite](observation-definitions.html#Observation.bodySite "Observation.bodySite : Indicates the site on the subject's body where the observation was made (i.e. the target site).") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Observed body part [SNOMED CT Body Structures](valueset-body-site.html "Codes describing anatomical locations. May include laterality.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [method](observation-definitions.html#Observation.method "Observation.method : Indicates the mechanism used to perform the observation.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How it was done [Observation Methods](valueset-observation-methods.html "Methods for simple observations.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specimen](observation-definitions.html#Observation.specimen "Observation.specimen : The specimen that was used when this observation was made.") |  | 0..1 | [Reference](references.html#Reference)([Specimen](specimen.html)) | Specimen used for this observation |
| ... [device](observation-definitions.html#Observation.device "Observation.device : The device used to generate the observation data.") |  | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [DeviceMetric](devicemetric.html)) | (Measurement) Device |
| ... [referenceRange](observation-definitions.html#Observation.referenceRange "Observation.referenceRange : Guidance on how to interpret the value by comparison to a normal or recommended range.  Multiple reference ranges are interpreted as an \"OR\".   In other words, to represent two distinct target populations, two `referenceRange` elements would be used.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Provides guide for interpretation + Rule: Must have at least a low or a high or text |
| .... [low](observation-definitions.html#Observation.referenceRange.low "Observation.referenceRange.low : The value of the low bound of the reference range.  The low bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless (e.g. reference range is <=2.3).") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Low Range, if relevant |
| .... [high](observation-definitions.html#Observation.referenceRange.high "Observation.referenceRange.high : The value of the high bound of the reference range.  The high bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless (e.g. reference range is >= 2.3).") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | High Range, if relevant |
| .... [type](observation-definitions.html#Observation.referenceRange.type "Observation.referenceRange.type : Codes to indicate the what part of the targeted reference population it applies to. For example, the normal or therapeutic range.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reference range qualifier [Observation Reference Range Meaning Codes](valueset-referencerange-meaning.html "Code for the meaning of a reference range.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [appliesTo](observation-definitions.html#Observation.referenceRange.appliesTo "Observation.referenceRange.appliesTo : Codes to indicate the target population this reference range applies to.  For example, a reference range may be based on the normal population or a particular sex or race.  Multiple `appliesTo`  are interpreted as an \"AND\" of the target populations.  For example, to represent a target population of African American females, both a code of female and a code for African American would be used.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Reference range population [Observation Reference Range Applies To Codes](valueset-referencerange-appliesto.html "Codes identifying the population the reference range applies to.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [age](observation-definitions.html#Observation.referenceRange.age "Observation.referenceRange.age : The age at which this reference range is applicable. This is a neonatal age (e.g. number of weeks at term) if the meaning says so.") |  | 0..1 | [Range](datatypes.html#Range) | Applicable age range, if relevant |
| .... [text](observation-definitions.html#Observation.referenceRange.text "Observation.referenceRange.text : Text based reference range in an observation which may be used when a quantitative range is not appropriate for an observation.  An example would be a reference value of \"Negative\" or a list or table of \"normals\".") |  | 0..1 | [string](datatypes.html#string) | Text based reference range in an observation |
| ... [hasMember](observation-definitions.html#Observation.hasMember "Observation.hasMember : This observation is a group observation (e.g. a battery, a panel of tests, a set of vital sign measurements) that includes the target as a member of the group.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Observation](observation.html) | [QuestionnaireResponse](questionnaireresponse.html) | [MolecularSequence](molecularsequence.html)) | Related resource that belongs to the Observation group |
| ... [derivedFrom](observation-definitions.html#Observation.derivedFrom "Observation.derivedFrom : The target resource that represents a measurement from which this observation value is derived. For example, a calculated anion gap or a fetal measurement based on an ultrasound image.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([DocumentReference](documentreference.html) | [ImagingStudy](imagingstudy.html) | [Media](media.html) | [QuestionnaireResponse](questionnaireresponse.html) | [Observation](observation.html) | [MolecularSequence](molecularsequence.html)) | Related measurements the observation is made from |
| ... [component](observation-definitions.html#Observation.component "Observation.component : Some observations have multiple component observations.  These component observations are expressed as separate code value pairs that share the same attributes.  Examples include systolic and diastolic component observations for blood pressure measurement and multiple component observations for genetics observations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Component results |
| .... [code](observation-definitions.html#Observation.component.code "Observation.component.code : Describes what was observed. Sometimes this is called the observation \"code\".") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of component observation (code / type) [LOINC Codes](valueset-observation-codes.html "Codes identifying names of simple observations.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [value[x]](observation-definitions.html#Observation.component.value_x_ "Observation.component.value[x] : The information determined as a result of making the observation, if the information has a simple value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Actual component result |
| ..... valueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| ..... valueCodeableConcept |  |  | [CodeableConcept](datatypes.html#CodeableConcept) |  |
| ..... valueString |  |  | [string](datatypes.html#string) |  |
| ..... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| ..... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| ..... valueRange |  |  | [Range](datatypes.html#Range) |  |
| ..... valueRatio |  |  | [Ratio](datatypes.html#Ratio) |  |
| ..... valueSampledData |  |  | [SampledData](datatypes.html#SampledData) |  |
| ..... valueTime |  |  | [time](datatypes.html#time) |  |
| ..... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| ..... valuePeriod |  |  | [Period](datatypes.html#Period) |  |
| .... [dataAbsentReason](observation-definitions.html#Observation.component.dataAbsentReason "Observation.component.dataAbsentReason : Provides a reason why the expected value in the element Observation.component.value[x] is missing.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the component result is missing [DataAbsentReason](valueset-data-absent-reason.html "Codes specifying why the result (`Observation.value[x]`) is missing.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [interpretation](observation-definitions.html#Observation.component.interpretation "Observation.component.interpretation : A categorical assessment of an observation value.  For example, high, low, normal.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | High, low, normal, etc. [Observation Interpretation Codes](valueset-observation-interpretation.html "Codes identifying interpretations of observations.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [referenceRange](observation-definitions.html#Observation.component.referenceRange "Observation.component.referenceRange : Guidance on how to interpret the value by comparison to a normal or recommended range.") |  | 0..\* | see [referenceRange](#Observation.referenceRange "Observation.referenceRange") | Provides guide for interpretation of component result |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Observation xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Business Identifier for observation --></identifier>
 <basedOn><!-- 0..* Reference(CarePlan|DeviceRequest|ImmunizationRecommendation|
   MedicationRequest|NutritionOrder|ServiceRequest) Fulfills plan, proposal or order --></basedOn>
 <partOf><!-- 0..* Reference(MedicationAdministration|MedicationDispense|
   MedicationStatement|Procedure|Immunization|ImagingStudy) Part of referenced event --></partOf>
 <status value="[code]"/><!-- 1..1 registered | preliminary | final | amended + -->
 <category><!-- 0..* CodeableConcept Classification of  type of observation --></category>
 <code><!-- 1..1 CodeableConcept Type of observation (code / type) --></code>
 <subject><!-- 0..1 Reference(Patient|Group|Device|Location) Who and/or what the observation is about --></subject>
 <focus><!-- 0..* Reference(Any) What the observation is about, when it is not about the subject of record --></focus>
 <encounter><!-- 0..1 Reference(Encounter) Healthcare event during which this observation is made --></encounter>
 <effective[x]><!-- 0..1 dateTime|Period|Timing|instant Clinically relevant time/time-period for observation --></effective[x]>
 <issued value="[instant]"/><!-- 0..1 Date/Time this version was made available -->
 <performer><!-- 0..* Reference(Practitioner|PractitionerRole|Organization|
   CareTeam|Patient|RelatedPerson) Who is responsible for the observation --></performer>
 <value[x]><!-- ![??](lock.png) 0..1 Quantity|CodeableConcept|string|boolean|integer|Range|Ratio|
   SampledData|time|dateTime|Period Actual result --></value[x]>
 <dataAbsentReason><!-- ![??](lock.png) 0..1 CodeableConcept Why the result is missing --></dataAbsentReason>
 <interpretation><!-- 0..* CodeableConcept High, low, normal, etc. --></interpretation>
 <note><!-- 0..* Annotation Comments about the observation --></note>
 <bodySite><!-- 0..1 CodeableConcept Observed body part --></bodySite>
 <method><!-- 0..1 CodeableConcept How it was done --></method>
 <specimen><!-- 0..1 Reference(Specimen) Specimen used for this observation --></specimen>
 <device><!-- 0..1 Reference(Device|DeviceMetric) (Measurement) Device --></device>
 <referenceRange>  <!-- 0..* Provides guide for interpretation -->
  <low><!-- ![??](lock.png) 0..1 Quantity(SimpleQuantity) Low Range, if relevant --></low>
  <high><!-- ![??](lock.png) 0..1 Quantity(SimpleQuantity) High Range, if relevant --></high>
  <type><!-- 0..1 CodeableConcept Reference range qualifier --></type>
  <appliesTo><!-- 0..* CodeableConcept Reference range population --></appliesTo>
  <age><!-- 0..1 Range Applicable age range, if relevant --></age>
  <text value="[string]"/><!-- 0..1 Text based reference range in an observation -->
 </referenceRange>
 <hasMember><!-- 0..* Reference(Observation|QuestionnaireResponse|
   MolecularSequence) Related resource that belongs to the Observation group --></hasMember>
 <derivedFrom><!-- 0..* Reference(DocumentReference|ImagingStudy|Media|
   QuestionnaireResponse|Observation|MolecularSequence) Related measurements the observation is made from --></derivedFrom>
 <component>  <!-- 0..* Component results -->
  <code><!-- 1..1 CodeableConcept Type of component observation (code / type) --></code>
  <value[x]><!-- 0..1 Quantity|CodeableConcept|string|boolean|integer|Range|
    Ratio|SampledData|time|dateTime|Period Actual component result --></value[x]>
  <dataAbsentReason><!-- ![??](lock.png) 0..1 CodeableConcept Why the component result is missing --></dataAbsentReason>
  <interpretation><!-- 0..* CodeableConcept High, low, normal, etc. --></interpretation>
  <referenceRange><!-- 0..* Content as for Observation.referenceRange Provides guide for interpretation of component result --></referenceRange>
 </component>
</Observation>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Observation",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Business Identifier for observation
  "basedOn" : [{ Reference(CarePlan|DeviceRequest|ImmunizationRecommendation|
   MedicationRequest|NutritionOrder|ServiceRequest) }], // Fulfills plan, proposal or order
  "partOf" : [{ Reference(MedicationAdministration|MedicationDispense|
   MedicationStatement|Procedure|Immunization|ImagingStudy) }], // Part of referenced event
  "status" : "<code>", // R!  registered | preliminary | final | amended +
  "category" : [{ CodeableConcept }], // Classification of  type of observation
  "code" : { CodeableConcept }, // R!  Type of observation (code / type)
  "subject" : { Reference(Patient|Group|Device|Location) }, // Who and/or what the observation is about
  "focus" : [{ Reference(Any) }], // What the observation is about, when it is not about the subject of record
  "encounter" : { Reference(Encounter) }, // Healthcare event during which this observation is made
  // effective[x]: Clinically relevant time/time-period for observation. One of these 4:
  "effectiveDateTime" : "<dateTime>",
  "effectivePeriod" : { Period },
  "effectiveTiming" : { Timing },
  "effectiveInstant" : "<instant>",
  "issued" : "<instant>", // Date/Time this version was made available
  "performer" : [{ Reference(Practitioner|PractitionerRole|Organization|
   CareTeam|Patient|RelatedPerson) }], // Who is responsible for the observation
  // value[x]: Actual result. One of these 11:
  "valueQuantity" : { Quantity },
  "valueCodeableConcept" : { CodeableConcept },
  "valueString" : "<string>",
  "valueBoolean" : <boolean>,
  "valueInteger" : <integer>,
  "valueRange" : { Range },
  "valueRatio" : { Ratio },
  "valueSampledData" : { SampledData },
  "valueTime" : "<time>",
  "valueDateTime" : "<dateTime>",
  "valuePeriod" : { Period },
  "dataAbsentReason" : { CodeableConcept }, // C? Why the result is missing
  "interpretation" : [{ CodeableConcept }], // High, low, normal, etc.
  "note" : [{ Annotation }], // Comments about the observation
  "bodySite" : { CodeableConcept }, // Observed body part
  "method" : { CodeableConcept }, // How it was done
  "specimen" : { Reference(Specimen) }, // Specimen used for this observation
  "device" : { Reference(Device|DeviceMetric) }, // (Measurement) Device
  "referenceRange" : [{ // Provides guide for interpretation
    "low" : { Quantity(SimpleQuantity) }, // C? Low Range, if relevant
    "high" : { Quantity(SimpleQuantity) }, // C? High Range, if relevant
    "type" : { CodeableConcept }, // Reference range qualifier
    "appliesTo" : [{ CodeableConcept }], // Reference range population
    "age" : { Range }, // Applicable age range, if relevant
    "text" : "<string>" // Text based reference range in an observation
  }],
  "hasMember" : [{ Reference(Observation|QuestionnaireResponse|
   MolecularSequence) }], // Related resource that belongs to the Observation group
  "derivedFrom" : [{ Reference(DocumentReference|ImagingStudy|Media|
   QuestionnaireResponse|Observation|MolecularSequence) }], // Related measurements the observation is made from
  "component" : [{ // Component results
    "code" : { CodeableConcept }, // R!  Type of component observation (code / type)
    // value[x]: Actual component result. One of these 11:
    "valueQuantity" : { Quantity },
    "valueCodeableConcept" : { CodeableConcept },
    "valueString" : "<string>",
    "valueBoolean" : <boolean>,
    "valueInteger" : <integer>,
    "valueRange" : { Range },
    "valueRatio" : { Ratio },
    "valueSampledData" : { SampledData },
    "valueTime" : "<time>",
    "valueDateTime" : "<dateTime>",
    "valuePeriod" : { Period },
    "dataAbsentReason" : { CodeableConcept }, // C? Why the component result is missing
    "interpretation" : [{ CodeableConcept }], // High, low, normal, etc.
    "referenceRange" : [{ Content as for Observation.referenceRange }] // Provides guide for interpretation of component result
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Observation;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Observation.identifier [ Identifier ], ... ; # 0..* Business Identifier for observation
  fhir:Observation.basedOn [ Reference(CarePlan|DeviceRequest|ImmunizationRecommendation|MedicationRequest|
  NutritionOrder|ServiceRequest) ], ... ; # 0..* Fulfills plan, proposal or order
  fhir:Observation.partOf [ Reference(MedicationAdministration|MedicationDispense|MedicationStatement|Procedure|
  Immunization|ImagingStudy) ], ... ; # 0..* Part of referenced event
  fhir:Observation.status [ code ]; # 1..1 registered | preliminary | final | amended +
  fhir:Observation.category [ CodeableConcept ], ... ; # 0..* Classification of  type of observation
  fhir:Observation.code [ CodeableConcept ]; # 1..1 Type of observation (code / type)
  fhir:Observation.subject [ Reference(Patient|Group|Device|Location) ]; # 0..1 Who and/or what the observation is about
  fhir:Observation.focus [ Reference(Any) ], ... ; # 0..* What the observation is about, when it is not about the subject of record
  fhir:Observation.encounter [ Reference(Encounter) ]; # 0..1 Healthcare event during which this observation is made
  # Observation.effective[x] : 0..1 Clinically relevant time/time-period for observation. One of these 4
    fhir:Observation.effectiveDateTime [ dateTime ]
    fhir:Observation.effectivePeriod [ Period ]
    fhir:Observation.effectiveTiming [ Timing ]
    fhir:Observation.effectiveInstant [ instant ]
  fhir:Observation.issued [ instant ]; # 0..1 Date/Time this version was made available
  fhir:Observation.performer [ Reference(Practitioner|PractitionerRole|Organization|CareTeam|Patient|RelatedPerson) ], ... ; # 0..* Who is responsible for the observation
  # Observation.value[x] : 0..1 Actual result. One of these 11
    fhir:Observation.valueQuantity [ Quantity ]
    fhir:Observation.valueCodeableConcept [ CodeableConcept ]
    fhir:Observation.valueString [ string ]
    fhir:Observation.valueBoolean [ boolean ]
    fhir:Observation.valueInteger [ integer ]
    fhir:Observation.valueRange [ Range ]
    fhir:Observation.valueRatio [ Ratio ]
    fhir:Observation.valueSampledData [ SampledData ]
    fhir:Observation.valueTime [ time ]
    fhir:Observation.valueDateTime [ dateTime ]
    fhir:Observation.valuePeriod [ Period ]
  fhir:Observation.dataAbsentReason [ CodeableConcept ]; # 0..1 Why the result is missing
  fhir:Observation.interpretation [ CodeableConcept ], ... ; # 0..* High, low, normal, etc.
  fhir:Observation.note [ Annotation ], ... ; # 0..* Comments about the observation
  fhir:Observation.bodySite [ CodeableConcept ]; # 0..1 Observed body part
  fhir:Observation.method [ CodeableConcept ]; # 0..1 How it was done
  fhir:Observation.specimen [ Reference(Specimen) ]; # 0..1 Specimen used for this observation
  fhir:Observation.device [ Reference(Device|DeviceMetric) ]; # 0..1 (Measurement) Device
  fhir:Observation.referenceRange [ # 0..* Provides guide for interpretation
    fhir:Observation.referenceRange.low [ Quantity(SimpleQuantity) ]; # 0..1 Low Range, if relevant
    fhir:Observation.referenceRange.high [ Quantity(SimpleQuantity) ]; # 0..1 High Range, if relevant
    fhir:Observation.referenceRange.type [ CodeableConcept ]; # 0..1 Reference range qualifier
    fhir:Observation.referenceRange.appliesTo [ CodeableConcept ], ... ; # 0..* Reference range population
    fhir:Observation.referenceRange.age [ Range ]; # 0..1 Applicable age range, if relevant
    fhir:Observation.referenceRange.text [ string ]; # 0..1 Text based reference range in an observation
  ], ...;
  fhir:Observation.hasMember [ Reference(Observation|QuestionnaireResponse|MolecularSequence) ], ... ; # 0..* Related resource that belongs to the Observation group
  fhir:Observation.derivedFrom [ Reference(DocumentReference|ImagingStudy|Media|QuestionnaireResponse|Observation|
  MolecularSequence) ], ... ; # 0..* Related measurements the observation is made from
  fhir:Observation.component [ # 0..* Component results
    fhir:Observation.component.code [ CodeableConcept ]; # 1..1 Type of component observation (code / type)
    # Observation.component.value[x] : 0..1 Actual component result. One of these 11
      fhir:Observation.component.valueQuantity [ Quantity ]
      fhir:Observation.component.valueCodeableConcept [ CodeableConcept ]
      fhir:Observation.component.valueString [ string ]
      fhir:Observation.component.valueBoolean [ boolean ]
      fhir:Observation.component.valueInteger [ integer ]
      fhir:Observation.component.valueRange [ Range ]
      fhir:Observation.component.valueRatio [ Ratio ]
      fhir:Observation.component.valueSampledData [ SampledData ]
      fhir:Observation.component.valueTime [ time ]
      fhir:Observation.component.valueDateTime [ dateTime ]
      fhir:Observation.component.valuePeriod [ Period ]
    fhir:Observation.component.dataAbsentReason [ CodeableConcept ]; # 0..1 Why the component result is missing
    fhir:Observation.component.interpretation [ CodeableConcept ], ... ; # 0..* High, low, normal, etc.
    fhir:Observation.component.referenceRange [ See Observation.referenceRange ], ... ; # 0..* Provides guide for interpretation of component result
  ], ...;
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Observation](observation.html#Observation) |  |
| Observation.basedOn | - Type Reference: Added Target Type ServiceRequest - Type Reference: Removed Target Types ProcedureRequest, ReferralRequest |
| Observation.partOf | - Added Element |
| Observation.status | - Change value set from http://hl7.org/fhir/ValueSet/observation-status to http://hl7.org/fhir/ValueSet/observation-status|4.0.1 |
| Observation.focus | - Added Element |
| Observation.encounter | - Renamed from context to encounter - Type Reference: Removed Target Type EpisodeOfCare |
| Observation.effective[x] | - Add Types Timing, instant |
| Observation.performer | - Type Reference: Added Target Types PractitionerRole, CareTeam |
| Observation.value[x] | - Add Type integer - Remove Type Attachment |
| Observation.dataAbsentReason | - Change value set from http://hl7.org/fhir/ValueSet/observation-valueabsentreason to http://hl7.org/fhir/ValueSet/data-absent-reason - Change code system for extensibly bound codes from "http://hl7.org/fhir/data-absent-reason" to "http://terminology.hl7.org/CodeSystem/data-absent-reason" |
| Observation.interpretation | - Max Cardinality changed from 1 to \* - Change code system for extensibly bound codes from "http://terminology.hl7.org/CodeSystem/v2-0078" to "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation" |
| Observation.note | - Renamed from comment to note - Max Cardinality changed from 1 to \* - Type changed from string to Annotation |
| Observation.referenceRange.type | - Remove Binding `http://hl7.org/fhir/ValueSet/referencerange-meaning` (extensible) |
| Observation.hasMember | - Added Element |
| Observation.derivedFrom | - Added Element |
| Observation.component.value[x] | - Add Types boolean, integer - Remove Type Attachment |
| Observation.component.dataAbsentReason | - Change value set from http://hl7.org/fhir/ValueSet/observation-valueabsentreason to http://hl7.org/fhir/ValueSet/data-absent-reason - Change code system for extensibly bound codes from "http://hl7.org/fhir/data-absent-reason" to "http://terminology.hl7.org/CodeSystem/data-absent-reason" |
| Observation.component.interpretation | - Max Cardinality changed from 1 to \* - Change code system for extensibly bound codes from "http://terminology.hl7.org/CodeSystem/v2-0078" to "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation" |
| Observation.related | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](observation.diff.xml) or [JSON](observation.diff.json).

See [R3 <--> R4 Conversion Maps](observation-version-maps.html) (status = 48 tests that all execute ok. All tests pass round-trip testing and 23 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Observation](observation-definitions.html#Observation "Observation : Measurements and simple assertions made about a patient, device or other subject.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | Measurements and simple assertions + Rule: dataAbsentReason SHALL only be present if Observation.value[x] is not present + Rule: If Observation.code is the same as an Observation.component.code then the value element associated with the code SHALL NOT be present Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](observation-definitions.html#Observation.identifier "Observation.identifier : A unique identifier assigned to this observation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Business Identifier for observation |
| ... [basedOn](observation-definitions.html#Observation.basedOn "Observation.basedOn : A plan, proposal or order that is fulfilled in whole or in part by this event.  For example, a MedicationRequest may require a patient to have laboratory test performed before  it is dispensed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([CarePlan](careplan.html) | [DeviceRequest](devicerequest.html) | [ImmunizationRecommendation](immunizationrecommendation.html) | [MedicationRequest](medicationrequest.html) | [NutritionOrder](nutritionorder.html) | [ServiceRequest](servicerequest.html)) | Fulfills plan, proposal or order |
| ... [partOf](observation-definitions.html#Observation.partOf "Observation.partOf : A larger event of which this particular Observation is a component or step.  For example,  an observation as part of a procedure.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([MedicationAdministration](medicationadministration.html) | [MedicationDispense](medicationdispense.html) | [MedicationStatement](medicationstatement.html) | [Procedure](procedure.html) | [Immunization](immunization.html) | [ImagingStudy](imagingstudy.html)) | Part of referenced event |
| ... [status](observation-definitions.html#Observation.status "Observation.status : The status of the result value.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | registered | preliminary | final | amended + [ObservationStatus](valueset-observation-status.html "Codes providing the status of an observation.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [category](observation-definitions.html#Observation.category "Observation.category : A code that classifies the general type of observation being made.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of type of observation [Observation Category Codes](valueset-observation-category.html "Codes for high level observation categories.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [code](observation-definitions.html#Observation.code "Observation.code : Describes what was observed. Sometimes this is called the observation \"name\".") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of observation (code / type) [LOINC Codes](valueset-observation-codes.html "Codes identifying names of simple observations.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [subject](observation-definitions.html#Observation.subject "Observation.subject : The patient, or group of patients, location, or device this observation is about and into whose record the observation is placed. If the actual focus of the observation is different from the subject (or a sample of, part, or region of the subject), the `focus` element or the `code` itself specifies the actual focus of the observation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html) | [Device](device.html) | [Location](location.html)) | Who and/or what the observation is about |
| ... [focus](observation-definitions.html#Observation.focus "Observation.focus : The actual focus of an observation when it is not the patient of record representing something or someone associated with the patient such as a spouse, parent, fetus, or donor. For example, fetus observations in a mother's record.  The focus of an observation could also be an existing condition,  an intervention, the subject's diet,  another observation of the subject,  or a body structure such as tumor or implanted device.   An example use case would be using the Observation resource to capture whether the mother is trained to change her child's tracheostomy tube. In this example, the child is the patient of record and the mother is the focus.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [Reference](references.html#Reference)([Any](resourcelist.html)) | What the observation is about, when it is not about the subject of record |
| ... [encounter](observation-definitions.html#Observation.encounter "Observation.encounter : The healthcare event  (e.g. a patient and healthcare provider interaction) during which this observation is made.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Healthcare event during which this observation is made |
| ... [effective[x]](observation-definitions.html#Observation.effective_x_ "Observation.effective[x] : The time or time-period the observed value is asserted as being true. For biological subjects - e.g. human patients - this is usually called the \"physiologically relevant time\". This is usually either the time of the procedure or of specimen collection, but very often the source of the date/time is not known, only the date/time itself.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Clinically relevant time/time-period for observation |
| .... effectiveDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... effectivePeriod |  |  | [Period](datatypes.html#Period) |  |
| .... effectiveTiming |  |  | [Timing](datatypes.html#Timing) |  |
| .... effectiveInstant |  |  | [instant](datatypes.html#instant) |  |
| ... [issued](observation-definitions.html#Observation.issued "Observation.issued : The date and time this version of the observation was made available to providers, typically after the results have been reviewed and verified.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [instant](datatypes.html#instant) | Date/Time this version was made available |
| ... [performer](observation-definitions.html#Observation.performer "Observation.performer : Who was responsible for asserting the observed value as \"true\".") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [CareTeam](careteam.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who is responsible for the observation |
| ... [value[x]](observation-definitions.html#Observation.value_x_ "Observation.value[x] : The information determined as a result of making the observation, if the information has a simple value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 |  | Actual result |
| .... valueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| .... valueCodeableConcept |  |  | [CodeableConcept](datatypes.html#CodeableConcept) |  |
| .... valueString |  |  | [string](datatypes.html#string) |  |
| .... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| .... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| .... valueRange |  |  | [Range](datatypes.html#Range) |  |
| .... valueRatio |  |  | [Ratio](datatypes.html#Ratio) |  |
| .... valueSampledData |  |  | [SampledData](datatypes.html#SampledData) |  |
| .... valueTime |  |  | [time](datatypes.html#time) |  |
| .... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... valuePeriod |  |  | [Period](datatypes.html#Period) |  |
| ... [dataAbsentReason](observation-definitions.html#Observation.dataAbsentReason "Observation.dataAbsentReason : Provides a reason why the expected value in the element Observation.value[x] is missing.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the result is missing [DataAbsentReason](valueset-data-absent-reason.html "Codes specifying why the result (`Observation.value[x]`) is missing.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [interpretation](observation-definitions.html#Observation.interpretation "Observation.interpretation : A categorical assessment of an observation value.  For example, high, low, normal.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | High, low, normal, etc. [Observation Interpretation Codes](valueset-observation-interpretation.html "Codes identifying interpretations of observations.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [note](observation-definitions.html#Observation.note "Observation.note : Comments about the observation or the results.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Comments about the observation |
| ... [bodySite](observation-definitions.html#Observation.bodySite "Observation.bodySite : Indicates the site on the subject's body where the observation was made (i.e. the target site).") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Observed body part [SNOMED CT Body Structures](valueset-body-site.html "Codes describing anatomical locations. May include laterality.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [method](observation-definitions.html#Observation.method "Observation.method : Indicates the mechanism used to perform the observation.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How it was done [Observation Methods](valueset-observation-methods.html "Methods for simple observations.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specimen](observation-definitions.html#Observation.specimen "Observation.specimen : The specimen that was used when this observation was made.") |  | 0..1 | [Reference](references.html#Reference)([Specimen](specimen.html)) | Specimen used for this observation |
| ... [device](observation-definitions.html#Observation.device "Observation.device : The device used to generate the observation data.") |  | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [DeviceMetric](devicemetric.html)) | (Measurement) Device |
| ... [referenceRange](observation-definitions.html#Observation.referenceRange "Observation.referenceRange : Guidance on how to interpret the value by comparison to a normal or recommended range.  Multiple reference ranges are interpreted as an \"OR\".   In other words, to represent two distinct target populations, two `referenceRange` elements would be used.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Provides guide for interpretation + Rule: Must have at least a low or a high or text |
| .... [low](observation-definitions.html#Observation.referenceRange.low "Observation.referenceRange.low : The value of the low bound of the reference range.  The low bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless (e.g. reference range is <=2.3).") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Low Range, if relevant |
| .... [high](observation-definitions.html#Observation.referenceRange.high "Observation.referenceRange.high : The value of the high bound of the reference range.  The high bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless (e.g. reference range is >= 2.3).") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | High Range, if relevant |
| .... [type](observation-definitions.html#Observation.referenceRange.type "Observation.referenceRange.type : Codes to indicate the what part of the targeted reference population it applies to. For example, the normal or therapeutic range.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reference range qualifier [Observation Reference Range Meaning Codes](valueset-referencerange-meaning.html "Code for the meaning of a reference range.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| .... [appliesTo](observation-definitions.html#Observation.referenceRange.appliesTo "Observation.referenceRange.appliesTo : Codes to indicate the target population this reference range applies to.  For example, a reference range may be based on the normal population or a particular sex or race.  Multiple `appliesTo`  are interpreted as an \"AND\" of the target populations.  For example, to represent a target population of African American females, both a code of female and a code for African American would be used.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Reference range population [Observation Reference Range Applies To Codes](valueset-referencerange-appliesto.html "Codes identifying the population the reference range applies to.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [age](observation-definitions.html#Observation.referenceRange.age "Observation.referenceRange.age : The age at which this reference range is applicable. This is a neonatal age (e.g. number of weeks at term) if the meaning says so.") |  | 0..1 | [Range](datatypes.html#Range) | Applicable age range, if relevant |
| .... [text](observation-definitions.html#Observation.referenceRange.text "Observation.referenceRange.text : Text based reference range in an observation which may be used when a quantitative range is not appropriate for an observation.  An example would be a reference value of \"Negative\" or a list or table of \"normals\".") |  | 0..1 | [string](datatypes.html#string) | Text based reference range in an observation |
| ... [hasMember](observation-definitions.html#Observation.hasMember "Observation.hasMember : This observation is a group observation (e.g. a battery, a panel of tests, a set of vital sign measurements) that includes the target as a member of the group.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Observation](observation.html) | [QuestionnaireResponse](questionnaireresponse.html) | [MolecularSequence](molecularsequence.html)) | Related resource that belongs to the Observation group |
| ... [derivedFrom](observation-definitions.html#Observation.derivedFrom "Observation.derivedFrom : The target resource that represents a measurement from which this observation value is derived. For example, a calculated anion gap or a fetal measurement based on an ultrasound image.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([DocumentReference](documentreference.html) | [ImagingStudy](imagingstudy.html) | [Media](media.html) | [QuestionnaireResponse](questionnaireresponse.html) | [Observation](observation.html) | [MolecularSequence](molecularsequence.html)) | Related measurements the observation is made from |
| ... [component](observation-definitions.html#Observation.component "Observation.component : Some observations have multiple component observations.  These component observations are expressed as separate code value pairs that share the same attributes.  Examples include systolic and diastolic component observations for blood pressure measurement and multiple component observations for genetics observations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Component results |
| .... [code](observation-definitions.html#Observation.component.code "Observation.component.code : Describes what was observed. Sometimes this is called the observation \"code\".") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of component observation (code / type) [LOINC Codes](valueset-observation-codes.html "Codes identifying names of simple observations.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [value[x]](observation-definitions.html#Observation.component.value_x_ "Observation.component.value[x] : The information determined as a result of making the observation, if the information has a simple value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Actual component result |
| ..... valueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| ..... valueCodeableConcept |  |  | [CodeableConcept](datatypes.html#CodeableConcept) |  |
| ..... valueString |  |  | [string](datatypes.html#string) |  |
| ..... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| ..... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| ..... valueRange |  |  | [Range](datatypes.html#Range) |  |
| ..... valueRatio |  |  | [Ratio](datatypes.html#Ratio) |  |
| ..... valueSampledData |  |  | [SampledData](datatypes.html#SampledData) |  |
| ..... valueTime |  |  | [time](datatypes.html#time) |  |
| ..... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| ..... valuePeriod |  |  | [Period](datatypes.html#Period) |  |
| .... [dataAbsentReason](observation-definitions.html#Observation.component.dataAbsentReason "Observation.component.dataAbsentReason : Provides a reason why the expected value in the element Observation.component.value[x] is missing.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the component result is missing [DataAbsentReason](valueset-data-absent-reason.html "Codes specifying why the result (`Observation.value[x]`) is missing.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [interpretation](observation-definitions.html#Observation.component.interpretation "Observation.component.interpretation : A categorical assessment of an observation value.  For example, high, low, normal.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | High, low, normal, etc. [Observation Interpretation Codes](valueset-observation-interpretation.html "Codes identifying interpretations of observations.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [referenceRange](observation-definitions.html#Observation.component.referenceRange "Observation.component.referenceRange : Guidance on how to interpret the value by comparison to a normal or recommended range.") |  | 0..\* | see [referenceRange](#Observation.referenceRange "Observation.referenceRange") | Provides guide for interpretation of component result |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Observation xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Business Identifier for observation --></identifier>
 <basedOn><!-- 0..* Reference(CarePlan|DeviceRequest|ImmunizationRecommendation|
   MedicationRequest|NutritionOrder|ServiceRequest) Fulfills plan, proposal or order --></basedOn>
 <partOf><!-- 0..* Reference(MedicationAdministration|MedicationDispense|
   MedicationStatement|Procedure|Immunization|ImagingStudy) Part of referenced event --></partOf>
 <status value="[code]"/><!-- 1..1 registered | preliminary | final | amended + -->
 <category><!-- 0..* CodeableConcept Classification of  type of observation --></category>
 <code><!-- 1..1 CodeableConcept Type of observation (code / type) --></code>
 <subject><!-- 0..1 Reference(Patient|Group|Device|Location) Who and/or what the observation is about --></subject>
 <focus><!-- 0..* Reference(Any) What the observation is about, when it is not about the subject of record --></focus>
 <encounter><!-- 0..1 Reference(Encounter) Healthcare event during which this observation is made --></encounter>
 <effective[x]><!-- 0..1 dateTime|Period|Timing|instant Clinically relevant time/time-period for observation --></effective[x]>
 <issued value="[instant]"/><!-- 0..1 Date/Time this version was made available -->
 <performer><!-- 0..* Reference(Practitioner|PractitionerRole|Organization|
   CareTeam|Patient|RelatedPerson) Who is responsible for the observation --></performer>
 <value[x]><!-- ![??](lock.png) 0..1 Quantity|CodeableConcept|string|boolean|integer|Range|Ratio|
   SampledData|time|dateTime|Period Actual result --></value[x]>
 <dataAbsentReason><!-- ![??](lock.png) 0..1 CodeableConcept Why the result is missing --></dataAbsentReason>
 <interpretation><!-- 0..* CodeableConcept High, low, normal, etc. --></interpretation>
 <note><!-- 0..* Annotation Comments about the observation --></note>
 <bodySite><!-- 0..1 CodeableConcept Observed body part --></bodySite>
 <method><!-- 0..1 CodeableConcept How it was done --></method>
 <specimen><!-- 0..1 Reference(Specimen) Specimen used for this observation --></specimen>
 <device><!-- 0..1 Reference(Device|DeviceMetric) (Measurement) Device --></device>
 <referenceRange>  <!-- 0..* Provides guide for interpretation -->
  <low><!-- ![??](lock.png) 0..1 Quantity(SimpleQuantity) Low Range, if relevant --></low>
  <high><!-- ![??](lock.png) 0..1 Quantity(SimpleQuantity) High Range, if relevant --></high>
  <type><!-- 0..1 CodeableConcept Reference range qualifier --></type>
  <appliesTo><!-- 0..* CodeableConcept Reference range population --></appliesTo>
  <age><!-- 0..1 Range Applicable age range, if relevant --></age>
  <text value="[string]"/><!-- 0..1 Text based reference range in an observation -->
 </referenceRange>
 <hasMember><!-- 0..* Reference(Observation|QuestionnaireResponse|
   MolecularSequence) Related resource that belongs to the Observation group --></hasMember>
 <derivedFrom><!-- 0..* Reference(DocumentReference|ImagingStudy|Media|
   QuestionnaireResponse|Observation|MolecularSequence) Related measurements the observation is made from --></derivedFrom>
 <component>  <!-- 0..* Component results -->
  <code><!-- 1..1 CodeableConcept Type of component observation (code / type) --></code>
  <value[x]><!-- 0..1 Quantity|CodeableConcept|string|boolean|integer|Range|
    Ratio|SampledData|time|dateTime|Period Actual component result --></value[x]>
  <dataAbsentReason><!-- ![??](lock.png) 0..1 CodeableConcept Why the component result is missing --></dataAbsentReason>
  <interpretation><!-- 0..* CodeableConcept High, low, normal, etc. --></interpretation>
  <referenceRange><!-- 0..* Content as for Observation.referenceRange Provides guide for interpretation of component result --></referenceRange>
 </component>
</Observation>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Observation",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Business Identifier for observation
  "basedOn" : [{ Reference(CarePlan|DeviceRequest|ImmunizationRecommendation|
   MedicationRequest|NutritionOrder|ServiceRequest) }], // Fulfills plan, proposal or order
  "partOf" : [{ Reference(MedicationAdministration|MedicationDispense|
   MedicationStatement|Procedure|Immunization|ImagingStudy) }], // Part of referenced event
  "status" : "<code>", // R!  registered | preliminary | final | amended +
  "category" : [{ CodeableConcept }], // Classification of  type of observation
  "code" : { CodeableConcept }, // R!  Type of observation (code / type)
  "subject" : { Reference(Patient|Group|Device|Location) }, // Who and/or what the observation is about
  "focus" : [{ Reference(Any) }], // What the observation is about, when it is not about the subject of record
  "encounter" : { Reference(Encounter) }, // Healthcare event during which this observation is made
  // effective[x]: Clinically relevant time/time-period for observation. One of these 4:
  "effectiveDateTime" : "<dateTime>",
  "effectivePeriod" : { Period },
  "effectiveTiming" : { Timing },
  "effectiveInstant" : "<instant>",
  "issued" : "<instant>", // Date/Time this version was made available
  "performer" : [{ Reference(Practitioner|PractitionerRole|Organization|
   CareTeam|Patient|RelatedPerson) }], // Who is responsible for the observation
  // value[x]: Actual result. One of these 11:
  "valueQuantity" : { Quantity },
  "valueCodeableConcept" : { CodeableConcept },
  "valueString" : "<string>",
  "valueBoolean" : <boolean>,
  "valueInteger" : <integer>,
  "valueRange" : { Range },
  "valueRatio" : { Ratio },
  "valueSampledData" : { SampledData },
  "valueTime" : "<time>",
  "valueDateTime" : "<dateTime>",
  "valuePeriod" : { Period },
  "dataAbsentReason" : { CodeableConcept }, // C? Why the result is missing
  "interpretation" : [{ CodeableConcept }], // High, low, normal, etc.
  "note" : [{ Annotation }], // Comments about the observation
  "bodySite" : { CodeableConcept }, // Observed body part
  "method" : { CodeableConcept }, // How it was done
  "specimen" : { Reference(Specimen) }, // Specimen used for this observation
  "device" : { Reference(Device|DeviceMetric) }, // (Measurement) Device
  "referenceRange" : [{ // Provides guide for interpretation
    "low" : { Quantity(SimpleQuantity) }, // C? Low Range, if relevant
    "high" : { Quantity(SimpleQuantity) }, // C? High Range, if relevant
    "type" : { CodeableConcept }, // Reference range qualifier
    "appliesTo" : [{ CodeableConcept }], // Reference range population
    "age" : { Range }, // Applicable age range, if relevant
    "text" : "<string>" // Text based reference range in an observation
  }],
  "hasMember" : [{ Reference(Observation|QuestionnaireResponse|
   MolecularSequence) }], // Related resource that belongs to the Observation group
  "derivedFrom" : [{ Reference(DocumentReference|ImagingStudy|Media|
   QuestionnaireResponse|Observation|MolecularSequence) }], // Related measurements the observation is made from
  "component" : [{ // Component results
    "code" : { CodeableConcept }, // R!  Type of component observation (code / type)
    // value[x]: Actual component result. One of these 11:
    "valueQuantity" : { Quantity },
    "valueCodeableConcept" : { CodeableConcept },
    "valueString" : "<string>",
    "valueBoolean" : <boolean>,
    "valueInteger" : <integer>,
    "valueRange" : { Range },
    "valueRatio" : { Ratio },
    "valueSampledData" : { SampledData },
    "valueTime" : "<time>",
    "valueDateTime" : "<dateTime>",
    "valuePeriod" : { Period },
    "dataAbsentReason" : { CodeableConcept }, // C? Why the component result is missing
    "interpretation" : [{ CodeableConcept }], // High, low, normal, etc.
    "referenceRange" : [{ Content as for Observation.referenceRange }] // Provides guide for interpretation of component result
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Observation;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Observation.identifier [ Identifier ], ... ; # 0..* Business Identifier for observation
  fhir:Observation.basedOn [ Reference(CarePlan|DeviceRequest|ImmunizationRecommendation|MedicationRequest|
  NutritionOrder|ServiceRequest) ], ... ; # 0..* Fulfills plan, proposal or order
  fhir:Observation.partOf [ Reference(MedicationAdministration|MedicationDispense|MedicationStatement|Procedure|
  Immunization|ImagingStudy) ], ... ; # 0..* Part of referenced event
  fhir:Observation.status [ code ]; # 1..1 registered | preliminary | final | amended +
  fhir:Observation.category [ CodeableConcept ], ... ; # 0..* Classification of  type of observation
  fhir:Observation.code [ CodeableConcept ]; # 1..1 Type of observation (code / type)
  fhir:Observation.subject [ Reference(Patient|Group|Device|Location) ]; # 0..1 Who and/or what the observation is about
  fhir:Observation.focus [ Reference(Any) ], ... ; # 0..* What the observation is about, when it is not about the subject of record
  fhir:Observation.encounter [ Reference(Encounter) ]; # 0..1 Healthcare event during which this observation is made
  # Observation.effective[x] : 0..1 Clinically relevant time/time-period for observation. One of these 4
    fhir:Observation.effectiveDateTime [ dateTime ]
    fhir:Observation.effectivePeriod [ Period ]
    fhir:Observation.effectiveTiming [ Timing ]
    fhir:Observation.effectiveInstant [ instant ]
  fhir:Observation.issued [ instant ]; # 0..1 Date/Time this version was made available
  fhir:Observation.performer [ Reference(Practitioner|PractitionerRole|Organization|CareTeam|Patient|RelatedPerson) ], ... ; # 0..* Who is responsible for the observation
  # Observation.value[x] : 0..1 Actual result. One of these 11
    fhir:Observation.valueQuantity [ Quantity ]
    fhir:Observation.valueCodeableConcept [ CodeableConcept ]
    fhir:Observation.valueString [ string ]
    fhir:Observation.valueBoolean [ boolean ]
    fhir:Observation.valueInteger [ integer ]
    fhir:Observation.valueRange [ Range ]
    fhir:Observation.valueRatio [ Ratio ]
    fhir:Observation.valueSampledData [ SampledData ]
    fhir:Observation.valueTime [ time ]
    fhir:Observation.valueDateTime [ dateTime ]
    fhir:Observation.valuePeriod [ Period ]
  fhir:Observation.dataAbsentReason [ CodeableConcept ]; # 0..1 Why the result is missing
  fhir:Observation.interpretation [ CodeableConcept ], ... ; # 0..* High, low, normal, etc.
  fhir:Observation.note [ Annotation ], ... ; # 0..* Comments about the observation
  fhir:Observation.bodySite [ CodeableConcept ]; # 0..1 Observed body part
  fhir:Observation.method [ CodeableConcept ]; # 0..1 How it was done
  fhir:Observation.specimen [ Reference(Specimen) ]; # 0..1 Specimen used for this observation
  fhir:Observation.device [ Reference(Device|DeviceMetric) ]; # 0..1 (Measurement) Device
  fhir:Observation.referenceRange [ # 0..* Provides guide for interpretation
    fhir:Observation.referenceRange.low [ Quantity(SimpleQuantity) ]; # 0..1 Low Range, if relevant
    fhir:Observation.referenceRange.high [ Quantity(SimpleQuantity) ]; # 0..1 High Range, if relevant
    fhir:Observation.referenceRange.type [ CodeableConcept ]; # 0..1 Reference range qualifier
    fhir:Observation.referenceRange.appliesTo [ CodeableConcept ], ... ; # 0..* Reference range population
    fhir:Observation.referenceRange.age [ Range ]; # 0..1 Applicable age range, if relevant
    fhir:Observation.referenceRange.text [ string ]; # 0..1 Text based reference range in an observation
  ], ...;
  fhir:Observation.hasMember [ Reference(Observation|QuestionnaireResponse|MolecularSequence) ], ... ; # 0..* Related resource that belongs to the Observation group
  fhir:Observation.derivedFrom [ Reference(DocumentReference|ImagingStudy|Media|QuestionnaireResponse|Observation|
  MolecularSequence) ], ... ; # 0..* Related measurements the observation is made from
  fhir:Observation.component [ # 0..* Component results
    fhir:Observation.component.code [ CodeableConcept ]; # 1..1 Type of component observation (code / type)
    # Observation.component.value[x] : 0..1 Actual component result. One of these 11
      fhir:Observation.component.valueQuantity [ Quantity ]
      fhir:Observation.component.valueCodeableConcept [ CodeableConcept ]
      fhir:Observation.component.valueString [ string ]
      fhir:Observation.component.valueBoolean [ boolean ]
      fhir:Observation.component.valueInteger [ integer ]
      fhir:Observation.component.valueRange [ Range ]
      fhir:Observation.component.valueRatio [ Ratio ]
      fhir:Observation.component.valueSampledData [ SampledData ]
      fhir:Observation.component.valueTime [ time ]
      fhir:Observation.component.valueDateTime [ dateTime ]
      fhir:Observation.component.valuePeriod [ Period ]
    fhir:Observation.component.dataAbsentReason [ CodeableConcept ]; # 0..1 Why the component result is missing
    fhir:Observation.component.interpretation [ CodeableConcept ], ... ; # 0..* High, low, normal, etc.
    fhir:Observation.component.referenceRange [ See Observation.referenceRange ], ... ; # 0..* Provides guide for interpretation of component result
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Observation](observation.html#Observation) |  |
| Observation.basedOn | - Type Reference: Added Target Type ServiceRequest - Type Reference: Removed Target Types ProcedureRequest, ReferralRequest |
| Observation.partOf | - Added Element |
| Observation.status | - Change value set from http://hl7.org/fhir/ValueSet/observation-status to http://hl7.org/fhir/ValueSet/observation-status|4.0.1 |
| Observation.focus | - Added Element |
| Observation.encounter | - Renamed from context to encounter - Type Reference: Removed Target Type EpisodeOfCare |
| Observation.effective[x] | - Add Types Timing, instant |
| Observation.performer | - Type Reference: Added Target Types PractitionerRole, CareTeam |
| Observation.value[x] | - Add Type integer - Remove Type Attachment |
| Observation.dataAbsentReason | - Change value set from http://hl7.org/fhir/ValueSet/observation-valueabsentreason to http://hl7.org/fhir/ValueSet/data-absent-reason - Change code system for extensibly bound codes from "http://hl7.org/fhir/data-absent-reason" to "http://terminology.hl7.org/CodeSystem/data-absent-reason" |
| Observation.interpretation | - Max Cardinality changed from 1 to \* - Change code system for extensibly bound codes from "http://terminology.hl7.org/CodeSystem/v2-0078" to "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation" |
| Observation.note | - Renamed from comment to note - Max Cardinality changed from 1 to \* - Type changed from string to Annotation |
| Observation.referenceRange.type | - Remove Binding `http://hl7.org/fhir/ValueSet/referencerange-meaning` (extensible) |
| Observation.hasMember | - Added Element |
| Observation.derivedFrom | - Added Element |
| Observation.component.value[x] | - Add Types boolean, integer - Remove Type Attachment |
| Observation.component.dataAbsentReason | - Change value set from http://hl7.org/fhir/ValueSet/observation-valueabsentreason to http://hl7.org/fhir/ValueSet/data-absent-reason - Change code system for extensibly bound codes from "http://hl7.org/fhir/data-absent-reason" to "http://terminology.hl7.org/CodeSystem/data-absent-reason" |
| Observation.component.interpretation | - Max Cardinality changed from 1 to \* - Change code system for extensibly bound codes from "http://terminology.hl7.org/CodeSystem/v2-0078" to "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation" |
| Observation.related | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](observation.diff.xml) or [JSON](observation.diff.json).

See [R3 <--> R4 Conversion Maps](observation-version-maps.html) (status = 48 tests that all execute ok. All tests pass round-trip testing and 23 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](observation-profiles.html) and the alternate definitions:
Master Definition [XML](observation.profile.xml.html) + [JSON](observation.profile.json.html),
[XML](xml.html) [Schema](observation.xsd)/[Schematron](observation.sch) + [JSON](json.html)
[Schema](observation.schema.json.html), [ShEx](observation.shex.html) (for [Turtle](rdf.html)) + [see the extensions](observation-profiles.html) & the [dependency analysis](observation-dependencies.html)

### 10.1.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Observation.status | Codes providing the status of an observation. | [Required](terminologies.html#required) | [ObservationStatus](valueset-observation-status.html) |
| Observation.category | Codes for high level observation categories. | [Preferred](terminologies.html#preferred) | [ObservationCategoryCodes](valueset-observation-category.html) |
| Observation.code Observation.component.code | Codes identifying names of simple observations. | [Example](terminologies.html#example) | [LOINCCodes](valueset-observation-codes.html) |
| Observation.dataAbsentReason Observation.component.dataAbsentReason | Codes specifying why the result (`Observation.value[x]`) is missing. | [Extensible](terminologies.html#extensible) | [DataAbsentReason](valueset-data-absent-reason.html) |
| Observation.interpretation Observation.component.interpretation | Codes identifying interpretations of observations. | [Extensible](terminologies.html#extensible) | [ObservationInterpretationCodes](valueset-observation-interpretation.html) |
| Observation.bodySite | Codes describing anatomical locations. May include laterality. | [Example](terminologies.html#example) | [SNOMEDCTBodyStructures](valueset-body-site.html) |
| Observation.method | Methods for simple observations. | [Example](terminologies.html#example) | [ObservationMethods](valueset-observation-methods.html) |
| Observation.referenceRange.type | Code for the meaning of a reference range. | [Preferred](terminologies.html#preferred) | [ObservationReferenceRangeMeaningCodes](valueset-referencerange-meaning.html) |
| Observation.referenceRange.appliesTo | Codes identifying the population the reference range applies to. | [Example](terminologies.html#example) | [ObservationReferenceRangeAppliesToCodes](valueset-referencerange-appliesto.html) |

### 10.1.3.2 Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **obs-3** | [Rule](conformance-rules.html#rule) | Observation.referenceRange | Must have at least a low or a high or text | low.exists() or high.exists() or text.exists() |
| **obs-6** | [Rule](conformance-rules.html#rule) | (base) | dataAbsentReason SHALL only be present if Observation.value[x] is not present | dataAbsentReason.empty() or value.empty() |
| **obs-7** | [Rule](conformance-rules.html#rule) | (base) | If Observation.code is the same as an Observation.component.code then the value element associated with the code SHALL NOT be present | value.empty() or component.code.where(coding.intersect(%resource.code.coding).exists()).empty() |

## 10.1.4 Notes:

### 10.1.4.1 Profiling Observation

At its simplest, a resource instance can consist of only a code and a value, and status flag. The relevance of other properties will vary based on the type of observation.
[Profiles](observation-profiles.html) are created to provide guidance on capturing certain types of observations for a given use case. The Observation resource focuses on the level of detail captured by most systems. However, for a given use case there may be additional constraints and additional information relevant in certain circumstances. As with other resources, [extensions](extensibility.html) can be used to introduce this additional complexity.

### 10.1.4.2 Subject of an Observation

Typically, an observation is made about the subject - a patient, or group of patients, location, or device - and the distinction between the subject and what is directly measured for an observation is specified in the observation code itself ( e.g., "Blood Glucose") and does not need to be represented separately. However, three attributes may be used for representing the focus of the observation if it is not the subject itself. The `specimen` and `bodySite` elements are used to represent measurements taken on subject samples or anatomic and morphological locations, and `focus` represents specific aspect of the subject that are the point of attention such as another observation or a device implanted in a patient.

### 10.1.4.3 Observation Grouping

Many observations have important relationships to other observations and need to be grouped together. These structures have been defined to do this: DiagnosticReport and `DiagnosticReport.result`, Observation and the elements: `Observation.component`, `Observation.hasMember` and `Observation.derivedFrom`. The sections below provides guidance around which structure to use. Because the idea of what to group together is often highly contextual and based upon the end user's point of view, the choice of which structure to use will be driven by jurisdiction, organizational practice and context. Profiling will normally be necessary for implementation.

#### 10.1.4.3.1 DiagnosticReport.result

DiagnosticReport relates directly to an order (ServiceRequest). The `DiagnosticReport.code` names the panel and serves as the grouping element, which is traditionally referred to as a "panel" or "battery" by laboratories. The `DiagnosticReport.result` element references the individual observations. Several [examples](diagnosticreport-examples.html) demonstrate observation grouping using DiagnosticReport as the grouping structure.

#### 10.1.4.3.2 Observation.component

`Observation.component` is used for any supporting result that cannot reasonably be interpreted and used outside the scope of the Observation it is a component of. Component observations may make up the separate and individual parts of the observation or may provide qualifying information to `Observation.code` and may only be able to be understood in relation to the `Observation.code` (for example, see the [`$stats` operation](observation-operation-stats.html)). Therefore **all** code-value and component.code-component.value pairs need to be taken into account to correctly understand the meaning of the observation. Components should only be used when there is only one method, one observation, one performer, one device, and one time. Some use cases for using this structure include:

1. Observations that are commonly produced and interpreted together. For example, systolic and diastolic blood pressure are represented as a single [Blood pressure panel](observation-example-bloodpressure.html).
2. Assessment tool results that are commonly produced and interpreted together. For example, a newborn [Apgar score](observation-example-5minute-apgar-score.html) that is a single Observation with five components.
3. Representing multiple answers to a question ([relationship and boundaries](questionnaireresponse.html#bnr) between Observation and Questionnaire/QuestionnaireResponse). For example, reporting the [types of alcohol](observation-example-alcohol-type.html) consumed by a patient

On the other hand, any observations that are clinically relevant outside the context of being a component of another observation should be represented by separate Observation resources. For example a [Body Mass Index (BMI)](observation-example-bmi-using-related.html) Observation should *not* contain components for height and weight because they are clinically relevant observations on their own and should be represented by separate Observation resources. See the section below on how to relate independent Observations.

#### 10.1.4.3.3 Observation.hasMember of and Observation.derivedFrom

`Observation.hasMember` and `Observation.derivedFrom` and the core extensions: [Observation-sequelTo ![](external.png)](http://hl7.org/fhir/StructureDefinition/observation-sequelTo) and [Observation-replaces ![](external.png)](http://hl7.org/fhir/StructureDefinition/observation-replaces) are used for any supporting result that can be interpreted and used on its own and has one or more different values for method, observation, performer, device, time, and/or error conditions. Two common use cases for using this structure are:

1. For grouping related observations such as for a "panel" or "battery". In this case the `Observation.code` represents the "panel" code, typically `Observation.value[x]` is not present, and the set of member Observations are listed in `Observation.hasMember`. This structure permits *nested grouping* when used with DiagnosticReport (e.g. [complex micro isolate and sensitivities report](diagnosticreport-micro1.html)).
2. When linking to other Observations from which an Observation is derived. In this case both `Observation.code` and `Observation.value[x]` are present, and the linked observations are listed in `Observation.derivedFrom`. An example of this would be a [Body Mass Index (BMI)](observation-example-bmi-using-related.html) Observation where the height and weight measurements are referenced.

### 10.1.4.4 Using codes in Observation

When a result value is a represented as a predefined concept using a code, `valueCodeableConcept` is used. This element is [bound](terminologies.html) to a value set comprised of a standard nomenclature such as SNOMED CT or a source system ("local") coded result values.

#### 10.1.4.4.1 Multiple Codings

Results may be coded in multiple value sets based on different code systems and these may be mapped using the [ConceptMap](conceptmap.html) resource and/or given as [additional codings](datatypes.html#CodeableConcept) directly in the element as shown in the example below.

For example the LOINC 43304-5 *Chlamydia trachomatis rRNA [Presence] in Unspecified specimen by Probe and target amplification method* is typically associated with coded presence/absence concepts. Using the coded value for 'negative' with a standard code translation, `valueCodeableConcept` would be:

```


	"valueCodeableConcept": {
		"coding": [
			{
				"system": "http://snomed.info/sct",
				"code": "260385009",
				"display": "Negative"
			}, {
				"system": "https://acme.lab/resultcodes",
				"code": "NEG",
				"display": "Negative"
			}
		],
		"text": "Negative for Chlamydia Trachomatis rRNA"
	}

	
```

#### 10.1.4.4.2 Text values for coded results:

When the data element is usually coded or the type associated with the `code` element defines a coded value, use `valueCodeableConcept`
*even if* there is no appropriate code and only free text is available. For example using text only, the `valueCodeableConcept` element would be:

```


	"valueCodeableConcept": {
		"text": "uncoded free text result"
	}

			
```

When a coded answer list includes a concept code for "other" and there is a free text description of the concept, the `valueCodeableConcept.text` element should be used to capture the full meaning of the source. In the example below, the answer code "Other" is provided in the `valueCodeableConcept` element and the text value supplied value in the `CodeableConcept.text` element.

```

{
	"resourceType": "Observation",
	... snip ...
	"code": {
		"coding": [
			{
				"system": "http://loinc.org",
				"code": "74076-1",
				"display": "Medication or substance involved"
			}
		]
	},
	.. snip ...
	"valueCodeableConcept": {
		"coding": [
			{
				"system": "http://loinc.org",
				"code": " LA20343-2",
				"display": "Other substance: PLEASE SPECIFY"
			}
		],
		"text": "Other: Blue pills I found under my couch"
	}
	.. snip ...
}
	
```

#### 10.1.4.4.3 Interoperability Issues using code value pairs in FHIR

A recurring issue for many observation events, regardless of the particular pattern, is determining how to populate observation.code and observation.value. While this is typically straight-forward for laboratory observations, it can get blurry for other types of observations, such as findings and disorders, family history observations, etc. This discussion focuses on the way in which the coded representation of such statements is expressed using the `Observation.code` and `Observation.value` elements.

There are two distinct facets that are central to a FHIR Observations:

- The action taken to make the finding and/or the property about which the property was observed. For example: measurement of blood hemoglobin.
- The result of the observation. For example: 14 g/dl.

Several different ways of representing the same information exist using different combinations of the `Observation.code` and `Observation.value`. Unconstrained use of the alternatives presents a major challenge for computation of semantic equivalence and for safe interpretation of observations originating from different applications and users. The following four patterns could reasonably represent the same case. Considering that the Observation resource needs to support many use cases, the appropriate place to define the specific pattern is expected to be done through profiles and implementation guides as specified by the jurisdictions and/or organizations implementing FHIR:

1. `Observation.code` represents the nature of the observation and the `Observation.value` a code represents the non-numeric result value. These are two distinct facets that are central to a FHIR Observations. For example:
   - code=[Examination]
   - value=[Abdomen tender]
2. `Observation.code` is nearly identical to 1) above, but the level of granularity is shifted from the value to code. For example:
   - code=[Abdominal examination]
   - value=[Tenderness]
3. The `Observation.code` is also expressed in a way that does not specify the observation action but indicates a statement about findings reduced to a single name (or term), as in the above item. In this example, the `Observation.value` is present and "qualifies" the finding typically confirming or refuting it. For example:
   - code=[Abdominal tenderness]
   - value=[found/true]
4. in this example the `Observation.code` is expressed in a way that does not specify the observation action but indicates a statement about findings reduced to a single name (or term). In this particular example in that context, the `Observation.value` is omitted. For example:
   - code=[Abdominal tenderness]
   - value element is omitted

#### 10.1.4.4.4 Guidance:

1. Recommended rules for case 1 and 2 patterns:
   - The Observation.code is preferably a [LOINC ![](external.png)](https://loinc.org/) concept code.
     - If a [SNOMED CT ![](external.png)](http://snomed.info/sct) concept code is used, the expression SHOULD represent a 363787002 (Observable entity(Observable entity)) or 386053000 (Evaluation procedure(evaluation procedure))
   - For non-numeric values, the Observation.value is preferably a SNOMED CT concept code.
2. Recommended rules for case 3 pattern:
   - The Observation.code is preferably a LOINC or SNOMED CT concept code.
     - If a SNOMED CT concept code is used, the expression SHOULD represent a 404684003 (Clinical finding (finding)) , 413350009 (Finding with explicit context(finding)), or 272379006 (Event(event)).
   - The Observation.value is represented by either
     - valueBoolean
     - valueCodeableConcept preferably using:
       - SNOMED CT where concept is-a 362981000 (Qualifier value (qualifier value))
       - [v2 Yes/no Indicator](v2/0136/index.html)
       - [v2 Expanded Yes/no Indicator](v2/0136/index.html) (unfortunately is missing 'not given')
3. Recommended rules for case 4 pattern:
   - The Observation.code is preferably a SNOMED CT concept code where the concept is-a 404684003 (Clinical finding (finding)) , 413350009 (Finding with explicit context(finding)), or 272379006 (Event(event)).
   - The Observation.value is omitted. The default interpretation is the concept (single code or expression) represented in Observation.code is present in the patient. An Observation.dataAbsentReason value of 'clinical-finding' SHOULD be used to indicate why the expected value is missing.
4. SHOULD NOT use the *Assertion* pattern as described in [HL7 Version 3 Implementation Guide: TermInfo - Using SNOMED CT in CDA R2 Models, Release 1 ![](external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=418). ( The code is 'ASSERTION' and the value is a SNOMED CT concept or expression )

### 10.1.4.5 Refining the interpretation of an Observation using additional codes or Observations

The following list provides guidance on using codes or other observations to provide additional context that may alter how an observation is interpreted.:

1. If possible, use the most specific code you can

   e.g.:

   ```
   
   {
   "resourceType": "Observation",
   ... snip ...
   "code": {
   	"coding": [
   		{
   			"system": "http://loinc.org",
   			"code": "6689-4",
   			"display": "Glucose [Mass/​volume] in Blood --2 hours post meal"
   		}
   	]
   },
   ... snip ...
   }
   		
   ```
2. Alternatively, use additional codes in Observation.code as described [above](#mult-codes).

   e.g.: Observation.code = coding-1: 59408-5 Oxygen saturation in Arterial blood by Pulse oximetry, coding-2: 20564-1 Oxygen saturation in Blood

   ```
   
   {
   "resourceType": "Observation",
   ... snip ...
   "code": {
   	"coding": [
   		{
   			"system": "http://loinc.org",
   			"code": "59408-5",
   			"display": "Oxygen saturation in Arterial blood by Pulse oximetry"
   		},
   		{
   			"system": "http://loinc.org",
   			"code": "20564-1",
   			"display": "Oxygen saturation in Blood"
   		}
   	]
   },
   ... snip ...
   }
   		
   ```
3. As described [above](#obsgrouping), observations are typically grouped together
   to provide additional information needed for correctly understanding and interpreting the observation.
   As an alternative to grouping observations, extensions may be used to provide references to other
   observations needed for understanding and interpreting an observation.

> **Note:**We are seeking input from the implementer community in evaluating existing [Observation Extensions](observation-profiles.html#extensions) for this purpose
>
> Feedback [here ![](external.png)](https://chat.fhir.org/#narrow/stream/103-Orders-and.20Observation.20WG).

### 10.1.4.6 Value[x] and Datatypes

- The element, Observation.value[x], has a variable name depending on the type as follows:
  - valueQuantity
  - valueCodeableConcept
  - valueString
  - valueBoolean
  - valueInteger
  - valueRange
  - valueRatio
  - valueSampledData
  - valueTime
  - valueDateTime
  - valuePeriod
- See above section on [Using codes for result values](#usingcodes)
- The Boolean data type is rarely used for `value[x]` because most observations result values are never truly Boolean due to exceptional values such as "unknown", therefore they should use the CodeableConcept data type instead and select codes from [http://terminology.hl7.org/ValueSet/v2-0136 ![](external.png)](http://terminology.hl7.org/ValueSet/v2-0136) (these "yes/no" concepts can be mapped to the display name "true/false" or other mutually exclusive terms that may be needed")
- The special values "E" (error), "L" (below detection limit) and "U" (above detection limit) can be used are in the SampledData data type. However, when using valueQuantity in an observation for above and below detection limit values, valueQuantity should be used by stating the limit along with the comparator. In addition, when there is an error the dataAbsentReason element should be used with the appropriate value ('error' or 'NaN'). For example if the value was below the lower limit of detection of <2.0 mmol/L the `valueQuantity` would be:

  ```
  
  	"valueQuantity": {
  		"value": 2.0,
  		"comparator": "<",
  		"unit": "mmol/l",
  		"system": "http://unitsofmeasure.org",
  		"code": "mmol/L"
  	}
  ```

  If the value was "NaN" (i.e. an error) the `valueCodeableConcept` element would be absent and `dataAbsentReason` element would be:

  ```
  
  	"dataAbsentReason": {
  		"coding": [
  			{
  				"system": "http://terminology.hl7.org/CodeSystem/data-absent-reason",
  				"code": "NaN",
  				"display": "Not a Number"
  			}
  		]
  	}
  	
  ```
- Because there are multiple types allowed for the *value* element, multiple value search parameters are defined. There is no standard parameter for searching values of type Ratio

### 10.1.4.7 Physiologically Relevant Time of the Observation

The effectiveDateTime or effectivePeriod is the time that the observation is most relevant as an observation of the subject. For a biological subject (e.g. a human patient), this is the physiologically relevant time of the observation. In the case of an observation using a specimen, this represents the start and end of the specimen collection (e.g. 24-hour Urine Sodium), but if the collection time is sufficiently short, this is reported as a point in time value (e.g. normal venipuncture). In the case of an observation obtained directly from a subject (e.g. BP, Chest X-ray), this is the start and end time of the observation process, which again, is often reported as a single point in time.

### 10.1.4.8 Reference Range

Most common observations will only have one generic reference range. Reference ranges may be useful for laboratory tests and other measures like systolic blood pressure but will have little relevance for something like "pregnancy status". Systems MAY choose to restrict to only supplying the relevant reference range based on knowledge about the patient (e.g. specific to the patient's age, gender, weight and other factors), but this might not be possible or appropriate. Whenever more than one reference range is supplied, the differences between them SHOULD be provided in the reference range and/or age properties.

### 10.1.4.9 Canceled or Aborted Observations

If a measurement or test could not be completed (for example if the specimen is unsatisfactory or the provider cancelled the order), then the status value should be updated to "cancelled" and the specific details given - preferably as coded values in the dataAbsentReason or valueCodeableConcept element. Additional information may be provided in the `note` element as well. The [specimen reject example](observation-example-unsat.html) demonstrates this using a coded value for unsatisfactory specimen in dataAbsentReason.

### 10.1.4.10 Genetic Observations

Genetic reporting makes heavy use of the DiagnosticReport and Observation resources. An implementation guide describing how to represent genetic results can be found [here ![](external.png)](http://hl7.org/fhir/uv/genomics-reporting/index.html).

## 10.1.5 Operations defined for Observation

### 10.1.5.1 Searching for the Last N Observations

The *lastn* query operation meets the common need for searching for the most recent or "last known" Observations for a subject. Examples where this query could be used:

- Fetch the last 5 temperatures for a patient to view trends
- Get the most recent laboratory results for patient
- Fetch the last 3 results for all vitals for a patient

See the [Last N Observations Query](observation-operation-lastn.html) section in the Observation resource operations page for more information and examples

### 10.1.5.2 Retrieving Statistics for Laboratory Observations

The *stats* operation performs a set of statistical calculations on a set of clinical measurements such as a blood pressure as stored on the server. This operation is focused on Observation resources with valueQuantity elements that have UCUM unit codes. Examples where this operation could be used:

- Get the average, min, max and count of a series of BP measurements for a patient
- Determine 20th or 80th percentile on a set of measurements over a time period

See the [Observation Statistics](observation-operation-stats.html) section in the Observation resource operations page for more information and examples

## 10.1.6 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| based-on [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Reference to the service request. | Observation.basedOn ([CarePlan](careplan.html), [MedicationRequest](medicationrequest.html), [NutritionOrder](nutritionorder.html), [DeviceRequest](devicerequest.html), [ServiceRequest](servicerequest.html), [ImmunizationRecommendation](immunizationrecommendation.html)) |  |
| category [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The classification of the type of observation | Observation.category |  |
| code [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The code of the observation type | Observation.code | [13 Resources](searchparameter-registry.html#clinical-code) |
| code-value-concept [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Code and coded value parameter pair | On Observation:   code: code   value-concept: value.as(CodeableConcept) |  |
| code-value-date [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Code and date/time value parameter pair | On Observation:   code: code   value-date: value.as(DateTime) | value.as(Period) |  |
| code-value-quantity [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Code and quantity value parameter pair | On Observation:   code: code   value-quantity: value.as(Quantity) |  |
| code-value-string [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Code and string value parameter pair | On Observation:   code: code   value-string: value.as(string) |  |
| combo-code [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The code of the observation type or component type | Observation.code | Observation.component.code |  |
| combo-code-value-concept [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Code and coded value parameter pair, including in components | On Observation | Observation.component:   combo-code: code   combo-value-concept: value.as(CodeableConcept) |  |
| combo-code-value-quantity [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Code and quantity value parameter pair, including in components | On Observation | Observation.component:   combo-code: code   combo-value-quantity: value.as(Quantity) |  |
| combo-data-absent-reason [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The reason why the expected value in the element Observation.value[x] or Observation.component.value[x] is missing. | Observation.dataAbsentReason | Observation.component.dataAbsentReason |  |
| combo-value-concept [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The value or component value of the observation, if the value is a CodeableConcept | (Observation.value as CodeableConcept) | (Observation.component.value as CodeableConcept) |  |
| combo-value-quantity [TU](versions.html#std-process "Trial Use Content") | [quantity](search.html#quantity) | The value or component value of the observation, if the value is a Quantity, or a SampledData (just search on the bounds of the values in sampled data) | (Observation.value as Quantity) | (Observation.value as SampledData) | (Observation.component.value as Quantity) | (Observation.component.value as SampledData) |  |
| component-code [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The component code of the observation type | Observation.component.code |  |
| component-code-value-concept [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Component code and component coded value parameter pair | On Observation.component:   component-code: code   component-value-concept: value.as(CodeableConcept) |  |
| component-code-value-quantity [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | Component code and component quantity value parameter pair | On Observation.component:   component-code: code   component-value-quantity: value.as(Quantity) |  |
| component-data-absent-reason [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The reason why the expected value in the element Observation.component.value[x] is missing. | Observation.component.dataAbsentReason |  |
| component-value-concept [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The value of the component observation, if the value is a CodeableConcept | (Observation.component.value as CodeableConcept) |  |
| component-value-quantity [TU](versions.html#std-process "Trial Use Content") | [quantity](search.html#quantity) | The value of the component observation, if the value is a Quantity, or a SampledData (just search on the bounds of the values in sampled data) | (Observation.component.value as Quantity) | (Observation.component.value as SampledData) |  |
| data-absent-reason [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The reason why the expected value in the element Observation.value[x] is missing. | Observation.dataAbsentReason |  |
| date [TU](versions.html#std-process "Trial Use Content") | [date](search.html#date) | Obtained date/time. If the obtained element is a period, a date that falls in the period | Observation.effective | [17 Resources](searchparameter-registry.html#clinical-date) |
| derived-from [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Related measurements the observation is made from | Observation.derivedFrom ([Media](media.html), [Observation](observation.html), [ImagingStudy](imagingstudy.html), [MolecularSequence](molecularsequence.html), [QuestionnaireResponse](questionnaireresponse.html), [DocumentReference](documentreference.html)) |  |
| device [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | The Device that generated the observation data. | Observation.device ([Device](device.html), [DeviceMetric](devicemetric.html)) |  |
| encounter [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Encounter related to the observation | Observation.encounter ([Encounter](encounter.html)) | [12 Resources](searchparameter-registry.html#clinical-encounter) |
| focus [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | The focus of an observation when the focus is not the patient of record. | Observation.focus (Any) |  |
| has-member [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Related resource that belongs to the Observation group | Observation.hasMember ([Observation](observation.html), [MolecularSequence](molecularsequence.html), [QuestionnaireResponse](questionnaireresponse.html)) |  |
| identifier [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The unique id for a particular observation | Observation.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) |
| method [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The method used for the observation | Observation.method |  |
| part-of [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Part of referenced event | Observation.partOf ([Immunization](immunization.html), [MedicationDispense](medicationdispense.html), [MedicationAdministration](medicationadministration.html), [Procedure](procedure.html), [ImagingStudy](imagingstudy.html), [MedicationStatement](medicationstatement.html)) |  |
| patient [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | The subject that the observation is about (if patient) | Observation.subject.where(resolve() is Patient) ([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) |
| performer [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Who performed the observation | Observation.performer ([Practitioner](practitioner.html), [Organization](organization.html), [CareTeam](careteam.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |  |
| specimen [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Specimen used for this observation | Observation.specimen ([Specimen](specimen.html)) |  |
| status [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The status of the observation | Observation.status |  |
| subject [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | The subject that the observation is about | Observation.subject ([Group](group.html), [Device](device.html), [Patient](patient.html), [Location](location.html)) |  |
| value-concept [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The value of the observation, if the value is a CodeableConcept | (Observation.value as CodeableConcept) |  |
| value-date [TU](versions.html#std-process "Trial Use Content") | [date](search.html#date) | The value of the observation, if the value is a date or period of time | (Observation.value as dateTime) | (Observation.value as Period) |  |
| value-quantity [TU](versions.html#std-process "Trial Use Content") | [quantity](search.html#quantity) | The value of the observation, if the value is a Quantity, or a SampledData (just search on the bounds of the values in sampled data) | (Observation.value as Quantity) | (Observation.value as SampledData) |  |
| value-string [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The value of the observation, if the value is a string, and also searches in CodeableConcept.text | (Observation.value as string) | (Observation.value as CodeableConcept).text |  |
