"""Initializes 'models' module."""

import redis
from rackspace_app import APP


# Configuring Redis server and initializing Redis client to use through out the
# application.
REDIS_CLIENT = redis.StrictRedis(
		host=APP.config['REDIS_IP'], port=APP.config['REDIS_PORT'], db=0)
