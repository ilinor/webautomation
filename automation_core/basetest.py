# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import unittest
import datetime
import time
import logging, os
from selenium import webdriver
from automation_core.confparser import ConfigParser


class BaseTestClass(unittest.TestCase):
    """This is a base test case class"""

    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'log'))
    dataset = ConfigParser()
    selected_driver = dataset.selected_driver
    log_path = dataset.log_filename
    logging.basicConfig(filename=file_path + log_path,
                        level=dataset.logging_level)
    time_mark = datetime.datetime.fromtimestamp(time.time()).strftime(
        '%d%m%Y_%H%M%S')
    driver = None

    def setUp(self):

        self.test_name = ""
        logging.info("Starting Test ")
        if self.selected_driver == "Firefox":
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.download.folderList", 2)
            fp.set_preference("browser.startup.homepage_override.mstone",
                              "ignore")
            fp.set_preference("browser.startup.homepage", "about:blank")
            fp.set_preference("browser.download.manager.showWhenStarting",
                              False)
            fp.set_preference("browser.download.dir", os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', 'results')))
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                              "application/octet-stream")
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                              "application/zip")
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                              "application/vnd.openxmlformats-officedocument"
                              ".spreadsheetml.sheet")
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                              "application/vnd.ms-excel")
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                              "application/octet-stream;charset=UTF-8")
            self.driver = webdriver.Firefox(firefox_profile=fp)

        elif self.selected_driver == "Chrome":
            self.driver = webdriver.Chrome()

        elif self.selected_driver == "Ie" or self.selected_driver == "IE":
            self.driver = webdriver.Ie

        else:
            logging.error("None driver configured in config.yaml ")

        logging.debug("Using %s as webdriver" % self.selected_driver)
        self.driver.implicitly_wait(self.dataset.webdriver_wait)
        self.driver.get(self.dataset.test_app_url)
        self.driver.maximize_window()
        logging.debug("driver navigated to: %s" % self.driver.title)

    def take_screenshot(self):
        logging.info("Taking screenshot")
        file_screen = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'results'))
        self.file_name = file_screen + "\\" + self.test_name + \
                         self.time_mark + ".png"
        self.driver.save_screenshot(self.file_name)

    def verify_response(self, ethalon: str, returned_value: str)-> bool:
        """
        used instead raw assert
        :param ethalon:
        :param returned_value:
        :return:
        """
        return self.assertEquals(ethalon, returned_value)

    def tearDown(self):
        logging.info("Calling tear down procedure for this test")
        self.driver.close()
        self.driver.quit()
        logging.debug("Closing driver")
