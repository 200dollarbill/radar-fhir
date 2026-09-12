---
id: capabilitystatement
title: CapabilityStatement
source_url: https://hl7.org/fhir/R4/capabilitystatement.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:10Z'
sha256: 5debf69f978a1573491eb43a7686486289a92574dee35a2b4034b1713d0ba41b
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/capabilitystatement.html) [R4B](http://hl7.org/fhir/R4B/capabilitystatement.html) **R4** [R3](http://hl7.org/fhir/STU3/capabilitystatement.html)

- [Content](#)
- [Examples](capabilitystatement-examples.html)
- [Detailed Descriptions](capabilitystatement-definitions.html)
- [Mappings](capabilitystatement-mappings.html)
- [Profiles & Extensions](capabilitystatement-profiles.html)
- [Operations](capabilitystatement-operations.html)
- [R3 Conversions](capabilitystatement-version-maps.html)

# 5.2 Resource CapabilityStatement - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) | [Normative](versions.html#std-process "Standard Status") (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Anonymous | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Conformance](ansi-conformance.html) Package for further details. |

A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.

## 5.2.1 Scope and Usage

The capability statement is a key part of the overall conformance framework in FHIR.
It is used as a statement of the features of actual software, or of a set of
rules for an application to provide. This statement connects to all the detailed
statements of functionality, such as [StructureDefinitions](structuredefinition.html)
and [ValueSets](valueset.html). This composite statement of application
capability may be used for system compatibility testing, code generation, or as
the basis for a conformance assessment. For further information about Conformance
testing, see [Conformance Rules](conformance-rules.html) and
[Profiling FHIR](profiling.html).

Specifically, capability statements are used in one of three ways:

|  |  |
| --- | --- |
| [Instance](#instance) | `implementation` must be present and `software` may be present |
| [Capability](#capability) | `implementation` must be absent, `software` must be present |
| [Requirements](#requirements) | `implementation` and `software` must be absent |

### 5.2.1.1 Instance: Describe an actual implementation

In this scenario, the capability statement describes the capabilities of a deployed
and configured solution available at a particular access point or set of access points.
The statement describes exactly how to interface with that deployed solution and thus
provides for a degree of self-configuration of software solutions.

This is the type of
statement that FHIR restful solutions are expected to make available on invocation of the
*capabilities* operation. It is also the type of statement that forms a basis for
the testing, certification or commissioning of specific software installations.

### 5.2.1.2 Capability: Describe software solution capabilities

In this scenario, the capability statement describes generic capabilities of a
software application or component solution. The solution might be available for
purchase or other acquisition and might be deployed and configured at any number of
independent sites. Because it is not dependent on any particular implementation, the
profile cannot provide specific details such as endpoint addresses. It may also need
to document various configurations in which the application can be set up or describe
the degree of customizability associated with the solution.

This type of statement may be used as a marketing tool by software and system
developers to formally describe their capabilities. It can also be used as the basis
for conformance testing of software solutions independent of a particular installation.

### 5.2.1.3 Requirements: Describe a desired solution

In this scenario, the capability statement describes the capabilities of a desired
system. It might be used as part of an architectural design process to document
needed system capabilities, or might be used as part of an RFP process to formally
document the requirements of a requested solution and to document the criteria by
which proposals will be evaluated.

These three types of profiles can be used together. A requirements statement can
be compared against the solution statements proffered by respondents to an RFP. A
solution statement for a software package forms the starting point for the implementation
statement associated with a particular installation of that software package.

CapabilityStatements of type "requirement" describe what capabilities are potentially relevant;
additional documentation or extensions (see [capabilitystatement-expectation](extension-capabilitystatement-expectation.html)) within the
CapabilityStatement are expected to make more explicit statements of degree of expectation
associated with each capability.

## 5.2.2 Background and Context

Capability Statements provide for a degree of automatic configuration and adaptation.
However, capturing absolutely every variation that could impact the interoperability of
two systems, let alone keeping that detailed information up-to-date as systems evolve
through maintenance and upgrades, is rarely practical. Therefore, capability statements
should be seen as an interim step. They provide a degree of automation. However, they
also provide a great deal of human-readable content that can minimize the need for direct
communication between the operators of the systems being configured to interoperate.

### 5.2.2.1 Supporting Multiple Versions

Applications may implement multiple versions. If they do, then a `CapabilityStatement`
describes the system's support for a particular version of FHIR, and the system will have multiple
statements, one for each version it supports. For further information, see [Managing
Multiple Versions](versioning.html), and the [$versions](capabilitystatement-operation-versions.html) operation.

### 5.2.2.2 Mixed Normative Content

While the core of the `CapabilityStatement` resource is [Normative](versions.html#std-process),
many of the flags that indicate exactly how the system operates are marked as `trial-use`. Roughly,
the portions of the resource that correspond to [OpenAPI document ![](external.png)](https://github.com/OAI/OpenAPI-Specification) elements
are normative.

Applications looking for normative stability should only use the normative parts of the
resource, and not populate or ignore the portions labelled trial-use. To assist with this, clients
can ask for the server to return a 'Normative content only' CapabilityStatement using the [mode parameter
on `/metadata`](http.html#capabilities).

Community discussion regarding more capable, efficient and computable representations of
an applications capabilities may lead to change to the trial-use parts of this resource or the creation of new
resources and/or functionality in future versions of this specification.

This resource is referenced by itself and [TestScript](testscript.html#TestScript)

## 5.2.3 Resource Content

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
| .. [CapabilityStatement](capabilitystatement-definitions.html#CapabilityStatement "CapabilityStatement : A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | A statement of system capabilities + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation + Rule: A Capability Statement SHALL have at least one of REST, messaging or document element. + Rule: A Capability Statement SHALL have at least one of description, software, or implementation element. + Rule: Messaging end-point is required (and is only permitted) when a statement is for an implementation. + Rule: The set of documents must be unique by the combination of profile and mode. + Rule: If kind = instance, implementation must be present and software may be present + Rule: If kind = capability, implementation must be absent, software must be present + Rule: If kind = requirements, implementation and software must be absent Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](capabilitystatement-definitions.html#CapabilityStatement.url "CapabilityStatement.url : An absolute URI that is used to identify this capability statement when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this capability statement is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the capability statement is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Canonical identifier for this capability statement, represented as a URI (globally unique) |
| ... [version](capabilitystatement-definitions.html#CapabilityStatement.version "CapabilityStatement.version : The identifier that is used to identify this version of the capability statement when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the capability statement author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the capability statement |
| ... [name](capabilitystatement-definitions.html#CapabilityStatement.name "CapabilityStatement.name : A natural language name identifying the capability statement. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name for this capability statement (computer friendly) |
| ... [title](capabilitystatement-definitions.html#CapabilityStatement.title "CapabilityStatement.title : A short, descriptive, user-friendly title for the capability statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this capability statement (human friendly) |
| ... [status](capabilitystatement-definitions.html#CapabilityStatement.status "CapabilityStatement.status : The status of this capability statement. Enables tracking the life-cycle of the content.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](capabilitystatement-definitions.html#CapabilityStatement.experimental "CapabilityStatement.experimental : A Boolean value to indicate that this capability statement is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](capabilitystatement-definitions.html#CapabilityStatement.date "CapabilityStatement.date : The date  (and optionally time) when the capability statement was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the capability statement changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](capabilitystatement-definitions.html#CapabilityStatement.publisher "CapabilityStatement.publisher : The name of the organization or individual that published the capability statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](capabilitystatement-definitions.html#CapabilityStatement.contact "CapabilityStatement.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](capabilitystatement-definitions.html#CapabilityStatement.description "CapabilityStatement.description : A free text natural language description of the capability statement from a consumer's perspective. Typically, this is used when the capability statement describes a desired rather than an actual solution, for example as a formal expression of requirements as part of an RFP.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the capability statement |
| ... [useContext](capabilitystatement-definitions.html#CapabilityStatement.useContext "CapabilityStatement.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate capability statement instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](capabilitystatement-definitions.html#CapabilityStatement.jurisdiction "CapabilityStatement.jurisdiction : A legal or geographic region in which the capability statement is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for capability statement (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [purpose](capabilitystatement-definitions.html#CapabilityStatement.purpose "CapabilityStatement.purpose : Explanation of why this capability statement is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this capability statement is defined |
| ... [copyright](capabilitystatement-definitions.html#CapabilityStatement.copyright "CapabilityStatement.copyright : A copyright statement relating to the capability statement and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the capability statement.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [kind](capabilitystatement-definitions.html#CapabilityStatement.kind "CapabilityStatement.kind : The way that this statement is intended to be used, to describe an actual running instance of software, a particular product (kind, not instance of software) or a class of implementation (e.g. a desired purchase).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [code](datatypes.html#code) | instance | capability | requirements [CapabilityStatementKind](valueset-capability-statement-kind.html "How a capability statement is intended to be used.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [instantiates](capabilitystatement-definitions.html#CapabilityStatement.instantiates "CapabilityStatement.instantiates : Reference to a canonical URL of another CapabilityStatement that this software implements. This capability statement is a published API description that corresponds to a business service. The server may actually implement a subset of the capability statement it claims to implement, so the capability statement must specify the full capability details.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([CapabilityStatement](capabilitystatement.html)) | Canonical URL of another capability statement this implements |
| ... [imports](capabilitystatement-definitions.html#CapabilityStatement.imports "CapabilityStatement.imports : Reference to a canonical URL of another CapabilityStatement that this software adds to. The capability statement automatically includes everything in the other statement, and it is not duplicated, though the server may repeat the same resources, interactions and operations to add additional details to them.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [canonical](datatypes.html#canonical)([CapabilityStatement](capabilitystatement.html)) | Canonical URL of another capability statement this adds to |
| ... [software](capabilitystatement-definitions.html#CapabilityStatement.software "CapabilityStatement.software : Software that is covered by this capability statement.  It is used when the capability statement describes the capabilities of a particular software version, independent of an installation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Software that is covered by this capability statement |
| .... [name](capabilitystatement-definitions.html#CapabilityStatement.software.name "CapabilityStatement.software.name : Name the software is known by.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | A name the software is known by |
| .... [version](capabilitystatement-definitions.html#CapabilityStatement.software.version "CapabilityStatement.software.version : The version identifier for the software covered by this statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Version covered by this statement |
| .... [releaseDate](capabilitystatement-definitions.html#CapabilityStatement.software.releaseDate "CapabilityStatement.software.releaseDate : Date this version of the software was released.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date this version was released |
| ... [implementation](capabilitystatement-definitions.html#CapabilityStatement.implementation "CapabilityStatement.implementation : Identifies a specific implementation instance that is described by the capability statement - i.e. a particular installation, rather than the capabilities of a software program.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | If this describes a specific instance |
| .... [description](capabilitystatement-definitions.html#CapabilityStatement.implementation.description "CapabilityStatement.implementation.description : Information about the specific installation that this capability statement relates to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Describes this specific instance |
| .... [url](capabilitystatement-definitions.html#CapabilityStatement.implementation.url "CapabilityStatement.implementation.url : An absolute base URL for the implementation.  This forms the base for REST interfaces as well as the mailbox and document interfaces.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [url](datatypes.html#url) | Base URL for the installation |
| .... [custodian](capabilitystatement-definitions.html#CapabilityStatement.implementation.custodian "CapabilityStatement.implementation.custodian : The organization responsible for the management of the instance and oversight of the data on the server at the specified URL.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that manages the data |
| ... [fhirVersion](capabilitystatement-definitions.html#CapabilityStatement.fhirVersion "CapabilityStatement.fhirVersion : The version of the FHIR specification that this CapabilityStatement describes (which SHALL be the same as the FHIR version of the CapabilityStatement itself). There is no default value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | FHIR Version the system supports [FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [format](capabilitystatement-definitions.html#CapabilityStatement.format "CapabilityStatement.format : A list of the formats supported by this implementation using their content types.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..\* | [code](datatypes.html#code) | formats supported (xml | json | ttl | mime type) [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [patchFormat](capabilitystatement-definitions.html#CapabilityStatement.patchFormat "CapabilityStatement.patchFormat : A list of the patch formats supported by this implementation using their content types.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | Patch formats supported [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [implementationGuide](capabilitystatement-definitions.html#CapabilityStatement.implementationGuide "CapabilityStatement.implementationGuide : A list of implementation guides that the server does (or should) support in their entirety.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([ImplementationGuide](implementationguide.html)) | Implementation guides supported |
| ... [rest](capabilitystatement-definitions.html#CapabilityStatement.rest "CapabilityStatement.rest : A definition of the restful capabilities of the solution, if any.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | If the endpoint is a RESTful one + Rule: A given resource can only be described once per RESTful mode. |
| .... [mode](capabilitystatement-definitions.html#CapabilityStatement.rest.mode "CapabilityStatement.rest.mode : Identifies whether this portion of the statement is describing the ability to initiate or receive restful operations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | client | server [RestfulCapabilityMode](valueset-restful-capability-mode.html "The mode of a RESTful capability statement.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.documentation "CapabilityStatement.rest.documentation : Information about the system's restful capabilities that apply across all applications, such as security.") |  | 0..1 | [markdown](datatypes.html#markdown) | General description of implementation |
| .... [security](capabilitystatement-definitions.html#CapabilityStatement.rest.security "CapabilityStatement.rest.security : Information about security implementation from an interface perspective - what a client needs to know.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [BackboneElement](backboneelement.html) | Information about security of implementation |
| ..... [cors](capabilitystatement-definitions.html#CapabilityStatement.rest.security.cors "CapabilityStatement.rest.security.cors : Server adds CORS headers when responding to requests - this enables Javascript applications to use the server.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Adds CORS Headers (http://enable-cors.org/) |
| ..... [service](capabilitystatement-definitions.html#CapabilityStatement.rest.security.service "CapabilityStatement.rest.security.service : Types of security services that are supported/required by the system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates [RestfulSecurityService](valueset-restful-security-service.html "Types of security services used with FHIR.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ..... [description](capabilitystatement-definitions.html#CapabilityStatement.rest.security.description "CapabilityStatement.rest.security.description : General description of how security works.") |  | 0..1 | [markdown](datatypes.html#markdown) | General description of how security works |
| .... [resource](capabilitystatement-definitions.html#CapabilityStatement.rest.resource "CapabilityStatement.rest.resource : A specification of the restful capabilities of the solution for a specific resource type.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Resource served on the REST interface + Rule: Search parameter names must be unique in the context of a resource. |
| ..... [type](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.type "CapabilityStatement.rest.resource.type : A type of resource exposed via the restful interface.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | A resource type that is supported [ResourceType](valueset-resource-types.html "One of the resource types defined as part of this version of FHIR.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [profile](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.profile "CapabilityStatement.rest.resource.profile : A specification of the profile that describes the solution's overall support for the resource, including any constraints on cardinality, bindings, lengths or other limitations. See further discussion in [Using Profiles](profiling.html#profile-uses).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Base System profile for all uses of resource |
| ..... [supportedProfile](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.supportedProfile "CapabilityStatement.rest.resource.supportedProfile : A list of profiles that represent different use cases supported by the system. For a server, \"supported by the system\" means the system hosts/produces a set of resources that are conformant to a particular profile, and allows clients that use its services to search using this profile and to find appropriate data. For a client, it means the system will search by this profile and process data according to the guidance implicit in the profile. See further discussion in [Using Profiles](profiling.html#profile-uses).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Profiles for use cases supported |
| ..... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.documentation "CapabilityStatement.rest.resource.documentation : Additional information about the resource type used by the system.") |  | 0..1 | [markdown](datatypes.html#markdown) | Additional information about the use of the resource type |
| ..... [interaction](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.interaction "CapabilityStatement.rest.resource.interaction : Identifies a restful operation supported by the solution.") |  | 0..\* | [BackboneElement](backboneelement.html) | What operations are supported? |
| ...... [code](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.interaction.code "CapabilityStatement.rest.resource.interaction.code : Coded identifier of the operation, supported by the system resource.") |  | 1..1 | [code](datatypes.html#code) | read | vread | update | patch | delete | history-instance | history-type | create | search-type [TypeRestfulInteraction](valueset-type-restful-interaction.html "Operations supported by REST at the type or instance level.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ...... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.interaction.documentation "CapabilityStatement.rest.resource.interaction.documentation : Guidance specific to the implementation of this operation, such as 'delete is a logical delete' or 'updates are only allowed with version id' or 'creates permitted from pre-authorized certificates only'.") |  | 0..1 | [markdown](datatypes.html#markdown) | Anything special about operation behavior |
| ..... [versioning](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.versioning "CapabilityStatement.rest.resource.versioning : This field is set to no-version to specify that the system does not support (server) or use (client) versioning for this resource type. If this has some other value, the server must at least correctly track and populate the versionId meta-property on resources. If the value is 'versioned-update', then the server supports all the versioning features, including using e-tags for version integrity in the API.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [code](datatypes.html#code) | no-version | versioned | versioned-update [ResourceVersionPolicy](valueset-versioning-policy.html "How the system supports versioning for a resource.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [readHistory](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.readHistory "CapabilityStatement.rest.resource.readHistory : A flag for whether the server is able to return past versions as part of the vRead operation.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | Whether vRead can return past versions |
| ..... [updateCreate](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate "CapabilityStatement.rest.resource.updateCreate : A flag to indicate that the server allows or needs to allow the client to create new identities on the server (that is, the client PUTs to a location where there is no existing resource). Allowing this operation means that the server allows the client to create new identities on the server.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If update can commit to a new identity |
| ..... [conditionalCreate](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalCreate "CapabilityStatement.rest.resource.conditionalCreate : A flag that indicates that the server supports conditional create.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If allows/uses conditional create |
| ..... [conditionalRead](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalRead "CapabilityStatement.rest.resource.conditionalRead : A code that indicates how the server supports conditional read.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [code](datatypes.html#code) | not-supported | modified-since | not-match | full-support [ConditionalReadStatus](valueset-conditional-read-status.html "A code that indicates how the server supports conditional read.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [conditionalUpdate](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalUpdate "CapabilityStatement.rest.resource.conditionalUpdate : A flag that indicates that the server supports conditional update.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If allows/uses conditional update |
| ..... [conditionalDelete](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalDelete "CapabilityStatement.rest.resource.conditionalDelete : A code that indicates how the server supports conditional delete.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [code](datatypes.html#code) | not-supported | single | multiple - how conditional delete is supported [ConditionalDeleteStatus](valueset-conditional-delete-status.html "A code that indicates how the server supports conditional delete.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [referencePolicy](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.referencePolicy "CapabilityStatement.rest.resource.referencePolicy : A set of flags that defines how references are supported.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [code](datatypes.html#code) | literal | logical | resolves | enforced | local [ReferenceHandlingPolicy](valueset-reference-handling-policy.html "A set of flags that defines how references are supported.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [searchInclude](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchInclude "CapabilityStatement.rest.resource.searchInclude : A list of _include values supported by the server.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [string](datatypes.html#string) | \_include values supported by the server |
| ..... [searchRevInclude](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchRevInclude "CapabilityStatement.rest.resource.searchRevInclude : A list of _revinclude (reverse include) values supported by the server.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [string](datatypes.html#string) | \_revinclude values supported by the server |
| ..... [searchParam](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam "CapabilityStatement.rest.resource.searchParam : Search parameters for implementations to support and/or make use of - either references to ones defined in the specification, or additional ones defined for/by the implementation.") |  | 0..\* | [BackboneElement](backboneelement.html) | Search parameters supported by implementation |
| ...... [name](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.name "CapabilityStatement.rest.resource.searchParam.name : The name of the search parameter used in the interface.") |  | 1..1 | [string](datatypes.html#string) | Name of search parameter |
| ...... [definition](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.definition "CapabilityStatement.rest.resource.searchParam.definition : An absolute URI that is a formal reference to where this parameter was first defined, so that a client can be confident of the meaning of the search parameter (a reference to [[[SearchParameter.url]]]). This element SHALL be populated if the search parameter refers to a SearchParameter defined by the FHIR core specification or externally defined IGs.") |  | 0..1 | [canonical](datatypes.html#canonical)([SearchParameter](searchparameter.html)) | Source of definition for parameter |
| ...... [type](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.type "CapabilityStatement.rest.resource.searchParam.type : The type of value a search parameter refers to, and how the content is interpreted.") |  | 1..1 | [code](datatypes.html#code) | number | date | string | token | reference | composite | quantity | uri | special [SearchParamType](valueset-search-param-type.html "Data types allowed to be used for search parameters.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ...... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.documentation "CapabilityStatement.rest.resource.searchParam.documentation : This allows documentation of any distinct behaviors about how the search parameter is used.  For example, text matching algorithms.") |  | 0..1 | [markdown](datatypes.html#markdown) | Server-specific usage |
| ..... [operation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation "CapabilityStatement.rest.resource.operation : Definition of an operation or a named query together with its parameters and their meaning and type. Consult the definition of the operation for details about how to invoke the operation, and the parameters.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Definition of a resource operation |
| ...... [name](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation.name "CapabilityStatement.rest.resource.operation.name : The name of the operation or query. For an operation, this is the name  prefixed with $ and used in the URL. For a query, this is the name used in the _query parameter when the query is called.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Name by which the operation/query is invoked |
| ...... [definition](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation.definition "CapabilityStatement.rest.resource.operation.definition : Where the formal definition can be found. If a server references the base definition of an Operation (i.e. from the specification itself such as ```http://hl7.org/fhir/OperationDefinition/ValueSet-expand```), that means it supports the full capabilities of the operation - e.g. both GET and POST invocation.  If it only supports a subset, it must define its own custom [[[OperationDefinition]]] with a 'base' of the original OperationDefinition.  The custom definition would describe the specific subset of functionality supported.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [canonical](datatypes.html#canonical)([OperationDefinition](operationdefinition.html)) | The defined operation/query |
| ...... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation.documentation "CapabilityStatement.rest.resource.operation.documentation : Documentation that describes anything special about the operation behavior, possibly detailing different behavior for system, type and instance-level invocation of the operation.") |  | 0..1 | [markdown](datatypes.html#markdown) | Specific details about operation behavior |
| .... [interaction](capabilitystatement-definitions.html#CapabilityStatement.rest.interaction "CapabilityStatement.rest.interaction : A specification of restful operations supported by the system.") |  | 0..\* | [BackboneElement](backboneelement.html) | What operations are supported? |
| ..... [code](capabilitystatement-definitions.html#CapabilityStatement.rest.interaction.code "CapabilityStatement.rest.interaction.code : A coded identifier of the operation, supported by the system.") |  | 1..1 | [code](datatypes.html#code) | transaction | batch | search-system | history-system [SystemRestfulInteraction](valueset-system-restful-interaction.html "Operations supported by REST at the system level.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.interaction.documentation "CapabilityStatement.rest.interaction.documentation : Guidance specific to the implementation of this operation, such as limitations on the kind of transactions allowed, or information about system wide search is implemented.") |  | 0..1 | [markdown](datatypes.html#markdown) | Anything special about operation behavior |
| .... [searchParam](capabilitystatement-definitions.html#CapabilityStatement.rest.searchParam "CapabilityStatement.rest.searchParam : Search parameters that are supported for searching all resources for implementations to support and/or make use of - either references to ones defined in the specification, or additional ones defined for/by the implementation.") |  | 0..\* | see [searchParam](#CapabilityStatement.rest.resource.searchParam "CapabilityStatement.rest.resource.searchParam") | Search parameters for searching all resources |
| .... [operation](capabilitystatement-definitions.html#CapabilityStatement.rest.operation "CapabilityStatement.rest.operation : Definition of an operation or a named query together with its parameters and their meaning and type.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | see [operation](#CapabilityStatement.rest.resource.operation "CapabilityStatement.rest.resource.operation") | Definition of a system level operation |
| .... [compartment](capabilitystatement-definitions.html#CapabilityStatement.rest.compartment "CapabilityStatement.rest.compartment : An absolute URI which is a reference to the definition of a compartment that the system supports. The reference is to a CompartmentDefinition resource by its canonical URL .") |  | 0..\* | [canonical](datatypes.html#canonical)([CompartmentDefinition](compartmentdefinition.html)) | Compartments served/used by system |
| ... [messaging](capabilitystatement-definitions.html#CapabilityStatement.messaging "CapabilityStatement.messaging : A description of the messaging capabilities of the solution.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [BackboneElement](backboneelement.html) | If messaging is supported |
| .... [endpoint](capabilitystatement-definitions.html#CapabilityStatement.messaging.endpoint "CapabilityStatement.messaging.endpoint : An endpoint (network accessible address) to which messages and/or replies are to be sent.") |  | 0..\* | [BackboneElement](backboneelement.html) | Where messages should be sent |
| ..... [protocol](capabilitystatement-definitions.html#CapabilityStatement.messaging.endpoint.protocol "CapabilityStatement.messaging.endpoint.protocol : A list of the messaging transport protocol(s) identifiers, supported by this endpoint.") |  | 1..1 | [Coding](datatypes.html#Coding) | http | ftp | mllp + [MessageTransport](valueset-message-transport.html "The protocol used for message transport.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ..... [address](capabilitystatement-definitions.html#CapabilityStatement.messaging.endpoint.address "CapabilityStatement.messaging.endpoint.address : The network address of the endpoint. For solutions that do not use network addresses for routing, it can be just an identifier.") |  | 1..1 | [url](datatypes.html#url) | Network address or identifier of the end-point |
| .... [reliableCache](capabilitystatement-definitions.html#CapabilityStatement.messaging.reliableCache "CapabilityStatement.messaging.reliableCache : Length if the receiver's reliable messaging cache in minutes (if a receiver) or how long the cache length on the receiver should be (if a sender).") |  | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Reliable Message Cache Length (min) |
| .... [documentation](capabilitystatement-definitions.html#CapabilityStatement.messaging.documentation "CapabilityStatement.messaging.documentation : Documentation about the system's messaging capabilities for this endpoint not otherwise documented by the capability statement.  For example, the process for becoming an authorized messaging exchange partner.") |  | 0..1 | [markdown](datatypes.html#markdown) | Messaging interface behavior details |
| .... [supportedMessage](capabilitystatement-definitions.html#CapabilityStatement.messaging.supportedMessage "CapabilityStatement.messaging.supportedMessage : References to message definitions for messages this system can send or receive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Messages supported by this system |
| ..... [mode](capabilitystatement-definitions.html#CapabilityStatement.messaging.supportedMessage.mode "CapabilityStatement.messaging.supportedMessage.mode : The mode of this event declaration - whether application is sender or receiver.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | sender | receiver [EventCapabilityMode](valueset-event-capability-mode.html "The mode of a message capability statement.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [definition](capabilitystatement-definitions.html#CapabilityStatement.messaging.supportedMessage.definition "CapabilityStatement.messaging.supportedMessage.definition : Points to a message definition that identifies the messaging event, message structure, allowed responses, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [canonical](datatypes.html#canonical)([MessageDefinition](messagedefinition.html)) | Message supported by this system |
| ... [document](capabilitystatement-definitions.html#CapabilityStatement.document "CapabilityStatement.document : A document definition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [BackboneElement](backboneelement.html) | Document definition |
| .... [mode](capabilitystatement-definitions.html#CapabilityStatement.document.mode "CapabilityStatement.document.mode : Mode of this document declaration - whether an application is a producer or consumer.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | producer | consumer [DocumentMode](valueset-document-mode.html "Whether the application produces or consumes documents.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [documentation](capabilitystatement-definitions.html#CapabilityStatement.document.documentation "CapabilityStatement.document.documentation : A description of how the application supports or uses the specified document profile.  For example, when documents are created, what action is taken with consumed documents, etc.") |  | 0..1 | [markdown](datatypes.html#markdown) | Description of document support |
| .... [profile](capabilitystatement-definitions.html#CapabilityStatement.document.profile "CapabilityStatement.document.profile : A profile on the document Bundle that constrains which resources are present, and their contents.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Constraint on the resources used in the document |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<CapabilityStatement xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 0..1 Canonical identifier for this capability statement, represented as a URI (globally unique) -->
 <version value="[string]"/><!-- 0..1 Business version of the capability statement -->
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name for this capability statement (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this capability statement (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 1..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- ![??](lock.png) 0..1 Natural language description of the capability statement -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for capability statement (if applicable) --></jurisdiction>
 <purpose value="[markdown]"/><!-- 0..1 Why this capability statement is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <kind value="[code]"/><!-- ![??](lock.png) 1..1 instance | capability | requirements -->
 <instantiates><!-- 0..* canonical(CapabilityStatement) Canonical URL of another capability statement this implements --></instantiates>
 <imports><!-- 0..* canonical(CapabilityStatement) Canonical URL of another capability statement this adds to --></imports>
 <software>  <!-- ![??](lock.png) 0..1 Software that is covered by this capability statement -->
  <name value="[string]"/><!-- 1..1 A name the software is known by -->
  <version value="[string]"/><!-- 0..1 Version covered by this statement -->
  <releaseDate value="[dateTime]"/><!-- 0..1 Date this version was released -->
 </software>
 <implementation>  <!-- ![??](lock.png) 0..1 If this describes a specific instance -->
  <description value="[string]"/><!-- 1..1 Describes this specific instance -->
  <url value="[url]"/><!-- 0..1 Base URL for the installation -->
  <custodian><!-- 0..1 Reference(Organization) Organization that manages the data --></custodian>
 </implementation>
 <fhirVersion value="[code]"/><!-- 1..1 FHIR Version the system supports -->
 <format value="[code]"/><!-- 1..* formats supported (xml | json | ttl | mime type) -->
 <patchFormat value="[code]"/><!-- 0..* Patch formats supported -->
 <implementationGuide><!-- 0..* canonical(ImplementationGuide) Implementation guides supported --></implementationGuide>
 <rest>  <!-- ![??](lock.png) 0..* If the endpoint is a RESTful one -->
  <mode value="[code]"/><!-- 1..1 client | server -->
  <documentation value="[markdown]"/><!-- 0..1 General description of implementation -->
  <security>  <!-- 0..1 Information about security of implementation -->
   <cors value="[boolean]"/><!-- 0..1 Adds CORS Headers (http://enable-cors.org/) -->
   <service><!-- 0..* CodeableConcept OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates --></service>
   <description value="[markdown]"/><!-- 0..1 General description of how security works -->
  </security>
  <resource>  <!-- 0..* Resource served on the REST interface -->
   <type value="[code]"/><!-- 1..1 A resource type that is supported -->
   <profile><!-- 0..1 canonical(StructureDefinition) Base System profile for all uses of resource --></profile>
   <supportedProfile><!-- 0..* canonical(StructureDefinition) Profiles for use cases supported --></supportedProfile>
   <documentation value="[markdown]"/><!-- 0..1 Additional information about the use of the resource type -->
   <interaction>  <!-- 0..* What operations are supported? -->
    <code value="[code]"/><!-- 1..1 read | vread | update | patch | delete | history-instance | history-type | create | search-type -->
    <documentation value="[markdown]"/><!-- 0..1 Anything special about operation behavior -->
   </interaction>
   <versioning value="[code]"/><!-- 0..1 no-version | versioned | versioned-update -->
   <readHistory value="[boolean]"/><!-- 0..1 Whether vRead can return past versions -->
   <updateCreate value="[boolean]"/><!-- 0..1 If update can commit to a new identity -->
   <conditionalCreate value="[boolean]"/><!-- 0..1 If allows/uses conditional create -->
   <conditionalRead value="[code]"/><!-- 0..1 not-supported | modified-since | not-match | full-support -->
   <conditionalUpdate value="[boolean]"/><!-- 0..1 If allows/uses conditional update -->
   <conditionalDelete value="[code]"/><!-- 0..1 not-supported | single | multiple - how conditional delete is supported -->
   <referencePolicy value="[code]"/><!-- 0..* literal | logical | resolves | enforced | local -->
   <searchInclude value="[string]"/><!-- 0..* _include values supported by the server -->
   <searchRevInclude value="[string]"/><!-- 0..* _revinclude values supported by the server -->
   <searchParam>  <!-- 0..* Search parameters supported by implementation -->
    <name value="[string]"/><!-- 1..1 Name of search parameter -->
    <definition><!-- 0..1 canonical(SearchParameter) Source of definition for parameter --></definition>
    <type value="[code]"/><!-- 1..1 number | date | string | token | reference | composite | quantity | uri | special -->
    <documentation value="[markdown]"/><!-- 0..1 Server-specific usage -->
   </searchParam>
   <operation>  <!-- 0..* Definition of a resource operation -->
    <name value="[string]"/><!-- 1..1 Name by which the operation/query is invoked -->
    <definition><!-- 1..1 canonical(OperationDefinition) The defined operation/query --></definition>
    <documentation value="[markdown]"/><!-- 0..1 Specific details about operation behavior -->
   </operation>
  </resource>
  <interaction>  <!-- 0..* What operations are supported? -->
   <code value="[code]"/><!-- 1..1 transaction | batch | search-system | history-system -->
   <documentation value="[markdown]"/><!-- 0..1 Anything special about operation behavior -->
  </interaction>
  <searchParam><!-- 0..* Content as for CapabilityStatement.rest.resource.searchParam Search parameters for searching all resources --></searchParam>
  <operation><!-- 0..* Content as for CapabilityStatement.rest.resource.operation Definition of a system level operation --></operation>
  <compartment><!-- 0..* canonical(CompartmentDefinition) Compartments served/used by system --></compartment>
 </rest>
 <messaging>  <!-- ![??](lock.png) 0..* If messaging is supported -->
  <endpoint>  <!-- 0..* Where messages should be sent -->
   <protocol><!-- 1..1 Coding http | ftp | mllp + --></protocol>
   <address value="[url]"/><!-- 1..1 Network address or identifier of the end-point -->
  </endpoint>
  <reliableCache value="[unsignedInt]"/><!-- 0..1 Reliable Message Cache Length (min) -->
  <documentation value="[markdown]"/><!-- 0..1 Messaging interface behavior details -->
  <supportedMessage>  <!-- 0..* Messages supported by this system -->
   <mode value="[code]"/><!-- 1..1 sender | receiver -->
   <definition><!-- 1..1 canonical(MessageDefinition) Message supported by this system --></definition>
  </supportedMessage>
 </messaging>
 <document>  <!-- ![??](lock.png) 0..* Document definition -->
  <mode value="[code]"/><!-- 1..1 producer | consumer -->
  <documentation value="[markdown]"/><!-- 0..1 Description of document support -->
  <profile><!-- 1..1 canonical(StructureDefinition) Constraint on the resources used in the document --></profile>
 </document>
</CapabilityStatement>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "CapabilityStatement",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // Canonical identifier for this capability statement, represented as a URI (globally unique)
  "version" : "<string>", // Business version of the capability statement
  "name" : "<string>", // C? Name for this capability statement (computer friendly)
  "title" : "<string>", // Name for this capability statement (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // R!  Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // C? Natural language description of the capability statement
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for capability statement (if applicable)
  "purpose" : "<markdown>", // Why this capability statement is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "kind" : "<code>", // C? R!  instance | capability | requirements
  "instantiates" : [{ canonical(CapabilityStatement) }], // Canonical URL of another capability statement this implements
  "imports" : [{ canonical(CapabilityStatement) }], // Canonical URL of another capability statement this adds to
  "software" : { // C? Software that is covered by this capability statement
    "name" : "<string>", // R!  A name the software is known by
    "version" : "<string>", // Version covered by this statement
    "releaseDate" : "<dateTime>" // Date this version was released
  },
  "implementation" : { // C? If this describes a specific instance
    "description" : "<string>", // R!  Describes this specific instance
    "url" : "<url>", // Base URL for the installation
    "custodian" : { Reference(Organization) } // Organization that manages the data
  },
  "fhirVersion" : "<code>", // R!  FHIR Version the system supports
  "format" : ["<code>"], // R!  formats supported (xml | json | ttl | mime type)
  "patchFormat" : ["<code>"], // Patch formats supported
  "implementationGuide" : [{ canonical(ImplementationGuide) }], // Implementation guides supported
  "rest" : [{ // C? If the endpoint is a RESTful one
    "mode" : "<code>", // R!  client | server
    "documentation" : "<markdown>", // General description of implementation
    "security" : { // Information about security of implementation
      "cors" : <boolean>, // Adds CORS Headers (http://enable-cors.org/)
      "service" : [{ CodeableConcept }], // OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates
      "description" : "<markdown>" // General description of how security works
    },
    "resource" : [{ // Resource served on the REST interface
      "type" : "<code>", // R!  A resource type that is supported
      "profile" : { canonical(StructureDefinition) }, // Base System profile for all uses of resource
      "supportedProfile" : [{ canonical(StructureDefinition) }], // Profiles for use cases supported
      "documentation" : "<markdown>", // Additional information about the use of the resource type
      "interaction" : [{ // What operations are supported?
        "code" : "<code>", // R!  read | vread | update | patch | delete | history-instance | history-type | create | search-type
        "documentation" : "<markdown>" // Anything special about operation behavior
      }],
      "versioning" : "<code>", // no-version | versioned | versioned-update
      "readHistory" : <boolean>, // Whether vRead can return past versions
      "updateCreate" : <boolean>, // If update can commit to a new identity
      "conditionalCreate" : <boolean>, // If allows/uses conditional create
      "conditionalRead" : "<code>", // not-supported | modified-since | not-match | full-support
      "conditionalUpdate" : <boolean>, // If allows/uses conditional update
      "conditionalDelete" : "<code>", // not-supported | single | multiple - how conditional delete is supported
      "referencePolicy" : ["<code>"], // literal | logical | resolves | enforced | local
      "searchInclude" : ["<string>"], // _include values supported by the server
      "searchRevInclude" : ["<string>"], // _revinclude values supported by the server
      "searchParam" : [{ // Search parameters supported by implementation
        "name" : "<string>", // R!  Name of search parameter
        "definition" : { canonical(SearchParameter) }, // Source of definition for parameter
        "type" : "<code>", // R!  number | date | string | token | reference | composite | quantity | uri | special
        "documentation" : "<markdown>" // Server-specific usage
      }],
      "operation" : [{ // Definition of a resource operation
        "name" : "<string>", // R!  Name by which the operation/query is invoked
        "definition" : { canonical(OperationDefinition) }, // R!  The defined operation/query
        "documentation" : "<markdown>" // Specific details about operation behavior
      }]
    }],
    "interaction" : [{ // What operations are supported?
      "code" : "<code>", // R!  transaction | batch | search-system | history-system
      "documentation" : "<markdown>" // Anything special about operation behavior
    }],
    "searchParam" : [{ Content as for CapabilityStatement.rest.resource.searchParam }], // Search parameters for searching all resources
    "operation" : [{ Content as for CapabilityStatement.rest.resource.operation }], // Definition of a system level operation
    "compartment" : [{ canonical(CompartmentDefinition) }] // Compartments served/used by system
  }],
  "messaging" : [{ // C? If messaging is supported
    "endpoint" : [{ // Where messages should be sent
      "protocol" : { Coding }, // R!  http | ftp | mllp +
      "address" : "<url>" // R!  Network address or identifier of the end-point
    }],
    "reliableCache" : "<unsignedInt>", // Reliable Message Cache Length (min)
    "documentation" : "<markdown>", // Messaging interface behavior details
    "supportedMessage" : [{ // Messages supported by this system
      "mode" : "<code>", // R!  sender | receiver
      "definition" : { canonical(MessageDefinition) } // R!  Message supported by this system
    }]
  }],
  "document" : [{ // C? Document definition
    "mode" : "<code>", // R!  producer | consumer
    "documentation" : "<markdown>", // Description of document support
    "profile" : { canonical(StructureDefinition) } // R!  Constraint on the resources used in the document
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:CapabilityStatement;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:CapabilityStatement.url [ uri ]; # 0..1 Canonical identifier for this capability statement, represented as a URI (globally unique)
  fhir:CapabilityStatement.version [ string ]; # 0..1 Business version of the capability statement
  fhir:CapabilityStatement.name [ string ]; # 0..1 Name for this capability statement (computer friendly)
  fhir:CapabilityStatement.title [ string ]; # 0..1 Name for this capability statement (human friendly)
  fhir:CapabilityStatement.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:CapabilityStatement.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:CapabilityStatement.date [ dateTime ]; # 1..1 Date last changed
  fhir:CapabilityStatement.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:CapabilityStatement.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:CapabilityStatement.description [ markdown ]; # 0..1 Natural language description of the capability statement
  fhir:CapabilityStatement.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:CapabilityStatement.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for capability statement (if applicable)
  fhir:CapabilityStatement.purpose [ markdown ]; # 0..1 Why this capability statement is defined
  fhir:CapabilityStatement.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:CapabilityStatement.kind [ code ]; # 1..1 instance | capability | requirements
  fhir:CapabilityStatement.instantiates [ canonical(CapabilityStatement) ], ... ; # 0..* Canonical URL of another capability statement this implements
  fhir:CapabilityStatement.imports [ canonical(CapabilityStatement) ], ... ; # 0..* Canonical URL of another capability statement this adds to
  fhir:CapabilityStatement.software [ # 0..1 Software that is covered by this capability statement
    fhir:CapabilityStatement.software.name [ string ]; # 1..1 A name the software is known by
    fhir:CapabilityStatement.software.version [ string ]; # 0..1 Version covered by this statement
    fhir:CapabilityStatement.software.releaseDate [ dateTime ]; # 0..1 Date this version was released
  ];
  fhir:CapabilityStatement.implementation [ # 0..1 If this describes a specific instance
    fhir:CapabilityStatement.implementation.description [ string ]; # 1..1 Describes this specific instance
    fhir:CapabilityStatement.implementation.url [ url ]; # 0..1 Base URL for the installation
    fhir:CapabilityStatement.implementation.custodian [ Reference(Organization) ]; # 0..1 Organization that manages the data
  ];
  fhir:CapabilityStatement.fhirVersion [ code ]; # 1..1 FHIR Version the system supports
  fhir:CapabilityStatement.format [ code ], ... ; # 1..* formats supported (xml | json | ttl | mime type)
  fhir:CapabilityStatement.patchFormat [ code ], ... ; # 0..* Patch formats supported
  fhir:CapabilityStatement.implementationGuide [ canonical(ImplementationGuide) ], ... ; # 0..* Implementation guides supported
  fhir:CapabilityStatement.rest [ # 0..* If the endpoint is a RESTful one
    fhir:CapabilityStatement.rest.mode [ code ]; # 1..1 client | server
    fhir:CapabilityStatement.rest.documentation [ markdown ]; # 0..1 General description of implementation
    fhir:CapabilityStatement.rest.security [ # 0..1 Information about security of implementation
      fhir:CapabilityStatement.rest.security.cors [ boolean ]; # 0..1 Adds CORS Headers (http://enable-cors.org/)
      fhir:CapabilityStatement.rest.security.service [ CodeableConcept ], ... ; # 0..* OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates
      fhir:CapabilityStatement.rest.security.description [ markdown ]; # 0..1 General description of how security works
    ];
    fhir:CapabilityStatement.rest.resource [ # 0..* Resource served on the REST interface
      fhir:CapabilityStatement.rest.resource.type [ code ]; # 1..1 A resource type that is supported
      fhir:CapabilityStatement.rest.resource.profile [ canonical(StructureDefinition) ]; # 0..1 Base System profile for all uses of resource
      fhir:CapabilityStatement.rest.resource.supportedProfile [ canonical(StructureDefinition) ], ... ; # 0..* Profiles for use cases supported
      fhir:CapabilityStatement.rest.resource.documentation [ markdown ]; # 0..1 Additional information about the use of the resource type
      fhir:CapabilityStatement.rest.resource.interaction [ # 0..* What operations are supported?
        fhir:CapabilityStatement.rest.resource.interaction.code [ code ]; # 1..1 read | vread | update | patch | delete | history-instance | history-type | create | search-type
        fhir:CapabilityStatement.rest.resource.interaction.documentation [ markdown ]; # 0..1 Anything special about operation behavior
      ], ...;
      fhir:CapabilityStatement.rest.resource.versioning [ code ]; # 0..1 no-version | versioned | versioned-update
      fhir:CapabilityStatement.rest.resource.readHistory [ boolean ]; # 0..1 Whether vRead can return past versions
      fhir:CapabilityStatement.rest.resource.updateCreate [ boolean ]; # 0..1 If update can commit to a new identity
      fhir:CapabilityStatement.rest.resource.conditionalCreate [ boolean ]; # 0..1 If allows/uses conditional create
      fhir:CapabilityStatement.rest.resource.conditionalRead [ code ]; # 0..1 not-supported | modified-since | not-match | full-support
      fhir:CapabilityStatement.rest.resource.conditionalUpdate [ boolean ]; # 0..1 If allows/uses conditional update
      fhir:CapabilityStatement.rest.resource.conditionalDelete [ code ]; # 0..1 not-supported | single | multiple - how conditional delete is supported
      fhir:CapabilityStatement.rest.resource.referencePolicy [ code ], ... ; # 0..* literal | logical | resolves | enforced | local
      fhir:CapabilityStatement.rest.resource.searchInclude [ string ], ... ; # 0..* _include values supported by the server
      fhir:CapabilityStatement.rest.resource.searchRevInclude [ string ], ... ; # 0..* _revinclude values supported by the server
      fhir:CapabilityStatement.rest.resource.searchParam [ # 0..* Search parameters supported by implementation
        fhir:CapabilityStatement.rest.resource.searchParam.name [ string ]; # 1..1 Name of search parameter
        fhir:CapabilityStatement.rest.resource.searchParam.definition [ canonical(SearchParameter) ]; # 0..1 Source of definition for parameter
        fhir:CapabilityStatement.rest.resource.searchParam.type [ code ]; # 1..1 number | date | string | token | reference | composite | quantity | uri | special
        fhir:CapabilityStatement.rest.resource.searchParam.documentation [ markdown ]; # 0..1 Server-specific usage
      ], ...;
      fhir:CapabilityStatement.rest.resource.operation [ # 0..* Definition of a resource operation
        fhir:CapabilityStatement.rest.resource.operation.name [ string ]; # 1..1 Name by which the operation/query is invoked
        fhir:CapabilityStatement.rest.resource.operation.definition [ canonical(OperationDefinition) ]; # 1..1 The defined operation/query
        fhir:CapabilityStatement.rest.resource.operation.documentation [ markdown ]; # 0..1 Specific details about operation behavior
      ], ...;
    ], ...;
    fhir:CapabilityStatement.rest.interaction [ # 0..* What operations are supported?
      fhir:CapabilityStatement.rest.interaction.code [ code ]; # 1..1 transaction | batch | search-system | history-system
      fhir:CapabilityStatement.rest.interaction.documentation [ markdown ]; # 0..1 Anything special about operation behavior
    ], ...;
    fhir:CapabilityStatement.rest.searchParam [ See CapabilityStatement.rest.resource.searchParam ], ... ; # 0..* Search parameters for searching all resources
    fhir:CapabilityStatement.rest.operation [ See CapabilityStatement.rest.resource.operation ], ... ; # 0..* Definition of a system level operation
    fhir:CapabilityStatement.rest.compartment [ canonical(CompartmentDefinition) ], ... ; # 0..* Compartments served/used by system
  ], ...;
  fhir:CapabilityStatement.messaging [ # 0..* If messaging is supported
    fhir:CapabilityStatement.messaging.endpoint [ # 0..* Where messages should be sent
      fhir:CapabilityStatement.messaging.endpoint.protocol [ Coding ]; # 1..1 http | ftp | mllp +
      fhir:CapabilityStatement.messaging.endpoint.address [ url ]; # 1..1 Network address or identifier of the end-point
    ], ...;
    fhir:CapabilityStatement.messaging.reliableCache [ unsignedInt ]; # 0..1 Reliable Message Cache Length (min)
    fhir:CapabilityStatement.messaging.documentation [ markdown ]; # 0..1 Messaging interface behavior details
    fhir:CapabilityStatement.messaging.supportedMessage [ # 0..* Messages supported by this system
      fhir:CapabilityStatement.messaging.supportedMessage.mode [ code ]; # 1..1 sender | receiver
      fhir:CapabilityStatement.messaging.supportedMessage.definition [ canonical(MessageDefinition) ]; # 1..1 Message supported by this system
    ], ...;
  ], ...;
  fhir:CapabilityStatement.document [ # 0..* Document definition
    fhir:CapabilityStatement.document.mode [ code ]; # 1..1 producer | consumer
    fhir:CapabilityStatement.document.documentation [ markdown ]; # 0..1 Description of document support
    fhir:CapabilityStatement.document.profile [ canonical(StructureDefinition) ]; # 1..1 Constraint on the resources used in the document
  ], ...;
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [CapabilityStatement](capabilitystatement.html#CapabilityStatement) |  |
| CapabilityStatement | - Min Cardinality changed from 1 to 0 - Max Cardinality changed from 1 to \* |
| CapabilityStatement.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| CapabilityStatement.experimental | - No longer marked as Modifier |
| CapabilityStatement.kind | - Change value set from http://hl7.org/fhir/ValueSet/capability-statement-kind to http://hl7.org/fhir/ValueSet/capability-statement-kind|4.0.1 |
| CapabilityStatement.instantiates | - Type changed from uri to canonical(CapabilityStatement) |
| CapabilityStatement.imports | - Added Element |
| CapabilityStatement.implementation.url | - Type changed from uri to url |
| CapabilityStatement.implementation.custodian | - Added Element |
| CapabilityStatement.fhirVersion | - Type changed from id to code - Add Binding `http://hl7.org/fhir/ValueSet/FHIR-version|4.0.1` (required) |
| CapabilityStatement.format | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |
| CapabilityStatement.patchFormat | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |
| CapabilityStatement.implementationGuide | - Type changed from uri to canonical(ImplementationGuide) |
| CapabilityStatement.rest.mode | - Change value set from http://hl7.org/fhir/ValueSet/restful-capability-mode to http://hl7.org/fhir/ValueSet/restful-capability-mode|4.0.1 |
| CapabilityStatement.rest.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.security.service | - Change code system for extensibly bound codes from "http://hl7.org/fhir/restful-security-service" to "http://terminology.hl7.org/CodeSystem/restful-security-service" |
| CapabilityStatement.rest.security.description | - Type changed from string to markdown |
| CapabilityStatement.rest.resource.type | - Change value set from http://hl7.org/fhir/ValueSet/resource-types to http://hl7.org/fhir/ValueSet/resource-types|4.0.1 |
| CapabilityStatement.rest.resource.profile | - Type changed from Reference(StructureDefinition) to canonical(StructureDefinition) |
| CapabilityStatement.rest.resource.supportedProfile | - Moved from CapabilityStatement.profile to supportedProfile - Type changed from Reference(StructureDefinition) to canonical(StructureDefinition) |
| CapabilityStatement.rest.resource.interaction | - Min Cardinality changed from 1 to 0 |
| CapabilityStatement.rest.resource.interaction.code | - Change value set from http://hl7.org/fhir/ValueSet/type-restful-interaction to http://hl7.org/fhir/ValueSet/type-restful-interaction|4.0.1 |
| CapabilityStatement.rest.resource.interaction.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.resource.versioning | - Change value set from http://hl7.org/fhir/ValueSet/versioning-policy to http://hl7.org/fhir/ValueSet/versioning-policy|4.0.1 |
| CapabilityStatement.rest.resource.conditionalRead | - Change value set from http://hl7.org/fhir/ValueSet/conditional-read-status to http://hl7.org/fhir/ValueSet/conditional-read-status|4.0.1 |
| CapabilityStatement.rest.resource.conditionalDelete | - Change value set from http://hl7.org/fhir/ValueSet/conditional-delete-status to http://hl7.org/fhir/ValueSet/conditional-delete-status|4.0.1 |
| CapabilityStatement.rest.resource.referencePolicy | - Change value set from http://hl7.org/fhir/ValueSet/reference-handling-policy to http://hl7.org/fhir/ValueSet/reference-handling-policy|4.0.1 |
| CapabilityStatement.rest.resource.searchParam.definition | - Type changed from uri to canonical(SearchParameter) |
| CapabilityStatement.rest.resource.searchParam.type | - Change value set from http://hl7.org/fhir/ValueSet/search-param-type to http://hl7.org/fhir/ValueSet/search-param-type|4.0.1 |
| CapabilityStatement.rest.resource.searchParam.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.resource.operation | - Added Element |
| CapabilityStatement.rest.resource.operation.name | - **Added Mandatory Element** |
| CapabilityStatement.rest.resource.operation.definition | - **Added Mandatory Element** |
| CapabilityStatement.rest.resource.operation.documentation | - Added Element |
| CapabilityStatement.rest.interaction.code | - Change value set from http://hl7.org/fhir/ValueSet/system-restful-interaction to http://hl7.org/fhir/ValueSet/system-restful-interaction|4.0.1 |
| CapabilityStatement.rest.interaction.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.operation | - Remove Type BackboneElement |
| CapabilityStatement.rest.compartment | - Type changed from uri to canonical(CompartmentDefinition) |
| CapabilityStatement.messaging.endpoint.protocol | - Change code system for extensibly bound codes from "http://hl7.org/fhir/message-transport" to "http://terminology.hl7.org/CodeSystem/message-transport" |
| CapabilityStatement.messaging.endpoint.address | - Type changed from uri to url |
| CapabilityStatement.messaging.documentation | - Type changed from string to markdown |
| CapabilityStatement.messaging.supportedMessage.mode | - Change value set from http://hl7.org/fhir/ValueSet/event-capability-mode to http://hl7.org/fhir/ValueSet/event-capability-mode|4.0.1 |
| CapabilityStatement.messaging.supportedMessage.definition | - Type changed from Reference(MessageDefinition) to canonical(MessageDefinition) |
| CapabilityStatement.document.mode | - Change value set from http://hl7.org/fhir/ValueSet/document-mode to http://hl7.org/fhir/ValueSet/document-mode|4.0.1 |
| CapabilityStatement.document.documentation | - Type changed from string to markdown |
| CapabilityStatement.document.profile | - Type changed from Reference(StructureDefinition) to canonical(StructureDefinition) |
| CapabilityStatement.acceptUnknown | - deleted |
| CapabilityStatement.rest.security.certificate | - deleted |
| CapabilityStatement.rest.operation.name | - deleted |
| CapabilityStatement.rest.operation.definition | - deleted |
| CapabilityStatement.messaging.event | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](capabilitystatement.diff.xml) or [JSON](capabilitystatement.diff.json).

See [R3 <--> R4 Conversion Maps](capabilitystatement-version-maps.html) (status = 9 tests that all execute ok. 1 fail round-trip testing and 9 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [CapabilityStatement](capabilitystatement-definitions.html#CapabilityStatement "CapabilityStatement : A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server for a particular version of FHIR that may be used as a statement of actual server functionality or a statement of required or desired server implementation.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | A statement of system capabilities + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation + Rule: A Capability Statement SHALL have at least one of REST, messaging or document element. + Rule: A Capability Statement SHALL have at least one of description, software, or implementation element. + Rule: Messaging end-point is required (and is only permitted) when a statement is for an implementation. + Rule: The set of documents must be unique by the combination of profile and mode. + Rule: If kind = instance, implementation must be present and software may be present + Rule: If kind = capability, implementation must be absent, software must be present + Rule: If kind = requirements, implementation and software must be absent Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](capabilitystatement-definitions.html#CapabilityStatement.url "CapabilityStatement.url : An absolute URI that is used to identify this capability statement when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this capability statement is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the capability statement is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Canonical identifier for this capability statement, represented as a URI (globally unique) |
| ... [version](capabilitystatement-definitions.html#CapabilityStatement.version "CapabilityStatement.version : The identifier that is used to identify this version of the capability statement when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the capability statement author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the capability statement |
| ... [name](capabilitystatement-definitions.html#CapabilityStatement.name "CapabilityStatement.name : A natural language name identifying the capability statement. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name for this capability statement (computer friendly) |
| ... [title](capabilitystatement-definitions.html#CapabilityStatement.title "CapabilityStatement.title : A short, descriptive, user-friendly title for the capability statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this capability statement (human friendly) |
| ... [status](capabilitystatement-definitions.html#CapabilityStatement.status "CapabilityStatement.status : The status of this capability statement. Enables tracking the life-cycle of the content.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](capabilitystatement-definitions.html#CapabilityStatement.experimental "CapabilityStatement.experimental : A Boolean value to indicate that this capability statement is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](capabilitystatement-definitions.html#CapabilityStatement.date "CapabilityStatement.date : The date  (and optionally time) when the capability statement was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the capability statement changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](capabilitystatement-definitions.html#CapabilityStatement.publisher "CapabilityStatement.publisher : The name of the organization or individual that published the capability statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](capabilitystatement-definitions.html#CapabilityStatement.contact "CapabilityStatement.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](capabilitystatement-definitions.html#CapabilityStatement.description "CapabilityStatement.description : A free text natural language description of the capability statement from a consumer's perspective. Typically, this is used when the capability statement describes a desired rather than an actual solution, for example as a formal expression of requirements as part of an RFP.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the capability statement |
| ... [useContext](capabilitystatement-definitions.html#CapabilityStatement.useContext "CapabilityStatement.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate capability statement instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](capabilitystatement-definitions.html#CapabilityStatement.jurisdiction "CapabilityStatement.jurisdiction : A legal or geographic region in which the capability statement is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for capability statement (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [purpose](capabilitystatement-definitions.html#CapabilityStatement.purpose "CapabilityStatement.purpose : Explanation of why this capability statement is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this capability statement is defined |
| ... [copyright](capabilitystatement-definitions.html#CapabilityStatement.copyright "CapabilityStatement.copyright : A copyright statement relating to the capability statement and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the capability statement.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [kind](capabilitystatement-definitions.html#CapabilityStatement.kind "CapabilityStatement.kind : The way that this statement is intended to be used, to describe an actual running instance of software, a particular product (kind, not instance of software) or a class of implementation (e.g. a desired purchase).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [code](datatypes.html#code) | instance | capability | requirements [CapabilityStatementKind](valueset-capability-statement-kind.html "How a capability statement is intended to be used.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [instantiates](capabilitystatement-definitions.html#CapabilityStatement.instantiates "CapabilityStatement.instantiates : Reference to a canonical URL of another CapabilityStatement that this software implements. This capability statement is a published API description that corresponds to a business service. The server may actually implement a subset of the capability statement it claims to implement, so the capability statement must specify the full capability details.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([CapabilityStatement](capabilitystatement.html)) | Canonical URL of another capability statement this implements |
| ... [imports](capabilitystatement-definitions.html#CapabilityStatement.imports "CapabilityStatement.imports : Reference to a canonical URL of another CapabilityStatement that this software adds to. The capability statement automatically includes everything in the other statement, and it is not duplicated, though the server may repeat the same resources, interactions and operations to add additional details to them.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [canonical](datatypes.html#canonical)([CapabilityStatement](capabilitystatement.html)) | Canonical URL of another capability statement this adds to |
| ... [software](capabilitystatement-definitions.html#CapabilityStatement.software "CapabilityStatement.software : Software that is covered by this capability statement.  It is used when the capability statement describes the capabilities of a particular software version, independent of an installation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Software that is covered by this capability statement |
| .... [name](capabilitystatement-definitions.html#CapabilityStatement.software.name "CapabilityStatement.software.name : Name the software is known by.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | A name the software is known by |
| .... [version](capabilitystatement-definitions.html#CapabilityStatement.software.version "CapabilityStatement.software.version : The version identifier for the software covered by this statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Version covered by this statement |
| .... [releaseDate](capabilitystatement-definitions.html#CapabilityStatement.software.releaseDate "CapabilityStatement.software.releaseDate : Date this version of the software was released.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date this version was released |
| ... [implementation](capabilitystatement-definitions.html#CapabilityStatement.implementation "CapabilityStatement.implementation : Identifies a specific implementation instance that is described by the capability statement - i.e. a particular installation, rather than the capabilities of a software program.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | If this describes a specific instance |
| .... [description](capabilitystatement-definitions.html#CapabilityStatement.implementation.description "CapabilityStatement.implementation.description : Information about the specific installation that this capability statement relates to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Describes this specific instance |
| .... [url](capabilitystatement-definitions.html#CapabilityStatement.implementation.url "CapabilityStatement.implementation.url : An absolute base URL for the implementation.  This forms the base for REST interfaces as well as the mailbox and document interfaces.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [url](datatypes.html#url) | Base URL for the installation |
| .... [custodian](capabilitystatement-definitions.html#CapabilityStatement.implementation.custodian "CapabilityStatement.implementation.custodian : The organization responsible for the management of the instance and oversight of the data on the server at the specified URL.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that manages the data |
| ... [fhirVersion](capabilitystatement-definitions.html#CapabilityStatement.fhirVersion "CapabilityStatement.fhirVersion : The version of the FHIR specification that this CapabilityStatement describes (which SHALL be the same as the FHIR version of the CapabilityStatement itself). There is no default value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | FHIR Version the system supports [FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [format](capabilitystatement-definitions.html#CapabilityStatement.format "CapabilityStatement.format : A list of the formats supported by this implementation using their content types.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..\* | [code](datatypes.html#code) | formats supported (xml | json | ttl | mime type) [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [patchFormat](capabilitystatement-definitions.html#CapabilityStatement.patchFormat "CapabilityStatement.patchFormat : A list of the patch formats supported by this implementation using their content types.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | Patch formats supported [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [implementationGuide](capabilitystatement-definitions.html#CapabilityStatement.implementationGuide "CapabilityStatement.implementationGuide : A list of implementation guides that the server does (or should) support in their entirety.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([ImplementationGuide](implementationguide.html)) | Implementation guides supported |
| ... [rest](capabilitystatement-definitions.html#CapabilityStatement.rest "CapabilityStatement.rest : A definition of the restful capabilities of the solution, if any.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | If the endpoint is a RESTful one + Rule: A given resource can only be described once per RESTful mode. |
| .... [mode](capabilitystatement-definitions.html#CapabilityStatement.rest.mode "CapabilityStatement.rest.mode : Identifies whether this portion of the statement is describing the ability to initiate or receive restful operations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | client | server [RestfulCapabilityMode](valueset-restful-capability-mode.html "The mode of a RESTful capability statement.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.documentation "CapabilityStatement.rest.documentation : Information about the system's restful capabilities that apply across all applications, such as security.") |  | 0..1 | [markdown](datatypes.html#markdown) | General description of implementation |
| .... [security](capabilitystatement-definitions.html#CapabilityStatement.rest.security "CapabilityStatement.rest.security : Information about security implementation from an interface perspective - what a client needs to know.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [BackboneElement](backboneelement.html) | Information about security of implementation |
| ..... [cors](capabilitystatement-definitions.html#CapabilityStatement.rest.security.cors "CapabilityStatement.rest.security.cors : Server adds CORS headers when responding to requests - this enables Javascript applications to use the server.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Adds CORS Headers (http://enable-cors.org/) |
| ..... [service](capabilitystatement-definitions.html#CapabilityStatement.rest.security.service "CapabilityStatement.rest.security.service : Types of security services that are supported/required by the system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates [RestfulSecurityService](valueset-restful-security-service.html "Types of security services used with FHIR.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ..... [description](capabilitystatement-definitions.html#CapabilityStatement.rest.security.description "CapabilityStatement.rest.security.description : General description of how security works.") |  | 0..1 | [markdown](datatypes.html#markdown) | General description of how security works |
| .... [resource](capabilitystatement-definitions.html#CapabilityStatement.rest.resource "CapabilityStatement.rest.resource : A specification of the restful capabilities of the solution for a specific resource type.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Resource served on the REST interface + Rule: Search parameter names must be unique in the context of a resource. |
| ..... [type](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.type "CapabilityStatement.rest.resource.type : A type of resource exposed via the restful interface.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | A resource type that is supported [ResourceType](valueset-resource-types.html "One of the resource types defined as part of this version of FHIR.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [profile](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.profile "CapabilityStatement.rest.resource.profile : A specification of the profile that describes the solution's overall support for the resource, including any constraints on cardinality, bindings, lengths or other limitations. See further discussion in [Using Profiles](profiling.html#profile-uses).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Base System profile for all uses of resource |
| ..... [supportedProfile](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.supportedProfile "CapabilityStatement.rest.resource.supportedProfile : A list of profiles that represent different use cases supported by the system. For a server, \"supported by the system\" means the system hosts/produces a set of resources that are conformant to a particular profile, and allows clients that use its services to search using this profile and to find appropriate data. For a client, it means the system will search by this profile and process data according to the guidance implicit in the profile. See further discussion in [Using Profiles](profiling.html#profile-uses).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Profiles for use cases supported |
| ..... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.documentation "CapabilityStatement.rest.resource.documentation : Additional information about the resource type used by the system.") |  | 0..1 | [markdown](datatypes.html#markdown) | Additional information about the use of the resource type |
| ..... [interaction](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.interaction "CapabilityStatement.rest.resource.interaction : Identifies a restful operation supported by the solution.") |  | 0..\* | [BackboneElement](backboneelement.html) | What operations are supported? |
| ...... [code](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.interaction.code "CapabilityStatement.rest.resource.interaction.code : Coded identifier of the operation, supported by the system resource.") |  | 1..1 | [code](datatypes.html#code) | read | vread | update | patch | delete | history-instance | history-type | create | search-type [TypeRestfulInteraction](valueset-type-restful-interaction.html "Operations supported by REST at the type or instance level.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ...... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.interaction.documentation "CapabilityStatement.rest.resource.interaction.documentation : Guidance specific to the implementation of this operation, such as 'delete is a logical delete' or 'updates are only allowed with version id' or 'creates permitted from pre-authorized certificates only'.") |  | 0..1 | [markdown](datatypes.html#markdown) | Anything special about operation behavior |
| ..... [versioning](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.versioning "CapabilityStatement.rest.resource.versioning : This field is set to no-version to specify that the system does not support (server) or use (client) versioning for this resource type. If this has some other value, the server must at least correctly track and populate the versionId meta-property on resources. If the value is 'versioned-update', then the server supports all the versioning features, including using e-tags for version integrity in the API.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [code](datatypes.html#code) | no-version | versioned | versioned-update [ResourceVersionPolicy](valueset-versioning-policy.html "How the system supports versioning for a resource.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [readHistory](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.readHistory "CapabilityStatement.rest.resource.readHistory : A flag for whether the server is able to return past versions as part of the vRead operation.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | Whether vRead can return past versions |
| ..... [updateCreate](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate "CapabilityStatement.rest.resource.updateCreate : A flag to indicate that the server allows or needs to allow the client to create new identities on the server (that is, the client PUTs to a location where there is no existing resource). Allowing this operation means that the server allows the client to create new identities on the server.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If update can commit to a new identity |
| ..... [conditionalCreate](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalCreate "CapabilityStatement.rest.resource.conditionalCreate : A flag that indicates that the server supports conditional create.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If allows/uses conditional create |
| ..... [conditionalRead](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalRead "CapabilityStatement.rest.resource.conditionalRead : A code that indicates how the server supports conditional read.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [code](datatypes.html#code) | not-supported | modified-since | not-match | full-support [ConditionalReadStatus](valueset-conditional-read-status.html "A code that indicates how the server supports conditional read.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [conditionalUpdate](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalUpdate "CapabilityStatement.rest.resource.conditionalUpdate : A flag that indicates that the server supports conditional update.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If allows/uses conditional update |
| ..... [conditionalDelete](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.conditionalDelete "CapabilityStatement.rest.resource.conditionalDelete : A code that indicates how the server supports conditional delete.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [code](datatypes.html#code) | not-supported | single | multiple - how conditional delete is supported [ConditionalDeleteStatus](valueset-conditional-delete-status.html "A code that indicates how the server supports conditional delete.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [referencePolicy](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.referencePolicy "CapabilityStatement.rest.resource.referencePolicy : A set of flags that defines how references are supported.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [code](datatypes.html#code) | literal | logical | resolves | enforced | local [ReferenceHandlingPolicy](valueset-reference-handling-policy.html "A set of flags that defines how references are supported.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [searchInclude](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchInclude "CapabilityStatement.rest.resource.searchInclude : A list of _include values supported by the server.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [string](datatypes.html#string) | \_include values supported by the server |
| ..... [searchRevInclude](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchRevInclude "CapabilityStatement.rest.resource.searchRevInclude : A list of _revinclude (reverse include) values supported by the server.") | [TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [string](datatypes.html#string) | \_revinclude values supported by the server |
| ..... [searchParam](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam "CapabilityStatement.rest.resource.searchParam : Search parameters for implementations to support and/or make use of - either references to ones defined in the specification, or additional ones defined for/by the implementation.") |  | 0..\* | [BackboneElement](backboneelement.html) | Search parameters supported by implementation |
| ...... [name](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.name "CapabilityStatement.rest.resource.searchParam.name : The name of the search parameter used in the interface.") |  | 1..1 | [string](datatypes.html#string) | Name of search parameter |
| ...... [definition](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.definition "CapabilityStatement.rest.resource.searchParam.definition : An absolute URI that is a formal reference to where this parameter was first defined, so that a client can be confident of the meaning of the search parameter (a reference to [[[SearchParameter.url]]]). This element SHALL be populated if the search parameter refers to a SearchParameter defined by the FHIR core specification or externally defined IGs.") |  | 0..1 | [canonical](datatypes.html#canonical)([SearchParameter](searchparameter.html)) | Source of definition for parameter |
| ...... [type](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.type "CapabilityStatement.rest.resource.searchParam.type : The type of value a search parameter refers to, and how the content is interpreted.") |  | 1..1 | [code](datatypes.html#code) | number | date | string | token | reference | composite | quantity | uri | special [SearchParamType](valueset-search-param-type.html "Data types allowed to be used for search parameters.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ...... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.documentation "CapabilityStatement.rest.resource.searchParam.documentation : This allows documentation of any distinct behaviors about how the search parameter is used.  For example, text matching algorithms.") |  | 0..1 | [markdown](datatypes.html#markdown) | Server-specific usage |
| ..... [operation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation "CapabilityStatement.rest.resource.operation : Definition of an operation or a named query together with its parameters and their meaning and type. Consult the definition of the operation for details about how to invoke the operation, and the parameters.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Definition of a resource operation |
| ...... [name](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation.name "CapabilityStatement.rest.resource.operation.name : The name of the operation or query. For an operation, this is the name  prefixed with $ and used in the URL. For a query, this is the name used in the _query parameter when the query is called.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Name by which the operation/query is invoked |
| ...... [definition](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation.definition "CapabilityStatement.rest.resource.operation.definition : Where the formal definition can be found. If a server references the base definition of an Operation (i.e. from the specification itself such as ```http://hl7.org/fhir/OperationDefinition/ValueSet-expand```), that means it supports the full capabilities of the operation - e.g. both GET and POST invocation.  If it only supports a subset, it must define its own custom [[[OperationDefinition]]] with a 'base' of the original OperationDefinition.  The custom definition would describe the specific subset of functionality supported.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [canonical](datatypes.html#canonical)([OperationDefinition](operationdefinition.html)) | The defined operation/query |
| ...... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.operation.documentation "CapabilityStatement.rest.resource.operation.documentation : Documentation that describes anything special about the operation behavior, possibly detailing different behavior for system, type and instance-level invocation of the operation.") |  | 0..1 | [markdown](datatypes.html#markdown) | Specific details about operation behavior |
| .... [interaction](capabilitystatement-definitions.html#CapabilityStatement.rest.interaction "CapabilityStatement.rest.interaction : A specification of restful operations supported by the system.") |  | 0..\* | [BackboneElement](backboneelement.html) | What operations are supported? |
| ..... [code](capabilitystatement-definitions.html#CapabilityStatement.rest.interaction.code "CapabilityStatement.rest.interaction.code : A coded identifier of the operation, supported by the system.") |  | 1..1 | [code](datatypes.html#code) | transaction | batch | search-system | history-system [SystemRestfulInteraction](valueset-system-restful-interaction.html "Operations supported by REST at the system level.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [documentation](capabilitystatement-definitions.html#CapabilityStatement.rest.interaction.documentation "CapabilityStatement.rest.interaction.documentation : Guidance specific to the implementation of this operation, such as limitations on the kind of transactions allowed, or information about system wide search is implemented.") |  | 0..1 | [markdown](datatypes.html#markdown) | Anything special about operation behavior |
| .... [searchParam](capabilitystatement-definitions.html#CapabilityStatement.rest.searchParam "CapabilityStatement.rest.searchParam : Search parameters that are supported for searching all resources for implementations to support and/or make use of - either references to ones defined in the specification, or additional ones defined for/by the implementation.") |  | 0..\* | see [searchParam](#CapabilityStatement.rest.resource.searchParam "CapabilityStatement.rest.resource.searchParam") | Search parameters for searching all resources |
| .... [operation](capabilitystatement-definitions.html#CapabilityStatement.rest.operation "CapabilityStatement.rest.operation : Definition of an operation or a named query together with its parameters and their meaning and type.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | see [operation](#CapabilityStatement.rest.resource.operation "CapabilityStatement.rest.resource.operation") | Definition of a system level operation |
| .... [compartment](capabilitystatement-definitions.html#CapabilityStatement.rest.compartment "CapabilityStatement.rest.compartment : An absolute URI which is a reference to the definition of a compartment that the system supports. The reference is to a CompartmentDefinition resource by its canonical URL .") |  | 0..\* | [canonical](datatypes.html#canonical)([CompartmentDefinition](compartmentdefinition.html)) | Compartments served/used by system |
| ... [messaging](capabilitystatement-definitions.html#CapabilityStatement.messaging "CapabilityStatement.messaging : A description of the messaging capabilities of the solution.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [BackboneElement](backboneelement.html) | If messaging is supported |
| .... [endpoint](capabilitystatement-definitions.html#CapabilityStatement.messaging.endpoint "CapabilityStatement.messaging.endpoint : An endpoint (network accessible address) to which messages and/or replies are to be sent.") |  | 0..\* | [BackboneElement](backboneelement.html) | Where messages should be sent |
| ..... [protocol](capabilitystatement-definitions.html#CapabilityStatement.messaging.endpoint.protocol "CapabilityStatement.messaging.endpoint.protocol : A list of the messaging transport protocol(s) identifiers, supported by this endpoint.") |  | 1..1 | [Coding](datatypes.html#Coding) | http | ftp | mllp + [MessageTransport](valueset-message-transport.html "The protocol used for message transport.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ..... [address](capabilitystatement-definitions.html#CapabilityStatement.messaging.endpoint.address "CapabilityStatement.messaging.endpoint.address : The network address of the endpoint. For solutions that do not use network addresses for routing, it can be just an identifier.") |  | 1..1 | [url](datatypes.html#url) | Network address or identifier of the end-point |
| .... [reliableCache](capabilitystatement-definitions.html#CapabilityStatement.messaging.reliableCache "CapabilityStatement.messaging.reliableCache : Length if the receiver's reliable messaging cache in minutes (if a receiver) or how long the cache length on the receiver should be (if a sender).") |  | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Reliable Message Cache Length (min) |
| .... [documentation](capabilitystatement-definitions.html#CapabilityStatement.messaging.documentation "CapabilityStatement.messaging.documentation : Documentation about the system's messaging capabilities for this endpoint not otherwise documented by the capability statement.  For example, the process for becoming an authorized messaging exchange partner.") |  | 0..1 | [markdown](datatypes.html#markdown) | Messaging interface behavior details |
| .... [supportedMessage](capabilitystatement-definitions.html#CapabilityStatement.messaging.supportedMessage "CapabilityStatement.messaging.supportedMessage : References to message definitions for messages this system can send or receive.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Messages supported by this system |
| ..... [mode](capabilitystatement-definitions.html#CapabilityStatement.messaging.supportedMessage.mode "CapabilityStatement.messaging.supportedMessage.mode : The mode of this event declaration - whether application is sender or receiver.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | sender | receiver [EventCapabilityMode](valueset-event-capability-mode.html "The mode of a message capability statement.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [definition](capabilitystatement-definitions.html#CapabilityStatement.messaging.supportedMessage.definition "CapabilityStatement.messaging.supportedMessage.definition : Points to a message definition that identifies the messaging event, message structure, allowed responses, etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [canonical](datatypes.html#canonical)([MessageDefinition](messagedefinition.html)) | Message supported by this system |
| ... [document](capabilitystatement-definitions.html#CapabilityStatement.document "CapabilityStatement.document : A document definition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [BackboneElement](backboneelement.html) | Document definition |
| .... [mode](capabilitystatement-definitions.html#CapabilityStatement.document.mode "CapabilityStatement.document.mode : Mode of this document declaration - whether an application is a producer or consumer.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | producer | consumer [DocumentMode](valueset-document-mode.html "Whether the application produces or consumes documents.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [documentation](capabilitystatement-definitions.html#CapabilityStatement.document.documentation "CapabilityStatement.document.documentation : A description of how the application supports or uses the specified document profile.  For example, when documents are created, what action is taken with consumed documents, etc.") |  | 0..1 | [markdown](datatypes.html#markdown) | Description of document support |
| .... [profile](capabilitystatement-definitions.html#CapabilityStatement.document.profile "CapabilityStatement.document.profile : A profile on the document Bundle that constrains which resources are present, and their contents.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Constraint on the resources used in the document |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<CapabilityStatement xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 0..1 Canonical identifier for this capability statement, represented as a URI (globally unique) -->
 <version value="[string]"/><!-- 0..1 Business version of the capability statement -->
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name for this capability statement (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this capability statement (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 1..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- ![??](lock.png) 0..1 Natural language description of the capability statement -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for capability statement (if applicable) --></jurisdiction>
 <purpose value="[markdown]"/><!-- 0..1 Why this capability statement is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <kind value="[code]"/><!-- ![??](lock.png) 1..1 instance | capability | requirements -->
 <instantiates><!-- 0..* canonical(CapabilityStatement) Canonical URL of another capability statement this implements --></instantiates>
 <imports><!-- 0..* canonical(CapabilityStatement) Canonical URL of another capability statement this adds to --></imports>
 <software>  <!-- ![??](lock.png) 0..1 Software that is covered by this capability statement -->
  <name value="[string]"/><!-- 1..1 A name the software is known by -->
  <version value="[string]"/><!-- 0..1 Version covered by this statement -->
  <releaseDate value="[dateTime]"/><!-- 0..1 Date this version was released -->
 </software>
 <implementation>  <!-- ![??](lock.png) 0..1 If this describes a specific instance -->
  <description value="[string]"/><!-- 1..1 Describes this specific instance -->
  <url value="[url]"/><!-- 0..1 Base URL for the installation -->
  <custodian><!-- 0..1 Reference(Organization) Organization that manages the data --></custodian>
 </implementation>
 <fhirVersion value="[code]"/><!-- 1..1 FHIR Version the system supports -->
 <format value="[code]"/><!-- 1..* formats supported (xml | json | ttl | mime type) -->
 <patchFormat value="[code]"/><!-- 0..* Patch formats supported -->
 <implementationGuide><!-- 0..* canonical(ImplementationGuide) Implementation guides supported --></implementationGuide>
 <rest>  <!-- ![??](lock.png) 0..* If the endpoint is a RESTful one -->
  <mode value="[code]"/><!-- 1..1 client | server -->
  <documentation value="[markdown]"/><!-- 0..1 General description of implementation -->
  <security>  <!-- 0..1 Information about security of implementation -->
   <cors value="[boolean]"/><!-- 0..1 Adds CORS Headers (http://enable-cors.org/) -->
   <service><!-- 0..* CodeableConcept OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates --></service>
   <description value="[markdown]"/><!-- 0..1 General description of how security works -->
  </security>
  <resource>  <!-- 0..* Resource served on the REST interface -->
   <type value="[code]"/><!-- 1..1 A resource type that is supported -->
   <profile><!-- 0..1 canonical(StructureDefinition) Base System profile for all uses of resource --></profile>
   <supportedProfile><!-- 0..* canonical(StructureDefinition) Profiles for use cases supported --></supportedProfile>
   <documentation value="[markdown]"/><!-- 0..1 Additional information about the use of the resource type -->
   <interaction>  <!-- 0..* What operations are supported? -->
    <code value="[code]"/><!-- 1..1 read | vread | update | patch | delete | history-instance | history-type | create | search-type -->
    <documentation value="[markdown]"/><!-- 0..1 Anything special about operation behavior -->
   </interaction>
   <versioning value="[code]"/><!-- 0..1 no-version | versioned | versioned-update -->
   <readHistory value="[boolean]"/><!-- 0..1 Whether vRead can return past versions -->
   <updateCreate value="[boolean]"/><!-- 0..1 If update can commit to a new identity -->
   <conditionalCreate value="[boolean]"/><!-- 0..1 If allows/uses conditional create -->
   <conditionalRead value="[code]"/><!-- 0..1 not-supported | modified-since | not-match | full-support -->
   <conditionalUpdate value="[boolean]"/><!-- 0..1 If allows/uses conditional update -->
   <conditionalDelete value="[code]"/><!-- 0..1 not-supported | single | multiple - how conditional delete is supported -->
   <referencePolicy value="[code]"/><!-- 0..* literal | logical | resolves | enforced | local -->
   <searchInclude value="[string]"/><!-- 0..* _include values supported by the server -->
   <searchRevInclude value="[string]"/><!-- 0..* _revinclude values supported by the server -->
   <searchParam>  <!-- 0..* Search parameters supported by implementation -->
    <name value="[string]"/><!-- 1..1 Name of search parameter -->
    <definition><!-- 0..1 canonical(SearchParameter) Source of definition for parameter --></definition>
    <type value="[code]"/><!-- 1..1 number | date | string | token | reference | composite | quantity | uri | special -->
    <documentation value="[markdown]"/><!-- 0..1 Server-specific usage -->
   </searchParam>
   <operation>  <!-- 0..* Definition of a resource operation -->
    <name value="[string]"/><!-- 1..1 Name by which the operation/query is invoked -->
    <definition><!-- 1..1 canonical(OperationDefinition) The defined operation/query --></definition>
    <documentation value="[markdown]"/><!-- 0..1 Specific details about operation behavior -->
   </operation>
  </resource>
  <interaction>  <!-- 0..* What operations are supported? -->
   <code value="[code]"/><!-- 1..1 transaction | batch | search-system | history-system -->
   <documentation value="[markdown]"/><!-- 0..1 Anything special about operation behavior -->
  </interaction>
  <searchParam><!-- 0..* Content as for CapabilityStatement.rest.resource.searchParam Search parameters for searching all resources --></searchParam>
  <operation><!-- 0..* Content as for CapabilityStatement.rest.resource.operation Definition of a system level operation --></operation>
  <compartment><!-- 0..* canonical(CompartmentDefinition) Compartments served/used by system --></compartment>
 </rest>
 <messaging>  <!-- ![??](lock.png) 0..* If messaging is supported -->
  <endpoint>  <!-- 0..* Where messages should be sent -->
   <protocol><!-- 1..1 Coding http | ftp | mllp + --></protocol>
   <address value="[url]"/><!-- 1..1 Network address or identifier of the end-point -->
  </endpoint>
  <reliableCache value="[unsignedInt]"/><!-- 0..1 Reliable Message Cache Length (min) -->
  <documentation value="[markdown]"/><!-- 0..1 Messaging interface behavior details -->
  <supportedMessage>  <!-- 0..* Messages supported by this system -->
   <mode value="[code]"/><!-- 1..1 sender | receiver -->
   <definition><!-- 1..1 canonical(MessageDefinition) Message supported by this system --></definition>
  </supportedMessage>
 </messaging>
 <document>  <!-- ![??](lock.png) 0..* Document definition -->
  <mode value="[code]"/><!-- 1..1 producer | consumer -->
  <documentation value="[markdown]"/><!-- 0..1 Description of document support -->
  <profile><!-- 1..1 canonical(StructureDefinition) Constraint on the resources used in the document --></profile>
 </document>
</CapabilityStatement>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "CapabilityStatement",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // Canonical identifier for this capability statement, represented as a URI (globally unique)
  "version" : "<string>", // Business version of the capability statement
  "name" : "<string>", // C? Name for this capability statement (computer friendly)
  "title" : "<string>", // Name for this capability statement (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // R!  Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // C? Natural language description of the capability statement
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for capability statement (if applicable)
  "purpose" : "<markdown>", // Why this capability statement is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "kind" : "<code>", // C? R!  instance | capability | requirements
  "instantiates" : [{ canonical(CapabilityStatement) }], // Canonical URL of another capability statement this implements
  "imports" : [{ canonical(CapabilityStatement) }], // Canonical URL of another capability statement this adds to
  "software" : { // C? Software that is covered by this capability statement
    "name" : "<string>", // R!  A name the software is known by
    "version" : "<string>", // Version covered by this statement
    "releaseDate" : "<dateTime>" // Date this version was released
  },
  "implementation" : { // C? If this describes a specific instance
    "description" : "<string>", // R!  Describes this specific instance
    "url" : "<url>", // Base URL for the installation
    "custodian" : { Reference(Organization) } // Organization that manages the data
  },
  "fhirVersion" : "<code>", // R!  FHIR Version the system supports
  "format" : ["<code>"], // R!  formats supported (xml | json | ttl | mime type)
  "patchFormat" : ["<code>"], // Patch formats supported
  "implementationGuide" : [{ canonical(ImplementationGuide) }], // Implementation guides supported
  "rest" : [{ // C? If the endpoint is a RESTful one
    "mode" : "<code>", // R!  client | server
    "documentation" : "<markdown>", // General description of implementation
    "security" : { // Information about security of implementation
      "cors" : <boolean>, // Adds CORS Headers (http://enable-cors.org/)
      "service" : [{ CodeableConcept }], // OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates
      "description" : "<markdown>" // General description of how security works
    },
    "resource" : [{ // Resource served on the REST interface
      "type" : "<code>", // R!  A resource type that is supported
      "profile" : { canonical(StructureDefinition) }, // Base System profile for all uses of resource
      "supportedProfile" : [{ canonical(StructureDefinition) }], // Profiles for use cases supported
      "documentation" : "<markdown>", // Additional information about the use of the resource type
      "interaction" : [{ // What operations are supported?
        "code" : "<code>", // R!  read | vread | update | patch | delete | history-instance | history-type | create | search-type
        "documentation" : "<markdown>" // Anything special about operation behavior
      }],
      "versioning" : "<code>", // no-version | versioned | versioned-update
      "readHistory" : <boolean>, // Whether vRead can return past versions
      "updateCreate" : <boolean>, // If update can commit to a new identity
      "conditionalCreate" : <boolean>, // If allows/uses conditional create
      "conditionalRead" : "<code>", // not-supported | modified-since | not-match | full-support
      "conditionalUpdate" : <boolean>, // If allows/uses conditional update
      "conditionalDelete" : "<code>", // not-supported | single | multiple - how conditional delete is supported
      "referencePolicy" : ["<code>"], // literal | logical | resolves | enforced | local
      "searchInclude" : ["<string>"], // _include values supported by the server
      "searchRevInclude" : ["<string>"], // _revinclude values supported by the server
      "searchParam" : [{ // Search parameters supported by implementation
        "name" : "<string>", // R!  Name of search parameter
        "definition" : { canonical(SearchParameter) }, // Source of definition for parameter
        "type" : "<code>", // R!  number | date | string | token | reference | composite | quantity | uri | special
        "documentation" : "<markdown>" // Server-specific usage
      }],
      "operation" : [{ // Definition of a resource operation
        "name" : "<string>", // R!  Name by which the operation/query is invoked
        "definition" : { canonical(OperationDefinition) }, // R!  The defined operation/query
        "documentation" : "<markdown>" // Specific details about operation behavior
      }]
    }],
    "interaction" : [{ // What operations are supported?
      "code" : "<code>", // R!  transaction | batch | search-system | history-system
      "documentation" : "<markdown>" // Anything special about operation behavior
    }],
    "searchParam" : [{ Content as for CapabilityStatement.rest.resource.searchParam }], // Search parameters for searching all resources
    "operation" : [{ Content as for CapabilityStatement.rest.resource.operation }], // Definition of a system level operation
    "compartment" : [{ canonical(CompartmentDefinition) }] // Compartments served/used by system
  }],
  "messaging" : [{ // C? If messaging is supported
    "endpoint" : [{ // Where messages should be sent
      "protocol" : { Coding }, // R!  http | ftp | mllp +
      "address" : "<url>" // R!  Network address or identifier of the end-point
    }],
    "reliableCache" : "<unsignedInt>", // Reliable Message Cache Length (min)
    "documentation" : "<markdown>", // Messaging interface behavior details
    "supportedMessage" : [{ // Messages supported by this system
      "mode" : "<code>", // R!  sender | receiver
      "definition" : { canonical(MessageDefinition) } // R!  Message supported by this system
    }]
  }],
  "document" : [{ // C? Document definition
    "mode" : "<code>", // R!  producer | consumer
    "documentation" : "<markdown>", // Description of document support
    "profile" : { canonical(StructureDefinition) } // R!  Constraint on the resources used in the document
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:CapabilityStatement;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:CapabilityStatement.url [ uri ]; # 0..1 Canonical identifier for this capability statement, represented as a URI (globally unique)
  fhir:CapabilityStatement.version [ string ]; # 0..1 Business version of the capability statement
  fhir:CapabilityStatement.name [ string ]; # 0..1 Name for this capability statement (computer friendly)
  fhir:CapabilityStatement.title [ string ]; # 0..1 Name for this capability statement (human friendly)
  fhir:CapabilityStatement.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:CapabilityStatement.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:CapabilityStatement.date [ dateTime ]; # 1..1 Date last changed
  fhir:CapabilityStatement.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:CapabilityStatement.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:CapabilityStatement.description [ markdown ]; # 0..1 Natural language description of the capability statement
  fhir:CapabilityStatement.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:CapabilityStatement.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for capability statement (if applicable)
  fhir:CapabilityStatement.purpose [ markdown ]; # 0..1 Why this capability statement is defined
  fhir:CapabilityStatement.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:CapabilityStatement.kind [ code ]; # 1..1 instance | capability | requirements
  fhir:CapabilityStatement.instantiates [ canonical(CapabilityStatement) ], ... ; # 0..* Canonical URL of another capability statement this implements
  fhir:CapabilityStatement.imports [ canonical(CapabilityStatement) ], ... ; # 0..* Canonical URL of another capability statement this adds to
  fhir:CapabilityStatement.software [ # 0..1 Software that is covered by this capability statement
    fhir:CapabilityStatement.software.name [ string ]; # 1..1 A name the software is known by
    fhir:CapabilityStatement.software.version [ string ]; # 0..1 Version covered by this statement
    fhir:CapabilityStatement.software.releaseDate [ dateTime ]; # 0..1 Date this version was released
  ];
  fhir:CapabilityStatement.implementation [ # 0..1 If this describes a specific instance
    fhir:CapabilityStatement.implementation.description [ string ]; # 1..1 Describes this specific instance
    fhir:CapabilityStatement.implementation.url [ url ]; # 0..1 Base URL for the installation
    fhir:CapabilityStatement.implementation.custodian [ Reference(Organization) ]; # 0..1 Organization that manages the data
  ];
  fhir:CapabilityStatement.fhirVersion [ code ]; # 1..1 FHIR Version the system supports
  fhir:CapabilityStatement.format [ code ], ... ; # 1..* formats supported (xml | json | ttl | mime type)
  fhir:CapabilityStatement.patchFormat [ code ], ... ; # 0..* Patch formats supported
  fhir:CapabilityStatement.implementationGuide [ canonical(ImplementationGuide) ], ... ; # 0..* Implementation guides supported
  fhir:CapabilityStatement.rest [ # 0..* If the endpoint is a RESTful one
    fhir:CapabilityStatement.rest.mode [ code ]; # 1..1 client | server
    fhir:CapabilityStatement.rest.documentation [ markdown ]; # 0..1 General description of implementation
    fhir:CapabilityStatement.rest.security [ # 0..1 Information about security of implementation
      fhir:CapabilityStatement.rest.security.cors [ boolean ]; # 0..1 Adds CORS Headers (http://enable-cors.org/)
      fhir:CapabilityStatement.rest.security.service [ CodeableConcept ], ... ; # 0..* OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates
      fhir:CapabilityStatement.rest.security.description [ markdown ]; # 0..1 General description of how security works
    ];
    fhir:CapabilityStatement.rest.resource [ # 0..* Resource served on the REST interface
      fhir:CapabilityStatement.rest.resource.type [ code ]; # 1..1 A resource type that is supported
      fhir:CapabilityStatement.rest.resource.profile [ canonical(StructureDefinition) ]; # 0..1 Base System profile for all uses of resource
      fhir:CapabilityStatement.rest.resource.supportedProfile [ canonical(StructureDefinition) ], ... ; # 0..* Profiles for use cases supported
      fhir:CapabilityStatement.rest.resource.documentation [ markdown ]; # 0..1 Additional information about the use of the resource type
      fhir:CapabilityStatement.rest.resource.interaction [ # 0..* What operations are supported?
        fhir:CapabilityStatement.rest.resource.interaction.code [ code ]; # 1..1 read | vread | update | patch | delete | history-instance | history-type | create | search-type
        fhir:CapabilityStatement.rest.resource.interaction.documentation [ markdown ]; # 0..1 Anything special about operation behavior
      ], ...;
      fhir:CapabilityStatement.rest.resource.versioning [ code ]; # 0..1 no-version | versioned | versioned-update
      fhir:CapabilityStatement.rest.resource.readHistory [ boolean ]; # 0..1 Whether vRead can return past versions
      fhir:CapabilityStatement.rest.resource.updateCreate [ boolean ]; # 0..1 If update can commit to a new identity
      fhir:CapabilityStatement.rest.resource.conditionalCreate [ boolean ]; # 0..1 If allows/uses conditional create
      fhir:CapabilityStatement.rest.resource.conditionalRead [ code ]; # 0..1 not-supported | modified-since | not-match | full-support
      fhir:CapabilityStatement.rest.resource.conditionalUpdate [ boolean ]; # 0..1 If allows/uses conditional update
      fhir:CapabilityStatement.rest.resource.conditionalDelete [ code ]; # 0..1 not-supported | single | multiple - how conditional delete is supported
      fhir:CapabilityStatement.rest.resource.referencePolicy [ code ], ... ; # 0..* literal | logical | resolves | enforced | local
      fhir:CapabilityStatement.rest.resource.searchInclude [ string ], ... ; # 0..* _include values supported by the server
      fhir:CapabilityStatement.rest.resource.searchRevInclude [ string ], ... ; # 0..* _revinclude values supported by the server
      fhir:CapabilityStatement.rest.resource.searchParam [ # 0..* Search parameters supported by implementation
        fhir:CapabilityStatement.rest.resource.searchParam.name [ string ]; # 1..1 Name of search parameter
        fhir:CapabilityStatement.rest.resource.searchParam.definition [ canonical(SearchParameter) ]; # 0..1 Source of definition for parameter
        fhir:CapabilityStatement.rest.resource.searchParam.type [ code ]; # 1..1 number | date | string | token | reference | composite | quantity | uri | special
        fhir:CapabilityStatement.rest.resource.searchParam.documentation [ markdown ]; # 0..1 Server-specific usage
      ], ...;
      fhir:CapabilityStatement.rest.resource.operation [ # 0..* Definition of a resource operation
        fhir:CapabilityStatement.rest.resource.operation.name [ string ]; # 1..1 Name by which the operation/query is invoked
        fhir:CapabilityStatement.rest.resource.operation.definition [ canonical(OperationDefinition) ]; # 1..1 The defined operation/query
        fhir:CapabilityStatement.rest.resource.operation.documentation [ markdown ]; # 0..1 Specific details about operation behavior
      ], ...;
    ], ...;
    fhir:CapabilityStatement.rest.interaction [ # 0..* What operations are supported?
      fhir:CapabilityStatement.rest.interaction.code [ code ]; # 1..1 transaction | batch | search-system | history-system
      fhir:CapabilityStatement.rest.interaction.documentation [ markdown ]; # 0..1 Anything special about operation behavior
    ], ...;
    fhir:CapabilityStatement.rest.searchParam [ See CapabilityStatement.rest.resource.searchParam ], ... ; # 0..* Search parameters for searching all resources
    fhir:CapabilityStatement.rest.operation [ See CapabilityStatement.rest.resource.operation ], ... ; # 0..* Definition of a system level operation
    fhir:CapabilityStatement.rest.compartment [ canonical(CompartmentDefinition) ], ... ; # 0..* Compartments served/used by system
  ], ...;
  fhir:CapabilityStatement.messaging [ # 0..* If messaging is supported
    fhir:CapabilityStatement.messaging.endpoint [ # 0..* Where messages should be sent
      fhir:CapabilityStatement.messaging.endpoint.protocol [ Coding ]; # 1..1 http | ftp | mllp +
      fhir:CapabilityStatement.messaging.endpoint.address [ url ]; # 1..1 Network address or identifier of the end-point
    ], ...;
    fhir:CapabilityStatement.messaging.reliableCache [ unsignedInt ]; # 0..1 Reliable Message Cache Length (min)
    fhir:CapabilityStatement.messaging.documentation [ markdown ]; # 0..1 Messaging interface behavior details
    fhir:CapabilityStatement.messaging.supportedMessage [ # 0..* Messages supported by this system
      fhir:CapabilityStatement.messaging.supportedMessage.mode [ code ]; # 1..1 sender | receiver
      fhir:CapabilityStatement.messaging.supportedMessage.definition [ canonical(MessageDefinition) ]; # 1..1 Message supported by this system
    ], ...;
  ], ...;
  fhir:CapabilityStatement.document [ # 0..* Document definition
    fhir:CapabilityStatement.document.mode [ code ]; # 1..1 producer | consumer
    fhir:CapabilityStatement.document.documentation [ markdown ]; # 0..1 Description of document support
    fhir:CapabilityStatement.document.profile [ canonical(StructureDefinition) ]; # 1..1 Constraint on the resources used in the document
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [CapabilityStatement](capabilitystatement.html#CapabilityStatement) |  |
| CapabilityStatement | - Min Cardinality changed from 1 to 0 - Max Cardinality changed from 1 to \* |
| CapabilityStatement.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| CapabilityStatement.experimental | - No longer marked as Modifier |
| CapabilityStatement.kind | - Change value set from http://hl7.org/fhir/ValueSet/capability-statement-kind to http://hl7.org/fhir/ValueSet/capability-statement-kind|4.0.1 |
| CapabilityStatement.instantiates | - Type changed from uri to canonical(CapabilityStatement) |
| CapabilityStatement.imports | - Added Element |
| CapabilityStatement.implementation.url | - Type changed from uri to url |
| CapabilityStatement.implementation.custodian | - Added Element |
| CapabilityStatement.fhirVersion | - Type changed from id to code - Add Binding `http://hl7.org/fhir/ValueSet/FHIR-version|4.0.1` (required) |
| CapabilityStatement.format | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |
| CapabilityStatement.patchFormat | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |
| CapabilityStatement.implementationGuide | - Type changed from uri to canonical(ImplementationGuide) |
| CapabilityStatement.rest.mode | - Change value set from http://hl7.org/fhir/ValueSet/restful-capability-mode to http://hl7.org/fhir/ValueSet/restful-capability-mode|4.0.1 |
| CapabilityStatement.rest.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.security.service | - Change code system for extensibly bound codes from "http://hl7.org/fhir/restful-security-service" to "http://terminology.hl7.org/CodeSystem/restful-security-service" |
| CapabilityStatement.rest.security.description | - Type changed from string to markdown |
| CapabilityStatement.rest.resource.type | - Change value set from http://hl7.org/fhir/ValueSet/resource-types to http://hl7.org/fhir/ValueSet/resource-types|4.0.1 |
| CapabilityStatement.rest.resource.profile | - Type changed from Reference(StructureDefinition) to canonical(StructureDefinition) |
| CapabilityStatement.rest.resource.supportedProfile | - Moved from CapabilityStatement.profile to supportedProfile - Type changed from Reference(StructureDefinition) to canonical(StructureDefinition) |
| CapabilityStatement.rest.resource.interaction | - Min Cardinality changed from 1 to 0 |
| CapabilityStatement.rest.resource.interaction.code | - Change value set from http://hl7.org/fhir/ValueSet/type-restful-interaction to http://hl7.org/fhir/ValueSet/type-restful-interaction|4.0.1 |
| CapabilityStatement.rest.resource.interaction.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.resource.versioning | - Change value set from http://hl7.org/fhir/ValueSet/versioning-policy to http://hl7.org/fhir/ValueSet/versioning-policy|4.0.1 |
| CapabilityStatement.rest.resource.conditionalRead | - Change value set from http://hl7.org/fhir/ValueSet/conditional-read-status to http://hl7.org/fhir/ValueSet/conditional-read-status|4.0.1 |
| CapabilityStatement.rest.resource.conditionalDelete | - Change value set from http://hl7.org/fhir/ValueSet/conditional-delete-status to http://hl7.org/fhir/ValueSet/conditional-delete-status|4.0.1 |
| CapabilityStatement.rest.resource.referencePolicy | - Change value set from http://hl7.org/fhir/ValueSet/reference-handling-policy to http://hl7.org/fhir/ValueSet/reference-handling-policy|4.0.1 |
| CapabilityStatement.rest.resource.searchParam.definition | - Type changed from uri to canonical(SearchParameter) |
| CapabilityStatement.rest.resource.searchParam.type | - Change value set from http://hl7.org/fhir/ValueSet/search-param-type to http://hl7.org/fhir/ValueSet/search-param-type|4.0.1 |
| CapabilityStatement.rest.resource.searchParam.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.resource.operation | - Added Element |
| CapabilityStatement.rest.resource.operation.name | - **Added Mandatory Element** |
| CapabilityStatement.rest.resource.operation.definition | - **Added Mandatory Element** |
| CapabilityStatement.rest.resource.operation.documentation | - Added Element |
| CapabilityStatement.rest.interaction.code | - Change value set from http://hl7.org/fhir/ValueSet/system-restful-interaction to http://hl7.org/fhir/ValueSet/system-restful-interaction|4.0.1 |
| CapabilityStatement.rest.interaction.documentation | - Type changed from string to markdown |
| CapabilityStatement.rest.operation | - Remove Type BackboneElement |
| CapabilityStatement.rest.compartment | - Type changed from uri to canonical(CompartmentDefinition) |
| CapabilityStatement.messaging.endpoint.protocol | - Change code system for extensibly bound codes from "http://hl7.org/fhir/message-transport" to "http://terminology.hl7.org/CodeSystem/message-transport" |
| CapabilityStatement.messaging.endpoint.address | - Type changed from uri to url |
| CapabilityStatement.messaging.documentation | - Type changed from string to markdown |
| CapabilityStatement.messaging.supportedMessage.mode | - Change value set from http://hl7.org/fhir/ValueSet/event-capability-mode to http://hl7.org/fhir/ValueSet/event-capability-mode|4.0.1 |
| CapabilityStatement.messaging.supportedMessage.definition | - Type changed from Reference(MessageDefinition) to canonical(MessageDefinition) |
| CapabilityStatement.document.mode | - Change value set from http://hl7.org/fhir/ValueSet/document-mode to http://hl7.org/fhir/ValueSet/document-mode|4.0.1 |
| CapabilityStatement.document.documentation | - Type changed from string to markdown |
| CapabilityStatement.document.profile | - Type changed from Reference(StructureDefinition) to canonical(StructureDefinition) |
| CapabilityStatement.acceptUnknown | - deleted |
| CapabilityStatement.rest.security.certificate | - deleted |
| CapabilityStatement.rest.operation.name | - deleted |
| CapabilityStatement.rest.operation.definition | - deleted |
| CapabilityStatement.messaging.event | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](capabilitystatement.diff.xml) or [JSON](capabilitystatement.diff.json).

See [R3 <--> R4 Conversion Maps](capabilitystatement-version-maps.html) (status = 9 tests that all execute ok. 1 fail round-trip testing and 9 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](capabilitystatement-profiles.html) and the alternate definitions:
Master Definition [XML](capabilitystatement.profile.xml.html) + [JSON](capabilitystatement.profile.json.html),
[XML](xml.html) [Schema](capabilitystatement.xsd)/[Schematron](capabilitystatement.sch) + [JSON](json.html)
[Schema](capabilitystatement.schema.json.html), [ShEx](capabilitystatement.shex.html) (for [Turtle](rdf.html)) + [see the extensions](capabilitystatement-profiles.html) & the [dependency analysis](capabilitystatement-dependencies.html)

### 5.2.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| CapabilityStatement.status | The lifecycle status of an artifact. | [Required](terminologies.html#required) | [PublicationStatus](valueset-publication-status.html) |
| CapabilityStatement.jurisdiction | Countries and regions within which this artifact is targeted for use. | [Extensible](terminologies.html#extensible) | [Jurisdiction ValueSet](valueset-jurisdiction.html) |
| CapabilityStatement.kind | How a capability statement is intended to be used. | [Required](terminologies.html#required) | [CapabilityStatementKind](valueset-capability-statement-kind.html) |
| CapabilityStatement.fhirVersion | All published FHIR Versions. | [Required](terminologies.html#required) | [FHIRVersion](valueset-FHIR-version.html) |
| CapabilityStatement.format CapabilityStatement.patchFormat | The mime type of an attachment. Any valid mime type is allowed. | [Required](terminologies.html#required) | [Mime Types](valueset-mimetypes.html) |
| CapabilityStatement.rest.mode | The mode of a RESTful capability statement. | [Required](terminologies.html#required) | [RestfulCapabilityMode](valueset-restful-capability-mode.html) |
| CapabilityStatement.rest.security.service | Types of security services used with FHIR. | [Extensible](terminologies.html#extensible) | [RestfulSecurityService](valueset-restful-security-service.html) |
| CapabilityStatement.rest.resource.type | One of the resource types defined as part of this version of FHIR. | [Required](terminologies.html#required) | [Resource Types](valueset-resource-types.html) |
| CapabilityStatement.rest.resource.interaction.code | Operations supported by REST at the type or instance level. | [Required](terminologies.html#required) | [TypeRestfulInteraction](valueset-type-restful-interaction.html) |
| CapabilityStatement.rest.resource.versioning | How the system supports versioning for a resource. | [Required](terminologies.html#required) | [ResourceVersionPolicy](valueset-versioning-policy.html) |
| CapabilityStatement.rest.resource.conditionalRead | A code that indicates how the server supports conditional read. | [Required](terminologies.html#required) | [ConditionalReadStatus](valueset-conditional-read-status.html) |
| CapabilityStatement.rest.resource.conditionalDelete | A code that indicates how the server supports conditional delete. | [Required](terminologies.html#required) | [ConditionalDeleteStatus](valueset-conditional-delete-status.html) |
| CapabilityStatement.rest.resource.referencePolicy | A set of flags that defines how references are supported. | [Required](terminologies.html#required) | [ReferenceHandlingPolicy](valueset-reference-handling-policy.html) |
| CapabilityStatement.rest.resource.searchParam.type | Data types allowed to be used for search parameters. | [Required](terminologies.html#required) | [SearchParamType](valueset-search-param-type.html) |
| CapabilityStatement.rest.interaction.code | Operations supported by REST at the system level. | [Required](terminologies.html#required) | [SystemRestfulInteraction](valueset-system-restful-interaction.html) |
| CapabilityStatement.messaging.endpoint.protocol | The protocol used for message transport. | [Extensible](terminologies.html#extensible) | [MessageTransport](valueset-message-transport.html) |
| CapabilityStatement.messaging.supportedMessage.mode | The mode of a message capability statement. | [Required](terminologies.html#required) | [EventCapabilityMode](valueset-event-capability-mode.html) |
| CapabilityStatement.document.mode | Whether the application produces or consumes documents. | [Required](terminologies.html#required) | [DocumentMode](valueset-document-mode.html) |

### 5.2.3.2 Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **cpb-0** | [Warning](conformance-rules.html#warning) | (base) | Name should be usable as an identifier for the module by machine processing applications such as code generation | name.matches('[A-Z]([A-Za-z0-9\_]){0,254}') |
| **cpb-1** | [Rule](conformance-rules.html#rule) | (base) | A Capability Statement SHALL have at least one of REST, messaging or document element. | rest.exists() or messaging.exists() or document.exists() |
| **cpb-2** | [Rule](conformance-rules.html#rule) | (base) | A Capability Statement SHALL have at least one of description, software, or implementation element. | (description.count() + software.count() + implementation.count()) > 0 |
| **cpb-3** | [Rule](conformance-rules.html#rule) | (base) | Messaging end-point is required (and is only permitted) when a statement is for an implementation. | messaging.endpoint.empty() or kind = 'instance' |
| **cpb-7** | [Rule](conformance-rules.html#rule) | (base) | The set of documents must be unique by the combination of profile and mode. | document.select(profile&mode).isDistinct() |
| **cpb-9** | [Rule](conformance-rules.html#rule) | CapabilityStatement.rest | A given resource can only be described once per RESTful mode. | resource.select(type).isDistinct() |
| **cpb-12** | [Rule](conformance-rules.html#rule) | CapabilityStatement.rest.resource | Search parameter names must be unique in the context of a resource. | searchParam.select(name).isDistinct() |
| **cpb-14** | [Rule](conformance-rules.html#rule) | (base) | If kind = instance, implementation must be present and software may be present | (kind != 'instance') or implementation.exists() |
| **cpb-15** | [Rule](conformance-rules.html#rule) | (base) | If kind = capability, implementation must be absent, software must be present | (kind != 'capability') or (implementation.exists().not() and software.exists()) |
| **cpb-16** | [Rule](conformance-rules.html#rule) | (base) | If kind = requirements, implementation and software must be absent | (kind!='requirements') or (implementation.exists().not() and software.exists().not()) |

## 5.2.4 Notes:

- The CapabilityStatement resource provides for an application to describe its use of the RESTful
  paradigm messaging events, or FHIR documents. Usually, an application would only describe one,
  but more than one may be described
- RESTful CapabilityStatement rules:
  - RESTful servers are required to provide [this resource on demand](http.html#capabilities).
    Servers SHALL specify what resource types and operations are supported, and SHOULD also
    specify profiles for each resource type.
  - The CapabilityStatement returned on demand may represent the specific capabilities granted to a specific user if retrieved with that specific user's credentials, if one is in context. Servers that require authentication SHOULD still return a CapabilityStatemnt before authentication/authorization is performed
  - RESTful clients SHOULD publish a capability statement
  - The search parameters that a server supports (or a client makes use of) are specified in the resource profile that the capability statement references
  - Resource Types or operations that are not listed are not supported
- Messaging CapabilityStatement rules:
  - The interpretation of request and response depends on the mode. If the mode is sender,
    then request specifies what the application sends, and response specifies what it accepts.
    If the mode is "receiver", then this is reversed
  - If a request or response is not specified for an event, then no rules are made for it
  - Events that are not listed are not supported
  - The [MessageDefinition](messagedefinition.html) resource is newly proposed and is still considered 'draft'.
    The `supportedMessage` element can be used in place of the `event` and the work group believes it may meet
    implementer needs better, however because the new mechanism has not yet been reviewed by ballot, the older 'event' mechanism has
    been retained. Implementers may use one or the other to define their capabilities. Feedback is welcome.
- Document CapabilityStatement rules:
  - Document profiles should directly constrain the Document.information.class & type elements so
    that there is no ambiguity concerning which profile any given document conforms to.
- Other service-based use of resources: Due to the variability of these services, the `CapabilityStatement` resource
  does not attempt to describe service-based use of resources. The various service specifications will need to describe this usage in their own way.

### 5.2.4.1 Supporting Profiles

A CapabilityStatement declares two different kinds of profiles for the functionality it describes.
For a discussion of the use of these two types of resources, see [two uses for profiles](profiling.html).

## 5.2.5 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| context [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A use context assigned to the capability statement | (CapabilityStatement.useContext.value as CodeableConcept) |  |
| context-quantity [TU](versions.html#std-process "Trial Use Content") | [quantity](search.html#quantity) | A quantity- or range-valued use context assigned to the capability statement | (CapabilityStatement.useContext.value as Quantity) | (CapabilityStatement.useContext.value as Range) |  |
| context-type [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A type of use context assigned to the capability statement | CapabilityStatement.useContext.code |  |
| context-type-quantity [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and quantity- or range-based value assigned to the capability statement | On CapabilityStatement.useContext:   context-type: code   context-quantity: value.as(Quantity) | value.as(Range) |  |
| context-type-value [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and value assigned to the capability statement | On CapabilityStatement.useContext:   context-type: code   context: value.as(CodeableConcept) |  |
| date [TU](versions.html#std-process "Trial Use Content") | [date](search.html#date) | The capability statement publication date | CapabilityStatement.date |  |
| description [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The description of the capability statement | CapabilityStatement.description |  |
| fhirversion [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The version of FHIR | CapabilityStatement.version |  |
| format [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | formats supported (xml | json | ttl | mime type) | CapabilityStatement.format |  |
| guide [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Implementation guides supported | CapabilityStatement.implementationGuide ([ImplementationGuide](implementationguide.html)) |  |
| jurisdiction [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Intended jurisdiction for the capability statement | CapabilityStatement.jurisdiction |  |
| mode [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Mode - restful (server/client) or messaging (sender/receiver) | CapabilityStatement.rest.mode |  |
| name [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Computationally friendly name of the capability statement | CapabilityStatement.name |  |
| publisher [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Name of the publisher of the capability statement | CapabilityStatement.publisher |  |
| resource [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Name of a resource mentioned in a capability statement | CapabilityStatement.rest.resource.type |  |
| resource-profile [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | A profile id invoked in a capability statement | CapabilityStatement.rest.resource.profile ([StructureDefinition](structuredefinition.html)) |  |
| security-service [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates | CapabilityStatement.rest.security.service |  |
| software [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Part of the name of a software application | CapabilityStatement.software.name |  |
| status [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The current status of the capability statement | CapabilityStatement.status |  |
| supported-profile [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Profiles for use cases supported | CapabilityStatement.rest.resource.supportedProfile ([StructureDefinition](structuredefinition.html)) |  |
| title [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The human-friendly name of the capability statement | CapabilityStatement.title |  |
| url [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | The uri that identifies the capability statement | CapabilityStatement.url |  |
| version [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The business version of the capability statement | CapabilityStatement.version |  |
