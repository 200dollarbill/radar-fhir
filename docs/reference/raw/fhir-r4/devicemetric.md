---
id: devicemetric
title: DeviceMetric
source_url: https://hl7.org/fhir/R4/devicemetric.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:00Z'
sha256: 79a0dced74ee336ae7d7ffc92c8a51a0f5eeb2b66c5b6db985e633fcd3c50480
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/devicemetric.html) [R4B](http://hl7.org/fhir/R4B/devicemetric.html) **R4** [R3](http://hl7.org/fhir/STU3/devicemetric.html) [R2](http://hl7.org/fhir/DSTU2/devicemetric.html)

- [Content](#)
- [Examples](devicemetric-examples.html)
- [Detailed Descriptions](devicemetric-definitions.html)
- [Mappings](devicemetric-mappings.html)
- [Profiles & Extensions](devicemetric-profiles.html)
- [R3 Conversions](devicemetric-version-maps.html)

# 8.16 Resource DeviceMetric - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Health Care Devices](http://www.hl7.org/Special/committees/healthcaredevices/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 1 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Anonymous | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

Describes a measurement, calculation or setting capability of a medical device.

## 8.16.1 Scope and Usage

The DeviceMetric resource describes mandatory static properties that characterize a direct or derived, quantitative or qualitative biosignal measurement, setting, or calculation produced by a medical device.
The DeviceMetric resource can also be used to describe the non-static but highly relevant properties to the metric such as metric status, metric last calibration time and type, measurement mode, color, reference link to the parent DeviceComponent to where it belongs, and any capabilities that the metric offers (for example: setting the metric label).

Note:

For the initial scope, this DeviceMetric resource is only applicable to describe a single metric node in the containment tree that is produced by the context scanner in any medical device that implements or derives from the ISO/IEEE 11073 standard.

## 8.16.2 Boundaries and Relationships

There are two related resources

- [Device](device.html) - The physical device that this DeviceMetric belongs to.

This resource is referenced by [Media](media.html#Media) and [Observation](observation.html#Observation)

## 8.16.3 Resource Content

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
| .. [DeviceMetric](devicemetric-definitions.html#DeviceMetric "DeviceMetric : Describes a measurement, calculation or setting capability of a medical device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Measurement, calculation or setting capability of a medical device Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](devicemetric-definitions.html#DeviceMetric.identifier "DeviceMetric.identifier : Unique instance identifiers assigned to a device by the device or gateway software, manufacturers, other organizations or owners. For example: handle ID.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Instance identifier |
| ... [type](devicemetric-definitions.html#DeviceMetric.type "DeviceMetric.type : Describes the type of the metric. For example: Heart Rate, PEEP Setting, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Identity of metric, for example Heart Rate or PEEP Setting [Device Metric and Component Types](valueset-devicemetric-type.html "Describes the metric type.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [unit](devicemetric-definitions.html#DeviceMetric.unit "DeviceMetric.unit : Describes the unit that an observed value determined for this metric will have. For example: Percent, Seconds, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Unit of Measure for the Metric [Device Metric and Component Types](valueset-devicemetric-type.html "Describes the unit of the metric.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [source](devicemetric-definitions.html#DeviceMetric.source "DeviceMetric.source : Describes the link to the  Device that this DeviceMetric belongs to and that contains administrative device information such as manufacturer, serial number, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Device](device.html)) | Describes the link to the source Device |
| ... [parent](devicemetric-definitions.html#DeviceMetric.parent "DeviceMetric.parent : Describes the link to the  Device that this DeviceMetric belongs to and that provide information about the location of this DeviceMetric in the containment structure of the parent Device. An example would be a Device that represents a Channel. This reference can be used by a client application to distinguish DeviceMetrics that have the same type, but should be interpreted based on their containment location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Device](device.html)) | Describes the link to the parent Device |
| ... [operationalStatus](devicemetric-definitions.html#DeviceMetric.operationalStatus "DeviceMetric.operationalStatus : Indicates current operational state of the device. For example: On, Off, Standby, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | on | off | standby | entered-in-error [DeviceMetricOperationalStatus](valueset-metric-operational-status.html "Describes the operational status of the DeviceMetric.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [color](devicemetric-definitions.html#DeviceMetric.color "DeviceMetric.color : Describes the color representation for the metric. This is often used to aid clinicians to track and identify parameter types by color. In practice, consider a Patient Monitor that has ECG/HR and Pleth for example; the parameters are displayed in different characteristic colors, such as HR-blue, BP-green, and PR and SpO2- magenta.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | black | red | green | yellow | blue | magenta | cyan | white [DeviceMetricColor](valueset-metric-color.html "Describes the typical color of representation.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [category](devicemetric-definitions.html#DeviceMetric.category "DeviceMetric.category : Indicates the category of the observation generation process. A DeviceMetric can be for example a setting, measurement, or calculation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | measurement | setting | calculation | unspecified [DeviceMetricCategory](valueset-metric-category.html "Describes the category of the metric.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [measurementPeriod](devicemetric-definitions.html#DeviceMetric.measurementPeriod "DeviceMetric.measurementPeriod : Describes the measurement repetition time. This is not necessarily the same as the update period. The measurement repetition time can range from milliseconds up to hours. An example for a measurement repetition time in the range of milliseconds is the sampling rate of an ECG. An example for a measurement repetition time in the range of hours is a NIBP that is triggered automatically every hour. The update period may be different than the measurement repetition time, if the device does not update the published observed value with the same frequency as it was measured.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Timing](datatypes.html#Timing) | Describes the measurement repetition time |
| ... [calibration](devicemetric-definitions.html#DeviceMetric.calibration "DeviceMetric.calibration : Describes the calibrations that have been performed or that are required to be performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Describes the calibrations that have been performed or that are required to be performed |
| .... [type](devicemetric-definitions.html#DeviceMetric.calibration.type "DeviceMetric.calibration.type : Describes the type of the calibration method.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | unspecified | offset | gain | two-point [DeviceMetricCalibrationType](valueset-metric-calibration-type.html "Describes the type of a metric calibration.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [state](devicemetric-definitions.html#DeviceMetric.calibration.state "DeviceMetric.calibration.state : Describes the state of the calibration.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | not-calibrated | calibration-required | calibrated | unspecified [DeviceMetricCalibrationState](valueset-metric-calibration-state.html "Describes the state of a metric calibration.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [time](devicemetric-definitions.html#DeviceMetric.calibration.time "DeviceMetric.calibration.time : Describes the time last calibration has been performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [instant](datatypes.html#instant) | Describes the time last calibration has been performed |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<DeviceMetric xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Instance identifier --></identifier>
 <type><!-- 1..1 CodeableConcept Identity of metric, for example Heart Rate or PEEP Setting --></type>
 <unit><!-- 0..1 CodeableConcept Unit of Measure for the Metric --></unit>
 <source><!-- 0..1 Reference(Device) Describes the link to the source Device --></source>
 <parent><!-- 0..1 Reference(Device) Describes the link to the parent Device --></parent>
 <operationalStatus value="[code]"/><!-- 0..1 on | off | standby | entered-in-error -->
 <color value="[code]"/><!-- 0..1 black | red | green | yellow | blue | magenta | cyan | white -->
 <category value="[code]"/><!-- 1..1 measurement | setting | calculation | unspecified -->
 <measurementPeriod><!-- 0..1 Timing Describes the measurement repetition time --></measurementPeriod>
 <calibration>  <!-- 0..* Describes the calibrations that have been performed or that are required to be performed -->
  <type value="[code]"/><!-- 0..1 unspecified | offset | gain | two-point -->
  <state value="[code]"/><!-- 0..1 not-calibrated | calibration-required | calibrated | unspecified -->
  <time value="[instant]"/><!-- 0..1 Describes the time last calibration has been performed -->
 </calibration>
</DeviceMetric>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "DeviceMetric",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Instance identifier
  "type" : { CodeableConcept }, // R!  Identity of metric, for example Heart Rate or PEEP Setting
  "unit" : { CodeableConcept }, // Unit of Measure for the Metric
  "source" : { Reference(Device) }, // Describes the link to the source Device
  "parent" : { Reference(Device) }, // Describes the link to the parent Device
  "operationalStatus" : "<code>", // on | off | standby | entered-in-error
  "color" : "<code>", // black | red | green | yellow | blue | magenta | cyan | white
  "category" : "<code>", // R!  measurement | setting | calculation | unspecified
  "measurementPeriod" : { Timing }, // Describes the measurement repetition time
  "calibration" : [{ // Describes the calibrations that have been performed or that are required to be performed
    "type" : "<code>", // unspecified | offset | gain | two-point
    "state" : "<code>", // not-calibrated | calibration-required | calibrated | unspecified
    "time" : "<instant>" // Describes the time last calibration has been performed
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:DeviceMetric;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:DeviceMetric.identifier [ Identifier ], ... ; # 0..* Instance identifier
  fhir:DeviceMetric.type [ CodeableConcept ]; # 1..1 Identity of metric, for example Heart Rate or PEEP Setting
  fhir:DeviceMetric.unit [ CodeableConcept ]; # 0..1 Unit of Measure for the Metric
  fhir:DeviceMetric.source [ Reference(Device) ]; # 0..1 Describes the link to the source Device
  fhir:DeviceMetric.parent [ Reference(Device) ]; # 0..1 Describes the link to the parent Device
  fhir:DeviceMetric.operationalStatus [ code ]; # 0..1 on | off | standby | entered-in-error
  fhir:DeviceMetric.color [ code ]; # 0..1 black | red | green | yellow | blue | magenta | cyan | white
  fhir:DeviceMetric.category [ code ]; # 1..1 measurement | setting | calculation | unspecified
  fhir:DeviceMetric.measurementPeriod [ Timing ]; # 0..1 Describes the measurement repetition time
  fhir:DeviceMetric.calibration [ # 0..* Describes the calibrations that have been performed or that are required to be performed
    fhir:DeviceMetric.calibration.type [ code ]; # 0..1 unspecified | offset | gain | two-point
    fhir:DeviceMetric.calibration.state [ code ]; # 0..1 not-calibrated | calibration-required | calibrated | unspecified
    fhir:DeviceMetric.calibration.time [ instant ]; # 0..1 Describes the time last calibration has been performed
  ], ...;
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [DeviceMetric](devicemetric.html#DeviceMetric) |  |
| DeviceMetric.identifier | - Min Cardinality changed from 1 to 0 - Max Cardinality changed from 1 to \* |
| DeviceMetric.parent | - Type Reference: Added Target Type Device - Type Reference: Removed Target Type DeviceComponent |
| DeviceMetric.operationalStatus | - Change value set from http://hl7.org/fhir/ValueSet/metric-operational-status to http://hl7.org/fhir/ValueSet/metric-operational-status|4.0.1 |
| DeviceMetric.color | - Change value set from http://hl7.org/fhir/ValueSet/metric-color to http://hl7.org/fhir/ValueSet/metric-color|4.0.1 |
| DeviceMetric.category | - Change value set from http://hl7.org/fhir/ValueSet/metric-category to http://hl7.org/fhir/ValueSet/metric-category|4.0.1 |
| DeviceMetric.calibration.type | - Change value set from http://hl7.org/fhir/ValueSet/metric-calibration-type to http://hl7.org/fhir/ValueSet/metric-calibration-type|4.0.1 |
| DeviceMetric.calibration.state | - Change value set from http://hl7.org/fhir/ValueSet/metric-calibration-state to http://hl7.org/fhir/ValueSet/metric-calibration-state|4.0.1 |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](devicemetric.diff.xml) or [JSON](devicemetric.diff.json).

See [R3 <--> R4 Conversion Maps](devicemetric-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [DeviceMetric](devicemetric-definitions.html#DeviceMetric "DeviceMetric : Describes a measurement, calculation or setting capability of a medical device.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Measurement, calculation or setting capability of a medical device Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](devicemetric-definitions.html#DeviceMetric.identifier "DeviceMetric.identifier : Unique instance identifiers assigned to a device by the device or gateway software, manufacturers, other organizations or owners. For example: handle ID.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Instance identifier |
| ... [type](devicemetric-definitions.html#DeviceMetric.type "DeviceMetric.type : Describes the type of the metric. For example: Heart Rate, PEEP Setting, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Identity of metric, for example Heart Rate or PEEP Setting [Device Metric and Component Types](valueset-devicemetric-type.html "Describes the metric type.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [unit](devicemetric-definitions.html#DeviceMetric.unit "DeviceMetric.unit : Describes the unit that an observed value determined for this metric will have. For example: Percent, Seconds, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Unit of Measure for the Metric [Device Metric and Component Types](valueset-devicemetric-type.html "Describes the unit of the metric.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [source](devicemetric-definitions.html#DeviceMetric.source "DeviceMetric.source : Describes the link to the  Device that this DeviceMetric belongs to and that contains administrative device information such as manufacturer, serial number, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Device](device.html)) | Describes the link to the source Device |
| ... [parent](devicemetric-definitions.html#DeviceMetric.parent "DeviceMetric.parent : Describes the link to the  Device that this DeviceMetric belongs to and that provide information about the location of this DeviceMetric in the containment structure of the parent Device. An example would be a Device that represents a Channel. This reference can be used by a client application to distinguish DeviceMetrics that have the same type, but should be interpreted based on their containment location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Device](device.html)) | Describes the link to the parent Device |
| ... [operationalStatus](devicemetric-definitions.html#DeviceMetric.operationalStatus "DeviceMetric.operationalStatus : Indicates current operational state of the device. For example: On, Off, Standby, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | on | off | standby | entered-in-error [DeviceMetricOperationalStatus](valueset-metric-operational-status.html "Describes the operational status of the DeviceMetric.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [color](devicemetric-definitions.html#DeviceMetric.color "DeviceMetric.color : Describes the color representation for the metric. This is often used to aid clinicians to track and identify parameter types by color. In practice, consider a Patient Monitor that has ECG/HR and Pleth for example; the parameters are displayed in different characteristic colors, such as HR-blue, BP-green, and PR and SpO2- magenta.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | black | red | green | yellow | blue | magenta | cyan | white [DeviceMetricColor](valueset-metric-color.html "Describes the typical color of representation.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [category](devicemetric-definitions.html#DeviceMetric.category "DeviceMetric.category : Indicates the category of the observation generation process. A DeviceMetric can be for example a setting, measurement, or calculation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | measurement | setting | calculation | unspecified [DeviceMetricCategory](valueset-metric-category.html "Describes the category of the metric.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [measurementPeriod](devicemetric-definitions.html#DeviceMetric.measurementPeriod "DeviceMetric.measurementPeriod : Describes the measurement repetition time. This is not necessarily the same as the update period. The measurement repetition time can range from milliseconds up to hours. An example for a measurement repetition time in the range of milliseconds is the sampling rate of an ECG. An example for a measurement repetition time in the range of hours is a NIBP that is triggered automatically every hour. The update period may be different than the measurement repetition time, if the device does not update the published observed value with the same frequency as it was measured.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Timing](datatypes.html#Timing) | Describes the measurement repetition time |
| ... [calibration](devicemetric-definitions.html#DeviceMetric.calibration "DeviceMetric.calibration : Describes the calibrations that have been performed or that are required to be performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Describes the calibrations that have been performed or that are required to be performed |
| .... [type](devicemetric-definitions.html#DeviceMetric.calibration.type "DeviceMetric.calibration.type : Describes the type of the calibration method.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | unspecified | offset | gain | two-point [DeviceMetricCalibrationType](valueset-metric-calibration-type.html "Describes the type of a metric calibration.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [state](devicemetric-definitions.html#DeviceMetric.calibration.state "DeviceMetric.calibration.state : Describes the state of the calibration.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | not-calibrated | calibration-required | calibrated | unspecified [DeviceMetricCalibrationState](valueset-metric-calibration-state.html "Describes the state of a metric calibration.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [time](devicemetric-definitions.html#DeviceMetric.calibration.time "DeviceMetric.calibration.time : Describes the time last calibration has been performed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [instant](datatypes.html#instant) | Describes the time last calibration has been performed |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<DeviceMetric xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Instance identifier --></identifier>
 <type><!-- 1..1 CodeableConcept Identity of metric, for example Heart Rate or PEEP Setting --></type>
 <unit><!-- 0..1 CodeableConcept Unit of Measure for the Metric --></unit>
 <source><!-- 0..1 Reference(Device) Describes the link to the source Device --></source>
 <parent><!-- 0..1 Reference(Device) Describes the link to the parent Device --></parent>
 <operationalStatus value="[code]"/><!-- 0..1 on | off | standby | entered-in-error -->
 <color value="[code]"/><!-- 0..1 black | red | green | yellow | blue | magenta | cyan | white -->
 <category value="[code]"/><!-- 1..1 measurement | setting | calculation | unspecified -->
 <measurementPeriod><!-- 0..1 Timing Describes the measurement repetition time --></measurementPeriod>
 <calibration>  <!-- 0..* Describes the calibrations that have been performed or that are required to be performed -->
  <type value="[code]"/><!-- 0..1 unspecified | offset | gain | two-point -->
  <state value="[code]"/><!-- 0..1 not-calibrated | calibration-required | calibrated | unspecified -->
  <time value="[instant]"/><!-- 0..1 Describes the time last calibration has been performed -->
 </calibration>
</DeviceMetric>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "DeviceMetric",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Instance identifier
  "type" : { CodeableConcept }, // R!  Identity of metric, for example Heart Rate or PEEP Setting
  "unit" : { CodeableConcept }, // Unit of Measure for the Metric
  "source" : { Reference(Device) }, // Describes the link to the source Device
  "parent" : { Reference(Device) }, // Describes the link to the parent Device
  "operationalStatus" : "<code>", // on | off | standby | entered-in-error
  "color" : "<code>", // black | red | green | yellow | blue | magenta | cyan | white
  "category" : "<code>", // R!  measurement | setting | calculation | unspecified
  "measurementPeriod" : { Timing }, // Describes the measurement repetition time
  "calibration" : [{ // Describes the calibrations that have been performed or that are required to be performed
    "type" : "<code>", // unspecified | offset | gain | two-point
    "state" : "<code>", // not-calibrated | calibration-required | calibrated | unspecified
    "time" : "<instant>" // Describes the time last calibration has been performed
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:DeviceMetric;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:DeviceMetric.identifier [ Identifier ], ... ; # 0..* Instance identifier
  fhir:DeviceMetric.type [ CodeableConcept ]; # 1..1 Identity of metric, for example Heart Rate or PEEP Setting
  fhir:DeviceMetric.unit [ CodeableConcept ]; # 0..1 Unit of Measure for the Metric
  fhir:DeviceMetric.source [ Reference(Device) ]; # 0..1 Describes the link to the source Device
  fhir:DeviceMetric.parent [ Reference(Device) ]; # 0..1 Describes the link to the parent Device
  fhir:DeviceMetric.operationalStatus [ code ]; # 0..1 on | off | standby | entered-in-error
  fhir:DeviceMetric.color [ code ]; # 0..1 black | red | green | yellow | blue | magenta | cyan | white
  fhir:DeviceMetric.category [ code ]; # 1..1 measurement | setting | calculation | unspecified
  fhir:DeviceMetric.measurementPeriod [ Timing ]; # 0..1 Describes the measurement repetition time
  fhir:DeviceMetric.calibration [ # 0..* Describes the calibrations that have been performed or that are required to be performed
    fhir:DeviceMetric.calibration.type [ code ]; # 0..1 unspecified | offset | gain | two-point
    fhir:DeviceMetric.calibration.state [ code ]; # 0..1 not-calibrated | calibration-required | calibrated | unspecified
    fhir:DeviceMetric.calibration.time [ instant ]; # 0..1 Describes the time last calibration has been performed
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [DeviceMetric](devicemetric.html#DeviceMetric) |  |
| DeviceMetric.identifier | - Min Cardinality changed from 1 to 0 - Max Cardinality changed from 1 to \* |
| DeviceMetric.parent | - Type Reference: Added Target Type Device - Type Reference: Removed Target Type DeviceComponent |
| DeviceMetric.operationalStatus | - Change value set from http://hl7.org/fhir/ValueSet/metric-operational-status to http://hl7.org/fhir/ValueSet/metric-operational-status|4.0.1 |
| DeviceMetric.color | - Change value set from http://hl7.org/fhir/ValueSet/metric-color to http://hl7.org/fhir/ValueSet/metric-color|4.0.1 |
| DeviceMetric.category | - Change value set from http://hl7.org/fhir/ValueSet/metric-category to http://hl7.org/fhir/ValueSet/metric-category|4.0.1 |
| DeviceMetric.calibration.type | - Change value set from http://hl7.org/fhir/ValueSet/metric-calibration-type to http://hl7.org/fhir/ValueSet/metric-calibration-type|4.0.1 |
| DeviceMetric.calibration.state | - Change value set from http://hl7.org/fhir/ValueSet/metric-calibration-state to http://hl7.org/fhir/ValueSet/metric-calibration-state|4.0.1 |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](devicemetric.diff.xml) or [JSON](devicemetric.diff.json).

See [R3 <--> R4 Conversion Maps](devicemetric-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

See the [Profiles & Extensions](devicemetric-profiles.html) and the alternate definitions:
Master Definition [XML](devicemetric.profile.xml.html) + [JSON](devicemetric.profile.json.html),
[XML](xml.html) [Schema](devicemetric.xsd)/[Schematron](devicemetric.sch) + [JSON](json.html)
[Schema](devicemetric.schema.json.html), [ShEx](devicemetric.shex.html) (for [Turtle](rdf.html)) + [see the extensions](devicemetric-profiles.html) & the [dependency analysis](devicemetric-dependencies.html)

### 8.16.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| DeviceMetric.type | Describes the metric type. | [Preferred](terminologies.html#preferred) | [DeviceMetricAndComponentTypes](valueset-devicemetric-type.html) |
| DeviceMetric.unit | Describes the unit of the metric. | [Preferred](terminologies.html#preferred) | [DeviceMetricAndComponentTypes](valueset-devicemetric-type.html) |
| DeviceMetric.operationalStatus | Describes the operational status of the DeviceMetric. | [Required](terminologies.html#required) | [DeviceMetricOperationalStatus](valueset-metric-operational-status.html) |
| DeviceMetric.color | Describes the typical color of representation. | [Required](terminologies.html#required) | [DeviceMetricColor](valueset-metric-color.html) |
| DeviceMetric.category | Describes the category of the metric. | [Required](terminologies.html#required) | [DeviceMetricCategory](valueset-metric-category.html) |
| DeviceMetric.calibration.type | Describes the type of a metric calibration. | [Required](terminologies.html#required) | [DeviceMetricCalibrationType](valueset-metric-calibration-type.html) |
| DeviceMetric.calibration.state | Describes the state of a metric calibration. | [Required](terminologies.html#required) | [DeviceMetricCalibrationState](valueset-metric-calibration-state.html) |

## 8.16.4 Notes:

- The correct codes for the metric types are registered in
  the [RTM Management service ![](external.png)](https://rtmms.nist.gov), but
  this is not required. See [Terminology
  Systems](terminologies-systems.html#urn:iso:std:iso:11073:10101) for the correct representation of these codes in a [Coding](datatypes.html#Coding) data type.

## 8.16.5 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| category | [token](search.html#token) | The category of the metric | DeviceMetric.category |  |
| identifier | [token](search.html#token) | The identifier of the metric | DeviceMetric.identifier |  |
| parent | [reference](search.html#reference) | The parent DeviceMetric resource | DeviceMetric.parent ([Device](device.html)) |  |
| source | [reference](search.html#reference) | The device resource | DeviceMetric.source ([Device](device.html)) |  |
| type | [token](search.html#token) | The component type | DeviceMetric.type |  |
