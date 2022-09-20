
from client.controllers.controller_responses import error_response, success_response

def get_healthcheck():
    return success_response({"status": "Ok"})