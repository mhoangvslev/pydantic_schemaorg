from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class SportsOrganization(SchemaOrgBase):
    """Represents the collection of all sports organizations, including sports teams, governing"
     "bodies, and sports associations.

    See: https://schema.org/SportsOrganization
    Model depth: 3
    """
    type_: str = Field(default="SportsOrganization", alias='@type')
    
    sport: Union[List[str], str] = Field(
        default=None,
        description="A type of sport (e.g. Baseball).",union_mode="smart"
    )
    
    actionableFeedbackPolicy: Union[List[str], str] = Field(
        default=None,
        description="For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement"
     "about public engagement activities (for news media, the newsroom’s), including involving"
     "the public - digitally or otherwise -- in coverage decisions, reporting and activities"
     "after publication.",union_mode="smart"
    )
    
    dissolutionDate: Union[List[str], str] = Field(
        default=None,
        description="The date that this organization was dissolved.",union_mode="smart"
    )
    
    funding: Union[List[str], str] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",union_mode="smart"
    )
    
    reviews: Union[List[str], str] = Field(
        default=None,
        description="Review of the item.",union_mode="smart"
    )
    
    memberOf: Union[List[str], str] = Field(
        default=None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",union_mode="smart"
    )
    
    event: Union[List[str], str] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",union_mode="smart"
    )
    
    foundingDate: Union[List[str], str] = Field(
        default=None,
        description="The date that this organization was founded.",union_mode="smart"
    )
    
    hasProductReturnPolicy: Union[List[str], str] = Field(
        default=None,
        description="Indicates a ProductReturnPolicy that may be applicable.",union_mode="smart"
    )
    
    foundingLocation: Union[List[str], str] = Field(
        default=None,
        description="The place where the Organization was founded.",union_mode="smart"
    )
    
    founder: Union[List[str], str] = Field(
        default=None,
        description="A person who founded this organization.",union_mode="smart"
    )
    
    employees: Union[List[str], str] = Field(
        default=None,
        description="People working for this organization.",union_mode="smart"
    )
    
    makesOffer: Union[List[str], str] = Field(
        default=None,
        description="A pointer to products or services offered by the organization or person.",union_mode="smart"
    )
    
    hasMerchantReturnPolicy: Union[List[str], str] = Field(
        default=None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",union_mode="smart"
    )
    
    telephone: Union[List[str], str] = Field(
        default=None,
        description="The telephone number.",union_mode="smart"
    )
    
    sponsor: Union[List[str], str] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",union_mode="smart"
    )
    
    diversityStaffingReport: Union[List[str], str] = Field(
        default=None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a report on staffing diversity issues. In a news context this might be for example ASNE"
     "or RTDNA (US) reports, or self-reported.",union_mode="smart"
    )
    
    numberOfEmployees: Union[List[str], str] = Field(
        default=None,
        description="The number of employees in an organization, e.g. business.",union_mode="smart"
    )
    
    owns: Union[List[str], str] = Field(
        default=None,
        description="Products owned by the organization or person.",union_mode="smart"
    )
    
    hasOfferCatalog: Union[List[str], str] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",union_mode="smart"
    )
    
    diversityPolicy: Union[List[str], str] = Field(
        default=None,
        description="Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]."
     "For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity"
     "policy on both staffing and sources, typically providing staffing data.",union_mode="smart"
    )
    
    nonprofitStatus: Union[List[str], str] = Field(
        default=None,
        description="nonprofitStatus indicates the legal status of a non-profit organization in its primary"
     "place of business.",union_mode="smart"
    )
    
    members: Union[List[str], str] = Field(
        default=None,
        description="A member of this organization.",union_mode="smart"
    )
    
    member: Union[List[str], str] = Field(
        default=None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
     "organizations; ProgramMembership is typically for individuals.",union_mode="smart"
    )
    
    legalName: Union[List[str], str] = Field(
        default=None,
        description="The official name of the organization, e.g. the registered company name.",union_mode="smart"
    )
    
    founders: Union[List[str], str] = Field(
        default=None,
        description="A person who founded this organization.",union_mode="smart"
    )
    
    globalLocationNumber: Union[List[str], str] = Field(
        default=None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",union_mode="smart"
    )
    
    correctionsPolicy: Union[List[str], str] = Field(
        default=None,
        description="For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing"
     "(in news media, the newsroom’s) disclosure and correction policy for errors.",union_mode="smart"
    )
    
    ethicsPolicy: Union[List[str], str] = Field(
        default=None,
        description="Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic"
     "and publishing practices, or of a [[Restaurant]], a page describing food source policies."
     "In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement"
     "describing the personal, organizational, and corporate standards of behavior expected"
     "by the organization.",union_mode="smart"
    )
    
    naics: Union[List[str], str] = Field(
        default=None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",union_mode="smart"
    )
    
    email: Union[List[str], str] = Field(
        default=None,
        description="Email address.",union_mode="smart"
    )
    
    unnamedSourcesPolicy: Union[List[str], str] = Field(
        default=None,
        description="For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about"
     "policy on use of unnamed sources and the decision process required.",union_mode="smart"
    )
    
    department: Union[List[str], str] = Field(
        default=None,
        description="A relationship between an organization and a department of that organization, also"
     "described as an organization (allowing different urls, logos, opening hours). For"
     "example: a store with a pharmacy, or a bakery with a cafe.",union_mode="smart"
    )
    
    vatID: Union[List[str], str] = Field(
        default=None,
        description="The Value-added Tax ID of the organization or person.",union_mode="smart"
    )
    
    parentOrganization: Union[List[str], str] = Field(
        default=None,
        description="The larger organization that this organization is a [[subOrganization]] of, if any.",union_mode="smart"
    )
    
    taxID: Union[List[str], str] = Field(
        default=None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",union_mode="smart"
    )
    
    faxNumber: Union[List[str], str] = Field(
        default=None,
        description="The fax number.",union_mode="smart"
    )
    
    knowsAbout: Union[List[str], str] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",union_mode="smart"
    )
    
    brand: Union[List[str], str] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",union_mode="smart"
    )
    
    aggregateRating: Union[List[str], str] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",union_mode="smart"
    )
    
    serviceArea: Union[List[str], str] = Field(
        default=None,
        description="The geographic area where the service is provided.",union_mode="smart"
    )
    
    interactionStatistic: Union[List[str], str] = Field(
        default=None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",union_mode="smart"
    )
    
    ownershipFundingInfo: Union[List[str], str] = Field(
        default=None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a description of organizational ownership structure; funding and grants. In a news/media"
     "setting, this is with particular reference to editorial independence. Note that the"
     "[[funder]] is also available and can be used to make basic funder information machine-readable.",union_mode="smart"
    )
    
    contactPoints: Union[List[str], str] = Field(
        default=None,
        description="A contact point for a person or organization.",union_mode="smart"
    )
    
    awards: Union[List[str], str] = Field(
        default=None,
        description="Awards won by or for this item.",union_mode="smart"
    )
    
    funder: Union[List[str], str] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",union_mode="smart"
    )
    
    leiCode: Union[List[str], str] = Field(
        default=None,
        description="An organization identifier that uniquely identifies a legal entity as defined in ISO"
     "17442.",union_mode="smart"
    )
    
    keywords: Union[List[str], str] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",union_mode="smart"
    )
    
    location: Union[List[str], str] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",union_mode="smart"
    )
    
    review: Union[List[str], str] = Field(
        default=None,
        description="A review of the item.",union_mode="smart"
    )
    
    agentInteractionStatistic: Union[List[str], str] = Field(
        default=None,
        description="The number of completed interactions for this entity, in a particular role (the 'agent'),"
     "in a particular action (indicated in the statistic), and in a particular context (i.e."
     "interactionService).",union_mode="smart"
    )
    
    subOrganization: Union[List[str], str] = Field(
        default=None,
        description="A relationship between two organizations where the first includes the second, e.g.,"
     "as a subsidiary. See also: the more specific 'department' property.",union_mode="smart"
    )
    
    seeks: Union[List[str], str] = Field(
        default=None,
        description="A pointer to products or services sought by the organization or person (demand).",union_mode="smart"
    )
    
    hasCredential: Union[List[str], str] = Field(
        default=None,
        description="A credential awarded to the Person or Organization.",union_mode="smart"
    )
    
    address: Union[List[str], str] = Field(
        default=None,
        description="Physical address of the item.",union_mode="smart"
    )
    
    contactPoint: Union[List[str], str] = Field(
        default=None,
        description="A contact point for a person or organization.",union_mode="smart"
    )
    
    knowsLanguage: Union[List[str], str] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",union_mode="smart"
    )
    
    alumni: Union[List[str], str] = Field(
        default=None,
        description="Alumni of an organization.",union_mode="smart"
    )
    
    hasPOS: Union[List[str], str] = Field(
        default=None,
        description="Points-of-Sales operated by the organization or person.",union_mode="smart"
    )
    
    areaServed: Union[List[str], str] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",union_mode="smart"
    )
    
    isicV4: Union[List[str], str] = Field(
        default=None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",union_mode="smart"
    )
    
    employee: Union[List[str], str] = Field(
        default=None,
        description="Someone working for this organization.",union_mode="smart"
    )
    
    duns: Union[List[str], str] = Field(
        default=None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",union_mode="smart"
    )
    
    award: Union[List[str], str] = Field(
        default=None,
        description="An award won by or for this item.",union_mode="smart"
    )
    
    publishingPrinciples: Union[List[str], str] = Field(
        default=None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]]"
     "writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity"
     "policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles"
     "are those of the party primarily responsible for the creation of the [[CreativeWork]]."
     "While such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",union_mode="smart"
    )
    
    slogan: Union[List[str], str] = Field(
        default=None,
        description="A slogan or motto associated with the item.",union_mode="smart"
    )
    
    iso6523Code: Union[List[str], str] = Field(
        default=None,
        description="An organization identifier as defined in ISO 6523(-1). Note that many existing organization"
     "identifiers such as [leiCode](http://schema.org/leiCode), [duns](http://schema.org/duns)"
     "and [vatID](http://schema.org/vatID) can be expressed as an ISO 6523 identifier by"
     "setting the ICD part of the ISO 6523 identifier accordingly.",union_mode="smart"
    )
    
    logo: Union[List[str], str] = Field(
        default=None,
        description="An associated logo.",union_mode="smart"
    )
    
    events: Union[List[str], str] = Field(
        default=None,
        description="Upcoming or past events associated with this place or organization.",union_mode="smart"
    )
    
    subjectOf: Union[List[str], str] = Field(
        default=None,
        description="A CreativeWork or Event about this Thing.",union_mode="smart"
    )
    
    mainEntityOfPage: Union[List[str], str] = Field(
        default=None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",union_mode="smart"
    )
    
    identifier: Union[List[str], str] = Field(
        default=None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",union_mode="smart"
    )
    
    image: Union[List[str], str] = Field(
        default=None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",union_mode="smart"
    )
    
    name: Union[List[str], str] = Field(
        default=None,
        description="The name of the item.",union_mode="smart"
    )
    
    url: Union[List[str], str] = Field(
        default=None,
        description="URL of the item.",union_mode="smart"
    )
    
    sameAs: Union[List[str], str] = Field(
        default=None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",union_mode="smart"
    )
    
    disambiguatingDescription: Union[List[str], str] = Field(
        default=None,
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",union_mode="smart"
    )
    
    alternateName: Union[List[str], str] = Field(
        default=None,
        description="An alias for the item.",union_mode="smart"
    )
    
    description: Union[List[str], str] = Field(
        default=None,
        description="A description of the item.",union_mode="smart"
    )
    
    potentialAction: Union[List[str], str] = Field(
        default=None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",union_mode="smart"
    )
    
    additionalType: Union[List[str], str] = Field(
        default=None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. Typically the value is a URI-identified RDF class, and in this case"
     "corresponds to the use of rdf:type in RDF. Text values can be used sparingly, for cases"
     "where useful information can be added without their being an appropriate schema to reference."
     "In the case of text values, the class label should follow the schema.org <a href=\"http://schema.org/docs/styleguide.html\">style"
     "guide</a>.",union_mode="smart"
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg import Text, URL, AnyUrl
    from pydantic_schemaorg import Grant, GeoShape, NonprofitType, Offer, Thing, Person, ProductReturnPolicy, Brand, ProgramMembership, AboutPage, DefinedTerm, date, OwnershipInfo, Text, EducationalOccupationalCredential, AggregateRating, ImageObject, CreativeWork, Language, Organization, MerchantReturnPolicy, Product, Demand, Date, URL, Place, AdministrativeArea, PostalAddress, InteractionCounter, Event, Review, AnyUrl, QuantitativeValue, OfferCatalog, VirtualLocation, ContactPoint, Article
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
