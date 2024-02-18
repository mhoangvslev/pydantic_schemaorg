from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from datetime import date
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class SomeProducts(SchemaOrgBase):
    """A placeholder for multiple similar products of the same kind.

    See: https://schema.org/SomeProducts
    Model depth: 3
    """
    type_: str = Field(default="SomeProducts", alias='@type')
    
    inventoryLevel: Union[List[str], str] = Field(
        default=None,
        description="The current approximate inventory level for the item or items.",union_mode="smart"
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
    
    pattern: Union[List[str], str] = Field(
        default=None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",union_mode="smart"
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
    
    funding: Union[List[str], str] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",union_mode="smart"
    )
    
    reviews: Union[List[str], str] = Field(
        default=None,
        description="Review of the item.",union_mode="smart"
    )
    
    size: Union[List[str], str] = Field(
        default=None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",union_mode="smart"
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
    
    isAccessoryOrSparePartFor: Union[List[str], str] = Field(
        default=None,
        description="A pointer to another product (or multiple products) for which this product is an accessory"
     "or spare part.",union_mode="smart"
    )
    
    audience: Union[List[str], str] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",union_mode="smart"
    )
    
    isFamilyFriendly: Union[List[str], str] = Field(
        default=None,
        description="Indicates whether this content is family friendly.",union_mode="smart"
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
    
    aggregateRating: Union[List[str], str] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",union_mode="smart"
    )
    
    inProductGroupWithID: Union[List[str], str] = Field(
        default=None,
        description="Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]].",union_mode="smart"
    )
    
    awards: Union[List[str], str] = Field(
        default=None,
        description="Awards won by or for this item.",union_mode="smart"
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
    
    keywords: Union[List[str], str] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",union_mode="smart"
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
    
    material: Union[List[str], str] = Field(
        default=None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",union_mode="smart"
    )
    
    review: Union[List[str], str] = Field(
        default=None,
        description="A review of the item.",union_mode="smart"
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
    
    award: Union[List[str], str] = Field(
        default=None,
        description="An award won by or for this item.",union_mode="smart"
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
    from pydantic_schemaorg import QuantitativeValue
    from pydantic_schemaorg import Grant, PhysicalActivityCategory, Thing, Offer, Service, ProductReturnPolicy, CategoryCode, Brand, DefinedTerm, date, Distance, SizeSpecification, Boolean, Country, PropertyValue, Text, StrictBool, AggregateRating, ImageObject, Organization, MerchantReturnPolicy, Product, Audience, Demand, AdultOrientedEnumeration, Date, ProductModel, URL, ProductGroup, EnergyConsumptionDetails, Review, QuantitativeValue, ListItem, WebContent, OfferItemCondition, AnyUrl, ItemList
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
