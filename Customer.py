class Customer:
    all_customers = []

    def __init__(self, name):
        self._name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def create_order(self, coffee, price):
        from Order import Order
        return Order(self, coffee, price)

    def orders(self):
        from Order import Order
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    @classmethod
    def most_aficionado(cls, coffee):
        from Order import Order
        customers = [order.customer for order in coffee.orders()]
        if not customers:
            return None

        customer_spending = {}
        for customer in customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            customer_spending[customer] = total_spent

        return max(customer_spending, key=customer_spending.get, default=None)
