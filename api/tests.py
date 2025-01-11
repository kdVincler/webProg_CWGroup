import time

from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from api.models import User


# Create your tests here.
class EndToEndTests(LiveServerTestCase):
    url = "http://localhost:5173/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

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


    def test_register(self):
        self._register()
        if not User.objects.filter(email="user@email.com").exists():
            self.fail("User not created")

    def test_login(self):
        self._register()
        self.selenium.get(f"{self.live_server_url}/login/")
        username_input = self.selenium.find_element(By.NAME, "email")
        username_input.send_keys("user@email.com")
        password_input = self.selenium.find_element(By.NAME, "pw")
        password_input.send_keys("secret")
        self.selenium.find_element(By.ID, 'login').click()

        if not User.objects.filter(email="user@email.com").exists():
            self.fail("User not created")
        if self.selenium.current_url == f"{self.live_server_url}/login/" or self.selenium.current_url == f"{self.live_server_url}/register/":
            self.fail("Not redirected to home page")

