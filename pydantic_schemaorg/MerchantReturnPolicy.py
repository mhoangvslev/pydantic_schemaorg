from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class MerchantReturnPolicy(SchemaOrgBase):
    """A MerchantReturnPolicy provides information about product return policies associated"
     "with an [[Organization]], [[Product]], or [[Offer]].

    See: https://schema.org/MerchantReturnPolicy
    Model depth: 3
    """
    type_: str = Field(default="MerchantReturnPolicy", alias='@type')
    
    customerRemorseReturnLabelSource: Union[List[str], str] = Field(
        default=None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a product returned due to customer remorse.",union_mode="smart"
    )
    
    inStoreReturnsOffered: Union[List[str], str] = Field(
        default=None,
        description="Are in-store returns offered? (For more advanced return methods use the [[returnMethod]]"
     "property.)",union_mode="smart"
    )
    
    restockingFee: Union[List[str], str] = Field(
        default=None,
        description="Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use"
     "[[Number]] to specify a percentage of the product price paid by the customer.",union_mode="smart"
    )
    
    refundType: Union[List[str], str] = Field(
        default=None,
        description="A refund type, from an enumerated list.",union_mode="smart"
    )
    
    returnMethod: Union[List[str], str] = Field(
        default=None,
        description="The type of return method offered, specified from an enumeration.",union_mode="smart"
    )
    
    applicableCountry: Union[List[str], str] = Field(
        default=None,
        description="A country where a particular merchant return policy applies to, for example the two-letter"
     "ISO 3166-1 alpha-2 country code.",union_mode="smart"
    )
    
    itemDefectReturnLabelSource: Union[List[str], str] = Field(
        default=None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a defect product.",union_mode="smart"
    )
    
    merchantReturnDays: Union[List[str], str] = Field(
        default=None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that"
     "a product can be returned. Used when the [[returnPolicyCategory]] property is specified"
     "as [[MerchantReturnFiniteReturnWindow]].",union_mode="smart"
    )
    
    customerRemorseReturnFees: Union[List[str], str] = Field(
        default=None,
        description="The type of return fees if the product is returned due to customer remorse.",union_mode="smart"
    )
    
    returnFees: Union[List[str], str] = Field(
        default=None,
        description="The type of return fees for purchased products (for any return reason).",union_mode="smart"
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
    
    itemCondition: Union[List[str], str] = Field(
        default=None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",union_mode="smart"
    )
    
    customerRemorseReturnShippingFeesAmount: Union[List[str], str] = Field(
        default=None,
        description="The amount of shipping costs if a product is returned due to customer remorse. Applicable"
     "when property [[customerRemorseReturnFees]] equals [[ReturnShippingFees]].",union_mode="smart"
    )
    
    returnPolicyCategory: Union[List[str], str] = Field(
        default=None,
        description="Specifies an applicable return policy (from an enumeration).",union_mode="smart"
    )
    
    returnLabelSource: Union[List[str], str] = Field(
        default=None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a product returned for any reason.",union_mode="smart"
    )
    
    merchantReturnLink: Union[List[str], str] = Field(
        default=None,
        description="Specifies a Web page or service by URL, for product returns.",union_mode="smart"
    )
    
    itemDefectReturnFees: Union[List[str], str] = Field(
        default=None,
        description="The type of return fees for returns of defect products.",union_mode="smart"
    )
    
    itemDefectReturnShippingFeesAmount: Union[List[str], str] = Field(
        default=None,
        description="Amount of shipping costs for defect product returns. Applicable when property [[itemDefectReturnFees]]"
     "equals [[ReturnShippingFees]].",union_mode="smart"
    )
    
    returnPolicySeasonalOverride: Union[List[str], str] = Field(
        default=None,
        description="Seasonal override of a return policy.",union_mode="smart"
    )
    
    returnShippingFeesAmount: Union[List[str], str] = Field(
        default=None,
        description="Amount of shipping costs for product returns (for any reason). Applicable when property"
     "[[returnFees]] equals [[ReturnShippingFees]].",union_mode="smart"
    )
    
    returnPolicyCountry: Union[List[str], str] = Field(
        default=None,
        description="The country where the product has to be sent to for returns, for example \"Ireland\" using"
     "the [[name]] property of [[Country]]. You can also provide the two-letter [ISO 3166-1"
     "alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this"
     "can be different from the country where the product was originally shipped from or sent"
     "to.",union_mode="smart"
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
    from pydantic_schemaorg import datetime, DateTime, MerchantReturnEnumeration, Date, MerchantReturnPolicySeasonalOverride, ReturnLabelSourceEnumeration, ReturnMethodEnumeration, URL, Integer, StrictInt, StrictFloat, ReturnFeesEnumeration, date, MonetaryAmount, Boolean, Country, int, PropertyValue, Text, StrictBool, RefundTypeEnumeration, OfferItemCondition, AnyUrl, Number
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
