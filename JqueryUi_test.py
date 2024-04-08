"""
 Test case file with all required test cases to execute
"""
import time

from JqueryUi_functions import JqueryUiClass
import pytest



url = "https://jqueryui.com/droppable/"
#Creating Instance of Class to utilise its methods / functions
jquery_ui = JqueryUiClass(url)

# Test case to navigate to URL
def test_navigate_url():
   testing_url = "https://jqueryui.com/droppable/"
   assert jquery_ui.fetch_url() == testing_url
print("Landed on login page")

# Test to perform drag and drop
def test_drag_and_drop():
   jquery_ui.drap_and_drop()


#Test Case to quit / shutdown browser
def test_shutdown():
   jquery_ui.shutdown()
