---
id: overview-dev
title: Overview for Developers (CI build)
source_url: https://build.fhir.org/overview-dev.html
group: fhir-ci
fhir_version: R6-ci
fetched_at: '2026-09-11T13:23:56Z'
sha256: dff5545ed109972b606b36839dc40674f24dab5436bde13bbb1105d820bd6c6a
---
This is the Continuous Integration Build of FHIR (will be incorrect/inconsistent at times).   
See the [Directory of published versions ![icon](external.png)](http://hl7.org/fhir/directory.html)

## 2.1.19 FHIR Overview - Developers

|  |  |
| --- | --- |
| Responsible Owner: [FHIR Infrastructure icon](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Standards Status](versions.html#std-process): [Informative](versions.html#std-process) |

FHIR (*Fast Healthcare Interoperability Resources*) is designed to
enable information exchange to support the provision
of healthcare in a wide variety of settings. The specification
builds on and adapts modern, widely used RESTful practices
to enable the provision of integrated healthcare across a
wide range of teams and organizations.

The intended scope of FHIR is broad, covering human and veterinary,
clinical care, public health, clinical trials, administration and
financial aspects. The standard is intended for global use and in a wide
variety of architectures and scenarios.

### 2.1.19.1 Framework

FHIR is based on "Resources" which are the common building blocks
for all exchanges. Resources are an instance-level representation of some kind of healthcare entity.
All resources have the following features in [common](resource.html):

- An identifier for the resource - typically a URL that defines where the resource is found
- Common metadata
- A [human-readable XHTML summary](narrative.html)
- A set of defined data elements - a different set for each type of resource
- An [extensibility framework](extensibility.html) to support variation in healthcare

Resource instances are represented as either [XML](xml.html), [JSON](json.html) or [RDF (Turtle)](rdf.html) and there are currently 119
different [resource types defined](resourcelist.html) in the FHIR specification.

This specification describes a set of resources - that is, a set of resource types that describe the set of resource instances that
can actually be exchanged. The term 'Resource' is sometimes used without clarifying whether it specifically refers to types or instances - the context of use makes this clear.

### 2.1.19.2 Example Resource Instance

This is an example of how a [patient](patient.html) is represented as a FHIR object in [JSON](json.html). An [XML encoding](xml.html) is also defined in the specification.

```
{
  "resourceType": "Patient",
  "id" : "23434",
  "meta" : {
    "versionId" : "12",
    "lastUpdated" : "2014-08-18T15:43:30Z"
  }
  "text": {
    "status": "generated",
    "div": "<!-- Snipped for Brevity -->"
  },
  "extension": [
    {
      "url": "http://example.org/consent#trials",
      "valueCode": "renal"
    }
  ],
  "identifier": [
    {
      "use": "usual",
      "label": "MRN",
      "system": "http://www.goodhealth.org/identifiers/mrn",
      "value": "123456"
    }
  ],
  "name": [
    {
      "family": "Levin",
      "given": [
        "Henry"
      ],
      "suffix": [
        "The 7th"
      ]
    }
  ],
  "gender": {
    "text": "Male"
  },
  "birthDate": "1932-09-24",
  "active": true
}
```

Each instance of a resource consists of:

- **resourceType** (line 2) - Required: FHIR defines many different types of resources. See [the full index](resourcelist.html)
- **id** (line 3) - The id of this resource. Always present when a resource is exchanged, except during the create operation (below)
- **meta** (lines 4 - 7) - Usually Present: [Common use/context data to all resources](resource.html#meta) and managed by the infrastructure. Missing if there is no metadata
- **text** (lines 8 - 11) - Recommended: XHTML that provides a [human readable representation](narrative.html) for the resource
- **extension** (lines 12 - 17) - Optional: [Extensions](extensibility.html) defined by the extensibility framework
- **data** (lines 18 - 42) - Optional: data elements - a different set, defined for each type of resource

Note that although this specification always shows the JSON properties in the order that they are defined, many JSON libraries order properties by other criteria.

### 2.1.19.3 URLs and Identities

All resources may have a `URL` that identifies the resource and specifies where it was/can be accessed from.
This URL is not represented inside the resource; the value arises in a context use, and changes as copies of the
resource are made, or following other deployment/security related changes. If the resource is accessed via
the FHIR RESTful API (see immediately below) then the URL for the resource is `[base]/[resourceType]/[id]`
where the `resourceType` and `id` come from the resource (see above).

Some resources - those typically associated with formal publication cycles, rather than operational
healthcare - have an explicit URL in them, which is normally the URL of master copy of the resource.
This URL remains constant as the resource is copied across systems. See [Canonical URLs](references.html#canonical) for further
information.

### 2.1.19.4 Interactions

For manipulation of resources, FHIR provides a [REST API](http.html) with a
rich but simple set of interactions:

- [Create](http.html#create) = POST https://example.com/base/{resourceType}
- [Read](http.html#read) = GET https://example.com/base/{resourceType}/{id}
- [Update](http.html#update) = PUT https://example.com/base/{resourceType}/{id}
- [Patch](http.html#patch) = PATCH https://example.com/base/{resourceType}/{id}
- [Delete](http.html#delete) = DELETE https://example.com/base/{resourceType}/{id}
- [Search](http.html#search) = GET https://example.com/base/{resourceType}?search parameters...
- [History](http.html#history) = GET https://example.com/base/{resourceType}/{id}/\_history
- [Transaction](http.html#transaction) = POST https://example.com/base/ *(POST a transaction bundle to the system)*
- [Operation](operations.html) = GET https://example.com/base/{resourceType}/{id}/${opname}

The FHIR specification describes other kinds of exchanges beyond this simple RESTful API,
including exchange of groups of resources as [Documents](documents.html),
as [Messages](messaging.html), and by using various types of [Services](services.html).

### 2.1.19.5 Managing Variability

There is a wide variation
between different geo-political jurisdictions and segments of the healthcare industry, and no
central authority to impose common business practices. Because of this,
the FHIR specification defines an [extension framework](extensibility.html) and defines
[a framework for managing variability](profiling.html).

Another key aspect of the variability encountered in healthcare is that the
same information may be represented differently and with different levels of
detail, granularity and nesting by various parties across the system.
For example, in some cases a blood pressure measurement may be just a simple observation, a
vital sign measure, while in other cases can be a rich set of highly defined
data that includes things like controlled vocabularies for posture, exercise, etc.
The [resource types](resourcelist.html) defined in this specification
focus on the general, common use cases. Richer and more specific content
can be supported and standardized by [defining "profiles"](profiling.html) on
the base resource types.

### 2.1.19.6 Managing Versions

Versions, in the context of FHIR, means one of three different things:

1. FHIR Version: Which FHIR version is in use?
2. Record Version: for tracking changes to resources, and preventing changes overwriting each other
3. Business Version: So humans know which version of the content they are dealing with (for some kinds of resources)

**FHIR Version**

Usually, the FHIR version is fixed by the context - the [CapabilityStatement](capabilitystatement.html)
that a client can use to find out about the server, but there are other ways
of [managing multiple FHIR versions](versioning.html).

**Record Version**

FHIR Servers do not have to support versioning, though they are strongly encouraged to do so.
There are three different levels of versioning support for FHIR servers:

- Versioning and .meta.version are not supported (and usually, .meta.lastUpdated is not supported either)
- Versioning and the VersionId meta-property are supported, but a history of old versions is not kept
- Versioning and the VersionId meta-property are supported, and a history of old versions is available

In addition, servers may require that [version](http.html#concurrency) aware updates are used, to prevent over-writing changes,
but this is not described on this page.

**Business Version**

Some resources - typically those that represent content that goes through a formal publishing cycle - carry
a `version` element that explicitly states what version of the content the resource represents.
This is changed explicitly by a human, or by some automated process in accordance with applicable business
rules.

### 2.1.19.7 Creating a resource

To [create a resource](http.html#create), send an HTTP POST request to the resource type's respective end
point.

```
  POST https://example.com/base/{resourceType}
```

In the example below we see the creation of a Patient.

```
POST /base/Patient HTTP/1.1
Authorization: Bearer 37CC0B0E-C15B-4578-9AC1-D83DCED2B2F9
Accept: application/fhir+json
Content-Type: application/fhir+json
Content-Length: 1198
 
{
  "resourceType": "Patient",
  ...(properties)
}
```

Submit a new patient to the server, and ask it to store the patient with an id of its own choice.

Notes:

- **/Patient** (line 1) - the manager for all patients - use the name of the type of resource
- **Authorization** (line 2) - see [Security for FHIR](security.html)
- **Accept, Content-Type** (lines 3-4) - the content type for all FHIR resources as represented in JSON (or application/fhir+xml for the XML version). FHIR resources are always represented in UTF-8
- **id** - The client does not need to provide an id for a resource that is being created - the server will assign one. If the client assigns one, the server will overwrite it
- Resource Content, lines 8+ - There's no meta property at this point. The rest of the resource is the same content as shown above

### 2.1.19.8 Create Response

A response will contain an HTTP code 201 to indicate that the
Resource has been created successfully. A location header
indicates where the resource can be fetched in subsequent requests.
The server may choose to return an [OperationOutcome](operationoutcome.html) resource, but is not required to
do so.

```
HTTP/1.1 201 Created
Content-Length: 161
Content-Type: application/fhir+json
Date: Mon, 18 Aug 2014 01:43:30 GMT
ETag: W/"1"
Location: http://example.com/base/Patient/f001
 
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">The operation was successful</div>"
  }
}
```

Notes:

- **HTTP/1.1 201** (line 1) - the operation was successful. Note that use of [HTTP v 1.1 ![icon](external.png)](https://tools.ietf.org/html/rfc7231) is strongly recommended but not required
- **ETag** (line 5) - used in the [version aware update](http.html#update) pattern (if the server supports versioning)
- **Location** (line 6) - the id the server assigned to the resource. The id in the URL must match the id in the resource when the resource is subsequently returned
- **OperationOutcome** (line 9) - OperationOutcome resources in this context have no id or meta element (they have no managed identity)

#### 2.1.19.8.1 Error response

For a variety of reasons, servers may need to return an error. Clients should be alert to
authentication related responses, but FHIR content related errors should be returned using an
appropriate HTTP status code, with an [OperationOutcome](operationoutcome.html) resource to provide additional information.
Here is an example of a server rejecting a resource because of server defined business rules:

```
HTTP/1.1 422 Unprocessable Entity
Content-Length: 161
Content-Type: application/fhir+json
Date: Mon, 18 Aug 2014 01:43:30 GMT
 
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">MRN conflict
   - the MRN 123456 is already assigned to a different patient</div>"
  },
}
```

Notes:

- The server can return additional structured information using the details of the [OperationOutcome](operationoutcome.html)

### 2.1.19.9 Read Request

[Reading a resource](http.html#read) is done by sending HTTP GET requests to the desired Resource Type
end-point.

```
  GET https://example.com/base/{resourceType}/{id}
```

Here's an example.

```
GET /base/Patient/f001?_format=xml HTTP/1.1
Host: example.com
Accept: application/fhir+xml
Cache-Control: no-cache
```

Notes:

- **347** (line 1) - The id of the resource that is being fetched
- **\_format=xml** (line 1) - this is another method for clients to indicate the desired response format, in addition to using the accept header, and is useful for clients that don't have access to the HTTP Headers (e.g., XSLT transforms) (see [Mime Types](http.html#mimetypes))
- **cache control** (line 4) - Cache control is important, though FHIR itself says nothing about it - see [http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ![icon](external.png)](http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html) or [https://www.mnot.net/cache\_docs/ ![icon](external.png)](https://www.mnot.net/cache_docs/)

### 2.1.19.10 Read Response

The response to a GET contains the Resource.

```
HTTP/1.1 200 OK
Content-Length: 729
Content-Type: application/fhir+xml
Last-Modified: Sun, 17 Aug 2014 15:43:30 GMT
ETag: W/"1"
 
<?xml version="1.0" encoding="UTF-8"?>
<Patient xmlns="http://hl7.org/fhir">
  <id value="347"/>
  <meta>
    <versionId value="1"/>
    <lastUpdated value="2014-08-17T15:43:30Z"/>
  </meta>
  <!-- content as shown above for patient -->  
</Patient>
```

Notes:

- **id** (line 9) - The id of the resource. This must match the id in the read request
- **versionId** (line 11) - The current version id of the resource (if the server supports versioning). Best practice is that this value matches the ETag (see [version aware update](http.html#update)), but clients must never assume this
- Note that servers are not required to support versioning, but are strongly encouraged to do so
- **lastUpdated** (line 12) - if present, this must match the value in the HTTP header

### 2.1.19.11 Search Request

In addition to getting single known resources it's possible to find a collection of resources by
[searching the resource type end-point](http.html#search) with a [set of
criteria](search.html) describing the set of resources that should be retrieved, and their order. The
general pattern is:

```
  GET https://example.com/base/{resourceType}?criteria
```

The criteria is a set of HTTP parameters that specify which resources to return. The search operation

```
https://example.com/base/MedicationRequest?patient=347
```

returns all the prescriptions for the patient created above.

### 2.1.19.12 Search Response

The response to a search request is a [Bundle](bundle.html): a list of matching resources with some metadata:

```
HTTP/1.1 200 OK
Content-Length: 14523
Content-Type: application/fhir+xml
Last-Modified: Sun, 17 Aug 2014 15:49:30 GMT
 
{
  "resourceType": "Bundle",
  "type": "searchset",
  "id" : "eceb4882-5c7e-4ca4-af62-995dfb8cef01"
  "timestamp": "2014-08-19T15:49:30Z",
  "total": "3",
  "link": [
    {
      "relation" : "next",
      "url" : "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"
    }, {
      "relation" : "self",
      "url" : "https://example.com/base/MedicationRequest?patient=347"
    }
  ],
  "entry": [
    {
      "resource" : {
        "resourceType": "MedicationRequest",
        "id" : "3123",
        "meta" : {
          "versionId" : "1",
          "lastUpdated" : "2014-08-16T05:31:17Z"
        }, 
        ... content of resource ...
      }, 
    }, 
    ... 2 additional resources ....
  ]
}
```

Notes:

- **resourceType/type** (line 7/8) - the result of a search is always a bundle of type "searchset"
- **id** (line 9) - An identifier assigned to this particular bundle. The server should assign a unique id to this bundle that it will not be re-used
- **timestamp** (line 11) - (if the server supports versioning) This should match the HTTP header, and should be the date the search was executed, or more recent, depending on how the [server handles ongoing updates](search.html#currency). The timestamp must be the same or more recent than the most recent resource in the results
- **total** (line 13) - The total number of matches in the search results. Not the number of matches in this particular bundle, which may be a [paged view into the results](http.html#search)
- **link** (line 14) - A set of named links that give related contexts to this bundle. Names defined in this specification: [first](http.html#search), [prev](http.html#search), [next](http.html#search), [last](http.html#search), [self](http.html#search)
- **entry** (line 23) - Actual resources in this set of results
- **entry.resource.id** (line 25) - Note that in some bundles, the combination of the resource type and `entry.resource.id` must be [unique in the bundle](bundle.html#bundle-unique)
- The search operation is also able to [return additional related resources](search.html#include) as well

### 2.1.19.13 Update Request

The client sends the server a new version of the resource to replace the existing version - it PUTs it to the location of the existing resource:

```
  PUT https://example.com/base/{resourceType}/{id}
```

Note that there does not need to be a resource already existing at {id} - the server may elect to automatically create the resource at the specified address.
Here is an example of updating a patient:

```
PUT /base/Patient/f001 HTTP/1.1
Host: example.com
Content-Type: application/fhir+json
Content-Length: 1435
Accept: application/fhir+json
If-Match: 1
 
{
  "resourceType": "Patient",
  "id" : "347",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2014-08-18T15:43:30Z"    
  },
  ...
}
```

Notes:

- **resourceType** (line 1) - "Patient" in the URL must match the resource type in the resource (line 9)
- **resource id** (line 1, "347") - This must match the id in the resource (line 10)
- **If-Match** (line 6) - if this is provided, it must match the value in meta.versionId (line 12), and the server must check the version integrity, or return 412 if it does not support versions
- **meta.lastUpdated** (line 13) - This value is ignored, and will be updated by the server (mostly, but not always, if the server does not support versioning)
- **resource content** (line 14) - Not shown here, the same as Patient above

### 2.1.19.14 Update Response

The response to an update request has metadata / status, and optionally an OperationOutcome:

```
HTTP/1.1 200 OK
Content-Length: 161
Content-Type: application/fhir+json
Date: Mon, 18 Aug 2014 01:43:30 GMT
ETag: W/"2"
Location: https://example.com/base/Patient/f001/_history/2
 
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">The operation was successful</div>"
  }
}
```

Notes:

- **ETag** (line 5) - This is the versionId of the new version, and is also found in the location header (line 6) (if the server supports versioning)

### 2.1.19.15 Base Resource Content

Here is an example that shows all the information found in all resources, fully populated:

```
{
  "resourceType" : "X",
  "id" : "12",
  "meta" : {
    "versionId" : "12",
    "lastUpdated" : "2014-08-18T15:43:30Z",
    "profile" : ["http://example-consortium.org/fhir/profile/patient"],
    "security" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
      "code" : "EMP"
    }],
    "tag" : [{
      "system" : "http://example.com/codes/workflow",
      "code" : "needs-review"
    }]
  },
  "implicitRules" : "http://example-consortium.org/fhir/ehr-plugins",
  "language" : "X"
}
```

Implementers notes:

- **resourceType** (line 2) - always found in every resource. In XML, this is the name of the root element for the resource
- **id** (line 3) - defined when the resource is created, and never changed. Only missing when the resource is first created
- **meta.versionId** (line 5) - changes each time any resource contents change (except for the last 3 elements in meta - `profile`, `security` and `tag`)
- **meta.lastUpdated** (line 6) - Changes when the versionId changes. Systems that don't support versions usually don't track lastUpdated either
- **meta.profile** (line 7) - An assertion that the content conforms to a profile. See [Extending and Restricting Resources](profiling.html#resources) for further discussion. Can be changed as profiles and value sets change or the system rechecks conformance
- **meta.security** (lines 8 - 11) - [Security labels](security-labels.html) applied to this resource. These tags connect resources in specific ways to the overall security policy and infrastructure. Security tags can be updated when the resource changes, or whenever the security sub-system chooses to
- **meta.tag** (lines 12 - 16) - [Tags](resource.html#Meta) applied to this resource. Tags are used to relate resources to process and workflow. Applications are not required to consider the tags when interpreting the meaning of a resource
- **implicitRules** (line 17) - indicates that there is a [custom agreement](profiling.html#agreement) about how the resources are used that must be understood in order to safely process the resource. Use of this is discouraged because it restricts sharing, but sometimes necessary
- **language** (line 18) - The [base language of the resource](narrative.html#language). The resource is allowed to have content from other languages; this is just the base, but should be the main language of the resource

The base properties of all resources are defined on the resource types [Resource](resource.html) and [DomainResource](domainresource.html).

Want more information?

- [Getting Started](modules.html)
- [Resource Index](resourcelist.html)
- [Resource Guide](resourceguide.html)
- [Documentation Index](documentation.html)
- [Support Links ![icon](external.png)](https://confluence.hl7.org/display/FHIR/Implementer+Support)
