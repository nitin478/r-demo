"""Module to define 'Product' related REST handlers."""

from bottle import request  # pylint: disable=redefined-outer-name
import json

from rackspace_app.models import products
from rackspace_app import LOGGER


# Error codes for different Server errors.
INTERNAL_ERROR = 500
BAD_REQUEST = 400


class ProductApiError(Exception):
    """Exception class to define errors for this module."""
    pass


class Product(object):
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
            # Return '200' with 'no data found' message.
            return {'success': True, 'msg': message}
        except Exception as error:
            message = ('Error while fetching product ID %s: %s' %
                       (product_id, error.message))
            LOGGER.error(message)
            return {'success': False, 'msg': message}, INTERNAL_ERROR
        return {'success': True, 'data': data.product_json}

    def post(self, product_id, request=request):  # pylint: disable=redefined-outer-name, no-self-use
        """Puts a product information in to DB with product ID as a key.

        Args:
            product_id: Unique ID of the product.

        Returns:
            A dictionary containing success message.
        """
        LOGGER.info('Recieved POST request for product ID: %s', product_id)
        data = request.forms.get('data', '{}')
        if not data:
            # Return '400' with 'no data to save' message.
            return {'success': False, 'msg': 'No data to post.'}, BAD_REQUEST
        try:
            data_dict = json.loads(data)
            product_name = data_dict.get('product_name', '')
            products.ProductsDetails.cached_create(
                    product_id=product_id, product_name=product_name,
                    product_json=data)
        except Exception as error:  #pylint: disable=broad-except
            message = ('Error while saving product ID %s: %s' %
                       (product_id, error.message))
            LOGGER.error(message)
            return {'success': False, 'msg': message}, INTERNAL_ERROR
        return {'success': True, 'msg': 'Data posted successfully.'}

    def delete(self, product_id):  # pylint: disable=no-self-use
        """Deletes a product information from DB.

        Args:
            product_id: Unique ID of the product.

        Returns:
            A dictionary containing success message.
        """
        LOGGER.info('Recieved DELETE request for product ID: %s', product_id)
        try:
            products.ProductsDetails.cached_delete(product_id=product_id)
        except products.ProductsDetails.DoesNotExist:
            message = 'No data found with product ID %s.' % product_id
            LOGGER.error(message)
            # Return '500' with 'no data found' message.
            return {'success': False, 'msg': message}, INTERNAL_ERROR
        except Exception as error:
            message = ('Error while deleting product ID %s: %s' %
                       (product_id, error.message))
            LOGGER.error(message)
            return {'success': False, 'msg': message}, INTERNAL_ERROR
        return {'success': True, 'msg': 'Data deleted successfully.'}
