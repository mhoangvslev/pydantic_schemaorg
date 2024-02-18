from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class BreadcrumbList(SchemaOrgBase):
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically"
     "described using at least their URL and their name, and typically ending with the current"
     "page. The [[position]] property is used to reconstruct the order of the items in a BreadcrumbList."
     "The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]]"
     "(lower values listed first), and that the first items in this list correspond to the \"top\""
     "or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific"
     "values of 'position' are not assigned meaning for a BreadcrumbList, but they should"
     "be integers, e.g. beginning with '1' for the first item in the list.

    See: https://schema.org/BreadcrumbList
    Model depth: 4
    """
    type_: str = Field(default="BreadcrumbList", alias='@type')
    
    numberOfItems: Union[List[str], str] = Field(
        default=None,
        description="The number of items in an ItemList. Note that some descriptions might not fully describe"
     "all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems"
     "would be for the entire list.",union_mode="smart"
    )
    
    itemListElement: Union[List[str], str] = Field(
        default=None,
        description="For itemListElement values, you can use simple strings (e.g. \"Peter\", \"Paul\","
     "\"Mary\"), existing entities, or use ListItem. Text values are best if the elements"
     "in the list are plain strings. Existing entities are best for a simple, unordered list"
     "of existing things in your data. ListItem is used with ordered lists when you want to provide"
     "additional context about the element in that list or when the same item might be in different"
     "places in different lists. Note: The order of elements in your mark-up is not sufficient"
     "for indicating the order or elements. Use ListItem with a 'position' property in such"
     "cases.",union_mode="smart"
    )
    
    itemListOrder: Union[List[str], str] = Field(
        default=None,
        description="Type of ordering (e.g. Ascending, Descending, Unordered).",union_mode="smart"
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
    from pydantic_schemaorg import Text, ItemListOrderType, Thing, Integer, int, ListItem
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
