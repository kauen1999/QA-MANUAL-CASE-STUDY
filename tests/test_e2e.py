import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage

@pytest.mark.e2e
def test_complete_purchase_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    finish = FinishPage(page)

    login.navigate()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart.proceed_to_checkout()

    checkout.fill_information("Jocean", "QA", "12345000")

    finish.finish_order()

    assert "Thank you for your order!" in finish.get_success_message()
