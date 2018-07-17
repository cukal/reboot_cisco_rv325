from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import unittest, time, re

options = Options()
options.add_argument("--headless")

class DoNotRebootCisco(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_options=options)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_do_not_reboot_cisco(self):
        driver = self.driver
        driver.get("https://<console ip:port>")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("<cisco admin username>")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("<cisco admin password>")
        driver.find_element_by_id("Login").click()
        time.sleep(15)
        frame = driver.find_element_by_id("menuPage")
        driver.switch_to.frame(frame)
        driver.find_element_by_id("menuNodeDiv_4").click()
        time.sleep(15)
        driver.find_element_by_link_text("Restart").click()
        time.sleep(15)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//div").click()
        frame = driver.find_element_by_id("contentFrame")
        driver.switch_to.frame(frame)
        driver.find_element_by_id("restart2").click()
        time.sleep(5)
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//*[@id='AlertDiv']/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/input[1]").click()
        time.sleep(10)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

}}}
