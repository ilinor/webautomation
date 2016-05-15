# -*- coding: utf-8 -*-
from selenium import webdriver
from automation_core.confparser import ConfigParser


class BasePage:
    page_name = ""
    parser = ConfigParser()

    def __init__(self, driver: parser.selected_driver):
        self.driver = driver

    def get_element(self, by, element_path):
        """
        gets webelement by any given way:
        xpath, id, css, name...so on...
        :param by:
        :param element_path:
        :return:
        """
        return self.driver.find_element(by, element_path)