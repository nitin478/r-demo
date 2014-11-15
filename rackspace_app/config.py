"""Defines application wise configurations."""


# pylint: disable=too-few-public-methods
class Config(object):
    """Defines default configurations for application."""

    DEBUG = True
    TESTING = True
    DATABASE_IP = ['127.0.0.1']
    DATABASE_NAME = 'rackspace_demo'
    REDIS_IP = '127.0.0.1'
    REDIS_PORT = '6379'
