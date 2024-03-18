from typing import List, Dict

class Product(object):
    def __init__(self, id: str|int, name: str, price: float):
        self.id = str(id)
        self.name = name
        self.price = price
    
class Products(object):
    def __init__(self, products: List[Product]):
        self.products = products
    
    def get_products(self):
        return [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price
            } for product in self.products
        ]
    
    def get_product_by_id(self, id: str|int) -> List[Dict]:
        return [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price
            } for product in self.products if product.id == str(id)
        ]
    
    def get_product_by_name(self, name: str) -> List[Dict]:
        return [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price
            } for product in self.products if product.name == name
        ]
    
    
    def get_product_by_price(self, price: float) -> List[Dict]:
        return [
            {
                "id": product.id,
                "name": product.name,
            } for product in self.products if product.price == price
        ]
    
