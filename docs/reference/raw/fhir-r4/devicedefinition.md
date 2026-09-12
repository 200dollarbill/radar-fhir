---
id: devicedefinition
title: DeviceDefinition
source_url: https://hl7.org/fhir/R4/devicedefinition.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:03Z'
sha256: 1083f92de49980a625a4117c35598dcf0009910743158fae882b88c617dc1de7
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/devicedefinition.html) [R4B](http://hl7.org/fhir/R4B/devicedefinition.html) **R4**

- [Content](#)
- [Examples](devicedefinition-examples.html)
- [Detailed Descriptions](devicedefinition-definitions.html)
- [Mappings](devicedefinition-mappings.html)
- [Profiles & Extensions](devicedefinition-profiles.html)

# 8.15 Resource DeviceDefinition - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Orders and Observations](http://www.hl7.org/Special/committees/orders/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 0 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Anonymous | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

The characteristics, operational status and capabilities of a medical-related component of a medical device.

## 8.15.1 Scope and Usage

The DeviceDefinition resource is used to describe the characteristics and capabilities of a medical device.

## 8.15.2 Boundaries and Relationships

The DeviceDefinition resource contains the "catalog" definition of a device - whether that definition is authored by the regulatory entities, or it is a local definition that includes assembled device configurations.
The DeviceDefinition allows defining hierarchical device configurations (devices as part of other devices).

Device vs deviceDefinition:
The Device resource is meant to refer to a physical instance of a device - hence having attributes like lot number, patient, location, which the DeviceDefinition resource does not have.

## 8.15.3 Background and Context

### 8.15.3.1

This resource is referenced by [Device](device.html#Device), itself, [MedicinalProductPackaged](medicinalproductpackaged.html#MedicinalProductPackaged) and [MedicinalProductPharmaceutical](medicinalproductpharmaceutical.html#MedicinalProductPharmaceutical)

## 8.15.4 Resource Content

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
| .. [DeviceDefinition](devicedefinition-definitions.html#DeviceDefinition "DeviceDefinition : The characteristics, operational status and capabilities of a medical-related component of a medical device.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | An instance of a medical-related component of a medical device Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](devicedefinition-definitions.html#DeviceDefinition.identifier "DeviceDefinition.identifier : Unique instance identifiers assigned to a device by the software, manufacturers, other organizations or owners. For example: handle ID.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | Instance identifier |
| ... [udiDeviceIdentifier](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier "DeviceDefinition.udiDeviceIdentifier : Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.") |  | 0..\* | [BackboneElement](backboneelement.html) | Unique Device Identifier (UDI) Barcode string |
| .... [deviceIdentifier](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier.deviceIdentifier "DeviceDefinition.udiDeviceIdentifier.deviceIdentifier : The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier.") |  | 1..1 | [string](datatypes.html#string) | The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier |
| .... [issuer](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier.issuer "DeviceDefinition.udiDeviceIdentifier.issuer : The organization that assigns the identifier algorithm.") |  | 1..1 | [uri](datatypes.html#uri) | The organization that assigns the identifier algorithm |
| .... [jurisdiction](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier.jurisdiction "DeviceDefinition.udiDeviceIdentifier.jurisdiction : The jurisdiction to which the deviceIdentifier applies.") |  | 1..1 | [uri](datatypes.html#uri) | The jurisdiction to which the deviceIdentifier applies |
| ... [manufacturer[x]](devicedefinition-definitions.html#DeviceDefinition.manufacturer_x_ "DeviceDefinition.manufacturer[x] : A name of the manufacturer.") |  | 0..1 |  | Name of device manufacturer |
| .... manufacturerString |  |  | [string](datatypes.html#string) |  |
| .... manufacturerReference |  |  | [Reference](references.html#Reference)([Organization](organization.html)) |  |
| ... [deviceName](devicedefinition-definitions.html#DeviceDefinition.deviceName "DeviceDefinition.deviceName : A name given to the device to identify it.") |  | 0..\* | [BackboneElement](backboneelement.html) | A name given to the device to identify it |
| .... [name](devicedefinition-definitions.html#DeviceDefinition.deviceName.name "DeviceDefinition.deviceName.name : The name of the device.") |  | 1..1 | [string](datatypes.html#string) | The name of the device |
| .... [type](devicedefinition-definitions.html#DeviceDefinition.deviceName.type "DeviceDefinition.deviceName.type : The type of deviceName. UDILabelName | UserFriendlyName | PatientReportedName | ManufactureDeviceName | ModelName.") |  | 1..1 | [code](datatypes.html#code) | udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other [DeviceNameType](valueset-device-nametype.html "The type of name the device is referred by.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [modelNumber](devicedefinition-definitions.html#DeviceDefinition.modelNumber "DeviceDefinition.modelNumber : The model number for the device.") |  | 0..1 | [string](datatypes.html#string) | The model number for the device |
| ... [type](devicedefinition-definitions.html#DeviceDefinition.type "DeviceDefinition.type : What kind of device or device system this is.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What kind of device or device system this is [FHIR Device Types](valueset-device-kind.html "Type of device e.g. according to official classification.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specialization](devicedefinition-definitions.html#DeviceDefinition.specialization "DeviceDefinition.specialization : The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.") |  | 0..\* | [BackboneElement](backboneelement.html) | The capabilities supported on a device, the standards to which the device conforms for a particular purpose, and used for the communication |
| .... [systemType](devicedefinition-definitions.html#DeviceDefinition.specialization.systemType "DeviceDefinition.specialization.systemType : The standard that is used to operate and communicate.") |  | 1..1 | [string](datatypes.html#string) | The standard that is used to operate and communicate |
| .... [version](devicedefinition-definitions.html#DeviceDefinition.specialization.version "DeviceDefinition.specialization.version : The version of the standard that is used to operate and communicate.") |  | 0..1 | [string](datatypes.html#string) | The version of the standard that is used to operate and communicate |
| ... [version](devicedefinition-definitions.html#DeviceDefinition.version "DeviceDefinition.version : The available versions of the device, e.g., software versions.") |  | 0..\* | [string](datatypes.html#string) | Available versions |
| ... [safety](devicedefinition-definitions.html#DeviceDefinition.safety "DeviceDefinition.safety : Safety characteristics of the device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Safety characteristics of the device [Device safety](valueset-device-safety.html) ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [shelfLifeStorage](devicedefinition-definitions.html#DeviceDefinition.shelfLifeStorage "DeviceDefinition.shelfLifeStorage : Shelf Life and storage information.") |  | 0..\* | [ProductShelfLife](productshelflife.html#ProductShelfLife) | Shelf Life and storage information |
| ... [physicalCharacteristics](devicedefinition-definitions.html#DeviceDefinition.physicalCharacteristics "DeviceDefinition.physicalCharacteristics : Dimensions, color etc.") |  | 0..1 | [ProdCharacteristic](prodcharacteristic.html#ProdCharacteristic) | Dimensions, color etc. |
| ... [languageCode](devicedefinition-definitions.html#DeviceDefinition.languageCode "DeviceDefinition.languageCode : Language code for the human-readable text strings produced by the device (all supported).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Language code for the human-readable text strings produced by the device (all supported) |
| ... [capability](devicedefinition-definitions.html#DeviceDefinition.capability "DeviceDefinition.capability : Device capabilities.") |  | 0..\* | [BackboneElement](backboneelement.html) | Device capabilities |
| .... [type](devicedefinition-definitions.html#DeviceDefinition.capability.type "DeviceDefinition.capability.type : Type of capability.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of capability |
| .... [description](devicedefinition-definitions.html#DeviceDefinition.capability.description "DeviceDefinition.capability.description : Description of capability.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Description of capability |
| ... [property](devicedefinition-definitions.html#DeviceDefinition.property "DeviceDefinition.property : The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.") |  | 0..\* | [BackboneElement](backboneelement.html) | The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties |
| .... [type](devicedefinition-definitions.html#DeviceDefinition.property.type "DeviceDefinition.property.type : Code that specifies the property DeviceDefinitionPropetyCode (Extensible).") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Code that specifies the property DeviceDefinitionPropetyCode (Extensible) |
| .... [valueQuantity](devicedefinition-definitions.html#DeviceDefinition.property.valueQuantity "DeviceDefinition.property.valueQuantity : Property value as a quantity.") |  | 0..\* | [Quantity](datatypes.html#Quantity) | Property value as a quantity |
| .... [valueCode](devicedefinition-definitions.html#DeviceDefinition.property.valueCode "DeviceDefinition.property.valueCode : Property value as a code, e.g., NTP4 (synced to NTP).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Property value as a code, e.g., NTP4 (synced to NTP) |
| ... [owner](devicedefinition-definitions.html#DeviceDefinition.owner "DeviceDefinition.owner : An organization that is responsible for the provision and ongoing maintenance of the device.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for device |
| ... [contact](devicedefinition-definitions.html#DeviceDefinition.contact "DeviceDefinition.contact : Contact details for an organization or a particular human that is responsible for the device.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Details for human/organization for support |
| ... [url](devicedefinition-definitions.html#DeviceDefinition.url "DeviceDefinition.url : A network address on which the device may be contacted directly.") |  | 0..1 | [uri](datatypes.html#uri) | Network address to contact device |
| ... [onlineInformation](devicedefinition-definitions.html#DeviceDefinition.onlineInformation "DeviceDefinition.onlineInformation : Access to on-line information about the device.") |  | 0..1 | [uri](datatypes.html#uri) | Access to on-line information |
| ... [note](devicedefinition-definitions.html#DeviceDefinition.note "DeviceDefinition.note : Descriptive information, usage information or implantation information that is not captured in an existing element.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Device notes and comments |
| ... [quantity](devicedefinition-definitions.html#DeviceDefinition.quantity "DeviceDefinition.quantity : The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product).") |  | 0..1 | [Quantity](datatypes.html#Quantity) | The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product) |
| ... [parentDevice](devicedefinition-definitions.html#DeviceDefinition.parentDevice "DeviceDefinition.parentDevice : The parent device it can be part of.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([DeviceDefinition](devicedefinition.html)) | The parent device it can be part of |
| ... [material](devicedefinition-definitions.html#DeviceDefinition.material "DeviceDefinition.material : A substance used to create the material(s) of which the device is made.") |  | 0..\* | [BackboneElement](backboneelement.html) | A substance used to create the material(s) of which the device is made |
| .... [substance](devicedefinition-definitions.html#DeviceDefinition.material.substance "DeviceDefinition.material.substance : The substance.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The substance |
| .... [alternate](devicedefinition-definitions.html#DeviceDefinition.material.alternate "DeviceDefinition.material.alternate : Indicates an alternative material of the device.") |  | 0..1 | [boolean](datatypes.html#boolean) | Indicates an alternative material of the device |
| .... [allergenicIndicator](devicedefinition-definitions.html#DeviceDefinition.material.allergenicIndicator "DeviceDefinition.material.allergenicIndicator : Whether the substance is a known or suspected allergen.") |  | 0..1 | [boolean](datatypes.html#boolean) | Whether the substance is a known or suspected allergen |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<DeviceDefinition xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Instance identifier --></identifier>
 <udiDeviceIdentifier>  <!-- 0..* Unique Device Identifier (UDI) Barcode string -->
  <deviceIdentifier value="[string]"/><!-- 1..1 The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier -->
  <issuer value="[uri]"/><!-- 1..1 The organization that assigns the identifier algorithm -->
  <jurisdiction value="[uri]"/><!-- 1..1 The jurisdiction to which the deviceIdentifier applies -->
 </udiDeviceIdentifier>
 <manufacturer[x]><!-- 0..1 string|Reference(Organization) Name of device manufacturer --></manufacturer[x]>
 <deviceName>  <!-- 0..* A name given to the device to identify it -->
  <name value="[string]"/><!-- 1..1 The name of the device -->
  <type value="[code]"/><!-- 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other -->
 </deviceName>
 <modelNumber value="[string]"/><!-- 0..1 The model number for the device -->
 <type><!-- 0..1 CodeableConcept What kind of device or device system this is --></type>
 <specialization>  <!-- 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication -->
  <systemType value="[string]"/><!-- 1..1 The standard that is used to operate and communicate -->
  <version value="[string]"/><!-- 0..1 The version of the standard that is used to operate and communicate -->
 </specialization>
 <version value="[string]"/><!-- 0..* Available versions -->
 <safety><!-- 0..* CodeableConcept Safety characteristics of the device --></safety>
 <shelfLifeStorage><!-- 0..* ProductShelfLife Shelf Life and storage information --></shelfLifeStorage>
 <physicalCharacteristics><!-- 0..1 ProdCharacteristic Dimensions, color etc. --></physicalCharacteristics>
 <languageCode><!-- 0..* CodeableConcept Language code for the human-readable text strings produced by the device (all supported) --></languageCode>
 <capability>  <!-- 0..* Device capabilities -->
  <type><!-- 1..1 CodeableConcept Type of capability --></type>
  <description><!-- 0..* CodeableConcept Description of capability --></description>
 </capability>
 <property>  <!-- 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties -->
  <type><!-- 1..1 CodeableConcept Code that specifies the property DeviceDefinitionPropetyCode (Extensible) --></type>
  <valueQuantity><!-- 0..* Quantity Property value as a quantity --></valueQuantity>
  <valueCode><!-- 0..* CodeableConcept Property value as a code, e.g., NTP4 (synced to NTP) --></valueCode>
 </property>
 <owner><!-- 0..1 Reference(Organization) Organization responsible for device --></owner>
 <contact><!-- 0..* ContactPoint Details for human/organization for support --></contact>
 <url value="[uri]"/><!-- 0..1 Network address to contact device -->
 <onlineInformation value="[uri]"/><!-- 0..1 Access to on-line information -->
 <note><!-- 0..* Annotation Device notes and comments --></note>
 <quantity><!-- 0..1 Quantity The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product) --></quantity>
 <parentDevice><!-- 0..1 Reference(DeviceDefinition) The parent device it can be part of --></parentDevice>
 <material>  <!-- 0..* A substance used to create the material(s) of which the device is made -->
  <substance><!-- 1..1 CodeableConcept The substance --></substance>
  <alternate value="[boolean]"/><!-- 0..1 Indicates an alternative material of the device -->
  <allergenicIndicator value="[boolean]"/><!-- 0..1 Whether the substance is a known or suspected allergen -->
 </material>
</DeviceDefinition>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "DeviceDefinition",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Instance identifier
  "udiDeviceIdentifier" : [{ // Unique Device Identifier (UDI) Barcode string
    "deviceIdentifier" : "<string>", // R!  The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier
    "issuer" : "<uri>", // R!  The organization that assigns the identifier algorithm
    "jurisdiction" : "<uri>" // R!  The jurisdiction to which the deviceIdentifier applies
  }],
  // manufacturer[x]: Name of device manufacturer. One of these 2:
  "manufacturerString" : "<string>",
  "manufacturerReference" : { Reference(Organization) },
  "deviceName" : [{ // A name given to the device to identify it
    "name" : "<string>", // R!  The name of the device
    "type" : "<code>" // R!  udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  }],
  "modelNumber" : "<string>", // The model number for the device
  "type" : { CodeableConcept }, // What kind of device or device system this is
  "specialization" : [{ // The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    "systemType" : "<string>", // R!  The standard that is used to operate and communicate
    "version" : "<string>" // The version of the standard that is used to operate and communicate
  }],
  "version" : ["<string>"], // Available versions
  "safety" : [{ CodeableConcept }], // Safety characteristics of the device
  "shelfLifeStorage" : [{ ProductShelfLife }], // Shelf Life and storage information
  "physicalCharacteristics" : { ProdCharacteristic }, // Dimensions, color etc.
  "languageCode" : [{ CodeableConcept }], // Language code for the human-readable text strings produced by the device (all supported)
  "capability" : [{ // Device capabilities
    "type" : { CodeableConcept }, // R!  Type of capability
    "description" : [{ CodeableConcept }] // Description of capability
  }],
  "property" : [{ // The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    "type" : { CodeableConcept }, // R!  Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    "valueQuantity" : [{ Quantity }], // Property value as a quantity
    "valueCode" : [{ CodeableConcept }] // Property value as a code, e.g., NTP4 (synced to NTP)
  }],
  "owner" : { Reference(Organization) }, // Organization responsible for device
  "contact" : [{ ContactPoint }], // Details for human/organization for support
  "url" : "<uri>", // Network address to contact device
  "onlineInformation" : "<uri>", // Access to on-line information
  "note" : [{ Annotation }], // Device notes and comments
  "quantity" : { Quantity }, // The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product)
  "parentDevice" : { Reference(DeviceDefinition) }, // The parent device it can be part of
  "material" : [{ // A substance used to create the material(s) of which the device is made
    "substance" : { CodeableConcept }, // R!  The substance
    "alternate" : <boolean>, // Indicates an alternative material of the device
    "allergenicIndicator" : <boolean> // Whether the substance is a known or suspected allergen
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:DeviceDefinition;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:DeviceDefinition.identifier [ Identifier ], ... ; # 0..* Instance identifier
  fhir:DeviceDefinition.udiDeviceIdentifier [ # 0..* Unique Device Identifier (UDI) Barcode string
    fhir:DeviceDefinition.udiDeviceIdentifier.deviceIdentifier [ string ]; # 1..1 The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier
    fhir:DeviceDefinition.udiDeviceIdentifier.issuer [ uri ]; # 1..1 The organization that assigns the identifier algorithm
    fhir:DeviceDefinition.udiDeviceIdentifier.jurisdiction [ uri ]; # 1..1 The jurisdiction to which the deviceIdentifier applies
  ], ...;
  # DeviceDefinition.manufacturer[x] : 0..1 Name of device manufacturer. One of these 2
    fhir:DeviceDefinition.manufacturerString [ string ]
    fhir:DeviceDefinition.manufacturerReference [ Reference(Organization) ]
  fhir:DeviceDefinition.deviceName [ # 0..* A name given to the device to identify it
    fhir:DeviceDefinition.deviceName.name [ string ]; # 1..1 The name of the device
    fhir:DeviceDefinition.deviceName.type [ code ]; # 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  ], ...;
  fhir:DeviceDefinition.modelNumber [ string ]; # 0..1 The model number for the device
  fhir:DeviceDefinition.type [ CodeableConcept ]; # 0..1 What kind of device or device system this is
  fhir:DeviceDefinition.specialization [ # 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    fhir:DeviceDefinition.specialization.systemType [ string ]; # 1..1 The standard that is used to operate and communicate
    fhir:DeviceDefinition.specialization.version [ string ]; # 0..1 The version of the standard that is used to operate and communicate
  ], ...;
  fhir:DeviceDefinition.version [ string ], ... ; # 0..* Available versions
  fhir:DeviceDefinition.safety [ CodeableConcept ], ... ; # 0..* Safety characteristics of the device
  fhir:DeviceDefinition.shelfLifeStorage [ ProductShelfLife ], ... ; # 0..* Shelf Life and storage information
  fhir:DeviceDefinition.physicalCharacteristics [ ProdCharacteristic ]; # 0..1 Dimensions, color etc.
  fhir:DeviceDefinition.languageCode [ CodeableConcept ], ... ; # 0..* Language code for the human-readable text strings produced by the device (all supported)
  fhir:DeviceDefinition.capability [ # 0..* Device capabilities
    fhir:DeviceDefinition.capability.type [ CodeableConcept ]; # 1..1 Type of capability
    fhir:DeviceDefinition.capability.description [ CodeableConcept ], ... ; # 0..* Description of capability
  ], ...;
  fhir:DeviceDefinition.property [ # 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    fhir:DeviceDefinition.property.type [ CodeableConcept ]; # 1..1 Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    fhir:DeviceDefinition.property.valueQuantity [ Quantity ], ... ; # 0..* Property value as a quantity
    fhir:DeviceDefinition.property.valueCode [ CodeableConcept ], ... ; # 0..* Property value as a code, e.g., NTP4 (synced to NTP)
  ], ...;
  fhir:DeviceDefinition.owner [ Reference(Organization) ]; # 0..1 Organization responsible for device
  fhir:DeviceDefinition.contact [ ContactPoint ], ... ; # 0..* Details for human/organization for support
  fhir:DeviceDefinition.url [ uri ]; # 0..1 Network address to contact device
  fhir:DeviceDefinition.onlineInformation [ uri ]; # 0..1 Access to on-line information
  fhir:DeviceDefinition.note [ Annotation ], ... ; # 0..* Device notes and comments
  fhir:DeviceDefinition.quantity [ Quantity ]; # 0..1 The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product)
  fhir:DeviceDefinition.parentDevice [ Reference(DeviceDefinition) ]; # 0..1 The parent device it can be part of
  fhir:DeviceDefinition.material [ # 0..* A substance used to create the material(s) of which the device is made
    fhir:DeviceDefinition.material.substance [ CodeableConcept ]; # 1..1 The substance
    fhir:DeviceDefinition.material.alternate [ boolean ]; # 0..1 Indicates an alternative material of the device
    fhir:DeviceDefinition.material.allergenicIndicator [ boolean ]; # 0..1 Whether the substance is a known or suspected allergen
  ], ...;
]
```

**Changes since R3**

This resource did not exist in Release 2

This analysis is available as [XML](devicedefinition.diff.xml) or [JSON](devicedefinition.diff.json).

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [DeviceDefinition](devicedefinition-definitions.html#DeviceDefinition "DeviceDefinition : The characteristics, operational status and capabilities of a medical-related component of a medical device.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | An instance of a medical-related component of a medical device Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](devicedefinition-definitions.html#DeviceDefinition.identifier "DeviceDefinition.identifier : Unique instance identifiers assigned to a device by the software, manufacturers, other organizations or owners. For example: handle ID.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | Instance identifier |
| ... [udiDeviceIdentifier](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier "DeviceDefinition.udiDeviceIdentifier : Unique device identifier (UDI) assigned to device label or package.  Note that the Device may include multiple udiCarriers as it either may include just the udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it could have been sold.") |  | 0..\* | [BackboneElement](backboneelement.html) | Unique Device Identifier (UDI) Barcode string |
| .... [deviceIdentifier](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier.deviceIdentifier "DeviceDefinition.udiDeviceIdentifier.deviceIdentifier : The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier.") |  | 1..1 | [string](datatypes.html#string) | The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier |
| .... [issuer](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier.issuer "DeviceDefinition.udiDeviceIdentifier.issuer : The organization that assigns the identifier algorithm.") |  | 1..1 | [uri](datatypes.html#uri) | The organization that assigns the identifier algorithm |
| .... [jurisdiction](devicedefinition-definitions.html#DeviceDefinition.udiDeviceIdentifier.jurisdiction "DeviceDefinition.udiDeviceIdentifier.jurisdiction : The jurisdiction to which the deviceIdentifier applies.") |  | 1..1 | [uri](datatypes.html#uri) | The jurisdiction to which the deviceIdentifier applies |
| ... [manufacturer[x]](devicedefinition-definitions.html#DeviceDefinition.manufacturer_x_ "DeviceDefinition.manufacturer[x] : A name of the manufacturer.") |  | 0..1 |  | Name of device manufacturer |
| .... manufacturerString |  |  | [string](datatypes.html#string) |  |
| .... manufacturerReference |  |  | [Reference](references.html#Reference)([Organization](organization.html)) |  |
| ... [deviceName](devicedefinition-definitions.html#DeviceDefinition.deviceName "DeviceDefinition.deviceName : A name given to the device to identify it.") |  | 0..\* | [BackboneElement](backboneelement.html) | A name given to the device to identify it |
| .... [name](devicedefinition-definitions.html#DeviceDefinition.deviceName.name "DeviceDefinition.deviceName.name : The name of the device.") |  | 1..1 | [string](datatypes.html#string) | The name of the device |
| .... [type](devicedefinition-definitions.html#DeviceDefinition.deviceName.type "DeviceDefinition.deviceName.type : The type of deviceName. UDILabelName | UserFriendlyName | PatientReportedName | ManufactureDeviceName | ModelName.") |  | 1..1 | [code](datatypes.html#code) | udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other [DeviceNameType](valueset-device-nametype.html "The type of name the device is referred by.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [modelNumber](devicedefinition-definitions.html#DeviceDefinition.modelNumber "DeviceDefinition.modelNumber : The model number for the device.") |  | 0..1 | [string](datatypes.html#string) | The model number for the device |
| ... [type](devicedefinition-definitions.html#DeviceDefinition.type "DeviceDefinition.type : What kind of device or device system this is.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What kind of device or device system this is [FHIR Device Types](valueset-device-kind.html "Type of device e.g. according to official classification.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specialization](devicedefinition-definitions.html#DeviceDefinition.specialization "DeviceDefinition.specialization : The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication.") |  | 0..\* | [BackboneElement](backboneelement.html) | The capabilities supported on a device, the standards to which the device conforms for a particular purpose, and used for the communication |
| .... [systemType](devicedefinition-definitions.html#DeviceDefinition.specialization.systemType "DeviceDefinition.specialization.systemType : The standard that is used to operate and communicate.") |  | 1..1 | [string](datatypes.html#string) | The standard that is used to operate and communicate |
| .... [version](devicedefinition-definitions.html#DeviceDefinition.specialization.version "DeviceDefinition.specialization.version : The version of the standard that is used to operate and communicate.") |  | 0..1 | [string](datatypes.html#string) | The version of the standard that is used to operate and communicate |
| ... [version](devicedefinition-definitions.html#DeviceDefinition.version "DeviceDefinition.version : The available versions of the device, e.g., software versions.") |  | 0..\* | [string](datatypes.html#string) | Available versions |
| ... [safety](devicedefinition-definitions.html#DeviceDefinition.safety "DeviceDefinition.safety : Safety characteristics of the device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Safety characteristics of the device [Device safety](valueset-device-safety.html) ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [shelfLifeStorage](devicedefinition-definitions.html#DeviceDefinition.shelfLifeStorage "DeviceDefinition.shelfLifeStorage : Shelf Life and storage information.") |  | 0..\* | [ProductShelfLife](productshelflife.html#ProductShelfLife) | Shelf Life and storage information |
| ... [physicalCharacteristics](devicedefinition-definitions.html#DeviceDefinition.physicalCharacteristics "DeviceDefinition.physicalCharacteristics : Dimensions, color etc.") |  | 0..1 | [ProdCharacteristic](prodcharacteristic.html#ProdCharacteristic) | Dimensions, color etc. |
| ... [languageCode](devicedefinition-definitions.html#DeviceDefinition.languageCode "DeviceDefinition.languageCode : Language code for the human-readable text strings produced by the device (all supported).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Language code for the human-readable text strings produced by the device (all supported) |
| ... [capability](devicedefinition-definitions.html#DeviceDefinition.capability "DeviceDefinition.capability : Device capabilities.") |  | 0..\* | [BackboneElement](backboneelement.html) | Device capabilities |
| .... [type](devicedefinition-definitions.html#DeviceDefinition.capability.type "DeviceDefinition.capability.type : Type of capability.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of capability |
| .... [description](devicedefinition-definitions.html#DeviceDefinition.capability.description "DeviceDefinition.capability.description : Description of capability.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Description of capability |
| ... [property](devicedefinition-definitions.html#DeviceDefinition.property "DeviceDefinition.property : The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties.") |  | 0..\* | [BackboneElement](backboneelement.html) | The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties |
| .... [type](devicedefinition-definitions.html#DeviceDefinition.property.type "DeviceDefinition.property.type : Code that specifies the property DeviceDefinitionPropetyCode (Extensible).") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Code that specifies the property DeviceDefinitionPropetyCode (Extensible) |
| .... [valueQuantity](devicedefinition-definitions.html#DeviceDefinition.property.valueQuantity "DeviceDefinition.property.valueQuantity : Property value as a quantity.") |  | 0..\* | [Quantity](datatypes.html#Quantity) | Property value as a quantity |
| .... [valueCode](devicedefinition-definitions.html#DeviceDefinition.property.valueCode "DeviceDefinition.property.valueCode : Property value as a code, e.g., NTP4 (synced to NTP).") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Property value as a code, e.g., NTP4 (synced to NTP) |
| ... [owner](devicedefinition-definitions.html#DeviceDefinition.owner "DeviceDefinition.owner : An organization that is responsible for the provision and ongoing maintenance of the device.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for device |
| ... [contact](devicedefinition-definitions.html#DeviceDefinition.contact "DeviceDefinition.contact : Contact details for an organization or a particular human that is responsible for the device.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Details for human/organization for support |
| ... [url](devicedefinition-definitions.html#DeviceDefinition.url "DeviceDefinition.url : A network address on which the device may be contacted directly.") |  | 0..1 | [uri](datatypes.html#uri) | Network address to contact device |
| ... [onlineInformation](devicedefinition-definitions.html#DeviceDefinition.onlineInformation "DeviceDefinition.onlineInformation : Access to on-line information about the device.") |  | 0..1 | [uri](datatypes.html#uri) | Access to on-line information |
| ... [note](devicedefinition-definitions.html#DeviceDefinition.note "DeviceDefinition.note : Descriptive information, usage information or implantation information that is not captured in an existing element.") |  | 0..\* | [Annotation](datatypes.html#Annotation) | Device notes and comments |
| ... [quantity](devicedefinition-definitions.html#DeviceDefinition.quantity "DeviceDefinition.quantity : The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product).") |  | 0..1 | [Quantity](datatypes.html#Quantity) | The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product) |
| ... [parentDevice](devicedefinition-definitions.html#DeviceDefinition.parentDevice "DeviceDefinition.parentDevice : The parent device it can be part of.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([DeviceDefinition](devicedefinition.html)) | The parent device it can be part of |
| ... [material](devicedefinition-definitions.html#DeviceDefinition.material "DeviceDefinition.material : A substance used to create the material(s) of which the device is made.") |  | 0..\* | [BackboneElement](backboneelement.html) | A substance used to create the material(s) of which the device is made |
| .... [substance](devicedefinition-definitions.html#DeviceDefinition.material.substance "DeviceDefinition.material.substance : The substance.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The substance |
| .... [alternate](devicedefinition-definitions.html#DeviceDefinition.material.alternate "DeviceDefinition.material.alternate : Indicates an alternative material of the device.") |  | 0..1 | [boolean](datatypes.html#boolean) | Indicates an alternative material of the device |
| .... [allergenicIndicator](devicedefinition-definitions.html#DeviceDefinition.material.allergenicIndicator "DeviceDefinition.material.allergenicIndicator : Whether the substance is a known or suspected allergen.") |  | 0..1 | [boolean](datatypes.html#boolean) | Whether the substance is a known or suspected allergen |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<DeviceDefinition xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Instance identifier --></identifier>
 <udiDeviceIdentifier>  <!-- 0..* Unique Device Identifier (UDI) Barcode string -->
  <deviceIdentifier value="[string]"/><!-- 1..1 The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier -->
  <issuer value="[uri]"/><!-- 1..1 The organization that assigns the identifier algorithm -->
  <jurisdiction value="[uri]"/><!-- 1..1 The jurisdiction to which the deviceIdentifier applies -->
 </udiDeviceIdentifier>
 <manufacturer[x]><!-- 0..1 string|Reference(Organization) Name of device manufacturer --></manufacturer[x]>
 <deviceName>  <!-- 0..* A name given to the device to identify it -->
  <name value="[string]"/><!-- 1..1 The name of the device -->
  <type value="[code]"/><!-- 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other -->
 </deviceName>
 <modelNumber value="[string]"/><!-- 0..1 The model number for the device -->
 <type><!-- 0..1 CodeableConcept What kind of device or device system this is --></type>
 <specialization>  <!-- 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication -->
  <systemType value="[string]"/><!-- 1..1 The standard that is used to operate and communicate -->
  <version value="[string]"/><!-- 0..1 The version of the standard that is used to operate and communicate -->
 </specialization>
 <version value="[string]"/><!-- 0..* Available versions -->
 <safety><!-- 0..* CodeableConcept Safety characteristics of the device --></safety>
 <shelfLifeStorage><!-- 0..* ProductShelfLife Shelf Life and storage information --></shelfLifeStorage>
 <physicalCharacteristics><!-- 0..1 ProdCharacteristic Dimensions, color etc. --></physicalCharacteristics>
 <languageCode><!-- 0..* CodeableConcept Language code for the human-readable text strings produced by the device (all supported) --></languageCode>
 <capability>  <!-- 0..* Device capabilities -->
  <type><!-- 1..1 CodeableConcept Type of capability --></type>
  <description><!-- 0..* CodeableConcept Description of capability --></description>
 </capability>
 <property>  <!-- 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties -->
  <type><!-- 1..1 CodeableConcept Code that specifies the property DeviceDefinitionPropetyCode (Extensible) --></type>
  <valueQuantity><!-- 0..* Quantity Property value as a quantity --></valueQuantity>
  <valueCode><!-- 0..* CodeableConcept Property value as a code, e.g., NTP4 (synced to NTP) --></valueCode>
 </property>
 <owner><!-- 0..1 Reference(Organization) Organization responsible for device --></owner>
 <contact><!-- 0..* ContactPoint Details for human/organization for support --></contact>
 <url value="[uri]"/><!-- 0..1 Network address to contact device -->
 <onlineInformation value="[uri]"/><!-- 0..1 Access to on-line information -->
 <note><!-- 0..* Annotation Device notes and comments --></note>
 <quantity><!-- 0..1 Quantity The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product) --></quantity>
 <parentDevice><!-- 0..1 Reference(DeviceDefinition) The parent device it can be part of --></parentDevice>
 <material>  <!-- 0..* A substance used to create the material(s) of which the device is made -->
  <substance><!-- 1..1 CodeableConcept The substance --></substance>
  <alternate value="[boolean]"/><!-- 0..1 Indicates an alternative material of the device -->
  <allergenicIndicator value="[boolean]"/><!-- 0..1 Whether the substance is a known or suspected allergen -->
 </material>
</DeviceDefinition>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "DeviceDefinition",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Instance identifier
  "udiDeviceIdentifier" : [{ // Unique Device Identifier (UDI) Barcode string
    "deviceIdentifier" : "<string>", // R!  The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier
    "issuer" : "<uri>", // R!  The organization that assigns the identifier algorithm
    "jurisdiction" : "<uri>" // R!  The jurisdiction to which the deviceIdentifier applies
  }],
  // manufacturer[x]: Name of device manufacturer. One of these 2:
  "manufacturerString" : "<string>",
  "manufacturerReference" : { Reference(Organization) },
  "deviceName" : [{ // A name given to the device to identify it
    "name" : "<string>", // R!  The name of the device
    "type" : "<code>" // R!  udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  }],
  "modelNumber" : "<string>", // The model number for the device
  "type" : { CodeableConcept }, // What kind of device or device system this is
  "specialization" : [{ // The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    "systemType" : "<string>", // R!  The standard that is used to operate and communicate
    "version" : "<string>" // The version of the standard that is used to operate and communicate
  }],
  "version" : ["<string>"], // Available versions
  "safety" : [{ CodeableConcept }], // Safety characteristics of the device
  "shelfLifeStorage" : [{ ProductShelfLife }], // Shelf Life and storage information
  "physicalCharacteristics" : { ProdCharacteristic }, // Dimensions, color etc.
  "languageCode" : [{ CodeableConcept }], // Language code for the human-readable text strings produced by the device (all supported)
  "capability" : [{ // Device capabilities
    "type" : { CodeableConcept }, // R!  Type of capability
    "description" : [{ CodeableConcept }] // Description of capability
  }],
  "property" : [{ // The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    "type" : { CodeableConcept }, // R!  Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    "valueQuantity" : [{ Quantity }], // Property value as a quantity
    "valueCode" : [{ CodeableConcept }] // Property value as a code, e.g., NTP4 (synced to NTP)
  }],
  "owner" : { Reference(Organization) }, // Organization responsible for device
  "contact" : [{ ContactPoint }], // Details for human/organization for support
  "url" : "<uri>", // Network address to contact device
  "onlineInformation" : "<uri>", // Access to on-line information
  "note" : [{ Annotation }], // Device notes and comments
  "quantity" : { Quantity }, // The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product)
  "parentDevice" : { Reference(DeviceDefinition) }, // The parent device it can be part of
  "material" : [{ // A substance used to create the material(s) of which the device is made
    "substance" : { CodeableConcept }, // R!  The substance
    "alternate" : <boolean>, // Indicates an alternative material of the device
    "allergenicIndicator" : <boolean> // Whether the substance is a known or suspected allergen
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:DeviceDefinition;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:DeviceDefinition.identifier [ Identifier ], ... ; # 0..* Instance identifier
  fhir:DeviceDefinition.udiDeviceIdentifier [ # 0..* Unique Device Identifier (UDI) Barcode string
    fhir:DeviceDefinition.udiDeviceIdentifier.deviceIdentifier [ string ]; # 1..1 The identifier that is to be associated with every Device that references this DeviceDefintiion for the issuer and jurisdication porvided in the DeviceDefinition.udiDeviceIdentifier
    fhir:DeviceDefinition.udiDeviceIdentifier.issuer [ uri ]; # 1..1 The organization that assigns the identifier algorithm
    fhir:DeviceDefinition.udiDeviceIdentifier.jurisdiction [ uri ]; # 1..1 The jurisdiction to which the deviceIdentifier applies
  ], ...;
  # DeviceDefinition.manufacturer[x] : 0..1 Name of device manufacturer. One of these 2
    fhir:DeviceDefinition.manufacturerString [ string ]
    fhir:DeviceDefinition.manufacturerReference [ Reference(Organization) ]
  fhir:DeviceDefinition.deviceName [ # 0..* A name given to the device to identify it
    fhir:DeviceDefinition.deviceName.name [ string ]; # 1..1 The name of the device
    fhir:DeviceDefinition.deviceName.type [ code ]; # 1..1 udi-label-name | user-friendly-name | patient-reported-name | manufacturer-name | model-name | other
  ], ...;
  fhir:DeviceDefinition.modelNumber [ string ]; # 0..1 The model number for the device
  fhir:DeviceDefinition.type [ CodeableConcept ]; # 0..1 What kind of device or device system this is
  fhir:DeviceDefinition.specialization [ # 0..* The capabilities supported on a  device, the standards to which the device conforms for a particular purpose, and used for the communication
    fhir:DeviceDefinition.specialization.systemType [ string ]; # 1..1 The standard that is used to operate and communicate
    fhir:DeviceDefinition.specialization.version [ string ]; # 0..1 The version of the standard that is used to operate and communicate
  ], ...;
  fhir:DeviceDefinition.version [ string ], ... ; # 0..* Available versions
  fhir:DeviceDefinition.safety [ CodeableConcept ], ... ; # 0..* Safety characteristics of the device
  fhir:DeviceDefinition.shelfLifeStorage [ ProductShelfLife ], ... ; # 0..* Shelf Life and storage information
  fhir:DeviceDefinition.physicalCharacteristics [ ProdCharacteristic ]; # 0..1 Dimensions, color etc.
  fhir:DeviceDefinition.languageCode [ CodeableConcept ], ... ; # 0..* Language code for the human-readable text strings produced by the device (all supported)
  fhir:DeviceDefinition.capability [ # 0..* Device capabilities
    fhir:DeviceDefinition.capability.type [ CodeableConcept ]; # 1..1 Type of capability
    fhir:DeviceDefinition.capability.description [ CodeableConcept ], ... ; # 0..* Description of capability
  ], ...;
  fhir:DeviceDefinition.property [ # 0..* The actual configuration settings of a device as it actually operates, e.g., regulation status, time properties
    fhir:DeviceDefinition.property.type [ CodeableConcept ]; # 1..1 Code that specifies the property DeviceDefinitionPropetyCode (Extensible)
    fhir:DeviceDefinition.property.valueQuantity [ Quantity ], ... ; # 0..* Property value as a quantity
    fhir:DeviceDefinition.property.valueCode [ CodeableConcept ], ... ; # 0..* Property value as a code, e.g., NTP4 (synced to NTP)
  ], ...;
  fhir:DeviceDefinition.owner [ Reference(Organization) ]; # 0..1 Organization responsible for device
  fhir:DeviceDefinition.contact [ ContactPoint ], ... ; # 0..* Details for human/organization for support
  fhir:DeviceDefinition.url [ uri ]; # 0..1 Network address to contact device
  fhir:DeviceDefinition.onlineInformation [ uri ]; # 0..1 Access to on-line information
  fhir:DeviceDefinition.note [ Annotation ], ... ; # 0..* Device notes and comments
  fhir:DeviceDefinition.quantity [ Quantity ]; # 0..1 The quantity of the device present in the packaging (e.g. the number of devices present in a pack, or the number of devices in the same package of the medicinal product)
  fhir:DeviceDefinition.parentDevice [ Reference(DeviceDefinition) ]; # 0..1 The parent device it can be part of
  fhir:DeviceDefinition.material [ # 0..* A substance used to create the material(s) of which the device is made
    fhir:DeviceDefinition.material.substance [ CodeableConcept ]; # 1..1 The substance
    fhir:DeviceDefinition.material.alternate [ boolean ]; # 0..1 Indicates an alternative material of the device
    fhir:DeviceDefinition.material.allergenicIndicator [ boolean ]; # 0..1 Whether the substance is a known or suspected allergen
  ], ...;
]
```

**Changes since Release 3**

This resource did not exist in Release 2

This analysis is available as [XML](devicedefinition.diff.xml) or [JSON](devicedefinition.diff.json).

See the [Profiles & Extensions](devicedefinition-profiles.html) and the alternate definitions:
Master Definition [XML](devicedefinition.profile.xml.html) + [JSON](devicedefinition.profile.json.html),
[XML](xml.html) [Schema](devicedefinition.xsd)/[Schematron](devicedefinition.sch) + [JSON](json.html)
[Schema](devicedefinition.schema.json.html), [ShEx](devicedefinition.shex.html) (for [Turtle](rdf.html)) + [see the extensions](devicedefinition-profiles.html) & the [dependency analysis](devicedefinition-dependencies.html)

### 8.15.4.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| DeviceDefinition.deviceName.type | The type of name the device is referred by. | [Required](terminologies.html#required) | [DeviceNameType](valueset-device-nametype.html) |
| DeviceDefinition.type | Type of device e.g. according to official classification. | [Example](terminologies.html#example) | [FHIRDeviceTypes](valueset-device-kind.html) |
| DeviceDefinition.safety |  | [Example](terminologies.html#example) | [DeviceSafety](valueset-device-safety.html) |

## 8.15.5 Notes:

## 8.15.6 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| identifier | [token](search.html#token) | The identifier of the component | DeviceDefinition.identifier |  |
| parent | [reference](search.html#reference) | The parent DeviceDefinition resource | DeviceDefinition.parentDevice ([DeviceDefinition](devicedefinition.html)) |  |
| type | [token](search.html#token) | The device component type | DeviceDefinition.type |  |
