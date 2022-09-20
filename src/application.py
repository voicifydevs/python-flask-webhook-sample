from types import SimpleNamespace
import json
import os
import client.controllers.healthcheck_controller as healthcheck_controller
import client.controllers.webhook_controller as webhook_controller
from client.controllers.controller_responses import error_response, success_response
from flask import Flask, request

application = Flask(__name__)
app = application
@app.before_first_request
def do_initial_setup():
   
   print("Doing initial setup things")

#register routes
@app.route("/")
def index():
    return "Ok"

@app.route("/api/handleVoicifyRequest", methods=["POST"])
def handleWebhook():
    return webhook_controller.handle_webhook(request)

@app.route("/api/healthcheck", methods=["GET"])
def healthcheck():
    return healthcheck_controller.get_healthcheck()

# catch all 500 error -> redirect 400
@app.errorhandler(Exception)
def handle_exception(e):
    return error_response("Unexpected error", 400)

if __name__ == '__main__':
    app.run()

