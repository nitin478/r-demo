"""Module to define 'Product' related REST handlers."""
from flask import request
from flask.ext import restful  # pylint: disable=no-name-in-module
import json
from rackspace_app.models import products
from rackspace_app import LOGGER


class ProductApiError(Exception):
    """Exception class to define errors for this module."""
    pass


class Product(restful.Resource):
    """Defines REST handlers for product APIs."""

    def __init__(self):
        pass

    def get(self, product_id):  # pylint: disable=no-self-use
        """Gets a product information by its product ID.

        Args:
            product_id: Unique ID of the product.

        Returns:
            A dictionary containing product info as JSON string.
        """
        LOGGER.info('Recieved GET request for product ID: %s', product_id)
        try:
            data = products.ProductsDetails.cached_get(product_id=product_id)
        except products.ProductsDetails.DoesNotExist:
            message = 'No data found with product ID %s.' % product_id
            LOGGER.error(message)
            return {'success': False, 'msg': message}
        except Exception as error:
            message = ('Error while fetching product ID %s: %s' %
                       (product_id, error.message))
            LOGGER.error(message)
            return {'success': False, 'msg': message}
        return {'msg': data.product_json}

    def post(self, product_id):  # pylint: disable=no-self-use
        """Puts a product information in to DB with product ID as a key.

        Args:
            product_id: Unique ID of the product.

        Returns:
            A dictionary containing success message.
        """
        LOGGER.info('Recieved POST request for product ID: %s', product_id)
        data = request.form.get('data', '{}')
        if not data:
            raise ProductApiError('No data to post.')
        try:
            data_dict = json.loads(data)
            product_name = data_dict.get('product_name', '')
            products.ProductsDetails.cached_create(
                    product_id=product_id, product_name=product_name,
                    product_json=data)
        except Exception as error:
            message = ('Error while saving product ID %s: %s' %
                       (product_id, error.message))
            LOGGER.error(message)
            return {'success': False, 'msg': message}
        return {'success': True, 'msg': 'Data posted...'}
