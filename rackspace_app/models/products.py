"""Defines Models for Product."""
from cqlengine import columns
from cqlengine import Model
from rackspace_app.models.db_cache_mixin import DbCacheMixin

class ProductsDetails(Model, DbCacheMixin):
    """Model to store Product information.

    properties:
        product_id: Pimary key, stores ID of product.
        product_name: Name of the product.
        product_json: JSON reprenstation for product information.
    """
    product_id = columns.Text(primary_key=True)
    product_name = columns.Text()
    product_json = columns.Text()
