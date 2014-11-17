"Rackspace demo application"

import bottle

print dir(bottle.FormsDict)

from rackspace_app import APP, db, LOGGER
from rackspace_app.endpoints.product_api import Product

class Server(object):

    """ Class to initialize bottle server """

    def __init__(self):
        self.route()

    def route(self):
        APP.route('/Rackspace/api/v1.0/product/<product_id>', \
                  method="GET", callback=Product().get)
        APP.route('/Rackspace/api/v1.0/product/<product_id>', \
                  method="POST", callback=Product().post)
        APP.route('/Rackspace/api/v1.0/product/<product_id>', \
                  method="DELETE", callback=Product().delData)

    def start(self):
        APP.run(host=APP.config.SERVER_IP, debug=APP.config.DEBUG)

if __name__ == '__main__':
    LOGGER.info('Starting Server & database connections...')
    db.Database().run()
    Server().start()
