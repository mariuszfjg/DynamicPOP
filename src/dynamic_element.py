from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions as SCE
import selenium.webdriver.support.expected_conditions as EC


from src.dynamic_view import DynamicView


class DynamicElement:
    def __init__(self,
                 locator,
                 context=False,
                 timeout=2,
                 poll_frequency=0.5,
                 ignored_exceptions=(SCE.StaleElementReferenceException, SCE.NoSuchElementException)):
        assert isinstance(locator, (list, tuple))
        assert len(locator) == 2
        assert locator[0] in _SUPPORTED_LOCATORS

        self.__locator = locator

        self.__has_context = bool(context)

        self.__timeout = timeout
        self.__poll_frequency = poll_frequency
        self.__ignored_exceptions = ignored_exceptions

    def get_by_context(self, context):
        return WebDriverWait(driver=context.get(),
                             timeout=self.timeout,
                             poll_frequency=self.poll_frequency,
                             ignored_exceptions=self.ignored_exceptions)\
            .until(EC.presence_of_element_located(self.locator))



    @property
    def locator(self):
        return self.__locator

    @property
    def locator_type(self):
        return self.__locator[0]

    @property
    def locator_value(self):
        return self.__locator[1]

    @property
    def has_context(self):
        return self.__has_context

    @property
    def timeout(self):
        return self.__timeout

    @property
    def poll_frequency(self):
        return self.__poll_frequency

    @property
    def ignored_exceptions(self):
        return self.__ignored_exceptions



_SUPPORTED_LOCATORS = (
    By.ID,
    By.XPATH,
    By.LINK_TEXT,
    By.PARTIAL_LINK_TEXT,
    By.NAME,
    By.TAG_NAME,
    By.CLASS_NAME,
    By.CSS_SELECTOR,
)
