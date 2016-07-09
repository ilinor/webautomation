import logging
import unittest
from automation_core.basetest import BaseTestClass
from pages.magentoSearchPage import MagentoSearchPage


class TestMagentoSearch(BaseTestClass):

    def test_search_phones(self):
        self.page = MagentoSearchPage(self.driver)
        self.page.click_on_search()
        self.page.enter_search("phones")
        phone_list = self.page.get_elements("xpath",".//*[@class='result-title']")
        logging.info(len(phone_list))


if __name__ == '__main__':
    unittest.main(verbosity=1)