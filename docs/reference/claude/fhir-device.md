# FHIR R4 — Device, DeviceMetric, DeviceDefinition

Purpose: `Device` is "a type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity" — the *administrative* resource for a physical device instance (Trial Use, maturity 2, security category Business, no compartments). `DeviceDefinition` is the "catalog" definition of a *kind* of device (Trial Use, maturity 0, Anonymous). `DeviceMetric` "describes a measurement, calculation or setting capability of a medical device" (Trial Use, maturity 1, Anonymous). Flags: `Σ` summary, `?!` modifier, `TU` trial use.

## How the three relate (as the pages state)
| Resource | Role stated on the page |
|---|---|
| Device | Tracks "individual instances of a device and their location"; referenced by other resources "for recording which device performed an action such as a procedure or an observation"; carries UDI; "does not change much and has manufacturer information etc." Physical composition = Devices pointing to their `parent` |
| DeviceDefinition | "Describes a 'kind' of device - not a physical instance", a "catalog entry" authored by manufacturer, reseller, regulator, or a local definition; allows hierarchical configurations via `parentDevice`. Has no lot number / patient / location |
| DeviceMetric | "Models the physical part, including operation status and is much more volatile"; describes "mandatory static properties that characterize a direct or derived, quantitative or qualitative biosignal measurement, setting, or calculation produced by a medical device" plus non-static properties (status, calibration, colour). Initial scope: a single metric node of an ISO/IEEE 11073 containment tree |

Devices differ from medications because they are not "used up"; implanted devices must not be represented with Medication.

