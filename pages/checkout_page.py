class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = "input[data-test='firstName']"
        self.last_name = "input[data-test='lastName']"
        self.postal_code = "input[data-test='postalCode']"
        self.continue_btn = "input[data-test='continue']"
        self.url_step_two = "https://www.saucedemo.com/checkout-step-two.html"

    def fill_information(self, fname, lname, zip_code):
        self.page.fill(self.first_name, fname)
        self.page.fill(self.last_name, lname)
        self.page.fill(self.postal_code, zip_code)
        self.page.click(self.continue_btn)

    def is_on_step_two(self):
        return self.page.url == self.url_step_two
