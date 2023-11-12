import pytest
from acme import Product
from acme_report import generate_products


def test_default_product_price():
    prod = Product("Test Product")
    assert prod.price == 10


def test_default_product_attributes():
    prod = Product("Test Product")
    assert prod.weight == 20
    assert prod.flammability == 0.5


def test_product_stealability():
    prod = Product("Test Product", price=20, weight=30)
    assert prod.stealability() == "Kinda stealable."


def test_product_explode():
    prod = Product("Test Product", weight=100, flammability=2.5)
    assert prod.explode() == "...BABOOM!!"


def test_generate_products_default_length():
    products = generate_products()
    assert len(products) == 30


# Run the tests
if __name__ == "__main__":
    pytest.main()
