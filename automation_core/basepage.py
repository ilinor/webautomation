# -*- coding: utf-8 -*-
from selenium import webdriver
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
        by.lower()
        if by == "xpath":
            return self.driver.find_element_by_xpath(element_path)
        if by == "id":
            return self.driver.find_element_by_id(element_path)