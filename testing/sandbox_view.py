from src.dynamic_view import DynamicView
from src.dynamic_element import DynamicElement


class SandboxView(DynamicView):
    """
    Class for representation of page/view in web app
    Parameters - elements in view
    Methods - actions for elements
    """
    element = DynamicElement(locator=("css selector", ' [class="button"]'))

    def __init__(self, driver):
        DynamicView.__init__(self, driver)

    def get_element(self):
        return self.element.get_by_context(self)
