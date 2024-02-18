from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field



from pydantic_schemaorg import SchemaOrgBase



class CDCPMDRecord(SchemaOrgBase):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format"
     "used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for"
     "details, and the linked CDC materials for authoritative definitions used as the source"
     "here.

    See: https://schema.org/CDCPMDRecord
    Model depth: 4
    """
    type_: str = Field(default="CDCPMDRecord", alias='@type')
    
    cvdNumC19Died: Union[List[str], str] = Field(
        default=None,
        description="numc19died - DEATHS: Patients with suspected or confirmed COVID-19 who died in the hospital,"
     "ED, or any overflow location.",union_mode="smart"
    )
    
    cvdNumVentUse: Union[List[str], str] = Field(
        default=None,
        description="numventuse - MECHANICAL VENTILATORS IN USE: Total number of ventilators in use.",union_mode="smart"
    )
    
    cvdNumC19OFMechVentPats: Union[List[str], str] = Field(
        default=None,
        description="numc19ofmechventpats - ED/OVERFLOW and VENTILATED: Patients with suspected or confirmed"
     "COVID-19 who are in the ED or any overflow location awaiting an inpatient bed and on a mechanical"
     "ventilator.",union_mode="smart"
    )
    
    cvdNumC19MechVentPats: Union[List[str], str] = Field(
        default=None,
        description="numc19mechventpats - HOSPITALIZED and VENTILATED: Patients hospitalized in an NHSN"
     "inpatient care location who have suspected or confirmed COVID-19 and are on a mechanical"
     "ventilator.",union_mode="smart"
    )
    
    cvdNumC19HOPats: Union[List[str], str] = Field(
        default=None,
        description="numc19hopats - HOSPITAL ONSET: Patients hospitalized in an NHSN inpatient care location"
     "with onset of suspected or confirmed COVID-19 14 or more days after hospitalization.",union_mode="smart"
    )
    
    cvdNumICUBeds: Union[List[str], str] = Field(
        default=None,
        description="numicubeds - ICU BEDS: Total number of staffed inpatient intensive care unit (ICU) beds.",union_mode="smart"
    )
    
    cvdNumBedsOcc: Union[List[str], str] = Field(
        default=None,
        description="numbedsocc - HOSPITAL INPATIENT BED OCCUPANCY: Total number of staffed inpatient beds"
     "that are occupied.",union_mode="smart"
    )
    
    cvdNumC19HospPats: Union[List[str], str] = Field(
        default=None,
        description="numc19hosppats - HOSPITALIZED: Patients currently hospitalized in an inpatient care"
     "location who have suspected or confirmed COVID-19.",union_mode="smart"
    )
    
    cvdNumTotBeds: Union[List[str], str] = Field(
        default=None,
        description="numtotbeds - ALL HOSPITAL BEDS: Total number of all inpatient and outpatient beds, including"
     "all staffed, ICU, licensed, and overflow (surge) beds used for inpatients or outpatients.",union_mode="smart"
    )
    
    cvdNumVent: Union[List[str], str] = Field(
        default=None,
        description="numvent - MECHANICAL VENTILATORS: Total number of ventilators available.",union_mode="smart"
    )
    
    cvdCollectionDate: Union[List[str], str] = Field(
        default=None,
        description="collectiondate - Date for which patient counts are reported.",union_mode="smart"
    )
    
    cvdNumC19OverflowPats: Union[List[str], str] = Field(
        default=None,
        description="numc19overflowpats - ED/OVERFLOW: Patients with suspected or confirmed COVID-19"
     "who are in the ED or any overflow location awaiting an inpatient bed.",union_mode="smart"
    )
    
    cvdNumBeds: Union[List[str], str] = Field(
        default=None,
        description="numbeds - HOSPITAL INPATIENT BEDS: Inpatient beds, including all staffed, licensed,"
     "and overflow (surge) beds used for inpatients.",union_mode="smart"
    )
    
    cvdFacilityId: Union[List[str], str] = Field(
        default=None,
        description="Identifier of the NHSN facility that this data record applies to. Use [[cvdFacilityCounty]]"
     "to indicate the county. To provide other details, [[healthcareReportingData]] can"
     "be used on a [[Hospital]] entry.",union_mode="smart"
    )
    
    datePosted: Union[List[str], str] = Field(
        default=None,
        description="Publication date of an online listing.",union_mode="smart"
    )
    
    cvdNumICUBedsOcc: Union[List[str], str] = Field(
        default=None,
        description="numicubedsocc - ICU BED OCCUPANCY: Total number of staffed inpatient ICU beds that are"
     "occupied.",union_mode="smart"
    )
    
    cvdFacilityCounty: Union[List[str], str] = Field(
        default=None,
        description="Name of the County of the NHSN facility that this data record applies to. Use [[cvdFacilityId]]"
     "to identify the facility. To provide other details, [[healthcareReportingData]]"
     "can be used on a [[Hospital]] entry.",union_mode="smart"
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
    from pydantic_schemaorg import Text, date, datetime, DateTime, Date, Number, StrictInt, StrictFloat
    from pydantic_schemaorg import Event, Action, PropertyValue, TextObject, Text, URL, ImageObject, CreativeWork, AnyUrl
