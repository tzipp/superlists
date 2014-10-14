from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest): 

    def test_cannot_add_empty_list_items(self):
        # Rob goes to the home page and accidentally tires to submit
        # an empty list item. He hits Enter on the empty input box.

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank.

        # He tires again with some text for the item, which now works.

        # Perversely, he now decides to submit a second blank list item.

        # He receives a similar warning on the list page.

        # And he can correct it by filling some text in.
        self.fail('write me!')

