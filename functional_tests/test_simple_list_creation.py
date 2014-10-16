from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Rob heard about a new online to-do list app. 
        # He wants to see if it might be useful for the IT
        # department at ABI Research.

        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        # He notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # He types "Move new online UPS into the server room" into a text box 
        # Rob is always concerned
        # with ABI's ability to withstand any adverse event affecting power to the business.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Move new online UPS into the server room')
        inputbox.send_keys(Keys.ENTER)

        rob_list_url = self.browser.current_url
        self.assertRegex(rob_list_url, '/lists/.+')
        self.check_for_row_in_list_table("1: Move new online UPS into the server room")


        # When he hits enter, the page updates, and now the page lists
        # "1: Move new online UPS into the server room" as an item in a to-do list
        # There is still a text box inviting him to add another item. He    
        # enters "Setup the UPS, ensuring that minimal shutdowns 
        # occur while rearranging the power plugs."
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Setup the UPS')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list.
        self.check_for_row_in_list_table('1: Move new online UPS into the server room')
        self.check_for_row_in_list_table('2: Setup the UPS')

        # Now a new user, Peter, comes along to the site.

        ## We use a new browser session to make sure that no information of
        ## Rob's is coming through the cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Peter visits the home page. There is no sign of Rob's list.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Move new online UPS', page_text)
        self.assertNotIn('Setup the UPS', page_text)


        # Peter starts a new list by entering a new item. He is less interesting
        # than Rob...
        inputbox = self.get_item_by_input_box()
        inputbox.send_keys('Write code')
        inputbox.send_keys(Keys.ENTER)

        # Peter gets his own unique URL
        peter_list_url = self.browser.current_url
        self.assertRegex(peter_list_url, '/lists/.+')
        self.assertNotEqual(peter_list_url, rob_list_url)

        # Again, there is no trace of Rob's list.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Move new online UPS', page_text)
        self.assertNotIn('Setup the UPS', page_text)

        # Satisfied, they both go back to sleep
        #        self.fail('Finish the test!')

        # He visits that URL - his to-do list is still there.	
    

