"""Rackspace demo application."""

from rackspace_app import APP, API, db
from rackspace_app.endpoints import product_api


# Add all avaiable API URls and endpoints here.
API.add_resource(
        product_api.Product, '/Rackspace/api/v1.0/product/<string:product_id>')


if __name__ == '__main__':
    db.Database().run()  # Runs Cassandra database server.
    APP.run(debug=APP.config['DEBUG'])
