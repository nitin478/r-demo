"Rackspace demo application"

import bottle
from rackspace_app import APP, db, LOGGER
from rackspace_app.endpoints.product_api import Product, Products

class Server(object):

    """ Class to initialize bottle server """

    def __init__(self):
        bottle.TEMPLATE_PATH.insert(0, '/home/umeshbhaskaran/r_demo/bottle/rackspace_app/templates')
        self.route()

    def route(self):  # pylint: disable=no-self-use
        """
        Method to define dynamic routing with appropriate callbacks for
        RESTFULL service methods GET, POST and DELETE
        """

        APP.route('/rackspace/bottle/api/v1.0/products', \
                  method="GET", callback=Products().get)
        APP.route('/rackspace/bottle/api/v1.0/product/<product_id>', \
                  method="GET", callback=Product().get)
        APP.route('/rackspace/bottle/api/v1.0/product/<product_id>', \
                  method="POST", callback=Product().post)
        APP.route('/rackspace/bottle/api/v1.0/product/<product_id>', \
                  method="DELETE", callback=Product().delete)
        APP.route('/static/<filename:path>', callback=Product().static)
        APP.route('/index.html', callback=Product().index)

    def start(self):  # pylint: disable=no-self-use
        """Implements method to run the in-built http server."""
        APP.run(host=APP.config.SERVER_IP, debug=APP.config.DEBUG)

if __name__ == '__main__':
    LOGGER.info('Starting Server & database connections...')
    db.Database().run()
    Server().start()
