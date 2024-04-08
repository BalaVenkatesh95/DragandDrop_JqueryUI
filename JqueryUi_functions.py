import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class JqueryUiClass:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.action_chains = ActionChains(self.driver)

   # browser initiation and url navigation
   def initiation_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : URL is incorrect/Network Error")
           return False


   # Quit browser
   def shutdown(self):
       if self.initiation_function():
           return self.driver.quit()
       else:
           return False

   def fetch_url(self):
       if self.initiation_function():
           return self.driver.current_url
       else:
           return False

  # Drag and Drop Function
   def drap_and_drop(self):
       if self.initiation_function():
           time.sleep(5)
           # Switch to respective iframe to avoid element exception
           iframe_element = self.driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
           self.driver.switch_to.frame(iframe_element)
           source_element = self.driver.find_element(By.XPATH, "//div[@id='draggable']")
           target_element = self.driver.find_element(By.XPATH, "//div[@id='droppable']")
           # Perform the drag-and-drop using action chains
           self.action_chains.drag_and_drop(source_element, target_element).perform()
