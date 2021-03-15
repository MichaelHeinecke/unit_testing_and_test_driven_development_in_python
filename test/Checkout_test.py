import pytest

from src.Checkout import Checkout


@pytest.fixture
def checkout():
    checkout = Checkout()
    checkout.add_item_price("item", 5)
    checkout.add_item_price("another_item", 10)
    return checkout


def test_can_calculate_checkout_total(checkout):
    checkout.add_item("item")
    assert checkout.calculate_total() == 5


def test_can_add_multiple_items_and_get_correct_total(checkout):
    checkout.add_item("item")
    checkout.add_item("another_item")
    assert checkout.calculate_total() == 15


def test_can_add_discount(checkout):
    checkout.add_discount("another_item", 2, 6)


def test_can_apply_discount(checkout):
    checkout.add_item("item")
    checkout.add_item("another_item")
    checkout.add_item("another_item")
    checkout.add_discount("another_item", 2, 6)
    assert checkout.calculate_total() == 17


def test_throw_error_on_adding_item_without_price(checkout):
    with pytest.raises(Exception):
        checkout.add_item("yet_another_item")
