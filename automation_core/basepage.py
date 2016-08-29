# -*- coding: utf-8 -*-
import logging
from selenium import webdriver
from selenium.common import exceptions
from automation_core.confparser import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    page_name = ""
    parser = ConfigParser()

    def __init__(self):
        if self.parser.selected_driver == "Chrome":
            self.driver = webdriver.Chrome
        elif self.parser.selected_driver == "Firefox":
            self.driver = webdriver.Firefox
        elif self.parser.selected_driver == "Ie":
            self.driver = webdriver.Ie

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
                return self.driver.find_element(By.XPATH, element_path)
            if by == "id":
                return self.driver.find_element(By.ID, element_path)
            if by == "name":
                return self.driver.find_element(By.NAME, element_path)
            if by == "class":
                return self.driver.find_element(By.CLASS_NAME, element_path)
            if by == "css":
                return self.driver.find_element(By.CSS_SELECTOR, element_path)

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
                return self.driver.find_elements(By.XPATH, element_path)
            if by == "id":
                return self.driver.find_elements(By.ID, element_path)
            if by == "name":
                return self.driver.find_elements(By.NAME, element_path)
            if by == "class":
                return self.driver.find_elements(By.CLASS_NAME, element_path)
            if by == "css":
                return self.driver.find_elements(By.CSS_SELECTOR, element_path)


        except (exceptions.WebDriverException, AssertionError) as ex:
            self.take_screenshot()
            logging.info('Exception', exc_info=True)
            print(type(ex).__name__)
            print(ex.args)
            self.fail("Caught an exception")

    def click(self, element):
        actions = ActionChains(self.driver)
        actions.click(element).perform()
    
    def double_click(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
