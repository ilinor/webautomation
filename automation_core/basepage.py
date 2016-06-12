# -*- coding: utf-8 -*-
import logging
from selenium import webdriver
from selenium.common import exceptions

from automation_core.confparser import ConfigParser
from selenium.webdriver.common.by import By


class BasePage:
    page_name = ""
    parser = ConfigParser()

    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def get_element(self, by: str, element_path: str):
        """
        gets webelement by any given way:
        xpath, id, css, name...so on...
        :param by:
        :param element_path:
        :return:
        """
        by = by.lower()
        try:
            if by == "xpath":
                return self.driver.find_element_by_xpath(element_path)
            if by == "id":
                return self.driver.find_element_by_id(element_path)
            if by == "name":
                return self.driver.find_element_by_name(element_path)
            if by == "class":
                return self.driver.find_element_by_class(element_path)
            if by == "css":
                return self.driver.find_element_by_css(element_path)

        except (exceptions.WebDriverException, AssertionError) as ex:
            self.take_screenshot()
            logging.info('Exception', exc_info=True)
            print(type(ex).__name__)
            print(ex.args)
            self.fail("Caught an exception")


    def get_elements(self, by: str, elements: str):
        """
        returns list of elements
        :param by:
        :param elements:
        :return:
        """
        by = by.lower()
        try:
            if by == "xpath":
                return self.driver.find_elements_by_xpath(elements)
            if by == "id":
                return self.driver.find_elements_by_id(elements)
            if by == "name":
                return self.driver.find_elements_by_name(elements)
            if by == "class":
                return self.driver.find_elements_by_class(elements)
            if by == "css":
                return self.driver.find_elements_by_css(elements)

        except (exceptions.WebDriverException, AssertionError) as ex:
            self.take_screenshot()
            logging.info('Exception', exc_info=True)
            print(type(ex).__name__)
            print(ex.args)
            self.fail("Caught an exception")