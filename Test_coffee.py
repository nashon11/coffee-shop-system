import unittest
from Coffee import Coffee
from Order import Order
from Customer import Customer

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(name="John Doe")
        self.coffee = Coffee(name="Espresso", price=5.0)
        self.order = self.customer.create_order(coffee=self.coffee, price=5.0)

    def test_coffee_orders(self):
        self.assertIn(self.order, self.coffee.orders())

    def test_coffee_str(self):
        self.assertEqual(str(self.coffee), "Espresso - $5.00")

if __name__ == '__main__':
    unittest.main()
