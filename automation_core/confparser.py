# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import yaml
import os


class ConfigParser(object):
    """
    Loads data from config.yaml and elements.yaml files
    """

    # current dir
    cd = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'automation_core'))
    cd2 = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'results'))

    # config varibles
    selected_driver = ''
    logging_level = ''
    test_app_url = ''
    reporting_email = ''
    reporting_email_pass = ''
    imap_server = ''
    imap_port = ''
    smtp_server = ''
    smtp_port = ''
    log_filename = ''
    downloads_path = ''
    webdriver_wait = ''
    csv_resource=''
    excell_resource=''

    def __init__(self):
        self.load_config()

    def load_config(self):
        """loads all configuration and location data"""

        # If added new item in config.yaml file add it here
        with open(self.cd + "\config.yaml") as c_data:
            config_data = yaml.load(c_data)

        # collect selected driver:
        self.selected_driver = config_data["driver"]["selected_driver"]
        self.webdriver_wait = config_data["webdriver_wait"]
        self.webdriver_wait = int(self.webdriver_wait)

        # collect logger information:
        self.log_filename = config_data["logger"]["log_filename"]
        self.logging_level = config_data["logger"]["logging_level"]

        # collect TT url:
        self.test_app_url = config_data["url"]["test_app_url"]

        # collect browser settings:
        self.downloads_path = config_data["browser_settings"]["downloads_path"]

        # collect email configuration for sending and receiving emails:
        self.reporting_email = config_data["email_config"]["reporting_email"]
        self.reporting_email_pass = config_data["email_config"][
            "reporting_email_password"]

        # collect imap and smtp information:
        self.imap_server = config_data["email_config"]["imap_server"]
        self.imap_port = config_data["email_config"]["imap_port"]
        self.smtp_server = config_data["email_config"]["smtp_server"]
        self.smtp_port = config_data["email_config"]["smtp_port"]

        #collect resource files
        self.csv_resource = config_data["csv_resource"]
        self.excell_resource = config_data["excell_resource"]
