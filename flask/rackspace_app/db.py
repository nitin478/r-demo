"""Initializes Cassandra DB connection."""
from cqlengine import connection
from cqlengine.management import sync_table
from rackspace_app.models import products
from rackspace_app import APP


# pylint: disable=too-few-public-methods
class Database(object):
    """Defines and provide functions to control DB connection."""

    def __init__(self):
        self.database_ip = APP.config['DATABASE_IP']
        self.database_name = APP.config['DATABASE_NAME']

    def run(self):
        """Runs DB server and sync models with Cassandra coloumn family."""
        connection.setup(self.database_ip, self.database_name)
        sync_table(products.ProductsDetails)
