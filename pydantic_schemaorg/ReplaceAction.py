from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from typing import List, Optional, Union
from datetime import datetime, time
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class ReplaceAction(SchemaOrgBase):
    """The act of editing a recipient by replacing an old object with a new object.

    See: https://schema.org/ReplaceAction
    Model depth: 4
    """
    type_: str = Field(default="ReplaceAction", alias='@type')
    
    replacee: Union[List[str], str] = Field(
        default=None,
        description="A sub property of object. The object that is being replaced.",union_mode="smart"
    )
    
    replacer: Union[List[str], str] = Field(
        default=None,
        description="A sub property of object. The object that replaces.",union_mode="smart"
    )
    
    collection: Union[List[str], str] = Field(
        default=None,
        description="A sub property of object. The collection target of the action.",union_mode="smart"
    )
    
    targetCollection: Union[List[str], str] = Field(
        default=None,
        description="A sub property of object. The collection target of the action.",union_mode="smart"
    )
    
    instrument: Union[List[str], str] = Field(
        default=None,
        description="The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.",union_mode="smart"
    )
    
    participant: Union[List[str], str] = Field(
        default=None,
        description="Other co-agents that participated in the action indirectly. E.g. John wrote a book with"
     "*Steve*.",union_mode="smart"
    )
    
    provider: Union[List[str], str] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",union_mode="smart"
    )
    
    startTime: Union[List[str], str] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",union_mode="smart"
    )
    
    object: Union[List[str], str] = Field(
        default=None,
        description="The object upon which the action is carried out, whose state is kept intact or changed."
     "Also known as the semantic roles patient, affected or undergoer (which change their"
     "state) or theme (which doesn't). E.g. John read *a book*.",union_mode="smart"
    )
    
    target: Union[List[str], str] = Field(
        default=None,
        description="Indicates a target EntryPoint, or url, for an Action.",union_mode="smart"
    )
    
    result: Union[List[str], str] = Field(
        default=None,
        description="The result produced in the action. E.g. John wrote *a book*.",union_mode="smart"
    )
    
    location: Union[List[str], str] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",union_mode="smart"
    )
    
    actionStatus: Union[List[str], str] = Field(
        default=None,
        description="Indicates the current disposition of the Action.",union_mode="smart"
    )
    
    agent: Union[List[str], str] = Field(
        default=None,
        description="The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote"
     "a book.",union_mode="smart"
    )
    
    endTime: Union[List[str], str] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",union_mode="smart"
    )
    
    error: Union[List[str], str] = Field(
        default=None,
        description="For failed actions, more information on the cause of the failure.",union_mode="smart"
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
    from pydantic_schemaorg import Thing
    from pydantic_schemaorg import Thing
    from pydantic_schemaorg import Organization, datetime, EntryPoint, DateTime, Thing, Time, Person, ActionStatusType, Text, URL, VirtualLocation, time, Place, AnyUrl, PostalAddress
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
