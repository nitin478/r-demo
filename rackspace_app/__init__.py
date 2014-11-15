"""Initializes rackspace demo application."""
from flask import Flask, request, render_template
from flask.ext import restful  # pylint: disable=no-name-in-module

APP = Flask(__name__)
API = restful.Api(APP)

# Loading configurations.
APP.config.from_object('rackspace_app.config.Config')
