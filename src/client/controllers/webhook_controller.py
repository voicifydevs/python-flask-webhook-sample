from client.controllers.controller_responses import error_response, success_response


def handle_webhook(request):
    # TODO: handle request
    print(request)
    return success_response({}) # TODO: return response override