"""Module to define 'Product' related REST handlers."""
from flask import request
from flask.ext import restful  # pylint: disable=no-name-in-module
import json
from rackspace_app.models import products


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
        data = products.ProductsDetails.cached_get(product_id=product_id)
        return {'msg': data.product_json}

    def post(self, product_id):  # pylint: disable=no-self-use
        """Puts a product information in to DB with product ID as a key.

        Args:
            product_id: Unique ID of the product.

        Returns:
            A dictionary containing success message.
        """
        data = request.form.get('data', '{}')
        data_dict = json.loads(data)
        product_name = data_dict.get('product_name', '')
        products.ProductsDetails.cached_create(
                product_id=product_id, product_name=product_name,
                product_json=data)
        return {'success': True, 'msg': 'Data posted...'}
