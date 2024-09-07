from Coffee import Coffee
from Customer import Customer

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Order must have a Customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Order must have a Coffee.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    def __str__(self):
        return f"Order for {self.customer.name}: {self.coffee.name} - ${self.price:.2f}"
