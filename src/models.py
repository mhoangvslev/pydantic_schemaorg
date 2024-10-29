from typing import Optional

from pydantic.v1 import BaseModel, validator


class PydanticBase(BaseModel):
    name: str
    description: str
    valid_name: Optional[str] = None

    @validator("valid_name", always=True)
    def ab(cls, v, values) -> str:
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
    fields: list[PydanticField]
    parents: list["PydanticClass"]
    depth: int = 1
    parent_imports: list[Import]
    field_imports: list[Import]
    pydantic_imports: list[Import] = []
    forward_refs: list[Import] = []
    filename: str = ""

    @validator("filename", always=True)
    def filename_val(cls, v, values) -> str:
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
            return f"{filename}_"
        return values["valid_name"]


PydanticClass.update_forward_refs()
