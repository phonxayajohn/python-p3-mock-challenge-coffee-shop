class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self.new_coffees = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):

        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee and isinstance(new_coffee, Coffee) and new_coffee not in self.new_coffees:
            self.new_coffees.append(new_coffee)
        return self.new_coffees
    
        # return list(set([order.coffee for order in self._orders]))


#         - `Customer create_order(coffee, price)`
#   - given a **coffee object** and a price(as an integer), creates a
#     new order and associates it with that customer and coffee.

    def create_order(self, coffee, price):
        from classes.coffee import Coffee
        from classes.order import Order
        if isinstance(coffee, Coffee) and isinstance(price, int):
            Order(self.name, coffee, price)
        else:
            raise Exception

