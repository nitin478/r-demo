"""Defines application wise configurations."""


# pylint: disable=too-few-public-methods
class Config(object):
    """Defines default configurations for application."""

    SERVER_IP = '0.0.0.0'
    DEBUG = True
    TESTING = False
    DATABASE_IP = ['127.0.0.1']
    DATABASE_NAME = 'rackspace_demo'
    REDIS_IP = '127.0.0.1'
    REDIS_PORT = '6379'
