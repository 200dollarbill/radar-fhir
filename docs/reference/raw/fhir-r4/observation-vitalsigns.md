---
id: observation-vitalsigns
title: Vital Signs Profile
source_url: https://hl7.org/fhir/R4/observation-vitalsigns.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:53Z'
sha256: 95a6c6f3660d5d56eaeb23bbc3b1677d2d306136fb7f027289d2c206938d00ac
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/observation-vitalsigns.html) **R4** [R3](http://hl7.org/fhir/STU3/observation-vitalsigns.html)

## 10.1.16 observation-vitalsigns

|  |  |  |  |
| --- | --- | --- | --- |
| [Orders and Observations](http://www.hl7.org/Special/committees/orders/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): N/A | [Standards Status](versions.html#levels): Informative |  |

## 10.1.17 Introduction

Vital signs will be one of the first areas where there is a need for a single, global vocabulary to allow for ubiquitous access and re-use. Particularly with the use of wearables by patients where they want to/need to share information from those devices. To meet this need there must be a consistent vocabulary and a common syntax to achieve semantic interoperability. The FHIR Vital Signs profile sets minimum expectations for the Observation resource to record, search and fetch the vital signs associated with a patient that include the primary vital signs plus additional measurements such as height, weight and BMI. Support for basic mandatory searching of resources is defined below in the [Quick Start](#Quick_Start) section. When a FHIR implementation supports any of the vital signs listed below, the implementation **SHALL** conform to this profile for the vital sign observation.

These requirements were originally developed, balloted, and published in FHIR DSTU2 as part of the ONC sponsored [Data Access Framework (DAF) ![](external.png)](http://wiki.siframework.org/Data+Access+Framework+Homepage) project and were subsequently updated to define the minimum mandatory conformance requirements needed for accessing patient data as defined by the [Argonaut ![](external.png)](http://argonautwiki.hl7.org/index.php?title=Main_Page) pilot implementations.

## 10.1.18 Scope and Usage

**Example Usage Scenarios:**

The following are example usage scenarios for this profile:

- Query for vital signs of a particular patient

##### 10.1.18.0.0.1 Mandatory Data Elements and Terminology

The following data-elements are mandatory (i.e. data SHALL be present). These are presented below in a simple human-readable explanation. Profile-specific guidance and valid examples are provided as well. Note that many of the examples capture more than the minimum required. The links to the [**Profile Definitions**](#content) provide the formal views of the profile content, descriptions, mappings and the StructureDefinitions in JSON and XML.

**Each Observation must have:**

1. a status
2. a category code of 'vital-signs'
3. a "magic value" which tells you what is being measured
   - LOINC was chosen for the "magic values" because this aligns with the most countries, but it can be treated as simply a fixed core set of common codes to communicate basic vital signs. Implementers that need to use a different code system can still map accordingly.
4. a patient
5. a time indicating when the measurement was taken
6. a numeric result value and standard UCUM unit which is taken from the Unit Code column in the table below.
   - note: if there is no numeric result then you have to supply a reason

## 10.1.19 Formal View of Profile Content

[Vital Signs Profile](vitalsigns.html) : Link to the formal definition views for the vital signs listed in this table.

- The table below represents a minimum set of vital sign concepts, the required codes ("magic values"), and UCUM units of measure codes used for representing vital signs observations. These are [extensible](terminologies.html#extensible) bindings and require that when a system supports any of these vital signs concepts, they must represent them using these codes. In addition, if you have a blood pressure observation, you must have both a systolic and a diastolic component, though one or both may have dataAbsentReason instead of a value.
- The first column of this table links to the formal views of the individual profile for each vital sign.
- If a more specific code or another code system is recorded or required, implementers must support both the values (LOINC) listed below and the translated code - e.g. method specific LOINC codes, SNOMED CT concepts, system specific (local) codes.
- In addition the implementer may choose to provide alternate codes in addition to the standard codes defined here. The examples illustrate using other codes as translations.
- Other profiles may make rules about which vital sign must be present or must be present as part of a panel or expand the list to include other vital signs. For implementers using LOINC, optional qualifier codes are provided in the notes below.

| Profile Name | "Magic Value" (LOINC) | LOINC Name and Comments | UCUM Unit Code | Examples |
| --- | --- | --- | --- | --- |
| [Vital Signs Panel](vitalspanel.html) | 85353-1 | *Vital signs, weight, height, head circumference, oxygen saturation and BMI panel* - It represent a panel of vital signs listed in this table. All members of the panel are optional and note that querying for the panel may miss individual results that are not part of the actual panel. When used, Observation.valueQuantity is not present; instead, related links (with type=has-member) reference the vital signs observations (e.g. respiratory rate, heart rate, BP, etc.). This code replaces the deprecated code 8716-3 - *Vital signs* which is used in the Argonaut Data Query Implementation Guide. | - | [Vital Signs Panel Example](observation-example-vitals-panel.html) |
| [Respiratory Rate](resprate.html) | 9279-1 | *Respiratory Rate* | /min | [Respiratory Rate Example](observation-example-respiratory-rate.html) |
| [Heart rate](heartrate.html) | 8867-4 | *Heart rate* - To supplement this vital sign observation, 8887-2 - *Heart rate device type* MAY be included as an additional observation. | /min | [Heart Rate Example](observation-example-heart-rate.html) |
| [Oxygen saturation](oxygensat.html) | 2708-6 | *Oxygen saturation in Arterial blood* - This code replaces 59408-5 *Oxygen saturation in Arterial blood by Pulse oximetry* which MAY be included as an additional observation code. | % | [Oxygen Saturation Example](observation-example-satO2.html) |
| [Body temperature](bodytemp.html) | 8310-5 | *Body temperature* - To supplement this vital sign observation, 8327-9 - *Body temperature measurement site* (oral, forehead, rectal, etc.) and 8326-1 -*Type of body temperature device* MAY be used as additional observations. | Cel, [degF] | [Body Temperature Example](observation-example-body-temperature.html) |
| [Body height](bodyheight.html) | 8302-2 | *Body height* - To supplement this vital sign observation, 8306-3 -*Body height - lying* (i.e., body length - typically used for infants) MAY be included as an additional observation code. | cm, [in\_i] | [Body height Example](observation-example-body-height.html) |
| [Head circumference](headcircum.html) | 9843-4 | *Head Occipital-frontal circumference* | cm, [in\_i] | [Head Circumference Example](observation-example-head-circumference.html) |
| [Body weight](bodyweight.html) | 29463-7 | *Body weight* - To supplement this vital sign observation, 8352-7 - *Clothing worn during measure* and 8361-8 - *Body position with respect to gravity* MAY be included as additional observation codes. | g, kg,[lb\_av] | [Body Weight Example](observation-example.html) |
| [Body mass index](bmi.html) | 39156-5 | *Body mass index (BMI) [Ratio]* | kg/m2 | [Body Mass Example](observation-example-bmi.html) |
| [Blood pressure systolic and diastolic](bp.html) | 85354-9 | *Blood pressure panel with all children optional* - This is a component observation. It has no value in Observation.valueQuantity and contains at least one component (systolic and/or diastolic). To supplement this vital sign observation, 8478-0 - *Mean blood pressure*, 8357-6 - *Blood pressure method*, 41904-4 - *Blood pressure measurement site*, 8358-4 - *Blood pressure device cuff size*, 41901-0 - *Type of blood pressure device* MAY be used as additional observations. | - | [Blood Pressure Example](observation-example-bloodpressure.html),  [Blood Pressure Example with missing Diastolic measurement](observation-example-bloodpressure-dar.html) |
| [Systolic blood pressure](bp.html) | 8480-6 | *Systolic blood pressure* - Observation.component code for a blood pressure Observation | mm[Hg] | [Blood Pressure Example](observation-example-bloodpressure.html) |
| [Diastolic blood pressure](bp.html) | 8462-4 | *Diastolic blood pressure* - Observation.component code for a blood pressure Observation | mm[Hg] | [Blood Pressure Example](observation-example-bloodpressure.html) |

## 10.1.20 Quick Start

Below is an overview of required search and read operations

**Clients**

- A client has connected to a server and fetched all of a patient's vital signs by searching by category using `GET [base]/Observation?patient=[id]&category=vital-signs`.
- A client has connected to a server and fetched all of a patient's vital signs searching by category code and date range using `GET [base]/Observation?patient=[id]&category=vital-signs&date=[date]{&date=[date]}`.
- A client has connected to a server and fetched any of a patient's vital signs by searching by one or more of the codes listed above using `GET [base]/Observation?patient=[id]&code[vital sign LOINC{,LOINC2,LOINC3,...}]`.

- A client **SHOULD** be capable of connecting to a server and fetching any of a patient's vital signs searching by one or more of the codes listed above and date range using `GET [base]/Observation?patient=[id]&code=[LOINC{,LOINC2...}]vital-signs&date=[date]{&date=[date]}`.

**Servers**

- A server is capable of returning all of a patient's vital signs that it supports using `GET [base]/Observation?patient=[id]&category=vital-signs`.
- A server is capable of returning all of a patient's vital signs queried by date range using `GET [base]/Observation?patient=[id]&category=vital-signs&date=[date]{&date=[date]}`.
- A server is capable of returning any of a patient's vital signs queried by one or more of the codes listed above using `GET [base]/Observation?patient=[id]&code[vital sign LOINC{,LOINC2,LOINC3,...}]`.

- A server **SHOULD** be capable of returning any of a patient's vital signs queried by one or more of the codes listed above and date range using `GET [base]/Observation?patient=[id]&code=[LOINC{,LOINC2...}]vital-signs&date=[date]{&date=[date]}`.

- A server has ensured that every API request includes a valid Authorization token, supplied via:Authorization: Bearer {server-specific-token-here}
- A server has rejected any unauthorized requests by returning an HTTP 401 Unauthorized response code.

---

#### 10.1.20.0.1 GET [base]/Observation?patient=[id]&category=vital-signs

**Example:**
Search for all Vital Signs measurements for a patient

[GET [base]/Observation?patient=1186747&category=vital-signs](#.html)

*Support:* Mandatory to support search by category code.

*Implementation Notes:* Search based on vital sign category code. This search fetches a bundle of all Observation resources with category 'vital-signs' for the specified patient [(how to search by reference)](search.html#reference) and [(how to search by token)](search.html#token). The table above is the minimum set, additional vital signs are allowed.

*Response Class:*

- (Status 200): successful operation
- (Status 400): invalid parameter
- (Status 401/4xx): unauthorized request
- (Status 403): insufficient scope

---

#### 10.1.20.0.2 GET [base]/Observation?patient=[id]&code=[vital sign LOINC{,LOINC2,LOINC3,...}]

**Example:**
Search for all heart rate observations for a patient:

[GET [base]/Observation?patient=1186747&code=8867-4](#.html)

**Example:**
Search for all heart rate, respiratory rate and blood pressure observations for a patient:

[GET [base]/Observation?patient=1186747&code=8867-4,9279-1,85354-9](#.html)

*Support:* Mandatory to support search by vital sign LOINC(s) listed above.

*Implementation Notes:* 1)Search based on vital sign LOINC code(s). This fetches a bundle of all Observation resources for specific vital sign(s) listed in the table above for the specified patient [(how to search by reference)](search.html#reference) and [how to search by token)]. 2) The "code" parameter searches only `Observation.code`. For example when fetching blood pressures the resource will be only be returned when the search is based on 85354-9(Systolic and Diastolic BP). Using the component codes 8480-6(Systolic BP) or 8462-4 (Diastolic BP) will not return the resource . In order to search both `Observation.code` and `Observation.component.code` in a single query, use the "combo-code" search parameter.

*Response Class:*

- (Status 200): successful operation
- (Status 400): invalid parameter
- (Status 401/4xx): unauthorized request
- (Status 403): insufficient scope

---

#### 10.1.20.0.3 GET [base]/Observation?patient=[id]&category=vital-signs&date=[date]{&date=[date]}

**Example:**
Find all the blood pressures after 2015-01-14

[GET [base]/Observation?patient=555580&code=85354-9&date=ge2015-01-14](#.hml)

*Support:* Mandatory to support search by category code and date

*Implementation Notes:* Search based on vital sign category code and date. This fetches a bundle of all Observation resources with category 'vital-signs' for the specified patient for a specified time period [(how to search by reference)](search.html#reference) and [(how to search by token)](search.html#token).

*Response Class:*

- (Status 200): successful operation
- (Status 400): invalid parameter
- (Status 401/4xx): unauthorized request
- (Status 403): insufficient scope

### 10.1.20.1 Content

|  |  |
| --- | --- |
| **Profiles**: | |
| [VitalSigns](vitalsigns.html) | FHIR Vital Signs Profile |