## Device — elements
Root `Device` (TU) is a DomainResource.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Device.identifier` |  | 0..* | Identifier | Instance identifier |
| `Device.definition` |  | 0..1 | Reference(DeviceDefinition) | The reference to the definition for the device |
| `Device.udiCarrier` | Σ | 0..* | BackboneElement | Unique Device Identifier (UDI) Barcode string |
| `Device.udiCarrier.deviceIdentifier` | Σ | 0..1 | string | Mandatory fixed portion of UDI |
| `Device.udiCarrier.issuer` |  | 0..1 | uri | UDI Issuing Organization |
| `Device.udiCarrier.jurisdiction` |  | 0..1 | uri | Regional UDI authority |
| `Device.udiCarrier.carrierAIDC` | Σ | 0..1 | base64Binary | UDI Machine Readable Barcode String |
| `Device.udiCarrier.carrierHRF` | Σ | 0..1 | string | UDI Human Readable Barcode String |
| `Device.udiCarrier.entryType` |  | 0..1 | code | barcode \| rfid \| manual +; UDIEntryType (Required) |
| `Device.status` | ?!Σ | 0..1 | code | active \| inactive \| entered-in-error \| unknown; FHIRDeviceStatus (Required) |
| `Device.statusReason` |  | 0..* | CodeableConcept | online \| paused \| standby \| offline \| not-ready \| transduc-discon \| hw-discon \| off; FHIRDeviceStatusReason (Extensible) |
| `Device.distinctIdentifier` |  | 0..1 | string | The distinct identification string |
| `Device.manufacturer` |  | 0..1 | string | Name of device manufacturer |
| `Device.manufactureDate` |  | 0..1 | dateTime | Date when the device was made |
| `Device.expirationDate` |  | 0..1 | dateTime | Date and time of expiry of this device (if applicable) |
| `Device.lotNumber` |  | 0..1 | string | Lot number of manufacture |
| `Device.serialNumber` |  | 0..1 | string | Serial number assigned by the manufacturer |
| `Device.deviceName` |  | 0..* | BackboneElement | The name of the device as given by the manufacturer |
| `Device.deviceName.name` |  | 1..1 | string | The name of the device |
| `Device.deviceName.type` |  | 1..1 | code | udi-label-name \| user-friendly-name \| patient-reported-name \| manufacturer-name \| model-name \| other; DeviceNameType (Required) |
| `Device.modelNumber` |  | 0..1 | string | The model number for the device |
| `Device.partNumber` |  | 0..1 | string | The part number of the device |
| `Device.type` |  | 0..1 | CodeableConcept | The kind or type of device; Device Type (Example) |
| `Device.specialization` |  | 0..* | BackboneElement | Capabilities supported / standards the device conforms to, used for communication |
| `Device.specialization.systemType` |  | 1..1 | CodeableConcept | The standard that is used to operate and communicate |
| `Device.specialization.version` |  | 0..1 | string | The version of the standard |
| `Device.version` |  | 0..* | BackboneElement | The actual design of the device or software version running on the device |
| `Device.version.type` |  | 0..1 | CodeableConcept | The type of the device version |
| `Device.version.component` |  | 0..1 | Identifier | A single component of the device version |
| `Device.version.value` |  | 1..1 | string | The version text |
| `Device.property` |  | 0..* | BackboneElement | Actual configuration settings as it operates, e.g., regulation status, time properties |
| `Device.property.type` |  | 1..1 | CodeableConcept | Code that specifies the property; DeviceDefinitionPropetyCode (Extensible) (sic) |
| `Device.property.valueQuantity` |  | 0..* | Quantity | Property value as a quantity |
| `Device.property.valueCode` |  | 0..* | CodeableConcept | Property value as a code, e.g., NTP4 (synced to NTP) |
| `Device.patient` |  | 0..1 | Reference(Patient) | Patient to whom Device is affixed |
| `Device.owner` |  | 0..1 | Reference(Organization) | Organization responsible for device |
| `Device.contact` |  | 0..* | ContactPoint | Details for human/organization for support |
| `Device.location` |  | 0..1 | Reference(Location) | Where the device is found |
| `Device.url` |  | 0..1 | uri | Network address to contact device |
| `Device.note` |  | 0..* | Annotation | Device notes and comments |
| `Device.safety` | Σ | 0..* | CodeableConcept | Safety Characteristics of Device |
| `Device.parent` |  | 0..1 | Reference(Device) | The parent device |

Bindings: `udiCarrier.entryType` Required UDIEntryType; `status` Required FHIRDeviceStatus; `statusReason` Extensible FHIRDeviceStatusReason; `deviceName.type` Required DeviceNameType; `type` Example DeviceType.

Notes on the page: `identifier` is *only* for an actual identifier of a specific instance (serial-numbered devices); reference/catalog numbers or GTIN describe a *kind* and go in `type` (code sources: SNOMED CT — the example binding, GMDN, RTM). UDI = Device Identifier (DI) + Production Identifier(s) (PI); "UDI carrier" = full barcode string; where a UDI is assigned, lot/expiry etc. SHALL be consistent with the UDI string; best practice transmits both the carrier and all parsed components.

### Device — search parameters
| Name | Type | Expression |
|---|---|---|
| identifier | token | `Device.identifier` |
| location | reference | `Device.location` (Location) |
| manufacturer | string | `Device.manufacturer` |
| model | string | `Device.modelNumber` |
| organization | reference | `Device.owner` (Organization) |
| patient | reference | `Device.patient` (Patient) |
| status | token | `Device.status` — active \| inactive \| entered-in-error \| unknown |
| type | token | `Device.type` |
| udi-carrier | string | `Device.udiCarrier.carrierHRF` (UDI barcode string in HRF format) |
| udi-di | string | `Device.udiCarrier.deviceIdentifier` |
| url | uri | `Device.url` |

## DeviceMetric — elements
Root `DeviceMetric` (ΣTU) is a DomainResource.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `DeviceMetric.identifier` | Σ | 0..* | Identifier | Instance identifier |
| `DeviceMetric.type` | Σ | 1..1 | CodeableConcept | Identity of metric, for example Heart Rate or PEEP Setting; Device Metric and Component Types (Preferred) |
| `DeviceMetric.unit` | Σ | 0..1 | CodeableConcept | Unit of Measure for the Metric; Device Metric and Component Types (Preferred) |
| `DeviceMetric.source` | Σ | 0..1 | Reference(Device) | Describes the link to the source Device |
| `DeviceMetric.parent` | Σ | 0..1 | Reference(Device) | Describes the link to the parent Device |
| `DeviceMetric.operationalStatus` | Σ | 0..1 | code | on \| off \| standby \| entered-in-error; DeviceMetricOperationalStatus (Required) |
| `DeviceMetric.color` | Σ | 0..1 | code | black \| red \| green \| yellow \| blue \| magenta \| cyan \| white; DeviceMetricColor (Required) |
| `DeviceMetric.category` | Σ | 1..1 | code | measurement \| setting \| calculation \| unspecified; DeviceMetricCategory (Required) |
| `DeviceMetric.measurementPeriod` | Σ | 0..1 | Timing | Describes the measurement repetition time |
| `DeviceMetric.calibration` | Σ | 0..* | BackboneElement | Calibrations performed or required |
| `DeviceMetric.calibration.type` | Σ | 0..1 | code | unspecified \| offset \| gain \| two-point; DeviceMetricCalibrationType (Required) |
| `DeviceMetric.calibration.state` | Σ | 0..1 | code | not-calibrated \| calibration-required \| calibrated \| unspecified; DeviceMetricCalibrationState (Required) |
| `DeviceMetric.calibration.time` | Σ | 0..1 | instant | Time last calibration has been performed |

Page note: correct codes for metric types are registered in the RTM Management service "but this is not required"; see Terminology Systems for `urn:iso:std:iso:11073:10101` in a Coding.

### DeviceMetric — search parameters
| Name | Type | Expression |
|---|---|---|
| identifier | token | `DeviceMetric.identifier` |
| parent | reference | `DeviceMetric.parent` (Device) |
| source | reference | `DeviceMetric.source` (Device) |
| type | token | `DeviceMetric.type` |

## DeviceDefinition — elements
Root `DeviceDefinition` (TU) is a DomainResource: "The characteristics, operational status and capabilities of a medical-related component of a medical device."

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `DeviceDefinition.identifier` |  | 0..* | Identifier | Instance identifier |
| `DeviceDefinition.udiDeviceIdentifier` |  | 0..* | BackboneElement | Unique Device Identifier (UDI) Barcode string |
| `DeviceDefinition.udiDeviceIdentifier.deviceIdentifier` |  | 1..1 | string | Identifier associated with every Device referencing this definition, for the issuer and jurisdiction given |
| `DeviceDefinition.udiDeviceIdentifier.issuer` |  | 1..1 | uri | The organization that assigns the identifier algorithm |
| `DeviceDefinition.udiDeviceIdentifier.jurisdiction` |  | 1..1 | uri | The jurisdiction to which the deviceIdentifier applies |
| `DeviceDefinition.manufacturer[x]` |  | 0..1 | string \| Reference(Organization) | Name of device manufacturer (`manufacturerString`, `manufacturerReference`) |
| `DeviceDefinition.deviceName` |  | 0..* | BackboneElement | A name given to the device to identify it |
| `DeviceDefinition.deviceName.name` |  | 1..1 | string | The name of the device |
| `DeviceDefinition.deviceName.type` |  | 1..1 | code | udi-label-name \| user-friendly-name \| patient-reported-name \| manufacturer-name \| model-name \| other; DeviceNameType (Required) |
| `DeviceDefinition.modelNumber` |  | 0..1 | string | The model number for the device |
| `DeviceDefinition.type` |  | 0..1 | CodeableConcept | What kind of device or device system this is; FHIR Device Types (Example) |
| `DeviceDefinition.specialization` |  | 0..* | BackboneElement | Capabilities / standards the device conforms to |
| `DeviceDefinition.specialization.systemType` |  | 1..1 | string | The standard that is used to operate and communicate |
| `DeviceDefinition.specialization.version` |  | 0..1 | string | The version of the standard |
| `DeviceDefinition.version` |  | 0..* | string | Available versions |
| `DeviceDefinition.safety` | Σ | 0..* | CodeableConcept | Safety characteristics of the device; Device safety (Example) |
| `DeviceDefinition.shelfLifeStorage` |  | 0..* | ProductShelfLife | Shelf Life and storage information |
| `DeviceDefinition.physicalCharacteristics` |  | 0..1 | ProdCharacteristic | Dimensions, color etc. |
| `DeviceDefinition.languageCode` |  | 0..* | CodeableConcept | Language code for the human-readable text strings produced by the device (all supported) |
| `DeviceDefinition.capability` |  | 0..* | BackboneElement | Device capabilities |
| `DeviceDefinition.capability.type` |  | 1..1 | CodeableConcept | Type of capability |
| `DeviceDefinition.capability.description` |  | 0..* | CodeableConcept | Description of capability |
| `DeviceDefinition.property` |  | 0..* | BackboneElement | Actual configuration settings as it operates |
| `DeviceDefinition.property.type` |  | 1..1 | CodeableConcept | Code that specifies the property; DeviceDefinitionPropetyCode (Extensible) (sic) |
| `DeviceDefinition.property.valueQuantity` |  | 0..* | Quantity | Property value as a quantity |
| `DeviceDefinition.property.valueCode` |  | 0..* | CodeableConcept | Property value as a code, e.g., NTP4 (synced to NTP) |
| `DeviceDefinition.owner` |  | 0..1 | Reference(Organization) | Organization responsible for device |
| `DeviceDefinition.contact` |  | 0..* | ContactPoint | Details for human/organization for support |
| `DeviceDefinition.url` |  | 0..1 | uri | Network address to contact device |
| `DeviceDefinition.onlineInformation` |  | 0..1 | uri | Access to on-line information |
| `DeviceDefinition.note` |  | 0..* | Annotation | Device notes and comments |
| `DeviceDefinition.quantity` |  | 0..1 | Quantity | Quantity of the device present in the packaging |
| `DeviceDefinition.parentDevice` | Σ | 0..1 | Reference(DeviceDefinition) | The parent device it can be part of |
| `DeviceDefinition.material` |  | 0..* | BackboneElement | A substance used to create the material(s) of which the device is made |
| `DeviceDefinition.material.substance` |  | 1..1 | CodeableConcept | The substance |
| `DeviceDefinition.material.alternate` |  | 0..1 | boolean | Indicates an alternative material of the device |
| `DeviceDefinition.material.allergenicIndicator` |  | 0..1 | boolean | Whether the substance is a known or suspected allergen |

Bindings: `deviceName.type` Required DeviceNameType; `type` Example FHIRDeviceTypes; `safety` Example DeviceSafety. The page's Notes section is empty.

### DeviceDefinition — search parameters
| Name | Type | Expression |
|---|---|---|
| parent | reference | `DeviceDefinition.parentDevice` (DeviceDefinition) |
| type | token | `DeviceDefinition.type` |

## Invariants / constraints
- None printed on any of the three pages (no Constraints table was scraped for Device, DeviceMetric or DeviceDefinition).

## Relationships
- Device references: DeviceDefinition (`definition`), Patient (`patient`), Organization (`owner`), Location (`location`), Device (`parent`).
- Device referenced by: Signature, Account, AdverseEvent, Appointment, AppointmentResponse, AuditEvent, CarePlan, CatalogEntry, ChargeItem, ChargeItemDefinition, Claim, Communication, CommunicationRequest, Composition, Consent, Contract, DetectedIssue, itself, DeviceMetric, DeviceRequest, DeviceUseStatement, DiagnosticReport, DocumentManifest, DocumentReference, ExplanationOfBenefit, Flag, Group, GuidanceResponse, ImagingStudy, Invoice, List, MeasureReport, Media, MedicationAdministration, MedicationDispense, MedicationRequest, MessageHeader, MolecularSequence, Observation, Procedure, Provenance, QuestionnaireResponse, RequestGroup, RiskAssessment, Schedule, ServiceRequest, Specimen, SupplyDelivery, SupplyRequest and Task.
- DeviceMetric references: Device (`source`, `parent`). Referenced by: Media and Observation.
- DeviceDefinition references: Organization (`manufacturerReference`, `owner`), DeviceDefinition (`parentDevice`). Referenced by: Device, itself, MedicinalProductPackaged and MedicinalProductPharmaceutical.

## Notes for our server
- No Device element is mandatory in base R4 (every top-level element is 0..1 / 0..*), so our Device profile must add the constraints itself: at least `identifier` (serial-numbered instance — `identifier` is *only* for instance identifiers), `type` (kind of device; the catalog/GTIN-style code belongs here, not in `identifier`), `status` (Required binding: active | inactive | entered-in-error | unknown), `deviceName` (`name` and `type` are 1..1 inside it), `manufacturer`, `modelNumber`, `serialNumber`, `patient` or `owner`/`location`.
- `Device.status` is a modifier element (`?!`) — treat `entered-in-error` devices as excluded from normal listings, mirroring Observation.status handling.
- `Observation.device` may point at `Device` or `DeviceMetric`; `DeviceMetric.type` (1..1) and `category` (1..1, e.g. `measurement`) plus `unit` and `source = Device/…` are what a per-channel description (heart rate, SpO2) needs if we go beyond a single Device reference. Base-profile decision: reference `Device` from Observations, optionally one `DeviceMetric` per measured vital sign.
- `DeviceDefinition` is the catalog entry (`udiDeviceIdentifier.*` all 1..1 inside it; `deviceName`, `modelNumber`, `type`); a Device instance links to it via `Device.definition`. Only worth serving if we model more than one device model; otherwise `Device.type` + `manufacturer` + `modelNumber` suffice.
- Search: index `identifier`, `patient`, `organization`, `location`, `status`, `type`, `manufacturer`/`model` (string), `udi-di`/`udi-carrier` (string, not token) and `url` (uri); for DeviceMetric `source`/`parent`/`type`; for DeviceDefinition `parent`/`type`.
- Security categories: Device is Business, DeviceMetric/DeviceDefinition Anonymous, none are in a compartment — so `Patient/[id]/Device` compartment search is *not* defined; use `Device?patient=[id]` instead. Access control for patient-linked devices must key off `Device.patient` explicitly.
- SATUSEHAT has no Device profile page in our raw set; treat these R4 tables as the base for the new profile and cross-check against fhir-profiling.md's checklist.

## Sources
- raw/fhir-r4/device.md
- raw/fhir-r4/devicemetric.md
- raw/fhir-r4/devicedefinition.md
