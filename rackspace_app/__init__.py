"""Initializes rackspace demo application."""
import logging
import logging.config
from flask import Flask, request, render_template
from flask.ext import restful  # pylint: disable=no-name-in-module

APP = Flask(__name__)
API = restful.Api(APP)

# Loading configurations.
APP.config.from_object('rackspace_app.config.Config')

# Initializing logger.
LOGGER = logging.getLogger('myapp')
HANDLER = logging.FileHandler('rackspace_app.log')
FORMATTER = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.DEBUG)
