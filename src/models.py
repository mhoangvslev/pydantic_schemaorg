from typing import Optional, List

from pydantic import BaseModel, Field, ValidationInfo, field_validator, validator


class PydanticBase(BaseModel):
    name: str
    description: str
    valid_name: Optional[str] = Field(validate_default=True, default=None)

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    # @validator("valid_name", always=True)
    @field_validator('valid_name')
    def ab(cls, v, info: ValidationInfo) -> str:
        values = info.data
        if not values["name"]:
            raise ValueError()
        elif values["name"] in {
            "class",
            "def",
            "from",
            "import",
            "return",
            "yield",
            "True",
            "False",
        }:
            return f"{values['name']}_"
        if values["name"][0].isdigit():
            return f"_{values['name']}"
        return values["name"]


class PydanticField(PydanticBase):
    type: str


class Import(BaseModel):
    type: str
    classPath: str
    classes_: set


class PydanticClass(PydanticBase):
    fields: List[PydanticField]
    parents: List['PydanticClass']
    depth: int = Field(default=1)
    parent_imports: List[Import]
    field_imports: List[Import]
    pydantic_imports: List[Import] = []
    forward_refs: List[Import] = []
    filename: str = Field(default="")

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    # @validator("filename", always=True)
    @field_validator("filename")
    def filename_val(cls, v, info: ValidationInfo) -> str:
        values = info.data
        if not values["valid_name"]:
            raise ValueError()
        filename = values["valid_name"]
        if filename in {
            "class",
            "def",
            "from",
            "import",
            "return",
            "yield",
        }:
            return f'{filename}_'
        return values['valid_name']


PydanticClass.model_rebuild()
