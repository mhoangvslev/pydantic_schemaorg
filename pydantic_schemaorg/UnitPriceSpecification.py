from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class UnitPriceSpecification(SchemaOrgBase):
    """The price asked for a given offer by the respective organization or person.

    See: https://schema.org/UnitPriceSpecification
    Model depth: 5
    """
    type_: str = Field(default="UnitPriceSpecification", alias='@type')
    
    unitText: Union[List[str], str] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",union_mode="smart"
    )
    
    unitCode: Union[List[str], str] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",union_mode="smart"
    )
    
    priceType: Union[List[str], str] = Field(
        default=None,
        description="Defines the type of a price specified for an offered product, for example a list price,"
     "a (temporary) sale price or a manufacturer suggested retail price. If multiple prices"
     "are specified for an offer the [[priceType]] property can be used to identify the type"
     "of each such specified price. The value of priceType can be specified as a value from enumeration"
     "PriceTypeEnumeration or as a free form text string for price types that are not already"
     "predefined in PriceTypeEnumeration.",union_mode="smart"
    )
    
    billingStart: Union[List[str], str] = Field(
        default=None,
        description="Specifies after how much time this price (or price component) becomes valid and billing"
     "starts. Can be used, for example, to model a price increase after the first year of a subscription."
     "The unit of measurement is specified by the unitCode property.",union_mode="smart"
    )
    
    billingDuration: Union[List[str], str] = Field(
        default=None,
        description="Specifies for how long this price (or price component) will be billed. Can be used, for"
     "example, to model the contractual duration of a subscription or payment plan. Type can"
     "be either a Duration or a Number (in which case the unit of measurement, for example month,"
     "is specified by the unitCode property).",union_mode="smart"
    )
    
    referenceQuantity: Union[List[str], str] = Field(
        default=None,
        description="The reference quantity for which a certain price applies, e.g. 1 EUR per 4 kWh of electricity."
     "This property is a replacement for unitOfMeasurement for the advanced cases where the"
     "price does not relate to a standard unit.",union_mode="smart"
    )
    
    priceComponentType: Union[List[str], str] = Field(
        default=None,
        description="Identifies a price component (for example, a line item on an invoice), part of the total"
     "price for an offer.",union_mode="smart"
    )
    
    billingIncrement: Union[List[str], str] = Field(
        default=None,
        description="This property specifies the minimal quantity and rounding increment that will be the"
     "basis for the billing. The unit of measurement is specified by the unitCode property.",union_mode="smart"
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
    
    priceCurrency: Union[List[str], str] = Field(
        default=None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",union_mode="smart"
    )
    
    price: Union[List[str], str] = Field(
        default=None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification"
     "and its subtypes. Usage guidelines: * Use the [[priceCurrency]] property (with standard"
     "formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\") instead of including [ambiguous"
     "symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign)"
     "such as '$' in the value. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate"
     "a decimal point. Avoid using these symbols as a readability separator. * Note that both"
     "[RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute)"
     "and Microdata syntax allow the use of a \"content=\" attribute for publishing simple"
     "machine-readable values alongside more human-friendly formatting. * Use values from"
     "0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
     "similar Unicode symbols.",union_mode="smart"
    )
    
    eligibleQuantity: Union[List[str], str] = Field(
        default=None,
        description="The interval and unit of measurement of ordering quantities for which the offer or price"
     "specification is valid. This allows e.g. specifying that a certain freight charge is"
     "valid only for a certain quantity.",union_mode="smart"
    )
    
    maxPrice: Union[List[str], str] = Field(
        default=None,
        description="The highest price if the price is a range.",union_mode="smart"
    )
    
    minPrice: Union[List[str], str] = Field(
        default=None,
        description="The lowest price if the price is a range.",union_mode="smart"
    )
    
    valueAddedTaxIncluded: Union[List[str], str] = Field(
        default=None,
        description="Specifies whether the applicable value-added tax (VAT) is included in the price specification"
     "or not.",union_mode="smart"
    )
    
    validThrough: Union[List[str], str] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",union_mode="smart"
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
    from pydantic_schemaorg import AnyUrl, QuantitativeValue, Text, PriceComponentTypeEnumeration, URL, Number, PriceTypeEnumeration, Duration, StrictInt, StrictFloat
    from pydantic_schemaorg import date, datetime, DateTime, PriceSpecification, Boolean, QuantitativeValue, Date, Text, StrictBool, Number, StrictInt, StrictFloat
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
