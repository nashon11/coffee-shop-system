class Coffee:
    all_coffees = []

    def __init__(self, name, price):
        if not isinstance(name, str) or not (1 <= len(name) <= 20):
            raise ValueError("Name must be a string between 1 and 20 characters.")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._name = name
        self._price = price
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def orders(self):
        from Order import Order
        return [order for order in Order.all_orders if order.coffee == self]

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
