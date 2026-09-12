---
id: device
title: Device
source_url: https://hl7.org/fhir/R4/device.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:57Z'
sha256: 461aaf538b42802cbfa66bfa92f1d8c544269cacd2a689d1c24208fd7ea910fc
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/device.html) [R4B](http://hl7.org/fhir/R4B/device.html) **R4** [R3](http://hl7.org/fhir/STU3/device.html) [R2](http://hl7.org/fhir/DSTU2/device.html)

- [Content](#)
- [Examples](device-examples.html)
- [Detailed Descriptions](device-definitions.html)
- [Mappings](device-mappings.html)
- [Profiles & Extensions](device-profiles.html)
- [R3 Conversions](device-version-maps.html)

# 8.14 Resource Device - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Orders and Observations](http://www.hl7.org/Special/committees/orders/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Business | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.

## 8.14.1 Scope and Usage

This resource is an administrative resource that tracks individual instances of a device and their location. It is referenced by other resources for recording which device performed an action such as a procedure or an observation, referenced when prescribing and dispensing devices for patient use or for ordering supplies, and used to record and transmit [Unique Device Identifier (UDI)](#udi) information about a device such as a patient's implant.

## 8.14.2 Boundaries and Relationships

These are the device related resources

- Device (this resource)
- [DeviceDefinition](devicedefinition.html) - Describes a "kind" of device - not a physical instance, cut a "catalog entry" where a device is defined by the manufacturer, reseller, or regulator.
- [DeviceMetric](devicemetric.html) - Describes a measurement, calculation or setting capability of a medical device.

In FHIR, the "Device" is the "administrative" resource for the device (it does not change much and has manufacturer information etc.), whereas the DeviceComponent and DeviceMetric (which is really a kind of DeviceComponent) model the physical part, including operation status and is much more volatile.
The physical composition of a Device is represented by the Devices pointing to their "parent".

Devices differ from medications because they are not "used up" - they remain active in a patient in an ongoing fashion. However, the specific boundary between medications and devices is defined at the implementation level and this standard does not enforce a boundary with the exception of devices that are implanted in a patient. The [Medication](medication.html) resource should not be used to represent implanted devices.

This resource is referenced by [Signature](datatypes.html#Signature), [Account](account.html#Account), [AdverseEvent](adverseevent.html#AdverseEvent), [Appointment](appointment.html#Appointment), [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [AuditEvent](auditevent.html#AuditEvent), [CarePlan](careplan.html#CarePlan), [CatalogEntry](catalogentry.html#CatalogEntry), [ChargeItem](chargeitem.html#ChargeItem), [ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition), [Claim](claim.html#Claim), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [DetectedIssue](detectedissue.html#DetectedIssue), itself, [DeviceMetric](devicemetric.html#DeviceMetric), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [Group](group.html#Group), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Invoice](invoice.html#Invoice), [List](list.html#List), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MessageHeader](messageheader.html#MessageHeader), [MolecularSequence](molecularsequence.html#MolecularSequence), [Observation](observation.html#Observation), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [Schedule](schedule.html#Schedule), [ServiceRequest](servicerequest.html#ServiceRequest), [Specimen](specimen.html#Specimen), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest) and [Task](task.html#Task)

## 8.14.3 Resource Content

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
| .. [Device](device-definitions.html#Device "Device : A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Item used in healthcare Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](device-definitions.html#Device.identifier "Device.identifier : Unique instance identifiers assigned to a device by manufacturers other organizations or owners.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | Instance identifier |
| ... [definition](device-definitions.html#Device.definition "Device.definition : The reference to the definition for the device.") |  | 0..1 | [Reference](references.html#Reference)([DeviceDefinition](devicedefinition.html)) | The reference to the definition for the device |
| ... [udiCarrier](device-definitions.html#Device.udiCarrier "Device.udiCarrier : Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Unique Device Identifier (UDI) Barcode string |
| .... [deviceIdentifier](device-definitions.html#Device.udiCarrier.deviceIdentifier "Device.udiCarrier.deviceIdentifier : The device identifier (DI) is a mandatory, fixed portion of a UDI that identifies the labeler and the specific version or model of a device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Mandatory fixed portion of UDI |
| .... [issuer](device-definitions.html#Device.udiCarrier.issuer "Device.udiCarrier.issuer : Organization that is charged with issuing UDIs for devices.  For example, the US FDA issuers include : 1) GS1:  http://hl7.org/fhir/NamingSystem/gs1-di,  2) HIBCC: http://hl7.org/fhir/NamingSystem/hibcc-dI,  3) ICCBBA for blood containers: http://hl7.org/fhir/NamingSystem/iccbba-blood-di,  4) ICCBA for other devices: http://hl7.org/fhir/NamingSystem/iccbba-other-di.") |  | 0..1 | [uri](datatypes.html#uri) | UDI Issuing Organization |
| .... [jurisdiction](device-definitions.html#Device.udiCarrier.jurisdiction "Device.udiCarrier.jurisdiction : The identity of the authoritative source for UDI generation within a  jurisdiction.  All UDIs are globally unique within a single namespace with the appropriate repository uri as the system.  For example,  UDIs of devices managed in the U.S. by the FDA, the value is  http://hl7.org/fhir/NamingSystem/fda-udi.") |  | 0..1 | [uri](datatypes.html#uri) | Regional UDI authority |
| .... [carrierAIDC](device-definitions.html#Device.udiCarrier.carrierAIDC "Device.udiCarrier.carrierAIDC : The full UDI carrier of the Automatic Identification and Data Capture (AIDC) technology representation of the barcode string as printed on the packaging of the device - e.g., a barcode or RFID.   Because of limitations on character sets in XML and the need to round-trip JSON data through XML, AIDC Formats *SHALL* be base64 encoded.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [base64Binary](datatypes.html#base64Binary) | UDI Machine Readable Barcode String |
| .... [carrierHRF](device-definitions.html#Device.udiCarrier.carrierHRF "Device.udiCarrier.carrierHRF : The full UDI carrier as the human readable form (HRF) representation of the barcode string as printed on the packaging of the device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | UDI Human Readable Barcode String |
| .... [entryType](device-definitions.html#Device.udiCarrier.entryType "Device.udiCarrier.entryType : A coded entry to indicate how the data was entered.") |  | 0..1 | [code](datatypes.html#code) | barcode | rfid | manual + [UDIEntryType](valueset-udi-entry-type.html "Codes to identify how UDI data was entered.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [status](device-definitions.html#Device.status "Device.status : Status of the Device availability.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | active | inactive | entered-in-error | unknown [FHIRDeviceStatus](valueset-device-status.html "The availability status of the device.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [statusReason](device-definitions.html#Device.statusReason "Device.statusReason : Reason for the dtatus of the Device availability.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off [FHIRDeviceStatusReason](valueset-device-status-reason.html "The availability status reason of the device.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [distinctIdentifier](device-definitions.html#Device.distinctIdentifier "Device.distinctIdentifier : The distinct identification string as required by regulation for a human cell, tissue, or cellular and tissue-based product.") |  | 0..1 | [string](datatypes.html#string) | The distinct identification string |
| ... [manufacturer](device-definitions.html#Device.manufacturer "Device.manufacturer : A name of the manufacturer.") |  | 0..1 | [string](datatypes.html#string) | Name of device manufacturer |
| ... [manufactureDate](device-definitions.html#Device.manufactureDate "Device.manufactureDate : The date and time when the device was manufactured.") |  | 0..1 | [dateTime](datatypes.html#dateTime) | Date when the device was made |
| ... [expirationDate](device-definitions.html#Device.expirationDate "Device.expirationDate : The date and time beyond which this device is no longer valid or should not be used (if applicable).") |  | 0..1 | [dateTime](datatypes.html#dateTime) | Date and time of expiry of this device (if applicable) |
| ... [lotNumber](device-definitions.html#Device.lotNumber "Device.lotNumber : Lot number assigned by the manufacturer.") |  | 0..1 | [string](datatypes.html#string) | Lot number of manufacture |
| ... [serialNumber](device-definitions.html#Device.serialNumber "Device.serialNumber : The serial number assigned by the organization when the device was manufactured.") |  | 0..1 | [string](datatypes.html#string) | Serial number assigned by the manufacturer |
| ... [deviceName](device-definitions.html#Device.deviceName "Device.deviceName : This represents the manufacturer's name of the device as provided by the device, from a UDI label, or by a person describing the Device.  This typically would be used when a person provides the name(s) or when the device represents one of the names available from DeviceDefinition.") |  | 0..\* | [BackboneElement](backboneelement.html) | The name of the device as given by the manufacturer |
| .... [name](device-definitions.html#Device.deviceName.name "Device.deviceName.name : The name of the device.") |  | 1..1 | [string](datatypes.html#string) | The name of the device |
| .... [type](device-definitions.html#Device.deviceName.type "Device.deviceName.type : The type of deviceName. UDILabelName | UserFriendlyName | PatientReportedName | ManufactureDeviceName | ModelName.") |  | 1..1 | [code](datatypes.html#code) | udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other [DeviceNameType](valueset-device-nametype.html "The type of name the device is referred by.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [modelNumber](device-definitions.html#Device.modelNumber "Device.modelNumber : The model number for the device.") |  | 0..1 | [string](datatypes.html#string) | The model number for the device |
| ... [partNumber](device-definitions.html#Device.partNumber "Device.partNumber : The part number of the device.") |  | 0..1 | [string](datatypes.html#string) | The part number of the device |
| ... [type](device-definitions.html#Device.type "Device.type : The kind or type of device.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The kind or type of device [Device Type](valueset-device-type.html "Codes to identify medical devices.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specialization](device-definitions.html#Device.specialization "Device.specialization : The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.") |  | 0..\* | [BackboneElement](backboneelement.html) | The capabilities supported on a device, the standards to which the device conforms for a particular purpose, and used for the communication |
| .... [systemType](device-definitions.html#Device.specialization.systemType "Device.specialization.systemType : The standard that is used to operate and communicate.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The standard that is used to operate and communicate |
| .... [version](device-definitions.html#Device.specialization.version "Device.specialization.version : The version of the standard that is used to operate and communicate.") |  | 0..1 | [string](datatypes.html#string) | The version of the standard that is used to operate and communicate |
| ... [version](device-definitions.html#Device.version "Device.version : The actual design of the device or software version running on the device.") |  | 0..\* | [BackboneElement](backboneelement.html) | The actual design of the device or software version running on the device |
| .... [type](device-definitions.html#Device.version.type "Device.version.type : The type of the device version.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of the device version |
| .... [component](device-definitions.html#Device.version.component "Device.version.component : A single component of the device version.") |  | 0..1 | [Identifier](datatypes.html#Identifier) | A single component of the device version |
| .... [value](device-definitions.html#Device.version.value "Device.version.value : The version text.") |  | 1..1 | [string](datatypes.html#string) | The version text |
| ... [property](device-definitions.html#Device.property "Device.property : The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.") |  | 0..\* | [BackboneElement](backboneelement.html) | The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties |
| .... [type](device-definitions.html#Device.property.type "Device.property.type : Code that specifies the property DeviceDefinitionPropetyCode (Extensible).") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Code that specifies the property DeviceDefinitionPropetyCode (Extensible) |
| .... [valueQuantity](device-definitions.html#Device.property.valueQuantity "Device.property.valueQuantity : Property value as a quantity.") |  | 0..\* | [Quantity](datatypes.html#Quantity) | Property value as a quantity |
| .... [valueCode](device-definitions.html#Device.property.valueCode "Device.property.valueCode : Property value as a code, e.g., NTP4 (synced to NTP).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Property value as a code, e.g., NTP4 (synced to NTP) |
| ... [patient](device-definitions.html#Device.patient "Device.patient : Patient information, If the device is affixed to a person.") |  | 0..1 | [Reference](references.html#Reference)([Patient](patient.html)) | Patient to whom Device is affixed |
| ... [owner](device-definitions.html#Device.owner "Device.owner : An organization that is responsible for the provision and ongoing maintenance of the device.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for device |
| ... [contact](device-definitions.html#Device.contact "Device.contact : Contact details for an organization or a particular human that is responsible for the device.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Details for human/organization for support |
| ... [location](device-definitions.html#Device.location "Device.location : The place where the device can be found.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Where the device is found |
| ... [url](device-definitions.html#Device.url "Device.url : A network address on which the device may be contacted directly.") |  | 0..1 | [uri](datatypes.html#uri) | Network address to contact device |
| ... [note](device-definitions.html#Device.note "Device.note : Descriptive information, usage information or implantation information that is not captured in an existing element.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Device notes and comments |
| ... [safety](device-definitions.html#Device.safety "Device.safety : Provides additional safety characteristics about a medical device.  For example devices containing latex.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Safety Characteristics of Device |
| ... [parent](device-definitions.html#Device.parent "Device.parent : The parent device.") |  | 0..1 | [Reference](references.html#Reference)([Device](device.html)) | The parent device |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Device xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Instance identifier --></identifier>
 <definition><!-- 0..1 Reference(DeviceDefinition) The reference to the definition for the device --></definition>
 <udiCarrier>  <!-- 0..* Unique Device Identifier (UDI) Barcode string -->
  <deviceIdentifier value="[string]"/><!-- 0..1 Mandatory fixed portion of UDI -->
  <issuer value="[uri]"/><!-- 0..1 UDI Issuing Organization -->
  <jurisdiction value="[uri]"/><!-- 0..1 Regional UDI authority -->
  <carrierAIDC value="[base64Binary]"/><!-- 0..1 UDI Machine Readable Barcode String -->
  <carrierHRF value="[string]"/><!-- 0..1 UDI Human Readable Barcode String -->
  <entryType value="[code]"/><!-- 0..1 barcode | rfid | manual + -->
 </udiCarrier>
 <status value="[code]"/><!-- 0..1 active | inactive | entered-in-error | unknown -->
 <statusReason><!-- 0..* CodeableConcept online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off --></statusReason>
 <distinctIdentifier value="[string]"/><!-- 0..1 The distinct identification string -->
 <manufacturer value="[string]"/><!-- 0..1 Name of device manufacturer -->
 <manufactureDate value="[dateTime]"/><!-- 0..1 Date when the device was made -->
 <expirationDate value="[dateTime]"/><!-- 0..1 Date and time of expiry of this device (if applicable) -->
 <lotNumber value="[string]"/><!-- 0..1 Lot number of manufacture -->
 <serialNumber value="[string]"/><!-- 0..1 Serial number assigned by the manufacturer -->
 <deviceName>  <!-- 0..* The name of the device as given by the manufacturer -->
  <name value="[string]"/><!-- 1..1 The name of the device -->
  <type value="[code]"/><!-- 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other -->
 </deviceName>
 <modelNumber value="[string]"/><!-- 0..1 The model number for the device -->
 <partNumber value="[string]"/><!-- 0..1 The part number of the device -->
 <type><!-- 0..1 CodeableConcept The kind or type of device --></type>
 <specialization>  <!-- 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication -->
  <systemType><!-- 1..1 CodeableConcept The standard that is used to operate and communicate --></systemType>
  <version value="[string]"/><!-- 0..1 The version of the standard that is used to operate and communicate -->
 </specialization>
 <version>  <!-- 0..* The actual design of the device or software version running on the device -->
  <type><!-- 0..1 CodeableConcept The type of the device version --></type>
  <component><!-- 0..1 Identifier A single component of the device version --></component>
  <value value="[string]"/><!-- 1..1 The version text -->
 </version>
 <property>  <!-- 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties -->
  <type><!-- 1..1 CodeableConcept Code that specifies the property DeviceDefinitionPropetyCode (Extensible) --></type>
  <valueQuantity><!-- 0..* Quantity Property value as a quantity --></valueQuantity>
  <valueCode><!-- 0..* CodeableConcept Property value as a code, e.g., NTP4 (synced to NTP) --></valueCode>
 </property>
 <patient><!-- 0..1 Reference(Patient) Patient to whom Device is affixed --></patient>
 <owner><!-- 0..1 Reference(Organization) Organization responsible for device --></owner>
 <contact><!-- 0..* ContactPoint Details for human/organization for support --></contact>
 <location><!-- 0..1 Reference(Location) Where the device is found --></location>
 <url value="[uri]"/><!-- 0..1 Network address to contact device -->
 <note><!-- 0..* Annotation Device notes and comments --></note>
 <safety><!-- 0..* CodeableConcept Safety Characteristics of Device --></safety>
 <parent><!-- 0..1 Reference(Device) The parent device --></parent>
</Device>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Device",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Instance identifier
  "definition" : { Reference(DeviceDefinition) }, // The reference to the definition for the device
  "udiCarrier" : [{ // Unique Device Identifier (UDI) Barcode string
    "deviceIdentifier" : "<string>", // Mandatory fixed portion of UDI
    "issuer" : "<uri>", // UDI Issuing Organization
    "jurisdiction" : "<uri>", // Regional UDI authority
    "carrierAIDC" : "<base64Binary>", // UDI Machine Readable Barcode String
    "carrierHRF" : "<string>", // UDI Human Readable Barcode String
    "entryType" : "<code>" // barcode | rfid | manual +
  }],
  "status" : "<code>", // active | inactive | entered-in-error | unknown
  "statusReason" : [{ CodeableConcept }], // online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off
  "distinctIdentifier" : "<string>", // The distinct identification string
  "manufacturer" : "<string>", // Name of device manufacturer
  "manufactureDate" : "<dateTime>", // Date when the device was made
  "expirationDate" : "<dateTime>", // Date and time of expiry of this device (if applicable)
  "lotNumber" : "<string>", // Lot number of manufacture
  "serialNumber" : "<string>", // Serial number assigned by the manufacturer
  "deviceName" : [{ // The name of the device as given by the manufacturer
    "name" : "<string>", // R!  The name of the device
    "type" : "<code>" // R!  udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  }],
  "modelNumber" : "<string>", // The model number for the device
  "partNumber" : "<string>", // The part number of the device
  "type" : { CodeableConcept }, // The kind or type of device
  "specialization" : [{ // The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    "systemType" : { CodeableConcept }, // R!  The standard that is used to operate and communicate
    "version" : "<string>" // The version of the standard that is used to operate and communicate
  }],
  "version" : [{ // The actual design of the device or software version running on the device
    "type" : { CodeableConcept }, // The type of the device version
    "component" : { Identifier }, // A single component of the device version
    "value" : "<string>" // R!  The version text
  }],
  "property" : [{ // The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    "type" : { CodeableConcept }, // R!  Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    "valueQuantity" : [{ Quantity }], // Property value as a quantity
    "valueCode" : [{ CodeableConcept }] // Property value as a code, e.g., NTP4 (synced to NTP)
  }],
  "patient" : { Reference(Patient) }, // Patient to whom Device is affixed
  "owner" : { Reference(Organization) }, // Organization responsible for device
  "contact" : [{ ContactPoint }], // Details for human/organization for support
  "location" : { Reference(Location) }, // Where the device is found
  "url" : "<uri>", // Network address to contact device
  "note" : [{ Annotation }], // Device notes and comments
  "safety" : [{ CodeableConcept }], // Safety Characteristics of Device
  "parent" : { Reference(Device) } // The parent device
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Device;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Device.identifier [ Identifier ], ... ; # 0..* Instance identifier
  fhir:Device.definition [ Reference(DeviceDefinition) ]; # 0..1 The reference to the definition for the device
  fhir:Device.udiCarrier [ # 0..* Unique Device Identifier (UDI) Barcode string
    fhir:Device.udiCarrier.deviceIdentifier [ string ]; # 0..1 Mandatory fixed portion of UDI
    fhir:Device.udiCarrier.issuer [ uri ]; # 0..1 UDI Issuing Organization
    fhir:Device.udiCarrier.jurisdiction [ uri ]; # 0..1 Regional UDI authority
    fhir:Device.udiCarrier.carrierAIDC [ base64Binary ]; # 0..1 UDI Machine Readable Barcode String
    fhir:Device.udiCarrier.carrierHRF [ string ]; # 0..1 UDI Human Readable Barcode String
    fhir:Device.udiCarrier.entryType [ code ]; # 0..1 barcode | rfid | manual +
  ], ...;
  fhir:Device.status [ code ]; # 0..1 active | inactive | entered-in-error | unknown
  fhir:Device.statusReason [ CodeableConcept ], ... ; # 0..* online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off
  fhir:Device.distinctIdentifier [ string ]; # 0..1 The distinct identification string
  fhir:Device.manufacturer [ string ]; # 0..1 Name of device manufacturer
  fhir:Device.manufactureDate [ dateTime ]; # 0..1 Date when the device was made
  fhir:Device.expirationDate [ dateTime ]; # 0..1 Date and time of expiry of this device (if applicable)
  fhir:Device.lotNumber [ string ]; # 0..1 Lot number of manufacture
  fhir:Device.serialNumber [ string ]; # 0..1 Serial number assigned by the manufacturer
  fhir:Device.deviceName [ # 0..* The name of the device as given by the manufacturer
    fhir:Device.deviceName.name [ string ]; # 1..1 The name of the device
    fhir:Device.deviceName.type [ code ]; # 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  ], ...;
  fhir:Device.modelNumber [ string ]; # 0..1 The model number for the device
  fhir:Device.partNumber [ string ]; # 0..1 The part number of the device
  fhir:Device.type [ CodeableConcept ]; # 0..1 The kind or type of device
  fhir:Device.specialization [ # 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    fhir:Device.specialization.systemType [ CodeableConcept ]; # 1..1 The standard that is used to operate and communicate
    fhir:Device.specialization.version [ string ]; # 0..1 The version of the standard that is used to operate and communicate
  ], ...;
  fhir:Device.version [ # 0..* The actual design of the device or software version running on the device
    fhir:Device.version.type [ CodeableConcept ]; # 0..1 The type of the device version
    fhir:Device.version.component [ Identifier ]; # 0..1 A single component of the device version
    fhir:Device.version.value [ string ]; # 1..1 The version text
  ], ...;
  fhir:Device.property [ # 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    fhir:Device.property.type [ CodeableConcept ]; # 1..1 Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    fhir:Device.property.valueQuantity [ Quantity ], ... ; # 0..* Property value as a quantity
    fhir:Device.property.valueCode [ CodeableConcept ], ... ; # 0..* Property value as a code, e.g., NTP4 (synced to NTP)
  ], ...;
  fhir:Device.patient [ Reference(Patient) ]; # 0..1 Patient to whom Device is affixed
  fhir:Device.owner [ Reference(Organization) ]; # 0..1 Organization responsible for device
  fhir:Device.contact [ ContactPoint ], ... ; # 0..* Details for human/organization for support
  fhir:Device.location [ Reference(Location) ]; # 0..1 Where the device is found
  fhir:Device.url [ uri ]; # 0..1 Network address to contact device
  fhir:Device.note [ Annotation ], ... ; # 0..* Device notes and comments
  fhir:Device.safety [ CodeableConcept ], ... ; # 0..* Safety Characteristics of Device
  fhir:Device.parent [ Reference(Device) ]; # 0..1 The parent device
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Device](device.html#Device) |  |
| Device.definition | - Added Element |
| Device.udiCarrier | - Added Element |
| Device.udiCarrier.deviceIdentifier | - Added Element |
| Device.udiCarrier.issuer | - Added Element |
| Device.udiCarrier.jurisdiction | - Added Element |
| Device.udiCarrier.carrierAIDC | - Added Element |
| Device.udiCarrier.carrierHRF | - Added Element |
| Device.udiCarrier.entryType | - Added Element |
| Device.status | - Change value set from http://hl7.org/fhir/ValueSet/device-status to http://hl7.org/fhir/ValueSet/device-status|4.0.1 |
| Device.statusReason | - Added Element |
| Device.distinctIdentifier | - Added Element |
| Device.serialNumber | - Added Element |
| Device.deviceName | - Added Element |
| Device.deviceName.name | - **Added Mandatory Element** |
| Device.deviceName.type | - **Added Mandatory Element** |
| Device.modelNumber | - Added Element |
| Device.partNumber | - Added Element |
| Device.specialization | - Added Element |
| Device.specialization.systemType | - **Added Mandatory Element** |
| Device.specialization.version | - Added Element |
| Device.version | - Max Cardinality changed from 1 to \* - Type changed from string to BackboneElement |
| Device.version.type | - Added Element |
| Device.version.component | - Added Element |
| Device.version.value | - **Added Mandatory Element** |
| Device.property | - Added Element |
| Device.property.type | - **Added Mandatory Element** |
| Device.property.valueQuantity | - Added Element |
| Device.property.valueCode | - Added Element |
| Device.parent | - Added Element |
| Device.udi | - deleted |
| Device.model | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](device.diff.xml) or [JSON](device.diff.json).

See [R3 <--> R4 Conversion Maps](device-version-maps.html) (status = 9 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Device](device-definitions.html#Device "Device : A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Item used in healthcare Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](device-definitions.html#Device.identifier "Device.identifier : Unique instance identifiers assigned to a device by manufacturers other organizations or owners.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | Instance identifier |
| ... [definition](device-definitions.html#Device.definition "Device.definition : The reference to the definition for the device.") |  | 0..1 | [Reference](references.html#Reference)([DeviceDefinition](devicedefinition.html)) | The reference to the definition for the device |
| ... [udiCarrier](device-definitions.html#Device.udiCarrier "Device.udiCarrier : Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Unique Device Identifier (UDI) Barcode string |
| .... [deviceIdentifier](device-definitions.html#Device.udiCarrier.deviceIdentifier "Device.udiCarrier.deviceIdentifier : The device identifier (DI) is a mandatory, fixed portion of a UDI that identifies the labeler and the specific version or model of a device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Mandatory fixed portion of UDI |
| .... [issuer](device-definitions.html#Device.udiCarrier.issuer "Device.udiCarrier.issuer : Organization that is charged with issuing UDIs for devices.  For example, the US FDA issuers include : 1) GS1:  http://hl7.org/fhir/NamingSystem/gs1-di,  2) HIBCC: http://hl7.org/fhir/NamingSystem/hibcc-dI,  3) ICCBBA for blood containers: http://hl7.org/fhir/NamingSystem/iccbba-blood-di,  4) ICCBA for other devices: http://hl7.org/fhir/NamingSystem/iccbba-other-di.") |  | 0..1 | [uri](datatypes.html#uri) | UDI Issuing Organization |
| .... [jurisdiction](device-definitions.html#Device.udiCarrier.jurisdiction "Device.udiCarrier.jurisdiction : The identity of the authoritative source for UDI generation within a  jurisdiction.  All UDIs are globally unique within a single namespace with the appropriate repository uri as the system.  For example,  UDIs of devices managed in the U.S. by the FDA, the value is  http://hl7.org/fhir/NamingSystem/fda-udi.") |  | 0..1 | [uri](datatypes.html#uri) | Regional UDI authority |
| .... [carrierAIDC](device-definitions.html#Device.udiCarrier.carrierAIDC "Device.udiCarrier.carrierAIDC : The full UDI carrier of the Automatic Identification and Data Capture (AIDC) technology representation of the barcode string as printed on the packaging of the device - e.g., a barcode or RFID.   Because of limitations on character sets in XML and the need to round-trip JSON data through XML, AIDC Formats *SHALL* be base64 encoded.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [base64Binary](datatypes.html#base64Binary) | UDI Machine Readable Barcode String |
| .... [carrierHRF](device-definitions.html#Device.udiCarrier.carrierHRF "Device.udiCarrier.carrierHRF : The full UDI carrier as the human readable form (HRF) representation of the barcode string as printed on the packaging of the device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | UDI Human Readable Barcode String |
| .... [entryType](device-definitions.html#Device.udiCarrier.entryType "Device.udiCarrier.entryType : A coded entry to indicate how the data was entered.") |  | 0..1 | [code](datatypes.html#code) | barcode | rfid | manual + [UDIEntryType](valueset-udi-entry-type.html "Codes to identify how UDI data was entered.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [status](device-definitions.html#Device.status "Device.status : Status of the Device availability.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | active | inactive | entered-in-error | unknown [FHIRDeviceStatus](valueset-device-status.html "The availability status of the device.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [statusReason](device-definitions.html#Device.statusReason "Device.statusReason : Reason for the dtatus of the Device availability.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off [FHIRDeviceStatusReason](valueset-device-status-reason.html "The availability status reason of the device.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [distinctIdentifier](device-definitions.html#Device.distinctIdentifier "Device.distinctIdentifier : The distinct identification string as required by regulation for a human cell, tissue, or cellular and tissue-based product.") |  | 0..1 | [string](datatypes.html#string) | The distinct identification string |
| ... [manufacturer](device-definitions.html#Device.manufacturer "Device.manufacturer : A name of the manufacturer.") |  | 0..1 | [string](datatypes.html#string) | Name of device manufacturer |
| ... [manufactureDate](device-definitions.html#Device.manufactureDate "Device.manufactureDate : The date and time when the device was manufactured.") |  | 0..1 | [dateTime](datatypes.html#dateTime) | Date when the device was made |
| ... [expirationDate](device-definitions.html#Device.expirationDate "Device.expirationDate : The date and time beyond which this device is no longer valid or should not be used (if applicable).") |  | 0..1 | [dateTime](datatypes.html#dateTime) | Date and time of expiry of this device (if applicable) |
| ... [lotNumber](device-definitions.html#Device.lotNumber "Device.lotNumber : Lot number assigned by the manufacturer.") |  | 0..1 | [string](datatypes.html#string) | Lot number of manufacture |
| ... [serialNumber](device-definitions.html#Device.serialNumber "Device.serialNumber : The serial number assigned by the organization when the device was manufactured.") |  | 0..1 | [string](datatypes.html#string) | Serial number assigned by the manufacturer |
| ... [deviceName](device-definitions.html#Device.deviceName "Device.deviceName : This represents the manufacturer's name of the device as provided by the device, from a UDI label, or by a person describing the Device.  This typically would be used when a person provides the name(s) or when the device represents one of the names available from DeviceDefinition.") |  | 0..\* | [BackboneElement](backboneelement.html) | The name of the device as given by the manufacturer |
| .... [name](device-definitions.html#Device.deviceName.name "Device.deviceName.name : The name of the device.") |  | 1..1 | [string](datatypes.html#string) | The name of the device |
| .... [type](device-definitions.html#Device.deviceName.type "Device.deviceName.type : The type of deviceName. UDILabelName | UserFriendlyName | PatientReportedName | ManufactureDeviceName | ModelName.") |  | 1..1 | [code](datatypes.html#code) | udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other [DeviceNameType](valueset-device-nametype.html "The type of name the device is referred by.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [modelNumber](device-definitions.html#Device.modelNumber "Device.modelNumber : The model number for the device.") |  | 0..1 | [string](datatypes.html#string) | The model number for the device |
| ... [partNumber](device-definitions.html#Device.partNumber "Device.partNumber : The part number of the device.") |  | 0..1 | [string](datatypes.html#string) | The part number of the device |
| ... [type](device-definitions.html#Device.type "Device.type : The kind or type of device.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The kind or type of device [Device Type](valueset-device-type.html "Codes to identify medical devices.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specialization](device-definitions.html#Device.specialization "Device.specialization : The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.") |  | 0..\* | [BackboneElement](backboneelement.html) | The capabilities supported on a device, the standards to which the device conforms for a particular purpose, and used for the communication |
| .... [systemType](device-definitions.html#Device.specialization.systemType "Device.specialization.systemType : The standard that is used to operate and communicate.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The standard that is used to operate and communicate |
| .... [version](device-definitions.html#Device.specialization.version "Device.specialization.version : The version of the standard that is used to operate and communicate.") |  | 0..1 | [string](datatypes.html#string) | The version of the standard that is used to operate and communicate |
| ... [version](device-definitions.html#Device.version "Device.version : The actual design of the device or software version running on the device.") |  | 0..\* | [BackboneElement](backboneelement.html) | The actual design of the device or software version running on the device |
| .... [type](device-definitions.html#Device.version.type "Device.version.type : The type of the device version.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of the device version |
| .... [component](device-definitions.html#Device.version.component "Device.version.component : A single component of the device version.") |  | 0..1 | [Identifier](datatypes.html#Identifier) | A single component of the device version |
| .... [value](device-definitions.html#Device.version.value "Device.version.value : The version text.") |  | 1..1 | [string](datatypes.html#string) | The version text |
| ... [property](device-definitions.html#Device.property "Device.property : The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.") |  | 0..\* | [BackboneElement](backboneelement.html) | The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties |
| .... [type](device-definitions.html#Device.property.type "Device.property.type : Code that specifies the property DeviceDefinitionPropetyCode (Extensible).") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Code that specifies the property DeviceDefinitionPropetyCode (Extensible) |
| .... [valueQuantity](device-definitions.html#Device.property.valueQuantity "Device.property.valueQuantity : Property value as a quantity.") |  | 0..\* | [Quantity](datatypes.html#Quantity) | Property value as a quantity |
| .... [valueCode](device-definitions.html#Device.property.valueCode "Device.property.valueCode : Property value as a code, e.g., NTP4 (synced to NTP).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Property value as a code, e.g., NTP4 (synced to NTP) |
| ... [patient](device-definitions.html#Device.patient "Device.patient : Patient information, If the device is affixed to a person.") |  | 0..1 | [Reference](references.html#Reference)([Patient](patient.html)) | Patient to whom Device is affixed |
| ... [owner](device-definitions.html#Device.owner "Device.owner : An organization that is responsible for the provision and ongoing maintenance of the device.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for device |
| ... [contact](device-definitions.html#Device.contact "Device.contact : Contact details for an organization or a particular human that is responsible for the device.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Details for human/organization for support |
| ... [location](device-definitions.html#Device.location "Device.location : The place where the device can be found.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Where the device is found |
| ... [url](device-definitions.html#Device.url "Device.url : A network address on which the device may be contacted directly.") |  | 0..1 | [uri](datatypes.html#uri) | Network address to contact device |
| ... [note](device-definitions.html#Device.note "Device.note : Descriptive information, usage information or implantation information that is not captured in an existing element.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Device notes and comments |
| ... [safety](device-definitions.html#Device.safety "Device.safety : Provides additional safety characteristics about a medical device.  For example devices containing latex.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Safety Characteristics of Device |
| ... [parent](device-definitions.html#Device.parent "Device.parent : The parent device.") |  | 0..1 | [Reference](references.html#Reference)([Device](device.html)) | The parent device |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Device xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Instance identifier --></identifier>
 <definition><!-- 0..1 Reference(DeviceDefinition) The reference to the definition for the device --></definition>
 <udiCarrier>  <!-- 0..* Unique Device Identifier (UDI) Barcode string -->
  <deviceIdentifier value="[string]"/><!-- 0..1 Mandatory fixed portion of UDI -->
  <issuer value="[uri]"/><!-- 0..1 UDI Issuing Organization -->
  <jurisdiction value="[uri]"/><!-- 0..1 Regional UDI authority -->
  <carrierAIDC value="[base64Binary]"/><!-- 0..1 UDI Machine Readable Barcode String -->
  <carrierHRF value="[string]"/><!-- 0..1 UDI Human Readable Barcode String -->
  <entryType value="[code]"/><!-- 0..1 barcode | rfid | manual + -->
 </udiCarrier>
 <status value="[code]"/><!-- 0..1 active | inactive | entered-in-error | unknown -->
 <statusReason><!-- 0..* CodeableConcept online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off --></statusReason>
 <distinctIdentifier value="[string]"/><!-- 0..1 The distinct identification string -->
 <manufacturer value="[string]"/><!-- 0..1 Name of device manufacturer -->
 <manufactureDate value="[dateTime]"/><!-- 0..1 Date when the device was made -->
 <expirationDate value="[dateTime]"/><!-- 0..1 Date and time of expiry of this device (if applicable) -->
 <lotNumber value="[string]"/><!-- 0..1 Lot number of manufacture -->
 <serialNumber value="[string]"/><!-- 0..1 Serial number assigned by the manufacturer -->
 <deviceName>  <!-- 0..* The name of the device as given by the manufacturer -->
  <name value="[string]"/><!-- 1..1 The name of the device -->
  <type value="[code]"/><!-- 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other -->
 </deviceName>
 <modelNumber value="[string]"/><!-- 0..1 The model number for the device -->
 <partNumber value="[string]"/><!-- 0..1 The part number of the device -->
 <type><!-- 0..1 CodeableConcept The kind or type of device --></type>
 <specialization>  <!-- 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication -->
  <systemType><!-- 1..1 CodeableConcept The standard that is used to operate and communicate --></systemType>
  <version value="[string]"/><!-- 0..1 The version of the standard that is used to operate and communicate -->
 </specialization>
 <version>  <!-- 0..* The actual design of the device or software version running on the device -->
  <type><!-- 0..1 CodeableConcept The type of the device version --></type>
  <component><!-- 0..1 Identifier A single component of the device version --></component>
  <value value="[string]"/><!-- 1..1 The version text -->
 </version>
 <property>  <!-- 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties -->
  <type><!-- 1..1 CodeableConcept Code that specifies the property DeviceDefinitionPropetyCode (Extensible) --></type>
  <valueQuantity><!-- 0..* Quantity Property value as a quantity --></valueQuantity>
  <valueCode><!-- 0..* CodeableConcept Property value as a code, e.g., NTP4 (synced to NTP) --></valueCode>
 </property>
 <patient><!-- 0..1 Reference(Patient) Patient to whom Device is affixed --></patient>
 <owner><!-- 0..1 Reference(Organization) Organization responsible for device --></owner>
 <contact><!-- 0..* ContactPoint Details for human/organization for support --></contact>
 <location><!-- 0..1 Reference(Location) Where the device is found --></location>
 <url value="[uri]"/><!-- 0..1 Network address to contact device -->
 <note><!-- 0..* Annotation Device notes and comments --></note>
 <safety><!-- 0..* CodeableConcept Safety Characteristics of Device --></safety>
 <parent><!-- 0..1 Reference(Device) The parent device --></parent>
</Device>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Device",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Instance identifier
  "definition" : { Reference(DeviceDefinition) }, // The reference to the definition for the device
  "udiCarrier" : [{ // Unique Device Identifier (UDI) Barcode string
    "deviceIdentifier" : "<string>", // Mandatory fixed portion of UDI
    "issuer" : "<uri>", // UDI Issuing Organization
    "jurisdiction" : "<uri>", // Regional UDI authority
    "carrierAIDC" : "<base64Binary>", // UDI Machine Readable Barcode String
    "carrierHRF" : "<string>", // UDI Human Readable Barcode String
    "entryType" : "<code>" // barcode | rfid | manual +
  }],
  "status" : "<code>", // active | inactive | entered-in-error | unknown
  "statusReason" : [{ CodeableConcept }], // online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off
  "distinctIdentifier" : "<string>", // The distinct identification string
  "manufacturer" : "<string>", // Name of device manufacturer
  "manufactureDate" : "<dateTime>", // Date when the device was made
  "expirationDate" : "<dateTime>", // Date and time of expiry of this device (if applicable)
  "lotNumber" : "<string>", // Lot number of manufacture
  "serialNumber" : "<string>", // Serial number assigned by the manufacturer
  "deviceName" : [{ // The name of the device as given by the manufacturer
    "name" : "<string>", // R!  The name of the device
    "type" : "<code>" // R!  udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  }],
  "modelNumber" : "<string>", // The model number for the device
  "partNumber" : "<string>", // The part number of the device
  "type" : { CodeableConcept }, // The kind or type of device
  "specialization" : [{ // The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    "systemType" : { CodeableConcept }, // R!  The standard that is used to operate and communicate
    "version" : "<string>" // The version of the standard that is used to operate and communicate
  }],
  "version" : [{ // The actual design of the device or software version running on the device
    "type" : { CodeableConcept }, // The type of the device version
    "component" : { Identifier }, // A single component of the device version
    "value" : "<string>" // R!  The version text
  }],
  "property" : [{ // The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    "type" : { CodeableConcept }, // R!  Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    "valueQuantity" : [{ Quantity }], // Property value as a quantity
    "valueCode" : [{ CodeableConcept }] // Property value as a code, e.g., NTP4 (synced to NTP)
  }],
  "patient" : { Reference(Patient) }, // Patient to whom Device is affixed
  "owner" : { Reference(Organization) }, // Organization responsible for device
  "contact" : [{ ContactPoint }], // Details for human/organization for support
  "location" : { Reference(Location) }, // Where the device is found
  "url" : "<uri>", // Network address to contact device
  "note" : [{ Annotation }], // Device notes and comments
  "safety" : [{ CodeableConcept }], // Safety Characteristics of Device
  "parent" : { Reference(Device) } // The parent device
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Device;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Device.identifier [ Identifier ], ... ; # 0..* Instance identifier
  fhir:Device.definition [ Reference(DeviceDefinition) ]; # 0..1 The reference to the definition for the device
  fhir:Device.udiCarrier [ # 0..* Unique Device Identifier (UDI) Barcode string
    fhir:Device.udiCarrier.deviceIdentifier [ string ]; # 0..1 Mandatory fixed portion of UDI
    fhir:Device.udiCarrier.issuer [ uri ]; # 0..1 UDI Issuing Organization
    fhir:Device.udiCarrier.jurisdiction [ uri ]; # 0..1 Regional UDI authority
    fhir:Device.udiCarrier.carrierAIDC [ base64Binary ]; # 0..1 UDI Machine Readable Barcode String
    fhir:Device.udiCarrier.carrierHRF [ string ]; # 0..1 UDI Human Readable Barcode String
    fhir:Device.udiCarrier.entryType [ code ]; # 0..1 barcode | rfid | manual +
  ], ...;
  fhir:Device.status [ code ]; # 0..1 active | inactive | entered-in-error | unknown
  fhir:Device.statusReason [ CodeableConcept ], ... ; # 0..* online | paused | standby | offline | not-ready | transduc-discon | hw-discon | off
  fhir:Device.distinctIdentifier [ string ]; # 0..1 The distinct identification string
  fhir:Device.manufacturer [ string ]; # 0..1 Name of device manufacturer
  fhir:Device.manufactureDate [ dateTime ]; # 0..1 Date when the device was made
  fhir:Device.expirationDate [ dateTime ]; # 0..1 Date and time of expiry of this device (if applicable)
  fhir:Device.lotNumber [ string ]; # 0..1 Lot number of manufacture
  fhir:Device.serialNumber [ string ]; # 0..1 Serial number assigned by the manufacturer
  fhir:Device.deviceName [ # 0..* The name of the device as given by the manufacturer
    fhir:Device.deviceName.name [ string ]; # 1..1 The name of the device
    fhir:Device.deviceName.type [ code ]; # 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  ], ...;
  fhir:Device.modelNumber [ string ]; # 0..1 The model number for the device
  fhir:Device.partNumber [ string ]; # 0..1 The part number of the device
  fhir:Device.type [ CodeableConcept ]; # 0..1 The kind or type of device
  fhir:Device.specialization [ # 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    fhir:Device.specialization.systemType [ CodeableConcept ]; # 1..1 The standard that is used to operate and communicate
    fhir:Device.specialization.version [ string ]; # 0..1 The version of the standard that is used to operate and communicate
  ], ...;
  fhir:Device.version [ # 0..* The actual design of the device or software version running on the device
    fhir:Device.version.type [ CodeableConcept ]; # 0..1 The type of the device version
    fhir:Device.version.component [ Identifier ]; # 0..1 A single component of the device version
    fhir:Device.version.value [ string ]; # 1..1 The version text
  ], ...;
  fhir:Device.property [ # 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    fhir:Device.property.type [ CodeableConcept ]; # 1..1 Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    fhir:Device.property.valueQuantity [ Quantity ], ... ; # 0..* Property value as a quantity
    fhir:Device.property.valueCode [ CodeableConcept ], ... ; # 0..* Property value as a code, e.g., NTP4 (synced to NTP)
  ], ...;
  fhir:Device.patient [ Reference(Patient) ]; # 0..1 Patient to whom Device is affixed
  fhir:Device.owner [ Reference(Organization) ]; # 0..1 Organization responsible for device
  fhir:Device.contact [ ContactPoint ], ... ; # 0..* Details for human/organization for support
  fhir:Device.location [ Reference(Location) ]; # 0..1 Where the device is found
  fhir:Device.url [ uri ]; # 0..1 Network address to contact device
  fhir:Device.note [ Annotation ], ... ; # 0..* Device notes and comments
  fhir:Device.safety [ CodeableConcept ], ... ; # 0..* Safety Characteristics of Device
  fhir:Device.parent [ Reference(Device) ]; # 0..1 The parent device
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Device](device.html#Device) |  |
| Device.definition | - Added Element |
| Device.udiCarrier | - Added Element |
| Device.udiCarrier.deviceIdentifier | - Added Element |
| Device.udiCarrier.issuer | - Added Element |
| Device.udiCarrier.jurisdiction | - Added Element |
| Device.udiCarrier.carrierAIDC | - Added Element |
| Device.udiCarrier.carrierHRF | - Added Element |
| Device.udiCarrier.entryType | - Added Element |
| Device.status | - Change value set from http://hl7.org/fhir/ValueSet/device-status to http://hl7.org/fhir/ValueSet/device-status|4.0.1 |
| Device.statusReason | - Added Element |
| Device.distinctIdentifier | - Added Element |
| Device.serialNumber | - Added Element |
| Device.deviceName | - Added Element |
| Device.deviceName.name | - **Added Mandatory Element** |
| Device.deviceName.type | - **Added Mandatory Element** |
| Device.modelNumber | - Added Element |
| Device.partNumber | - Added Element |
| Device.specialization | - Added Element |
| Device.specialization.systemType | - **Added Mandatory Element** |
| Device.specialization.version | - Added Element |
| Device.version | - Max Cardinality changed from 1 to \* - Type changed from string to BackboneElement |
| Device.version.type | - Added Element |
| Device.version.component | - Added Element |
| Device.version.value | - **Added Mandatory Element** |
| Device.property | - Added Element |
| Device.property.type | - **Added Mandatory Element** |
| Device.property.valueQuantity | - Added Element |
| Device.property.valueCode | - Added Element |
| Device.parent | - Added Element |
| Device.udi | - deleted |
| Device.model | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](device.diff.xml) or [JSON](device.diff.json).

See [R3 <--> R4 Conversion Maps](device-version-maps.html) (status = 9 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](device-profiles.html) and the alternate definitions:
Master Definition [XML](device.profile.xml.html) + [JSON](device.profile.json.html),
[XML](xml.html) [Schema](device.xsd)/[Schematron](device.sch) + [JSON](json.html)
[Schema](device.schema.json.html), [ShEx](device.shex.html) (for [Turtle](rdf.html)) + [see the extensions](device-profiles.html) & the [dependency analysis](device-dependencies.html)

### 8.14.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Device.udiCarrier.entryType | Codes to identify how UDI data was entered. | [Required](terminologies.html#required) | [UDIEntryType](valueset-udi-entry-type.html) |
| Device.status | The availability status of the device. | [Required](terminologies.html#required) | [FHIRDeviceStatus](valueset-device-status.html) |
| Device.statusReason | The availability status reason of the device. | [Extensible](terminologies.html#extensible) | [FHIRDeviceStatusReason](valueset-device-status-reason.html) |
| Device.deviceName.type | The type of name the device is referred by. | [Required](terminologies.html#required) | [DeviceNameType](valueset-device-nametype.html) |
| Device.type | Codes to identify medical devices. | [Example](terminologies.html#example) | [DeviceType](valueset-device-type.html) |

### 8.14.3.2 Notes

#### 8.14.3.2.1 Device Identifier and Device Type

Nearly all devices are assigned a string of characters to represent one or more identifiers or codes, which are usually printed or affixed to the device using either barcodes or RFIDs. The identifier or code can come from the manufacturer (for example, a 'serial number', 'reference number', or 'catalog number'), various institution and registries. Any of these identifiers or codes assigned to the device can and should be recorded in the device resource. However, there can there can be confusion where to represent them in the resource because codes and identifiers are represented in FHIR as semantically distinct elements and because organizations may conflate the term 'code' for an identifier or 'identifier' for a code in their names.

The `identifier` element is *only* intended for use when it's an actual identifier for a specific instance of a device. That would mean that each device would have a separate serial number and would be represented using this element - devices without serial numbers (for example, a box of syringes) would not. Concepts such as a reference number or catalog number or GTIN describe a code which represents a *kind* of device and are conveyed using the `type` element. Some sources of standard codes for devices and translations within `type` are listed below:

- [SNOMED CT](valueset-device-kind.html) - the example binding used here
- [Global Medical Device Nomenclature (GMDN®) ![](external.png)](https://www.gmdnagency.org/)
- [Rosetta Terminology Mapping (RTM) ![](external.png)](https://rtmms.nist.gov/rtmms/index.htm)

#### 8.14.3.2.2 Unique Device Identifier (UDI)

The International Medical Device Regulators Forum IMDRF UDI Working Group published [UDI System for Medical Devices (Version 2.0) ![](external.png)](http://www.imdrf.org/consultations/cons-udi.asp), the base specification for Unique Device Identifiers (UDI). The United States Food and Drug Administration has produced an [implementation guide ![](external.png)](http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/default.htm) for Unique Device Identifiers (UDI) which implements the IMDRF specification and other jurisdictions may produce similar IMDRF implementation guides as well. The full UDI string that represents the barcode as printed on the packaging of the device or Automatic Identification and Data Capture (AIDC) representation is called the "UDI carrier". The UDI has 2 components\*:

- Device identifier (DI)\*\*, which is the actual identification component
- Production identifier(s)(PI) which provide the means to track a device through its manufacture, distribution and use.

\*non-UDI elements may also appear within the UDI carrier.
\*\*a "GTIN" (sometimes also called an EAN number) is a code developed by [GS1 ![](external.png)](http://www.gs1.org/) for the kind of device not an identifier for the device. A GTIN may appear on its own or it may appear in a UDI string as the DI component.

The DI of the UDI may be stored in a jurisdictional repository and used as the primary key to access other device information. For example, in the United States, the DI of the UDI is submitted in a device record to the [Global Unique Device Identification Database (GUDID) ![](external.png)](http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/GlobalUDIDatabaseGUDID/default.htm). The UDI may identify an instance of a device uniquely (when the PI includes a serial number), or it may just identify the type of the device. The UDI is parsed into its constituent parts (DI, PI and other elements) by parsing rules developed by each Issuing Agency standard. Where the device has an assigned UDI, the other details carried in the resource (e.g., lot, expiration date, etc.) SHALL be consistent with the information encoded in the UDI string or registered in the local repository.

Best practice guidelines for transmitting UDI data using the Device resource dictate transmitting both the UDI Carrier and all components found within the UDI as described in Device [UDI Mapping](device-mappings.html#udi)). Several [examples](device-examples.html) are provided for further guidance.

## 8.14.4 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| device-name | [string](search.html#string) | A server defined search that may match any of the string fields in Device.deviceName or Device.type. | Device.deviceName.name | Device.type.coding.display | Device.type.text |  |
| identifier | [token](search.html#token) | Instance id from manufacturer, owner, and others | Device.identifier |  |
| location | [reference](search.html#reference) | A location, where the resource is found | Device.location ([Location](location.html)) |  |
| manufacturer | [string](search.html#string) | The manufacturer of the device | Device.manufacturer |  |
| model | [string](search.html#string) | The model of the device | Device.modelNumber |  |
| organization | [reference](search.html#reference) | The organization responsible for the device | Device.owner ([Organization](organization.html)) |  |
| patient | [reference](search.html#reference) | Patient information, if the resource is affixed to a person | Device.patient ([Patient](patient.html)) |  |
| status | [token](search.html#token) | active | inactive | entered-in-error | unknown | Device.status |  |
| type | [token](search.html#token) | The type of the device | Device.type |  |
| udi-carrier | [string](search.html#string) | UDI Barcode (RFID or other technology) string in \*HRF\* format. | Device.udiCarrier.carrierHRF |  |
| udi-di | [string](search.html#string) | The udi Device Identifier (DI) | Device.udiCarrier.deviceIdentifier |  |
| url | [uri](search.html#uri) | Network address to contact device | Device.url |  |
