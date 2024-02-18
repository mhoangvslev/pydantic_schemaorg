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



class MedicalSign(SchemaOrgBase):
    """Any physical manifestation of a person's medical condition discoverable by objective"
     "diagnostic tests or physical examination.

    See: https://schema.org/MedicalSign
    Model depth: 5
    """
    type_: str = Field(default="MedicalSign", alias='@type')
    
    identifyingTest: Union[List[str], str] = Field(
        default=None,
        description="A diagnostic test that can identify this sign.",union_mode="smart"
    )
    
    identifyingExam: Union[List[str], str] = Field(
        default=None,
        description="A physical examination that can identify this sign.",union_mode="smart"
    )
    
    possibleTreatment: Union[List[str], str] = Field(
        default=None,
        description="A possible treatment to address this condition, sign or symptom.",union_mode="smart"
    )
    
    typicalTest: Union[List[str], str] = Field(
        default=None,
        description="A medical test typically performed given this condition.",union_mode="smart"
    )
    
    differentialDiagnosis: Union[List[str], str] = Field(
        default=None,
        description="One of a set of differential diagnoses for the condition. Specifically, a closely-related"
     "or competing diagnosis typically considered later in the cognitive process whereby"
     "this medical condition is distinguished from others most likely responsible for a similar"
     "collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses"
     "in a patient.",union_mode="smart"
    )
    
    secondaryPrevention: Union[List[str], str] = Field(
        default=None,
        description="A preventative therapy used to prevent reoccurrence of the medical condition after"
     "an initial episode of the condition.",union_mode="smart"
    )
    
    expectedPrognosis: Union[List[str], str] = Field(
        default=None,
        description="The likely outcome in either the short term or long term of the medical condition.",union_mode="smart"
    )
    
    stage: Union[List[str], str] = Field(
        default=None,
        description="The stage of the condition, if applicable.",union_mode="smart"
    )
    
    primaryPrevention: Union[List[str], str] = Field(
        default=None,
        description="A preventative therapy used to prevent an initial occurrence of the medical condition,"
     "such as vaccination.",union_mode="smart"
    )
    
    status: Union[List[str], str] = Field(
        default=None,
        description="The status of the study (enumerated).",union_mode="smart"
    )
    
    drug: Union[List[str], str] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",union_mode="smart"
    )
    
    associatedAnatomy: Union[List[str], str] = Field(
        default=None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",union_mode="smart"
    )
    
    possibleComplication: Union[List[str], str] = Field(
        default=None,
        description="A possible unexpected and unfavorable evolution of a medical condition. Complications"
     "may include worsening of the signs or symptoms of the disease, extension of the condition"
     "to other organ systems, etc.",union_mode="smart"
    )
    
    riskFactor: Union[List[str], str] = Field(
        default=None,
        description="A modifiable or non-modifiable factor that increases the risk of a patient contracting"
     "this condition, e.g. age, coexisting condition.",union_mode="smart"
    )
    
    signOrSymptom: Union[List[str], str] = Field(
        default=None,
        description="A sign or symptom of this condition. Signs are objective or physically observable manifestations"
     "of the medical condition while symptoms are the subjective experience of the medical"
     "condition.",union_mode="smart"
    )
    
    pathophysiology: Union[List[str], str] = Field(
        default=None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated"
     "with this activity or condition.",union_mode="smart"
    )
    
    naturalProgression: Union[List[str], str] = Field(
        default=None,
        description="The expected progression of the condition if it is not treated and allowed to progress"
     "naturally.",union_mode="smart"
    )
    
    epidemiology: Union[List[str], str] = Field(
        default=None,
        description="The characteristics of associated patients, such as age, gender, race etc.",union_mode="smart"
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
    from pydantic_schemaorg import MedicalTest, PhysicalExam
    from pydantic_schemaorg import MedicalTherapy
    from pydantic_schemaorg import MedicalTest, AnatomicalSystem, AnatomicalStructure, MedicalTherapy, EventStatusType, DDxElement, MedicalStudyStatus, Text, MedicalConditionStage, SuperficialAnatomy, Drug, MedicalSignOrSymptom, MedicalRiskFactor
    from pydantic_schemaorg import Grant, Organization, MedicalStudy, MedicineSystem, DrugLegalStatus, Text, MedicalGuideline, MedicalCode, MedicalSpecialty, MedicalEnumeration
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
