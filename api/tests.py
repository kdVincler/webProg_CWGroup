import os
import time

from django.test import LiveServerTestCase
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# I have set selenium up with chrome and waits as it was causing threaded errors described here:
# https://docs.djangoproject.com/en/5.1/topics/testing/tools/#liveservertestcase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

from api.models import User, Friend
from dotenv import load_dotenv

load_dotenv()


class EndToEndTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.selenium.set_window_size(1920, 1080)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def wait_for_body(self, timeout=10):
        # Server keeps clashing with the backend, so I added a sleep to give it time to load :(
        time.sleep(0.2)
        WebDriverWait(self.selenium, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def _register(self, name="user", email="user@email.com", dob="01-01-2002", password="secret"):
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
        self.wait_for_body()
        self._register()
        self.assertTrue(User.objects.filter(email="user@email.com").exists(), "User not created")

    def test_login(self):
        self.wait_for_body()
        self._register()
        self._login()
        self.wait_for_body()

        self.assertTrue(User.objects.filter(email="user@email.com").exists(), "User not created")
        self.assertNotEqual(
            self.selenium.current_url,
            f"{self.live_server_url}/login/",
            "Not redirected to home page"
        )

    def test_edit_profile(self):
        self.wait_for_body()
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
        self.selenium.find_element(By.ID, 'edit').click()

        # Edit profile details
        self.selenium.find_element(By.ID, 'change_name').click()
        name_input = self.selenium.find_element(By.NAME, "name")
        name_input.clear()
        name_input.send_keys("new_user")

        self.selenium.find_element(By.ID, 'change_email').click()
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys("newemail@email.com")

        self.selenium.find_element(By.ID, 'change_dob').click()
        dob_input = self.selenium.find_element(By.NAME, "dob")
        dob_input.clear()
        dob_input.send_keys("02-02-2000")

        # Save changes
        self.selenium.find_element(By.ID, 'save').click()
        time.sleep(1)

        self.assertTrue(
            User.objects.filter(email="newemail@email.com").exists(),
            "User details not updated"
        )

        self.selenium.find_element(By.ID, 'edit').click()
        self.selenium.find_element(By.ID, 'edit_password').click()

        # Change password
        old_pw = self.selenium.find_element(By.NAME, "old_pw")
        old_pw.send_keys("secret")

        new_pw = self.selenium.find_element(By.NAME, "pw")
        new_pw.send_keys("new_secret")

        confirm_pw = self.selenium.find_element(By.ID, "change_confirm_new_password")
        confirm_pw.send_keys("new_secret")

        self.selenium.find_element(By.ID, 'save').click()
        self.wait_for_body(10)
        time.sleep(2)

        self._login(email="newemail@email.com", password="new_secret")
        self.wait_for_body(10)
        time.sleep(1)

        self.assertNotEqual(
            self.selenium.current_url,
            f"{self.live_server_url}/login/",
            "Not redirected to home page. Password not updated"
        )

    def _send_friend_request(self):
        self.wait_for_body()
        self._register()
        self._register("user2", "user2@email.com")
        self._login()
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'button1').click()
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'sidebar-logout').click()
        self.wait_for_body()
        time.sleep(1)

    def test_send_friend_request(self):
        self._send_friend_request()

        # Check friend request exists
        self.assertTrue(Friend.objects.filter(user1=User.objects.get(email="user@email.com"),
                                              user2=User.objects.get(email="user2@email.com")).exists(),
                        "Friend request not sent")

    def test_accept_friend_request(self):
        self._send_friend_request()

        time.sleep(1)
        self.wait_for_body()
        self._login(email="user2@email.com")
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'button1').click()
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'sidebar-logout').click()
        self.wait_for_body()

        # Check friend request accepted
        self.assertTrue(Friend.objects.filter(user1=User.objects.get(email="user@email.com"),
                                              user2=User.objects.get(email="user2@email.com"),
                                              accepted=True).exists(),
                        "Friend request not accepted")

    def test_filter_by_age(self):
        self._register()
        self._register("twentyfive", "twentyfive@email.com", "01-01-2000")
        self._register("fifteen", "fifteen@email.com", "01-01-2010")
        self._register("thirty", "thirty@email.com", "01-01-1995")
        self.wait_for_body()
        self._login()
        self.wait_for_body()

        # Check to see all 3 other users are displayed
        self.assertTrue(
            (
                    self.selenium.find_element(By.ID, 'podium_first').is_displayed() and \
                    self.selenium.find_element(By.ID, 'podium_second').is_displayed() and \
                    self.selenium.find_element(By.ID, 'podium_third').is_displayed()
            ),
            "Not all users are displayed"
        )

        self.wait_for_body()
        self.selenium.find_element(By.ID, 'filter_button').click()
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'filter_checkbox').click()
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'filter_from').click()
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'filter_from').send_keys("20")

        self.selenium.find_element(By.ID, 'filter_to').click()
        self.wait_for_body()
        self.selenium.find_element(By.ID, 'filter_to').send_keys("30")

        self.wait_for_body()
        self.selenium.find_element(By.ID, 'filter_apply').click()

        def is_element_displayed(element_id):
            # Speed up the search for elements so this doesnt take a minute
            self.selenium.implicitly_wait(1)
            try:
                element = self.selenium.find_element(By.ID, element_id)
                self.selenium.implicitly_wait(10)
                return element.is_displayed()
            except NoSuchElementException:
                self.selenium.implicitly_wait(10)
                return False

        # Check to see filters were applied proprerly
        self.assertTrue(
            (
                    is_element_displayed('user_display_1') and
                    is_element_displayed('user_display_2') and
                    not is_element_displayed('user_display_3') and
                    not is_element_displayed('podium_first') and
                    not is_element_displayed('podium_second') and
                    not is_element_displayed('podium_third')
            ),
            "Filters not applied, users that shouldn't be displayed are displayed."
        )
