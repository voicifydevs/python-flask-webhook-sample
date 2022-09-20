from flask import jsonify

from core.results import ResultType


def error_response(message, code):
    return jsonify([message]), code

def success_response(data):
    return jsonify(data), 200

def from_result(result):
    if result.resultType == ResultType.Ok:
        return success_response(result.data)
    elif result.resultType == ResultType.Invalid:
        print("Invalid request error: " + result.errors[0])
        return error_response(result.errors[0], 400)
    elif result.resultType == ResultType.AccessDenied:
        print("access denied request error: " + result.errors[0])
        return error_response(result.errors[0], 403)
    else:
        print("unexpected response error: " + result.errors[0])
        return error_response(result.errors, 500)