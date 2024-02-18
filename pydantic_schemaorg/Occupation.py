from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class Occupation(SchemaOrgBase):
    """A profession, may involve prolonged training and/or a formal qualification.

    See: https://schema.org/Occupation
    Model depth: 3
    """
    type_: str = Field(default="Occupation", alias='@type')
    
    occupationalCategory: Union[List[str], str] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",union_mode="smart"
    )
    
    qualifications: Union[List[str], str] = Field(
        default=None,
        description="Specific qualifications required for this role or Occupation.",union_mode="smart"
    )
    
    occupationLocation: Union[List[str], str] = Field(
        default=None,
        description="The region/country for which this occupational description is appropriate. Note that"
     "educational requirements and qualifications can vary between jurisdictions.",union_mode="smart"
    )
    
    skills: Union[List[str], str] = Field(
        default=None,
        description="A statement of knowledge, skill, ability, task or any other assertion expressing a competency"
     "that is desired or required to fulfill this role or to work in this occupation.",union_mode="smart"
    )
    
    educationRequirements: Union[List[str], str] = Field(
        default=None,
        description="Educational background needed for the position or Occupation.",union_mode="smart"
    )
    
    responsibilities: Union[List[str], str] = Field(
        default=None,
        description="Responsibilities associated with this role or Occupation.",union_mode="smart"
    )
    
    estimatedSalary: Union[List[str], str] = Field(
        default=None,
        description="An estimated salary for a job posting or occupation, based on a variety of variables including,"
     "but not limited to industry, job title, and location. Estimated salaries are often computed"
     "by outside organizations rather than the hiring organization, who may not have committed"
     "to the estimated value.",union_mode="smart"
    )
    
    experienceRequirements: Union[List[str], str] = Field(
        default=None,
        description="Description of skills and experience needed for the position or Occupation.",union_mode="smart"
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
    from pydantic_schemaorg import StrictInt, StrictFloat, MonetaryAmount, AdministrativeArea, OccupationalExperienceRequirements, MonetaryAmountDistribution, Text, EducationalOccupationalCredential, CategoryCode, DefinedTerm, Number
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
