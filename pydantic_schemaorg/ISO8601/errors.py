from pydantic.errors import PydanticErrorMixin


class ISO8601DateError(PydanticErrorMixin):
    code = 'ISO9801'


class ISO8601DateInvalid(PydanticErrorMixin):
    code = 'ISO9801 invalid date'