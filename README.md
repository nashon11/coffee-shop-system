# coffee-shop-system

Overview

The Coffee Shop System is a Python application designed to manage coffee orders and customer interactions in a coffee shop setting. It allows for the creation of customers, coffee types, and orders, and provides methods to track orders and analyze customer preferences.
Features

    Customer Management: Create and manage customer profiles.
    Coffee Management: Define different types of coffee with prices.
    Order Management: Place orders, associate them with customers and coffee types, and validate order details.
    Reports: Analyze customer spending and preferences.

Installation

To get started with the Coffee Shop System, follow these steps:

    Clone the Repository:

    bash

git clone <repository-url>
cd coffee-shop-system

Set Up a Virtual Environment:

bash

python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate

Install Dependencies:

bash

    pip install -r requirements.txt

Usage

    Create a Customer:

    python

from Customer import Customer
customer = Customer(name="John Doe")

Add Coffee Types:

python

from Coffee import Coffee
coffee = Coffee(name="Espresso", price=5.0)

Place an Order:

python

from Order import Order
order = Order(customer=customer, coffee=coffee, price=5.0)

View Orders:

python

    orders = customer.orders()
    for order in orders:
        print(order)

Testing

To run the tests for the Coffee Shop System, use the following command:

bash

python -m unittest discover -s . -p "Test_*.py"

Contributing

If you'd like to contribute to the Coffee Shop System, please follow these guidelines:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes and commit them (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
