from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.v1 import Field

from pydantic2_schemaorg.BioChemEntity import BioChemEntity


class ChemicalSubstance(BioChemEntity):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular"
     "entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

    See: https://schema.org/ChemicalSubstance
    Model depth: 3
    """

    type_: str = Field(default="ChemicalSubstance", alias="@type", const=True)
    potentialUse: None | (list[DefinedTerm | str] | DefinedTerm | str) = Field(
        default=None,
        description="Intended use of the BioChemEntity by humans.",
    )
    chemicalRole: None | (list[DefinedTerm | str] | DefinedTerm | str) = Field(
        default=None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    chemicalComposition: list[str | Text] | str | Text | None = Field(
        default=None,
        description="The chemical composition describes the identity and relative ratio of the chemical"
        "elements that make up the substance.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.Text import Text
