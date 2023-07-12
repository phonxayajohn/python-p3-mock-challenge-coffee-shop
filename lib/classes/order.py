
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        customer.orders(self)
        coffee.orders(self)
        coffee.customers(customer)
        customer.coffees(coffee)
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception