"Initialize demo bottle application"

import logging
import logging.config
from bottle import Bottle, request, TEMPLATE_PATH
from rackspace_app import config

APP = Bottle()
TEMPLATE_PATH.insert(0, '/home/umeshbhaskaran/r_demo/bottle/rackspace_app/templates')
# Loading Configurations
APP.config.update(config.Config.__dict__)

# Configuring logger

LOGGER = logging.getLogger('rackspace_app')
HANDLER = logging.FileHandler('/tmp/rackspace_app.log')
FORMATTER = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.DEBUG)
