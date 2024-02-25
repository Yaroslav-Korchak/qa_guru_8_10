import pytest
from .models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()

@pytest.fixture
def not_empty_cart(product, cart):
    hat = Product('шляпа', 10, 'зелёная', 3)
    cart.add_product(product, 10)
    cart.add_product(hat, 1)
    return cart
