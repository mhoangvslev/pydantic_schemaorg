from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class GeoShape(SchemaOrgBase):
    """The geographic shape of a place. A GeoShape can be described using several properties"
     "whose values are based on latitude/longitude pairs. Either whitespace or commas can"
     "be used to separate latitude and longitude; whitespace should be used when writing a"
     "list of several such points.

    See: https://schema.org/GeoShape
    Model depth: 4
    """
    type_: str = Field(default="GeoShape", alias='@type')
    
    addressCountry: Union[List[str], str] = Field(
        default=None,
        description="The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2"
     "country code](http://en.wikipedia.org/wiki/ISO_3166-1).",union_mode="smart"
    )
    
    elevation: Union[List[str], str] = Field(
        default=None,
        description="The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System))."
     "Values may be of the form 'NUMBER UNIT\_OF\_MEASUREMENT' (e.g., '1,000 m', '3,200 ft')"
     "while numbers alone should be assumed to be a value in meters.",union_mode="smart"
    )
    
    line: Union[List[str], str] = Field(
        default=None,
        description="A line is a point-to-point path consisting of two or more points. A line is expressed as"
     "a series of two or more point objects separated by space.",union_mode="smart"
    )
    
    polygon: Union[List[str], str] = Field(
        default=None,
        description="A polygon is the area enclosed by a point-to-point path for which the starting and ending"
     "points are the same. A polygon is expressed as a series of four or more space delimited"
     "points where the first and final points are identical.",union_mode="smart"
    )
    
    box: Union[List[str], str] = Field(
        default=None,
        description="A box is the area enclosed by the rectangle formed by two points. The first point is the"
     "lower corner, the second point is the upper corner. A box is expressed as two points separated"
     "by a space character.",union_mode="smart"
    )
    
    address: Union[List[str], str] = Field(
        default=None,
        description="Physical address of the item.",union_mode="smart"
    )
    
    circle: Union[List[str], str] = Field(
        default=None,
        description="A circle is the circular region of a specified radius centered at a specified latitude"
     "and longitude. A circle is expressed as a pair followed by a radius in meters.",union_mode="smart"
    )
    
    postalCode: Union[List[str], str] = Field(
        default=None,
        description="The postal code. For example, 94043.",union_mode="smart"
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
    from pydantic_schemaorg import Text, PostalAddress, Country, Number, StrictInt, StrictFloat
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
