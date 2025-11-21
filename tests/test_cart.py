import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.smoke
@pytest.mark.cart
def test_add_item_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.navigate()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    assert "Sauce Labs Backpack" in cart.get_item_name()


@pytest.mark.regression
@pytest.mark.cart
def test_remove_item_from_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.navigate()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    cart.remove_item()

    assert len(cart.get_cart_items()) == 0
