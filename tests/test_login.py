import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.navigate()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_on_page()


@pytest.mark.regression
def test_login_invalid(page):
    login = LoginPage(page)

    login.navigate()
    login.login("invalid", "invalid")

    assert "Username and password do not match" in login.get_error_message()


@pytest.mark.regression
def test_locked_out_user(page):
    login = LoginPage(page)

    login.navigate()
    login.login("locked_out_user", "secret_sauce")

    assert "Sorry, this user has been locked out" in login.get_error_message()
