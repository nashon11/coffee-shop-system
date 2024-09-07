import unittest
from Customer import Customer
from Coffee import Coffee  
from Order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(name="John Doe")
        self.coffee1 = Coffee(name="Espresso", price=5.0)
        self.coffee2 = Coffee(name="Latte", price=4.0)
        self.order = Order(customer=self.customer, coffee=self.coffee1, price=5.0)

    def test_order_total(self):
        self.assertEqual(self.order.price, 5.0)

    def test_order_string(self):
        self.assertEqual(str(self.order), "Order for John Doe: Espresso - $5.00")

if __name__ == '__main__':
    unittest.main()
