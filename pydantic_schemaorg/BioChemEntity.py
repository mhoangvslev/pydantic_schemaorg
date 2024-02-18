from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class BioChemEntity(SchemaOrgBase):
    """Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical;"
     "a synthetic chemical.

    See: https://schema.org/BioChemEntity
    Model depth: 2
    """
    type_: str = Field(default="BioChemEntity", alias='@type')
    
    funding: Union[List[str], str] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",union_mode="smart"
    )
    
    isLocatedInSubcellularLocation: Union[List[str], str] = Field(
        default=None,
        description="Subcellular location where this BioChemEntity is located; please use PropertyValue"
     "if you want to include any evidence.",union_mode="smart"
    )
    
    associatedDisease: Union[List[str], str] = Field(
        default=None,
        description="Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or"
     "a URL. If you want to add an evidence supporting the association, please use PropertyValue.",union_mode="smart"
    )
    
    hasBioChemEntityPart: Union[List[str], str] = Field(
        default=None,
        description="Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part.",union_mode="smart"
    )
    
    hasRepresentation: Union[List[str], str] = Field(
        default=None,
        description="A common representation such as a protein sequence or chemical structure for this entity."
     "For images use schema.org/image.",union_mode="smart"
    )
    
    isInvolvedInBiologicalProcess: Union[List[str], str] = Field(
        default=None,
        description="Biological process this BioChemEntity is involved in; please use PropertyValue if"
     "you want to include any evidence.",union_mode="smart"
    )
    
    isPartOfBioChemEntity: Union[List[str], str] = Field(
        default=None,
        description="Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity.",union_mode="smart"
    )
    
    biologicalRole: Union[List[str], str] = Field(
        default=None,
        description="A role played by the BioChemEntity within a biological context.",union_mode="smart"
    )
    
    hasMolecularFunction: Union[List[str], str] = Field(
        default=None,
        description="Molecular function performed by this BioChemEntity; please use PropertyValue if you"
     "want to include any evidence.",union_mode="smart"
    )
    
    bioChemSimilarity: Union[List[str], str] = Field(
        default=None,
        description="A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.",union_mode="smart"
    )
    
    isEncodedByBioChemEntity: Union[List[str], str] = Field(
        default=None,
        description="Another BioChemEntity encoding by this one.",union_mode="smart"
    )
    
    taxonomicRange: Union[List[str], str] = Field(
        default=None,
        description="The taxonomic grouping of the organism that expresses, encodes, or in some way related"
     "to the BioChemEntity.",union_mode="smart"
    )
    
    bioChemInteraction: Union[List[str], str] = Field(
        default=None,
        description="A BioChemEntity that is known to interact with this item.",union_mode="smart"
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
    from pydantic_schemaorg import Gene, Grant, BioChemEntity, PropertyValue, Text, URL, Taxon, DefinedTerm, AnyUrl, MedicalCondition
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
