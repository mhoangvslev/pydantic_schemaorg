from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class MonetaryAmount(SchemaOrgBase):
    """A monetary value or range. This type can be used to describe an amount of money such as $50"
     "USD, or a range as in describing a bank account being suitable for a balance between £1,000"
     "and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]]"
     "Types to describe the price of an Offer, Invoice, etc.

    See: https://schema.org/MonetaryAmount
    Model depth: 4
    """
    type_: str = Field(default="MonetaryAmount", alias='@type')
    
    validFrom: Union[List[str], str] = Field(
        default=None,
        description="The date when the item becomes valid.",union_mode="smart"
    )
    
    currency: Union[List[str], str] = Field(
        default=None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
     "currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. \"USD\"; [Ticker"
     "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies,"
     "e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",union_mode="smart"
    )
    
    value: Union[List[str], str] = Field(
        default=None,
        description="The value of a [[QuantitativeValue]] (including [[Observation]]) or property value"
     "node. * For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for"
     "values is 'Number'. * For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean',"
     "or 'StructuredValue'. * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",union_mode="smart"
    )
    
    minValue: Union[List[str], str] = Field(
        default=None,
        description="The lower value of some characteristic or property.",union_mode="smart"
    )
    
    maxValue: Union[List[str], str] = Field(
        default=None,
        description="The upper value of some characteristic or property.",union_mode="smart"
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
    from pydantic_schemaorg import date, StrictInt, StrictFloat, datetime, Boolean, DateTime, Date, Text, StrictBool, StructuredValue, Number
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
