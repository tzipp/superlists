from selenium import webdriver

browser = webdriver.Firefox()

# Rob heard about a new online to-do list app. He wants to see if it might be useful for the IT
# department at ABI Research.
browser.get('http://localhost:8000')

# He notices the page title and header mention to-do lists.
assert 'To-Do' in browser.title

# He is invited to enter a to-do item straight away

# He types "Move new online UPS into the server room" into a text box (Rob is always concerned
# with ABI's ability to withstand any adverse event affecting power to the business.

# When he hits enter, the page updates, and now the page lists
# "1: Move new online UPS into the server room" as an item in a to-do list

# There is still a text box inviting him to add another item. He
# enters "Setup the UPS, ensuring that minimal shutdowns occur while rearranging the power plugs."

# The page updates again, and now shows both items on his list.

# Rob wonders whether the site will remember his list. Then he sees that the site has generated
# a unique URL for him -- there is some explanatory text to that effect.

# He visits that URL - his to-do list is still there.



