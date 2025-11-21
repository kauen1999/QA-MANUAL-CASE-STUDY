from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_btn = "button[data-test='checkout']"
        self.item_name = ".inventory_item_name"
        self.remove_btn = "button[data-test='remove-sauce-labs-backpack']"

    def proceed_to_checkout(self):
        self.log("Prosseguindo para checkout.")
        self.page.click(self.checkout_btn)

    def remove_item(self):
        self.log("Removendo item do carrinho.")
        self.page.click(self.remove_btn)

    def get_item_name(self):
        self.log("Capturando nome do item no carrinho.")
        return self.page.inner_text(self.item_name)

    def get_cart_items(self):
        self.log("Capturando lista de itens no carrinho.")
        return self.page.query_selector_all(".cart_item")
