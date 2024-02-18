from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class ProductCollection(SchemaOrgBase):
    """A set of products (either [[ProductGroup]]s or specific variants) that are listed together"
     "e.g. in an [[Offer]].

    See: https://schema.org/ProductCollection
    Model depth: 3
    """
    type_: str = Field(default="ProductCollection", alias='@type')
    
    includesObject: Union[List[str], str] = Field(
        default=None,
        description="This links to a node or nodes indicating the exact quantity of the products included in"
     "an [[Offer]] or [[ProductCollection]].",union_mode="smart"
    )
    
    collectionSize: Union[List[str], str] = Field(
        default=None,
        description="The number of items in the [[Collection]].",union_mode="smart"
    )
    
    archivedAt: Union[List[str], str] = Field(
        default=None,
        description="Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case"
     "of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible,"
     "but be archived by archival, journalistic, activist, or law enforcement organizations."
     "In such cases, the referenced page may not directly publish the content.",union_mode="smart"
    )
    
    fileFormat: Union[List[str], str] = Field(
        default=None,
        description="Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml))"
     "of the content, e.g. application/zip of a SoftwareApplication binary. In cases where"
     "a CreativeWork has several media type representations, 'encoding' can be used to indicate"
     "each MediaObject alongside particular fileFormat information. Unregistered or niche"
     "file formats can be indicated instead via the most appropriate URL, e.g. defining Web"
     "page or a Wikipedia entry.",union_mode="smart"
    )
    
    pattern: Union[List[str], str] = Field(
        default=None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",union_mode="smart"
    )
    
    audio: Union[List[str], str] = Field(
        default=None,
        description="An embedded audio object.",union_mode="smart"
    )
    
    expires: Union[List[str], str] = Field(
        default=None,
        description="Date the content expires and is no longer useful or available. For example a [[VideoObject]]"
     "or [[NewsArticle]] whose availability or relevance is time-limited, or a [[ClaimReview]]"
     "fact check whose publisher wants to indicate that it may no longer be relevant (or helpful"
     "to highlight) after some date.",union_mode="smart"
    )
    
    funding: Union[List[str], str] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",union_mode="smart"
    )
    
    text: Union[List[str], str] = Field(
        default=None,
        description="The textual content of this CreativeWork.",union_mode="smart"
    )
    
    reviews: Union[List[str], str] = Field(
        default=None,
        description="Review of the item.",union_mode="smart"
    )
    
    isAccessibleForFree: Union[List[str], str] = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",union_mode="smart"
    )
    
    publication: Union[List[str], str] = Field(
        default=None,
        description="A publication event associated with the item.",union_mode="smart"
    )
    
    accessibilitySummary: Union[List[str], str] = Field(
        default=None,
        description="A human-readable summary of specific accessibility features or deficiencies, consistent"
     "with the other accessibility metadata but expressing subtleties such as \"short descriptions"
     "are present but long descriptions will be needed for non-visual users\" or \"short descriptions"
     "are present and no long descriptions are needed\".",union_mode="smart"
    )
    
    teaches: Union[List[str], str] = Field(
        default=None,
        description="The item being described is intended to help a person learn the competency or learning"
     "outcome defined by the referenced term.",union_mode="smart"
    )
    
    accountablePerson: Union[List[str], str] = Field(
        default=None,
        description="Specifies the Person that is legally accountable for the CreativeWork.",union_mode="smart"
    )
    
    temporal: Union[List[str], str] = Field(
        default=None,
        description="The \"temporal\" property can be used in cases where more specific properties (e.g."
     "[[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]])"
     "are not known to be appropriate.",union_mode="smart"
    )
    
    size: Union[List[str], str] = Field(
        default=None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",union_mode="smart"
    )
    
    about: Union[List[str], str] = Field(
        default=None,
        description="The subject matter of the content.",union_mode="smart"
    )
    
    exampleOfWork: Union[List[str], str] = Field(
        default=None,
        description="A creative work that this work is an example/instance/realization/derivation of.",union_mode="smart"
    )
    
    translationOfWork: Union[List[str], str] = Field(
        default=None,
        description="The work that this work has been translated from. E.g. 物种起源 is a translationOf “On the"
     "Origin of Species”.",union_mode="smart"
    )
    
    locationCreated: Union[List[str], str] = Field(
        default=None,
        description="The location where the CreativeWork was created, which may not be the same as the location"
     "depicted in the CreativeWork.",union_mode="smart"
    )
    
    sdPublisher: Union[List[str], str] = Field(
        default=None,
        description="Indicates the party responsible for generating and publishing the current structured"
     "data markup, typically in cases where the structured data is derived automatically"
     "from existing published content but published on a different site. For example, student"
     "projects and open data initiatives often re-publish existing content with more explicitly"
     "structured metadata. The [[sdPublisher]] property helps make such practices more"
     "explicit.",union_mode="smart"
    )
    
    sponsor: Union[List[str], str] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",union_mode="smart"
    )
    
    abstract: Union[List[str], str] = Field(
        default=None,
        description="An abstract is a short description that summarizes a [[CreativeWork]].",union_mode="smart"
    )
    
    schemaVersion: Union[List[str], str] = Field(
        default=None,
        description="Indicates (by URL or string) a particular version of a schema used in some CreativeWork."
     "This property was created primarily to indicate the use of a specific schema.org release,"
     "e.g. ```10.0``` as a simple string, or more explicitly via URL, ```http://schema.org/docs/releases.html#v10.0```."
     "There may be situations in which other schemas might usefully be referenced this way,"
     "e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/```"
     "but this has not been carefully explored in the community.",union_mode="smart"
    )
    
    workTranslation: Union[List[str], str] = Field(
        default=None,
        description="A work that is a translation of the content of this work. E.g. 西遊記 has an English workTranslation"
     "“Journey to the West”, a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese"
     "translation Tây du ký bình khảo.",union_mode="smart"
    )
    
    creditText: Union[List[str], str] = Field(
        default=None,
        description="Text that can be used to credit person(s) and/or organization(s) associated with a published"
     "Creative Work.",union_mode="smart"
    )
    
    educationalUse: Union[List[str], str] = Field(
        default=None,
        description="The purpose of a work in the context of education; for example, 'assignment', 'group"
     "work'.",union_mode="smart"
    )
    
    assesses: Union[List[str], str] = Field(
        default=None,
        description="The item being described is intended to assess the competency or learning outcome defined"
     "by the referenced term.",union_mode="smart"
    )
    
    discussionUrl: Union[List[str], str] = Field(
        default=None,
        description="A link to the page containing the comments of the CreativeWork.",union_mode="smart"
    )
    
    accessibilityHazard: Union[List[str], str] = Field(
        default=None,
        description="A characteristic of the described resource that is physiologically dangerous to some"
     "users. Related to WCAG 2.0 guideline 2.3. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityHazard-vocabulary).",union_mode="smart"
    )
    
    workExample: Union[List[str], str] = Field(
        default=None,
        description="Example/instance/realization/derivation of the concept of this creative work. E.g."
     "the paperback edition, first edition, or e-book.",union_mode="smart"
    )
    
    usageInfo: Union[List[str], str] = Field(
        default=None,
        description="The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]."
     "This property is applicable both to works that are freely available and to those that"
     "require payment or other transactions. It can reference additional information, e.g."
     "community expectations on preferred linking and citation conventions, as well as purchasing"
     "details. For something that can be commercially licensed, usageInfo can provide detailed,"
     "resource-specific information about licensing options. This property can be used"
     "alongside the license property which indicates license(s) applicable to some piece"
     "of content. The usageInfo property can provide information about other licensing options,"
     "e.g. acquiring commercial usage rights for an image that is also available under non-commercial"
     "creative commons licenses.",union_mode="smart"
    )
    
    license: Union[List[str], str] = Field(
        default=None,
        description="A license document that applies to this content, typically indicated by URL.",union_mode="smart"
    )
    
    inLanguage: Union[List[str], str] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",union_mode="smart"
    )
    
    offers: Union[List[str], str] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",union_mode="smart"
    )
    
    countryOfOrigin: Union[List[str], str] = Field(
        default=None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",union_mode="smart"
    )
    
    mentions: Union[List[str], str] = Field(
        default=None,
        description="Indicates that the CreativeWork contains a reference to, but is not necessarily about"
     "a concept.",union_mode="smart"
    )
    
    producer: Union[List[str], str] = Field(
        default=None,
        description="The person or organization who produced the work (e.g. music album, movie, TV/radio"
     "series etc.).",union_mode="smart"
    )
    
    publisherImprint: Union[List[str], str] = Field(
        default=None,
        description="The publishing division which published the comic.",union_mode="smart"
    )
    
    learningResourceType: Union[List[str], str] = Field(
        default=None,
        description="The predominant type or kind characterizing the learning resource. For example, 'presentation',"
     "'handout'.",union_mode="smart"
    )
    
    author: Union[List[str], str] = Field(
        default=None,
        description="The author of this content or rating. Please note that author is special in that HTML 5"
     "provides a special mechanism for indicating authorship via the rel tag. That is equivalent"
     "to this and may be used interchangeably.",union_mode="smart"
    )
    
    dateCreated: Union[List[str], str] = Field(
        default=None,
        description="The date on which the CreativeWork was created or the item was added to a DataFeed.",union_mode="smart"
    )
    
    isPartOf: Union[List[str], str] = Field(
        default=None,
        description="Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is"
     "part of.",union_mode="smart"
    )
    
    character: Union[List[str], str] = Field(
        default=None,
        description="Fictional person connected with a creative work.",union_mode="smart"
    )
    
    audience: Union[List[str], str] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",union_mode="smart"
    )
    
    educationalLevel: Union[List[str], str] = Field(
        default=None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",union_mode="smart"
    )
    
    accessibilityControl: Union[List[str], str] = Field(
        default=None,
        description="Identifies input methods that are sufficient to fully control the described resource."
     "Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityControl-vocabulary).",union_mode="smart"
    )
    
    isFamilyFriendly: Union[List[str], str] = Field(
        default=None,
        description="Indicates whether this content is family friendly.",union_mode="smart"
    )
    
    position: Union[List[str], str] = Field(
        default=None,
        description="The position of an item in a series or sequence of items.",union_mode="smart"
    )
    
    conditionsOfAccess: Union[List[str], str] = Field(
        default=None,
        description="Conditions that affect the availability of, or method(s) of access to, an item. Typically"
     "used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]."
     "This property is not suitable for use as a general Web access control mechanism. It is"
     "expressed only in natural language. For example \"Available by appointment from the"
     "Reading Room\" or \"Accessible only from logged-in accounts \".",union_mode="smart"
    )
    
    datePublished: Union[List[str], str] = Field(
        default=None,
        description="Date of first broadcast/publication.",union_mode="smart"
    )
    
    temporalCoverage: Union[List[str], str] = Field(
        default=None,
        description="The temporalCoverage of a CreativeWork indicates the period that the content applies"
     "to, i.e. that it describes, either as a DateTime or as a textual string indicating a time"
     "period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)."
     "In the case of a Dataset it will typically indicate the relevant time period in a precise"
     "notation (e.g. for a 2011 census dataset, the year 2011 would be written \"2011/2012\")."
     "Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate"
     "their temporalCoverage in broader terms - textually or via well-known URL. Written"
     "works such as books may sometimes have precise temporal coverage too, e.g. a work set"
     "in 1939 - 1945 can be indicated in ISO 8601 interval format format via \"1939/1945\"."
     "Open-ended date ranges can be written with \"..\" in place of the end date. For example,"
     "\"2015-11/..\" indicates a range beginning in November 2015 and with no specified final"
     "date. This is tentative and might be updated in future when ISO 8601 is officially updated.",union_mode="smart"
    )
    
    contentLocation: Union[List[str], str] = Field(
        default=None,
        description="The location depicted or described in the content. For example, the location in a photograph"
     "or painting.",union_mode="smart"
    )
    
    creativeWorkStatus: Union[List[str], str] = Field(
        default=None,
        description="The status of a creative work in terms of its stage in a lifecycle. Example terms include"
     "Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for"
     "the stages of their publication lifecycle.",union_mode="smart"
    )
    
    contentReferenceTime: Union[List[str], str] = Field(
        default=None,
        description="The specific time described by a creative work, for works (e.g. articles, video objects"
     "etc.) that emphasise a particular moment within an Event.",union_mode="smart"
    )
    
    spatialCoverage: Union[List[str], str] = Field(
        default=None,
        description="The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of"
     "the content. It is a subproperty of contentLocation intended primarily for more technical"
     "and detailed materials. For example with a Dataset, it indicates areas that the dataset"
     "describes: a dataset of New York weather would have spatialCoverage which was the place:"
     "the state of New York.",union_mode="smart"
    )
    
    encoding: Union[List[str], str] = Field(
        default=None,
        description="A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.",union_mode="smart"
    )
    
    editEIDR: Union[List[str], str] = Field(
        default=None,
        description="An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]]"
     "representing a specific edit / edition for a work of film or television. For example,"
     "the motion picture known as \"Ghostbusters\" whose [[titleEIDR]] is \"10.5240/7EC7-228A-510A-053E-CBB8-J\""
     "has several edits, e.g. \"10.5240/1F2A-E1C5-680A-14C6-E76B-I\" and \"10.5240/8A35-3BEE-6497-5D12-9E4F-3\"."
     "Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and"
     "their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general"
     "description), or alongside [[editEIDR]] for a more edit-specific description.",union_mode="smart"
    )
    
    copyrightHolder: Union[List[str], str] = Field(
        default=None,
        description="The party holding the legal copyright to the CreativeWork.",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    dateModified: Union[List[str], str] = Field(
        default=None,
        description="The date on which the CreativeWork was most recently modified or when the item's entry"
     "was modified within a DataFeed.",union_mode="smart"
    )
    
    citation: Union[List[str], str] = Field(
        default=None,
        description="A citation or reference to another creative work, such as another publication, web page,"
     "scholarly article, etc.",union_mode="smart"
    )
    
    editor: Union[List[str], str] = Field(
        default=None,
        description="Specifies the Person who edited the CreativeWork.",union_mode="smart"
    )
    
    mainEntity: Union[List[str], str] = Field(
        default=None,
        description="Indicates the primary entity described in some page or other CreativeWork.",union_mode="smart"
    )
    
    thumbnail: Union[List[str], str] = Field(
        default=None,
        description="Thumbnail image for an image or video.",union_mode="smart"
    )
    
    copyrightNotice: Union[List[str], str] = Field(
        default=None,
        description="Text of a notice appropriate for describing the copyright aspects of this Creative Work,"
     "ideally indicating the owner of the copyright for the Work.",union_mode="smart"
    )
    
    timeRequired: Union[List[str], str] = Field(
        default=None,
        description="Approximate or typical time it usually takes to work with or through the content of this"
     "work for the typical or target audience.",union_mode="smart"
    )
    
    typicalAgeRange: Union[List[str], str] = Field(
        default=None,
        description="The typical expected age range, e.g. '7-9', '11-'.",union_mode="smart"
    )
    
    educationalAlignment: Union[List[str], str] = Field(
        default=None,
        description="An alignment to an established educational framework. This property should not be used"
     "where the nature of the alignment can be described using a simple property, for example"
     "to express that a resource [[teaches]] or [[assesses]] a competency.",union_mode="smart"
    )
    
    isBasedOnUrl: Union[List[str], str] = Field(
        default=None,
        description="A resource that was used in the creation of this resource. This term can be repeated for"
     "multiple sources. For example, http://example.com/great-multiplication-intro.html.",union_mode="smart"
    )
    
    aggregateRating: Union[List[str], str] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",union_mode="smart"
    )
    
    headline: Union[List[str], str] = Field(
        default=None,
        description="Headline of the article.",union_mode="smart"
    )
    
    interactionStatistic: Union[List[str], str] = Field(
        default=None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",union_mode="smart"
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
    
    publisher: Union[List[str], str] = Field(
        default=None,
        description="The publisher of the creative work.",union_mode="smart"
    )
    
    acquireLicensePage: Union[List[str], str] = Field(
        default=None,
        description="Indicates a page documenting how licenses can be purchased or otherwise acquired, for"
     "the current item.",union_mode="smart"
    )
    
    commentCount: Union[List[str], str] = Field(
        default=None,
        description="The number of comments this CreativeWork (e.g. Article, Question or Answer) has received."
     "This is most applicable to works published in Web sites with commenting system; additional"
     "comments may exist elsewhere.",union_mode="smart"
    )
    
    keywords: Union[List[str], str] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",union_mode="smart"
    )
    
    copyrightYear: Union[List[str], str] = Field(
        default=None,
        description="The year during which the claimed copyright for the CreativeWork was first asserted.",union_mode="smart"
    )
    
    creator: Union[List[str], str] = Field(
        default=None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
     "CreativeWork.",union_mode="smart"
    )
    
    associatedMedia: Union[List[str], str] = Field(
        default=None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",union_mode="smart"
    )
    
    material: Union[List[str], str] = Field(
        default=None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",union_mode="smart"
    )
    
    version: Union[List[str], str] = Field(
        default=None,
        description="The version of the CreativeWork embodied by a specified resource.",union_mode="smart"
    )
    
    review: Union[List[str], str] = Field(
        default=None,
        description="A review of the item.",union_mode="smart"
    )
    
    isBasedOn: Union[List[str], str] = Field(
        default=None,
        description="A resource from which this work is derived or from which it is a modification or adaptation.",union_mode="smart"
    )
    
    accessModeSufficient: Union[List[str], str] = Field(
        default=None,
        description="A list of single or combined accessModes that are sufficient to understand all the intellectual"
     "content of a resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary).",union_mode="smart"
    )
    
    accessMode: Union[List[str], str] = Field(
        default=None,
        description="The human sensory perceptual system or cognitive faculty through which a person may"
     "process or perceive information. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessMode-vocabulary).",union_mode="smart"
    )
    
    alternativeHeadline: Union[List[str], str] = Field(
        default=None,
        description="A secondary title of the CreativeWork.",union_mode="smart"
    )
    
    interactivityType: Union[List[str], str] = Field(
        default=None,
        description="The predominant mode of learning supported by the learning resource. Acceptable values"
     "are 'active', 'expositive', or 'mixed'.",union_mode="smart"
    )
    
    translator: Union[List[str], str] = Field(
        default=None,
        description="Organization or person who adapts a creative work to different languages, regional"
     "differences and technical requirements of a target market, or that translates during"
     "some event.",union_mode="smart"
    )
    
    contributor: Union[List[str], str] = Field(
        default=None,
        description="A secondary contributor to the CreativeWork or Event.",union_mode="smart"
    )
    
    materialExtent: Union[List[str], str] = Field(
        default=None,
        description="The quantity of the materials being described or an expression of the physical space"
     "they occupy.",union_mode="smart"
    )
    
    comment: Union[List[str], str] = Field(
        default=None,
        description="Comments, typically from users.",union_mode="smart"
    )
    
    encodings: Union[List[str], str] = Field(
        default=None,
        description="A media object that encodes this CreativeWork.",union_mode="smart"
    )
    
    hasPart: Union[List[str], str] = Field(
        default=None,
        description="Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some"
     "sense).",union_mode="smart"
    )
    
    thumbnailUrl: Union[List[str], str] = Field(
        default=None,
        description="A thumbnail image relevant to the Thing.",union_mode="smart"
    )
    
    accessibilityAPI: Union[List[str], str] = Field(
        default=None,
        description="Indicates that the resource is compatible with the referenced accessibility API. Values"
     "should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityAPI-vocabulary).",union_mode="smart"
    )
    
    sdLicense: Union[List[str], str] = Field(
        default=None,
        description="A license document that applies to this structured data, typically indicated by URL.",union_mode="smart"
    )
    
    video: Union[List[str], str] = Field(
        default=None,
        description="An embedded video object.",union_mode="smart"
    )
    
    correction: Union[List[str], str] = Field(
        default=None,
        description="Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]],"
     "textually or in another document.",union_mode="smart"
    )
    
    interpretedAsClaim: Union[List[str], str] = Field(
        default=None,
        description="Used to indicate a specific claim contained, implied, translated or refined from the"
     "content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can"
     "be indicated using [[claimInterpreter]].",union_mode="smart"
    )
    
    releasedEvent: Union[List[str], str] = Field(
        default=None,
        description="The place and time the release was issued, expressed as a PublicationEvent.",union_mode="smart"
    )
    
    maintainer: Union[List[str], str] = Field(
        default=None,
        description="A maintainer of a [[Dataset]], software package ([[SoftwareApplication]]), or other"
     "[[Project]]. A maintainer is a [[Person]] or [[Organization]] that manages contributions"
     "to, and/or publication of, some (typically complex) artifact. It is common for distributions"
     "of software and data to be based on \"upstream\" sources. When [[maintainer]] is applied"
     "to a specific version of something e.g. a particular version or packaging of a [[Dataset]],"
     "it is always possible that the upstream source has a different maintainer. The [[isBasedOn]]"
     "property can be used to indicate such relationships between datasets to make the different"
     "maintenance roles clear. Similarly in the case of software, a package may have dedicated"
     "maintainers working on integration into software distributions such as Ubuntu, as"
     "well as upstream maintainers of the underlying work.",union_mode="smart"
    )
    
    sdDatePublished: Union[List[str], str] = Field(
        default=None,
        description="Indicates the date on which the current structured data was generated / published. Typically"
     "used alongside [[sdPublisher]].",union_mode="smart"
    )
    
    accessibilityFeature: Union[List[str], str] = Field(
        default=None,
        description="Content features of the resource, such as accessible media, alternatives and supported"
     "enhancements for accessibility. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityFeature-vocabulary).",union_mode="smart"
    )
    
    contentRating: Union[List[str], str] = Field(
        default=None,
        description="Official rating of a piece of content&#x2014;for example, 'MPAA PG-13'.",union_mode="smart"
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
    
    genre: Union[List[str], str] = Field(
        default=None,
        description="Genre of the creative work, broadcast channel or group.",union_mode="smart"
    )
    
    spatial: Union[List[str], str] = Field(
        default=None,
        description="The \"spatial\" property can be used in cases when more specific properties (e.g. [[locationCreated]],"
     "[[spatialCoverage]], [[contentLocation]]) are not known to be appropriate.",union_mode="smart"
    )
    
    encodingFormat: Union[List[str], str] = Field(
        default=None,
        description="Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)"
     "and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)),"
     "e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc. In"
     "cases where a [[CreativeWork]] has several media type representations, [[encoding]]"
     "can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]]"
     "information. Unregistered or niche encoding and file formats can be indicated instead"
     "via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.",union_mode="smart"
    )
    
    sourceOrganization: Union[List[str], str] = Field(
        default=None,
        description="The Organization on whose behalf the creator was working.",union_mode="smart"
    )
    
    recordedAt: Union[List[str], str] = Field(
        default=None,
        description="The Event where the CreativeWork was recorded. The CreativeWork may capture all or part"
     "of the event.",union_mode="smart"
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
    
    manufacturer: Union[List[str], str] = Field(
        default=None,
        description="The manufacturer of the product.",union_mode="smart"
    )
    
    gtin12: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12"
     "is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference,"
     "and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",union_mode="smart"
    )
    
    releaseDate: Union[List[str], str] = Field(
        default=None,
        description="The release date of a product or product model. This can be used to distinguish the exact"
     "variant of a product.",union_mode="smart"
    )
    
    mobileUrl: Union[List[str], str] = Field(
        default=None,
        description="The [[mobileUrl]] property is provided for specific situations in which data consumers"
     "need to determine whether one of several provided URLs is a dedicated 'mobile site'."
     "To discourage over-use, and reflecting intial usecases, the property is expected only"
     "on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology"
     "is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design)"
     "in which content can be flexibly adapted to a wide range of browsing environments. Pages"
     "and sites referenced with the long-established [[url]] property should ideally also"
     "be usable on a wide variety of devices, including mobile phones. In most cases, it would"
     "be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]]"
     "for more mobile-oriented pages. The property is intended for the case when items (primarily"
     "[[Product]] and [[Offer]]) have extra URLs hosted on an additional \"mobile site\""
     "alongside the main one. It should not be taken as an endorsement of this publication style.",union_mode="smart"
    )
    
    hasProductReturnPolicy: Union[List[str], str] = Field(
        default=None,
        description="Indicates a ProductReturnPolicy that may be applicable.",union_mode="smart"
    )
    
    countryOfAssembly: Union[List[str], str] = Field(
        default=None,
        description="The place where the product was assembled.",union_mode="smart"
    )
    
    productID: Union[List[str], str] = Field(
        default=None,
        description="The product identifier, such as ISBN. For example: ``` meta itemprop=\"productID\""
     "content=\"isbn:123-456-789\" ```.",union_mode="smart"
    )
    
    height: Union[List[str], str] = Field(
        default=None,
        description="The height of the item.",union_mode="smart"
    )
    
    hasMerchantReturnPolicy: Union[List[str], str] = Field(
        default=None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",union_mode="smart"
    )
    
    category: Union[List[str], str] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",union_mode="smart"
    )
    
    mpn: Union[List[str], str] = Field(
        default=None,
        description="The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.",union_mode="smart"
    )
    
    isAccessoryOrSparePartFor: Union[List[str], str] = Field(
        default=None,
        description="A pointer to another product (or multiple products) for which this product is an accessory"
     "or spare part.",union_mode="smart"
    )
    
    sku: Union[List[str], str] = Field(
        default=None,
        description="The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service,"
     "or the product to which the offer refers.",union_mode="smart"
    )
    
    weight: Union[List[str], str] = Field(
        default=None,
        description="The weight of the product or person.",union_mode="smart"
    )
    
    width: Union[List[str], str] = Field(
        default=None,
        description="The width of the item.",union_mode="smart"
    )
    
    gtin14: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN"
     "Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",union_mode="smart"
    )
    
    positiveNotes: Union[List[str], str] = Field(
        default=None,
        description="Provides positive considerations regarding something, for example product highlights"
     "or (alongside [[negativeNotes]]) pro/con lists for reviews. In the case of a [[Review]],"
     "the property describes the [[itemReviewed]] from the perspective of the review; in"
     "the case of a [[Product]], the product itself is being described. The property values"
     "can be expressed either as unstructured text (repeated as necessary), or if ordered,"
     "as a list (in which case the most positive is at the beginning of the list).",union_mode="smart"
    )
    
    brand: Union[List[str], str] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",union_mode="smart"
    )
    
    isRelatedTo: Union[List[str], str] = Field(
        default=None,
        description="A pointer to another, somehow related product (or multiple products).",union_mode="smart"
    )
    
    inProductGroupWithID: Union[List[str], str] = Field(
        default=None,
        description="Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]].",union_mode="smart"
    )
    
    isVariantOf: Union[List[str], str] = Field(
        default=None,
        description="Indicates the kind of product that this is a variant of. In the case of [[ProductModel]],"
     "this is a pointer (from a ProductModel) to a base product from which this product is a variant."
     "It is safe to infer that the variant inherits all product features from the base model,"
     "unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the"
     "group description also serves as a template, representing a set of Products that vary"
     "on explicitly defined, specific dimensions only (so it defines both a set of variants,"
     "as well as which values distinguish amongst those variants). When used with [[ProductGroup]],"
     "this property can apply to any [[Product]] included in the group.",union_mode="smart"
    )
    
    model: Union[List[str], str] = Field(
        default=None,
        description="The model of the product. Use with the URL of a ProductModel or a textual representation"
     "of the model identifier. The URL of the ProductModel can be from an external source. It"
     "is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14"
     "and mpn properties.",union_mode="smart"
    )
    
    additionalProperty: Union[List[str], str] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g."
     "a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. http://schema.org/width, http://schema.org/color,"
     "http://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",union_mode="smart"
    )
    
    hasEnergyConsumptionDetails: Union[List[str], str] = Field(
        default=None,
        description="Defines the energy efficiency Category (also known as \"class\" or \"rating\") for"
     "a product according to an international energy efficiency standard.",union_mode="smart"
    )
    
    itemCondition: Union[List[str], str] = Field(
        default=None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",union_mode="smart"
    )
    
    color: Union[List[str], str] = Field(
        default=None,
        description="The color of the product.",union_mode="smart"
    )
    
    gtin8: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also"
     "known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",union_mode="smart"
    )
    
    nsn: Union[List[str], str] = Field(
        default=None,
        description="Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number)"
     "(nsn) of a [[Product]].",union_mode="smart"
    )
    
    purchaseDate: Union[List[str], str] = Field(
        default=None,
        description="The date the item, e.g. vehicle, was purchased by the current owner.",union_mode="smart"
    )
    
    hasMeasurement: Union[List[str], str] = Field(
        default=None,
        description="A product measurement, for example the inseam of pants, the wheel size of a bicycle, or"
     "the gauge of a screw. Usually an exact measurement, but can also be a range of measurements"
     "for adjustable products, for example belts and ski bindings.",union_mode="smart"
    )
    
    negativeNotes: Union[List[str], str] = Field(
        default=None,
        description="Provides negative considerations regarding something, most typically in pro/con"
     "lists for reviews (alongside [[positiveNotes]]). For symmetry In the case of a [[Review]],"
     "the property describes the [[itemReviewed]] from the perspective of the review; in"
     "the case of a [[Product]], the product itself is being described. Since product descriptions"
     "tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]]"
     "used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used"
     "on [[Product]]. The property values can be expressed either as unstructured text (repeated"
     "as necessary), or if ordered, as a list (in which case the most negative is at the beginning"
     "of the list).",union_mode="smart"
    )
    
    gtin: Union[List[str], str] = Field(
        default=None,
        description="A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin))."
     "GTINs identify trade items, including products and services, using numeric identification"
     "codes. The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/)"
     "express GTINs as URLs (URIs, IRIs, etc.). Details including regular expression examples"
     "can be found in, Section 6 of the GS1 URI Syntax specification; see also [schema.org tracking"
     "issue](https://github.com/schemaorg/schemaorg/issues/3156#issuecomment-1209522809)"
     "for schema.org-specific discussion. A correct [[gtin]] value should be a valid GTIN,"
     "which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or"
     "a \"GS1 Digital Link\" URL based on such a string. The numeric component should also have"
     "a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)"
     "and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for"
     "more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]]"
     "property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]]"
     "properties. Note also that this is a definition for how to include GTINs in Schema.org"
     "data, and not a definition of GTINs in general - see the GS1 documentation for authoritative"
     "details.",union_mode="smart"
    )
    
    isConsumableFor: Union[List[str], str] = Field(
        default=None,
        description="A pointer to another product (or multiple products) for which this product is a consumable.",union_mode="smart"
    )
    
    depth: Union[List[str], str] = Field(
        default=None,
        description="The depth of the item.",union_mode="smart"
    )
    
    gtin13: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent"
     "to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into"
     "a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",union_mode="smart"
    )
    
    productionDate: Union[List[str], str] = Field(
        default=None,
        description="The date of production of the item, e.g. vehicle.",union_mode="smart"
    )
    
    countryOfLastProcessing: Union[List[str], str] = Field(
        default=None,
        description="The place where the item (typically [[Product]]) was last processed and tested before"
     "importation.",union_mode="smart"
    )
    
    hasAdultConsideration: Union[List[str], str] = Field(
        default=None,
        description="Used to tag an item to be intended or suitable for consumption or use by adults only.",union_mode="smart"
    )
    
    asin: Union[List[str], str] = Field(
        default=None,
        description="An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique"
     "identifier assigned by Amazon.com and its partners for product identification within"
     "the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s"
     "article). Note also that this is a definition for how to include ASINs in Schema.org data,"
     "and not a definition of ASINs in general - see documentation from Amazon for authoritative"
     "details. ASINs are most commonly encoded as text strings, but the [asin] property supports"
     "URL/URI as potential values too.",union_mode="smart"
    )
    
    slogan: Union[List[str], str] = Field(
        default=None,
        description="A slogan or motto associated with the item.",union_mode="smart"
    )
    
    logo: Union[List[str], str] = Field(
        default=None,
        description="An associated logo.",union_mode="smart"
    )
    
    isSimilarTo: Union[List[str], str] = Field(
        default=None,
        description="A pointer to another, functionally similar product (or multiple products).",union_mode="smart"
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg import TypeAndQuantityNode
    from pydantic_schemaorg import Integer, int
    from pydantic_schemaorg import Grant, datetime, DateTime, CorrectionComment, Claim, Thing, Offer, Person, Clip, Integer, DefinedTerm, StrictInt, StrictFloat, VideoObject, date, SizeSpecification, Boolean, Country, Text, StrictBool, AggregateRating, AlignmentObject, ImageObject, CreativeWork, WebPage, Number, Language, Organization, Audience, Product, Demand, MusicRecording, Date, URL, AudioObject, Place, Duration, InteractionCounter, Event, Review, QuantitativeValue, int, Comment, Rating, MediaObject, PublicationEvent, AnyUrl, ItemList
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
    from pydantic_schemaorg import Grant, PhysicalActivityCategory, Thing, Offer, Service, ProductReturnPolicy, CategoryCode, Brand, DefinedTerm, date, Distance, SizeSpecification, Boolean, Country, PropertyValue, Text, StrictBool, AggregateRating, ImageObject, Organization, MerchantReturnPolicy, Product, Audience, Demand, AdultOrientedEnumeration, Date, ProductModel, URL, ProductGroup, EnergyConsumptionDetails, Review, QuantitativeValue, ListItem, WebContent, OfferItemCondition, AnyUrl, ItemList
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
