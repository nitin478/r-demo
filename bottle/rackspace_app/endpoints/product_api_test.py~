import unittest
from mock import MagicMock
from bottle import LocalRequest, FormsDict
from rackspace_app.endpoints.product_api import Product
from rackspace_app.models import products

class TestProduct(unittest.TestCase):

    def testPost(self):
        key = "12345"
        class request():
            forms = {}
        dataDict = {'data' :'{"product_id":%s, \
                         "product_name": "Cisco 5SA", \
                         "product_type" : "FIREWALL"}' % key}
        request.forms = dataDict
        data =request.forms.get('data', '{}')
        api = Product()
        products.ProductsDetails.cached_create = MagicMock(return_value=None)
        api.post(product_id=key, request=request)
        products.ProductsDetails.cached_create.assert_called_once_with(product_id=key, product_name="Cisco 5SA", product_json=data) 

    def testGet(self): 
       
        key = "12345"
        products.ProductsDetails.product_id = key
        products.ProductsDetails.product_name = "Cisco 5SA"
        products.ProductsDetails.product_json = {"type": "FIREWALL"}
        
        dataDict = products.ProductsDetails()
        api = Product()
        products.ProductsDetails.cached_get = MagicMock(return_value=dataDict)
        api.get(product_id=key)
        products.ProductsDetails.cached_get(product_id=key)    
