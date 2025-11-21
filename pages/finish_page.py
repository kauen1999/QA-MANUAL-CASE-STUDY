class FinishPage:
    def __init__(self, page):
        self.page = page
        self.finish_btn = "button[data-test='finish']"
        self.success_msg = "h2.complete-header"

    def finish_order(self):
        self.page.click(self.finish_btn)

    def get_success_message(self):
        return self.page.inner_text(self.success_msg)
