import os
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from api.models import User

from dotenv import load_dotenv
load_dotenv()

# Create your tests here.
class EndToEndTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        os.environ['VITE_SERVER_URL'] = cls.live_server_url
        os.environ['APP_URL'] = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def _register(self, name="user", email="user@email.com", dob="2002-01-01", password="secret"):
        self.selenium.get(f"{self.live_server_url}/register/")
        name_input = self.selenium.find_element(By.NAME, "name")
        name_input.send_keys(name)
        username_input = self.selenium.find_element(By.NAME, "email")
        username_input.send_keys(email)
        dob_input = self.selenium.find_element(By.NAME, "dob")
        dob_input.send_keys(dob)
        password_input = self.selenium.find_element(By.NAME, "pw")
        password_input.send_keys(password)
        confirm_password_input = self.selenium.find_element(By.NAME, "cpw")
        confirm_password_input.send_keys(password)
        self.selenium.find_element(By.ID, 'register').click()

    def _login(self, email="user@email.com", password="secret"):
        self.selenium.get(f"{self.live_server_url}/login/")
        username_input = self.selenium.find_element(By.NAME, "email")
        username_input.send_keys(email)
        password_input = self.selenium.find_element(By.NAME, "pw")
        password_input.send_keys(password)
        self.selenium.find_element(By.ID, 'login').click()


    def test_register(self):
        self._register()
        if not User.objects.filter(email="user@email.com").exists():
            self.fail("User not created")

    def test_login(self):
        self._register()
        self._login()

        if not User.objects.filter(email="user@email.com").exists():
            self.fail("User not created")
        if self.selenium.current_url == f"{self.live_server_url}/login/" or self.selenium.current_url == f"{self.live_server_url}/register/":
            self.fail("Not redirected to home page")

    def test_edit_profile(self):
        self._register()
        self._login()

        time.sleep(20)

        self.selenium.get(f"{self.live_server_url}/profile")
        self.selenium.find_element(By.ID, 'edit').click()

        # Edit name
        self.selenium.find_element(By.ID, 'change_name').click()
        name_input = self.selenium.find_element(By.NAME, "name")
        name_input.clear()
        name_input.send_keys("new_user")

        # Edit email
        self.selenium.find_element(By.ID, 'change_email').click()
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys("newemail@email.com")

        # Save
        self.selenium.find_element(By.ID, 'save').click()

        if not User.objects.filter(email="newemail@email.com").exists():
            self.fail("User not updated")

