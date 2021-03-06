from selenium.webdriver.support.ui import WebDriverWait
import time
from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def test_login_with_persona(self):
        # Rob goes to the awesome superlists site
        # and notices a 'Sign in' link for the first time.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click() # id_ for HTML IDs

        # A Persona login box appears
        self.switch_to_new_window('Mozilla Persona')

        # Rob logs in with his email address
        ## use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys('rob@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # The Persona window closes
        self.switch_to_new_window('To-Do')

        # Rob can see that he is logged in
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('rob@mockmyid.com', navbar.text)


