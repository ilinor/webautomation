import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from automation_core.basepage import BasePage
from automation_core.confparser import ConfigParser


class PageDummy(BasePage):
    """
    Dummy Page helper to show the usage of
    Page Object
    """
    page_name = "Page Dummy"
    parser = ConfigParser()

    def google_search(self, requested_item: str):
        """
        Searches google.com for requested term
        :param requested_item:
        :return:
        """
        locator = 'q'
        search_box = self.driver.find_element_by_name(locator)
        search_box.clear()
        search_box.send_keys(requested_item)
        search_box.send_keys(Keys.ENTER)
        time.sleep(10)

    def select_similar_results(self, term) -> list:
        """
        Selects first result returned by the search
        :return:
        """
        locator = (".//a[contains(text(),'" + term +"')]")
        results = []
        results = self.driver.find_elements_by_xpath(locator)
        text_repr = []
        for element in results:
            text_repr.append(element.text)

        return text_repr
