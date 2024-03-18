import unittest
from bikeshop.products import Product, Products

class TestBikeShopProducts(unittest.TestCase):

    def test_get_product(self):
        _products = [Product(1, 'Mountain Bike', 1500), Product(2, 'Road Bike', 2500)]
        products = Products(_products)
        self.assertTrue({'id': "1", 'name': 'Mountain Bike', 'price': 1500} in products.get_product_by_id(1))
        self.assertTrue({'id': "2", 'name': 'Road Bike', 'price': 2500} in products.get_product_by_id(2))