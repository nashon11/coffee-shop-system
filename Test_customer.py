import unittest
from Customer import Customer
from Coffee import Coffee
from Order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(name="John Doe")
        self.coffee1 = Coffee(name="Espresso", price=5.0)
        self.coffee2 = Coffee(name="Latte", price=4.0)
        self.order1 = self.customer.create_order(coffee=self.coffee1, price=5.0)
        self.order2 = self.customer.create_order(coffee=self.coffee2, price=4.0)

    def test_customer_orders(self):
        self.assertIn(self.order1, self.customer.orders())
        self.assertIn(self.order2, self.customer.orders())

    def test_customer_coffees(self):
        self.assertIn(self.coffee1, self.customer.coffees())
        self.assertIn(self.coffee2, self.customer.coffees())

    def test_most_aficionado(self):
        self.assertEqual(Customer.most_aficionado(self.coffee1), self.customer)

if __name__ == '__main__':
    unittest.main()
