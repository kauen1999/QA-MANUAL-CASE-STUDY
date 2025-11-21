from utils.logger import logger

class BasePage:
    def __init__(self, page):
        self.page = page

    def log(self, message: str):
        logger.info(message)
