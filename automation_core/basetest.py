# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import csv
import unittest
import datetime
import time
import logging, os
import xlrd
from selenium import webdriver
from automation_core.confparser import ConfigParser
from ddt import ddt, data, unpack

@ddt
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
    driver_path_chrome = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'drivers\chromedriver.exe')
    )
    if dataset.csv_resource is not None:
        resource_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'resources/' +
                         dataset.csv_resource)
        )
    elif dataset.excell_resource is not None:
        resource_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'resources/' +
                         dataset.excell_resource)
        )
    else:
        logging.error("No resource file found")

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
            self.driver = webdriver.Chrome(self.driver_path_chrome)

        elif self.selected_driver == "Ie" or self.selected_driver == "IE":
            self.driver = webdriver.Ie

        else:
            logging.error("None driver configured in config.yaml ")

        logging.debug("Using %s as webdriver" % self.selected_driver)
        self.driver.implicitly_wait(self.dataset.webdriver_wait)
        self.driver.get(self.dataset.test_app_url)
        self.driver.maximize_window()
        logging.debug("driver navigated to: %s" % self.driver.title)

    def get_data(file_name):
        # empty row list
        rows = []

        # open csv file
        data_file = open(file_name, "rt")

        # check file type before processing
        ext = os.path.splitext(file_name)[1][1:]
        if ext == 'csv':
            # csv reader
            reader = csv.reader(data_file)

            for row in reader:
                rows.append(row)

        elif ext == 'xlsx' or ext == 'xls':
            # open the specified Excel spreadsheet as workbook
            book = xlrd.open_workbook(file_name)

            # get the first sheet
            sheet = book.sheet_by_index(0)

            # iterate through the sheet and get data from rows in list
            for row_idx in range(1, sheet.nrows):
                rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
        else:
            logging.error('Resource file extension unsupported')



        return rows

    def take_screenshot(self):
        logging.info("Taking screenshot")
        file_screen = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'results'))
        self.file_name = file_screen + "\\" + self.test_name + \
                         self.time_mark + ".png"
        self.driver.save_screenshot(self.file_name)

    # dodaj metodu load_data
    @data(*get_data(resource_file_path))
    @unpack
    def load_data(self):
        pass

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
