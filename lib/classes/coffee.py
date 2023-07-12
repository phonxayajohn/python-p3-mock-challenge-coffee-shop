class Coffee:
    def __init__(self, name):
        self._orders = []
        self.new_customers = []

        if isinstance(name, str):
            self.name = name
        else:
            raise Exception
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer) and new_customer not in self.new_customers:
            self.new_customers.append(new_customer)
        return self.new_customers

        # return list(set([order.customer for order in self._orders]))
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if len(self._orders) > 0:
            total_price = sum([order.price for order in self._orders])
            average_price = total_price / len(self._orders)
            return average_price
        return 0