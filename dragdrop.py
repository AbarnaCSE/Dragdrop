from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# ActionChain
from selenium.webdriver import ActionChains




class DragAndDrop:


   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.action = ActionChains(self.driver)


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait(5)


   def wait(self, secs):
       sleep(secs)


   def quit(self):
       self.driver.quit()


   def findElementById(self, id):
       return self.driver.find_element(by=By.ID, value=id)


   def dragAndDrop(self):
       try:
           self.boot()
           iframe = self.driver.find_element(By.XPATH, '//iframe') 
           self.driver.switch_to.frame(iframe)
           self.wait(3)
           source = self.findElementById("draggable")
           print("Element found:", source.text)
           destination = self.findElementById("droppable")
           self.action.drag_and_drop(source, destination).perform()
           self.wait(3)


           dropText = self.findElementById("droppable").text
           if dropText == "Dropped!":
               print("Success: We dragged the element and dropped it in its place")
           else:
               print("Error: The action was not performed")


       except NoSuchElementException as e:
           print(e)
       finally:
           self.wait(5)
           self.quit()

url = "https://jqueryui.com/droppable/"
obj = DragAndDrop(url)
obj.dragAndDrop()
