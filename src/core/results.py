from enum import Enum
from unittest import result


class Result:
    def __init__(self, data, errors, resultType):
        self.data = data
        self.errors = errors
        self.resultType = resultType

class ResultType(Enum):
    Ok = "Ok"
    Invalid = "Invalid"
    AccessDenied = "PermissionDenied"
    Unexpected = "Unexpected"

def success_result(data):
    return Result(data, None, ResultType.Ok)

def invalid_result(error):
    return Result(None, [error], ResultType.Invalid)

def access_denied_result(error):
    return Result(None, [error], ResultType.AccessDenied)

def unexpected_result(errors):
    return Result(None, errors or ["Unexpected error"], ResultType.Unexpected)