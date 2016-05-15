import os
import unittest
import logging
from selenium.common import exceptions
from automation_core.basetest import BaseTestClass
from automation_core.confparser import ConfigParser


from pages.PageDummy import PageDummy


class TestDummy(BaseTestClass):
    """
    Makes search for some item and prints the
    value of the first link
    """
    parser = ConfigParser()

    def test_search(self):
        """
        Makes the search and prints the string of the first link
        :return:
        """
        my_page = PageDummy(self.driver)
        requested_term = "Facebook"
        try:
            my_page.google_search(requested_term)
            result = my_page.select_similar_results(requested_term)
            print(result)
            self.assertEqual(len(result), 25, "Intentional error")
        except (exceptions.WebDriverException, AssertionError) as ex:
            self.take_screenshot()
            logging.info('Exception', exc_info=True)
            print(type(ex).__name__)
            print(ex.args)
            self.fail("Caught an exception")

if __name__ == '__main__':
    unittest.main(verbosity=1)
