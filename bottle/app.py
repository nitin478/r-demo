"Rackspace demo application"

import bottle

print dir(bottle.FormsDict)

from rackspace_app import APP, db, LOGGER
from rackspace_app.endpoints.product_api import Product

class Server(object):

    """ Class to initialize bottle server """

    def __init__(self):
        self.route()

    def route(self):  # pylint: disable=no-self-use
        """
        Method to define dynamic routing with appropriate callbacks for
        RESTFULL service methods GET, POST and DELETE
        """

        APP.route('/Rackspace/api/v1.0/product/<product_id>', \
                  method="GET", callback=Product().get)
        APP.route('/Rackspace/api/v1.0/product/<product_id>', \
                  method="POST", callback=Product().post)
        APP.route('/Rackspace/api/v1.0/product/<product_id>', \
                  method="DELETE", callback=Product().delete)

    def start(self):  # pylint: disable=no-self-use
        """Implements method to run the in-built http server."""
        APP.run(host=APP.config.SERVER_IP, debug=APP.config.DEBUG)

if __name__ == '__main__':
    LOGGER.info('Starting Server & database connections...')
    db.Database().run()
    Server().start()
