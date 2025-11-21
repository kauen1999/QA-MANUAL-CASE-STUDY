from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = "#user-name"
        self.password = "#password"
        self.button = "#login-button"
        self.error_msg = "[data-test='error']"
        self.url = "https://www.saucedemo.com/"

    def navigate(self):
        self.log("Navegando para página de login.")
        self.page.goto(self.url)

    def login(self, user, pwd):
        self.log(f"Preenchendo usuário: {user}")
        self.page.fill(self.username, user)

        self.log("Preenchendo senha.")
        self.page.fill(self.password, pwd)

        self.log("Clicando no botão de login.")
        self.page.click(self.button)

    def get_error_message(self):
        self.log("Capturando mensagem de erro.")
        return self.page.inner_text(self.error_msg)
