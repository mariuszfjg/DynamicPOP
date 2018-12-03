from selenium.webdriver.remote.webdriver import WebDriver


class DynamicView:
    def __init__(self, webdriver, root_uri=None):
        assert isinstance(webdriver, WebDriver)
        self.__driver = webdriver
        self.__root_uri = root_uri


    @property
    def root_uri(self):
        return self.__root_uri

    @property
    def driver(self):
        return self.__driver

    @property
    def get(self):
        return self.__driver
