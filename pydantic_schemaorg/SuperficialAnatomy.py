from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class SuperficialAnatomy(SchemaOrgBase):
    """Anatomical features that can be observed by sight (without dissection), including"
     "the form and proportions of the human body as well as surface landmarks that correspond"
     "to deeper subcutaneous structures. Superficial anatomy plays an important role in"
     "sports medicine, phlebotomy, and other medical specialties as underlying anatomical"
     "structures can be identified through surface palpation. For example, during back surgery,"
     "superficial anatomy can be used to palpate and count vertebrae to find the site of incision."
     "Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example,"
     "the median cubital vein can be located by palpating the borders of the cubital fossa (such"
     "as the epicondyles of the humerus) and then looking for the superficial signs of the vein,"
     "such as size, prominence, ability to refill after depression, and feel of surrounding"
     "tissue support. As another example, in a subluxation (dislocation) of the glenohumeral"
     "joint, the bony structure becomes pronounced with the deltoid muscle failing to cover"
     "the glenohumeral joint allowing the edges of the scapula to be superficially visible."
     "Here, the superficial anatomy is the visible edges of the scapula, implying the underlying"
     "dislocation of the joint (the related anatomical structure).

    See: https://schema.org/SuperficialAnatomy
    Model depth: 3
    """
    type_: str = Field(default="SuperficialAnatomy", alias='@type')
    
    significance: Union[List[str], str] = Field(
        default=None,
        description="The significance associated with the superficial anatomy; as an example, how characteristics"
     "of the superficial anatomy can suggest underlying medical conditions or courses of"
     "treatment.",union_mode="smart"
    )
    
    relatedTherapy: Union[List[str], str] = Field(
        default=None,
        description="A medical therapy related to this anatomy.",union_mode="smart"
    )
    
    relatedCondition: Union[List[str], str] = Field(
        default=None,
        description="A medical condition associated with this anatomy.",union_mode="smart"
    )
    
    relatedAnatomy: Union[List[str], str] = Field(
        default=None,
        description="Anatomical systems or structures that relate to the superficial anatomy.",union_mode="smart"
    )
    
    associatedPathophysiology: Union[List[str], str] = Field(
        default=None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",union_mode="smart"
    )
    
    funding: Union[List[str], str] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",union_mode="smart"
    )
    
    code: Union[List[str], str] = Field(
        default=None,
        description="A medical code for the entity, taken from a controlled vocabulary or ontology such as"
     "ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.",union_mode="smart"
    )
    
    guideline: Union[List[str], str] = Field(
        default=None,
        description="A medical guideline related to this entity.",union_mode="smart"
    )
    
    recognizingAuthority: Union[List[str], str] = Field(
        default=None,
        description="If applicable, the organization that officially recognizes this entity as part of its"
     "endorsed system of medicine.",union_mode="smart"
    )
    
    study: Union[List[str], str] = Field(
        default=None,
        description="A medical study or trial related to this entity.",union_mode="smart"
    )
    
    medicineSystem: Union[List[str], str] = Field(
        default=None,
        description="The system of medicine that includes this MedicalEntity, for example 'evidence-based',"
     "'homeopathic', 'chiropractic', etc.",union_mode="smart"
    )
    
    relevantSpecialty: Union[List[str], str] = Field(
        default=None,
        description="If applicable, a medical specialty in which this entity is relevant.",union_mode="smart"
    )
    
    legalStatus: Union[List[str], str] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",union_mode="smart"
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
    from pydantic_schemaorg import Text, AnatomicalSystem, AnatomicalStructure, MedicalTherapy, MedicalCondition
    from pydantic_schemaorg import Grant, Organization, MedicalStudy, MedicineSystem, DrugLegalStatus, Text, MedicalGuideline, MedicalCode, MedicalSpecialty, MedicalEnumeration
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
