from django.conf import settings
from store.models import Product
import logging

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.logger = logging.getLogger(__name__) 
    
    def __iter__(self):
       for product in self.cart.keys():
           product_obj = Product.objects.get(pk=product)
           self.cart[str(product)]["product"] = product_obj
           print(f"Product object for {product}: {product_obj}") # add this line
       for item in self.cart.values():
           item["price"] = int(item["product"].price * item["quantity"])
           yield item
    
    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())
    
    def save (self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": int(quantity), "id": product_id}
        
        if update_quantity:
            self.cart[product_id]["quantity"] += int(quantity)

        if self.cart[product_id]["quantity"] == 0:
            self.remove(product_id)

        self.save()
         
    
    def remove(self, product_id):
        if str(product_id) in self.cart:
            del self.cart[str(product_id)]
            self.save()
            

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        return sum(item["quantity"] * item["product"].price for item in self.cart.values())
    
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def total_quantity(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        return sum(item["quantity"] for item in self.cart.values())