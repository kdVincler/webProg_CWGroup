import os
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By

# I have set selenium up with chrome and waits as it was causing threaded errors described here:
# https://docs.djangoproject.com/en/5.1/topics/testing/tools/#liveservertestcase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

from api.models import User
from dotenv import load_dotenv

load_dotenv()

class EndToEndTests(LiveServerTestCase):
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

    def wait_for_body(self, timeout=10):
        WebDriverWait(self.selenium, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def _register(self, name="user", email="user@email.com", dob="2002-01-01", password="secret"):
        self.selenium.get(f"{self.live_server_url}/register/")
        self.wait_for_body()

        self.selenium.find_element(By.NAME, "name").send_keys(name)
        self.selenium.find_element(By.NAME, "email").send_keys(email)
        self.selenium.find_element(By.NAME, "dob").send_keys(dob)
        self.selenium.find_element(By.NAME, "pw").send_keys(password)
        self.selenium.find_element(By.NAME, "cpw").send_keys(password)
        self.selenium.find_element(By.ID, 'register').click()
        self.wait_for_body()

    def _login(self, email="user@email.com", password="secret"):
        self.selenium.get(f"{self.live_server_url}/login/")
        self.wait_for_body()

        self.selenium.find_element(By.NAME, "email").send_keys(email)
        self.selenium.find_element(By.NAME, "pw").send_keys(password)
        self.selenium.find_element(By.ID, 'login').click()
        self.wait_for_body()

    def test_register(self):
        self._register()
        self.assertTrue(User.objects.filter(email="user@email.com").exists(), "User not created")

    def test_login(self):
        self._register()
        self._login()

        self.assertTrue(User.objects.filter(email="user@email.com").exists(), "User not created")
        self.assertNotEqual(
            self.selenium.current_url,
            f"{self.live_server_url}/login/",
            "Not redirected to home page"
        )

    def test_edit_profile(self):
        self._register()
        self._login()
        self.wait_for_body()

        # Go to profile page
        dropdown = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable((By.ID, 'dropdown'))
        )
        dropdown.click()

        profile_link = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable((By.ID, 'profile'))
        )
        profile_link.find_element(By.XPATH, ".//a").click()

        # Edit profile details
        self.selenium.find_element(By.ID, 'edit').click()
        self.selenium.find_element(By.ID, 'change_name').click()
        name_input = self.selenium.find_element(By.NAME, "name")
        name_input.clear()
        name_input.send_keys("new_user")

        self.selenium.find_element(By.ID, 'change_email').click()
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys("newemail@email.com")

        # Save changes
        self.selenium.find_element(By.ID, 'save').click()
        self.assertTrue(User.objects.filter(email="newemail@email.com").exists(), "User not updated")
