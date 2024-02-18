from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class MolecularEntity(SchemaOrgBase):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical,"
     "radical ion, complex, conformer etc., identifiable as a separately distinguishable"
     "entity.

    See: https://schema.org/MolecularEntity
    Model depth: 3
    """
    type_: str = Field(default="MolecularEntity", alias='@type')
    
    potentialUse: Union[List[str], str] = Field(
        default=None,
        description="Intended use of the BioChemEntity by humans.",union_mode="smart"
    )
    
    chemicalRole: Union[List[str], str] = Field(
        default=None,
        description="A role played by the BioChemEntity within a chemical context.",union_mode="smart"
    )
    
    smiles: Union[List[str], str] = Field(
        default=None,
        description="A specification in form of a line notation for describing the structure of chemical species"
     "using short ASCII strings. Double bond stereochemistry \ indicators may need to be escaped"
     "in the string in formats where the backslash is an escape character.",union_mode="smart"
    )
    
    iupacName: Union[List[str], str] = Field(
        default=None,
        description="Systematic method of naming chemical compounds as recommended by the International"
     "Union of Pure and Applied Chemistry (IUPAC).",union_mode="smart"
    )
    
    inChI: Union[List[str], str] = Field(
        default=None,
        description="Non-proprietary identifier for molecular entity that can be used in printed and electronic"
     "data sources thus enabling easier linking of diverse data compilations.",union_mode="smart"
    )
    
    monoisotopicMolecularWeight: Union[List[str], str] = Field(
        default=None,
        description="The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound,"
     "ground-state, rest mass of the principal (most abundant) isotope for each element instead"
     "of the isotopic average mass. Please include the units in the form '&lt;Number&gt; &lt;unit&gt;',"
     "for example '770.230488 g/mol' or as '&lt;QuantitativeValue&gt;.",union_mode="smart"
    )
    
    molecularWeight: Union[List[str], str] = Field(
        default=None,
        description="This is the molecular weight of the entity being described, not of the parent. Units should"
     "be included in the form '&lt;Number&gt; &lt;unit&gt;', for example '12 amu' or as '&lt;QuantitativeValue&gt;.",union_mode="smart"
    )
    
    inChIKey: Union[List[str], str] = Field(
        default=None,
        description="InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm).",union_mode="smart"
    )
    
    molecularFormula: Union[List[str], str] = Field(
        default=None,
        description="The empirical formula is the simplest whole number ratio of all the atoms in a molecule.",union_mode="smart"
    )
    
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
    from pydantic_schemaorg import Text, QuantitativeValue, DefinedTerm
    from pydantic_schemaorg import Gene, Grant, BioChemEntity, PropertyValue, Text, URL, Taxon, DefinedTerm, AnyUrl, MedicalCondition
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
