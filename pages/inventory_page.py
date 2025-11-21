from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/inventory.html"
        self.add_backpack = "button[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_icon = ".shopping_cart_link"

    def is_on_page(self):
        self.log("Validando página de inventário.")
        return self.page.url == self.url

    def add_backpack_to_cart(self):
        self.log("Adicionando item 'Sauce Labs Backpack' ao carrinho.")
        self.page.click(self.add_backpack)

    def go_to_cart(self):
        self.log("Indo para o carrinho.")
        self.page.click(self.cart_icon)
