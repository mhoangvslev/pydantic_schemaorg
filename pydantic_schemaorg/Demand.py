from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime, time
from pydantic import AnyUrl
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Demand(SchemaOrgBase):
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive,"
     "announcement by an organization or person to seek a certain type of goods or services."
     "For describing demand using this type, the very same properties used for Offer apply.

    See: https://schema.org/Demand
    Model depth: 3
    """
    type_: str = Field(default="Demand", alias='@type')
    
    eligibleCustomerType: Union[List[str], str] = Field(
        default=None,
        description="The type(s) of customers for which the given offer is valid.",union_mode="smart"
    )
    
    eligibleDuration: Union[List[str], str] = Field(
        default=None,
        description="The duration for which the given offer is valid.",union_mode="smart"
    )
    
    eligibleRegion: Union[List[str], str] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",union_mode="smart"
    )
    
    gtin12: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12"
     "is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference,"
     "and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",union_mode="smart"
    )
    
    eligibleTransactionVolume: Union[List[str], str] = Field(
        default=None,
        description="The transaction volume, in a monetary unit, for which the offer or price specification"
     "is valid, e.g. for indicating a minimal purchasing volume, to express free shipping"
     "above a certain order volume, or to limit the acceptance of credit cards to purchases"
     "to a certain minimal amount.",union_mode="smart"
    )
    
    validFrom: Union[List[str], str] = Field(
        default=None,
        description="The date when the item becomes valid.",union_mode="smart"
    )
    
    advanceBookingRequirement: Union[List[str], str] = Field(
        default=None,
        description="The amount of time that is required between accepting the offer and the actual usage of"
     "the resource or service.",union_mode="smart"
    )
    
    itemOffered: Union[List[str], str] = Field(
        default=None,
        description="An item being offered (or demanded). The transactional nature of the offer or demand"
     "is documented using [[businessFunction]], e.g. sell, lease etc. While several common"
     "expected types are listed explicitly in this definition, others can be used. Using a"
     "second type, such as Product or a subtype of Product, can clarify the nature of the offer.",union_mode="smart"
    )
    
    availabilityEnds: Union[List[str], str] = Field(
        default=None,
        description="The end of the availability of the product or service included in the offer.",union_mode="smart"
    )
    
    mpn: Union[List[str], str] = Field(
        default=None,
        description="The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.",union_mode="smart"
    )
    
    availabilityStarts: Union[List[str], str] = Field(
        default=None,
        description="The beginning of the availability of the product or service included in the offer.",union_mode="smart"
    )
    
    eligibleQuantity: Union[List[str], str] = Field(
        default=None,
        description="The interval and unit of measurement of ordering quantities for which the offer or price"
     "specification is valid. This allows e.g. specifying that a certain freight charge is"
     "valid only for a certain quantity.",union_mode="smart"
    )
    
    availableAtOrFrom: Union[List[str], str] = Field(
        default=None,
        description="The place(s) from which the offer can be obtained (e.g. store locations).",union_mode="smart"
    )
    
    sku: Union[List[str], str] = Field(
        default=None,
        description="The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service,"
     "or the product to which the offer refers.",union_mode="smart"
    )
    
    seller: Union[List[str], str] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",union_mode="smart"
    )
    
    serialNumber: Union[List[str], str] = Field(
        default=None,
        description="The serial number or any alphanumeric identifier of a particular product. When attached"
     "to an offer, it is a shortcut for the serial number of the product included in the offer.",union_mode="smart"
    )
    
    gtin14: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN"
     "Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",union_mode="smart"
    )
    
    priceSpecification: Union[List[str], str] = Field(
        default=None,
        description="One or more detailed price specifications, indicating the unit price and delivery or"
     "payment charges.",union_mode="smart"
    )
    
    deliveryLeadTime: Union[List[str], str] = Field(
        default=None,
        description="The typical delay between the receipt of the order and the goods either leaving the warehouse"
     "or being prepared for pickup, in case the delivery method is on site pickup.",union_mode="smart"
    )
    
    ineligibleRegion: Union[List[str], str] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",union_mode="smart"
    )
    
    itemCondition: Union[List[str], str] = Field(
        default=None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",union_mode="smart"
    )
    
    availableDeliveryMethod: Union[List[str], str] = Field(
        default=None,
        description="The delivery method(s) available for this offer.",union_mode="smart"
    )
    
    gtin8: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also"
     "known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",union_mode="smart"
    )
    
    inventoryLevel: Union[List[str], str] = Field(
        default=None,
        description="The current approximate inventory level for the item or items.",union_mode="smart"
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
    
    includesObject: Union[List[str], str] = Field(
        default=None,
        description="This links to a node or nodes indicating the exact quantity of the products included in"
     "an [[Offer]] or [[ProductCollection]].",union_mode="smart"
    )
    
    acceptedPaymentMethod: Union[List[str], str] = Field(
        default=None,
        description="The payment method(s) accepted by seller for this offer.",union_mode="smart"
    )
    
    gtin13: Union[List[str], str] = Field(
        default=None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent"
     "to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into"
     "a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",union_mode="smart"
    )
    
    businessFunction: Union[List[str], str] = Field(
        default=None,
        description="The business function (e.g. sell, lease, repair, dispose) of the offer or component"
     "of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.",union_mode="smart"
    )
    
    areaServed: Union[List[str], str] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",union_mode="smart"
    )
    
    warranty: Union[List[str], str] = Field(
        default=None,
        description="The warranty promise(s) included in the offer.",union_mode="smart"
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
    
    validThrough: Union[List[str], str] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",union_mode="smart"
    )
    
    availability: Union[List[str], str] = Field(
        default=None,
        description="The availability of this item&#x2014;for example In stock, Out of stock, Pre-order,"
     "etc.",union_mode="smart"
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
    from pydantic_schemaorg import Product, GeoShape, datetime, Organization, DateTime, PriceSpecification, DeliveryMethod, BusinessEntityType, Date, Service, Time, Person, TypeAndQuantityNode, BusinessFunction, URL, time, Place, AdministrativeArea, date, Event, Trip, QuantitativeValue, AggregateOffer, LoanOrCredit, Text, MenuItem, OfferItemCondition, PaymentMethod, ItemAvailability, WarrantyPromise, CreativeWork, AnyUrl
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
