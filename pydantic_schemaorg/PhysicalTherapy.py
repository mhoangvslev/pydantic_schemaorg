from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from typing import List, Optional, Union
from typing import List, Optional, Union
from typing import List, Optional, Union
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class PhysicalTherapy(SchemaOrgBase):
    """A process of progressive physical care and rehabilitation aimed at improving a health"
     "condition.

    See: https://schema.org/PhysicalTherapy
    Model depth: 6
    """
    type_: str = Field(default="PhysicalTherapy", alias='@type')
    
    contraindication: Union[List[str], str] = Field(
        default=None,
        description="A contraindication for this therapy.",union_mode="smart"
    )
    
    duplicateTherapy: Union[List[str], str] = Field(
        default=None,
        description="A therapy that duplicates or overlaps this one.",union_mode="smart"
    )
    
    seriousAdverseOutcome: Union[List[str], str] = Field(
        default=None,
        description="A possible serious complication and/or serious side effect of this therapy. Serious"
     "adverse outcomes include those that are life-threatening; result in death, disability,"
     "or permanent damage; require hospitalization or prolong existing hospitalization;"
     "cause congenital anomalies or birth defects; or jeopardize the patient and may require"
     "medical or surgical intervention to prevent one of the outcomes in this definition.",union_mode="smart"
    )
    
    doseSchedule: Union[List[str], str] = Field(
        default=None,
        description="A dosing schedule for the drug for a given population, either observed, recommended,"
     "or maximum dose based on the type used.",union_mode="smart"
    )
    
    adverseOutcome: Union[List[str], str] = Field(
        default=None,
        description="A possible complication and/or side effect of this therapy. If it is known that an adverse"
     "outcome is serious (resulting in death, disability, or permanent damage; requiring"
     "hospitalization; or otherwise life-threatening or requiring immediate medical attention),"
     "tag it as a seriousAdverseOutcome instead.",union_mode="smart"
    )
    
    drug: Union[List[str], str] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",union_mode="smart"
    )
    
    bodyLocation: Union[List[str], str] = Field(
        default=None,
        description="Location in the body of the anatomical structure.",union_mode="smart"
    )
    
    howPerformed: Union[List[str], str] = Field(
        default=None,
        description="How the procedure is performed.",union_mode="smart"
    )
    
    procedureType: Union[List[str], str] = Field(
        default=None,
        description="The type of procedure, for example Surgical, Noninvasive, or Percutaneous.",union_mode="smart"
    )
    
    status: Union[List[str], str] = Field(
        default=None,
        description="The status of the study (enumerated).",union_mode="smart"
    )
    
    followup: Union[List[str], str] = Field(
        default=None,
        description="Typical or recommended followup care after the procedure is performed.",union_mode="smart"
    )
    
    preparation: Union[List[str], str] = Field(
        default=None,
        description="Typical preparation that a patient must undergo before having the procedure performed.",union_mode="smart"
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
    from pydantic_schemaorg import Text, MedicalEntity, MedicalContraindication, MedicalTherapy
    from pydantic_schemaorg import DoseSchedule, Drug, MedicalEntity
    from pydantic_schemaorg import Text, MedicalEntity, MedicalProcedureType, EventStatusType, MedicalStudyStatus
    from pydantic_schemaorg import Grant, Organization, MedicalStudy, MedicineSystem, DrugLegalStatus, Text, MedicalGuideline, MedicalCode, MedicalSpecialty, MedicalEnumeration
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
