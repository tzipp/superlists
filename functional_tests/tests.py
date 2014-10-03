from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Rob heard about a new online to-do list app. He wants to see if it might be useful for the IT
        # department at ABI Research.
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # He types "Move new online UPS into the server room" into a text box (Rob is always concerned
        # with ABI's ability to withstand any adverse event affecting power to the business.
        inputbox.send_keys('Move new online UPS into the server room')

        # When he hits enter, the page updates, and now the page lists
        # "1: Move new online UPS into the server room" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Move new online UPS into the server room')


# There is still a text box inviting him to add another item. He
# enters "Setup the UPS, ensuring that minimal shutdowns occur while rearranging the power plugs."
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Setup the UPS')
        inputbox.send_keys(Keys.ENTER)

# The page updates again, and now shows both items on his list.
        self.check_for_row_in_list_table('1: Move new online UPS into the server room')
        self.check_for_row_in_list_table('2: Setup the UPS')

# Rob wonders whether the site will remember his list. Then he sees that the site has generated
# a unique URL for him -- there is some explanatory text to that effect.
        self.fail('Finish the test!')

# He visits that URL - his to-do list is still there.


