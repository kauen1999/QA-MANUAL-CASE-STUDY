import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.regression
def test_checkout_form(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.navigate()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    cart.proceed_to_checkout()

    checkout.fill_information("Jocean", "QA", "12345000")

    assert checkout.is_on_step_two()
