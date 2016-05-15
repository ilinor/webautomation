from email import encoders
import glob
import logging
import os
import zipfile
from .confparser import ConfigParser
import smtplib
from os.path import join
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


class ZipAndSend(object):
    """this class is called to zip the
    results folder with all containing files and
    to send it to receiving email"""

    conf_parser = ConfigParser()
    log_path = conf_parser.log_filename
    file_path_log = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'log'))
    logging.basicConfig(filename=file_path_log + log_path,
                        level=conf_parser.logging_level)
    text = 'Hello, this is \n your test report with zipped attachment'
    with open("tests.html", "r") as myfile:
        xmlcontents = myfile.read()

    def __init__(self):
        self.zfName = self.file_to_zs
        self.file_to_zs = self.file_path + 'Results.zip'
        self.file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'results'))

    def zip_me(self):
        """zip results folder"""
        self.file_zip = zipfile.ZipFile(self.zfName, "w")

        for f in glob.glob(join(self.file_path, "*.*")):
            self.file_zip.write(f, os.path.basename(f))
        self.file_zip = open(self.zfName, "rb")

    def send_zip(self, files=None):
        """
        add it to email and zip
        :param files:
        :return:
        """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Test results"
        msg['From'] = self.conf_parser.reporting_email
        msg['To'] = self.conf_parser.reporting_email
        msg.attach(MIMEText(self.xmlcontents, 'html'))
        part = MIMEBase('application', 'zip')
        part.set_payload(self.file_zip.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="file.zip"')
        msg.attach(part)

        # now send it
        try:
            server = smtplib.SMTP(self.conf_parser.smtp_server,
                                  self.conf_parser.smtp_port)
            server.set_debuglevel(1)
            server.starttls()
            server.ehlo()
            server.login(self.conf_parser.reporting_email,
                         self.conf_parser.reporting_email_pass)
            logging.info("Logging using %s" % self.conf_parser.reporting_email)
            server.sendmail(self.conf_parser.reporting_email,
                            self.conf_parser.reporting_email,
                            msg.as_string())
            logging.info("Message sent to: %s" %
                         self.conf_parser.reporting_email)
            server.close()
        except Exception as err:
            logging.error("Exception has been raised %s" % err)

        self.file_zip.close()


if __name__ == "__main__":
    zipo = ZipAndSend()
    zipo.zip_me()
    zipo.send_zip()
