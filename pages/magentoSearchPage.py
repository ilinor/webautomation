from selenium.webdriver.common.keys import Keys

from automation_core.basepage import BasePage
from automation_core.confparser import ConfigParser
from selenium.webdriver.common.by import By

class MagentoSearchPage(BasePage):

    page_name = "MagentoPage"


    def click_on_search(self):
        search_button = self.get_element("XPATH",".//*[@class='fa fa-search']")
        search_button.click()

    def enter_search(self, search_term: str):
        search_field = self.get_element("xpath",".//*[contains(@placeholder, 'Search')]")
        search_field.clear()
        search_field.send_keys(search_term)
        search_field.send_keys(Keys.ENTER)

