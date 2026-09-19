"""Exercise 5: Your first tests.

Run them with:      pytest -v

These fail until Cart is implemented. Failing tests can also provide some important information.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from exercise3 import Cart, OutOfStockError

GYOZA = {"id": 2, "name": "Gyoza (6 pc)", "price": 8.00, "available": True}
RAMEN = {"id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "available": True}
MISO = {"id": 4, "name": "Spicy Miso Ramen", "price": 17.25, "available": False}


def test_empty_cart_total_is_zero():
    assert Cart().total() == 0


def test_total_across_multiple_items():
    cart = Cart()
    cart.add_item(GYOZA, 2)      # 16.00
    cart.add_item(RAMEN, 1)      # 16.50
    assert cart.total() == 32.50


def test_adding_same_item_twice_increases_quantity():
    cart = Cart()
    cart.add_item(GYOZA, 2)
    cart.add_item(GYOZA, 1)
    assert len(cart.lines) == 1
    assert cart.lines[0]["qty"] == 3


def test_zero_quantity_is_rejected():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item(GYOZA, 0)


def test_unavailable_item_is_rejected():
    cart = Cart()
    with pytest.raises(OutOfStockError):
        cart.add_item(MISO, 1)


def test_removing_an_absent_item_raises():
    cart = Cart()
    with pytest.raises(KeyError):
        cart.remove_item(999)


# TODO: add one test of your own. What behaviour is not covered above?
