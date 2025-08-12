from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logindata

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(r"C:\Users\Anusha\OneDrive\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Start WebDriver
driver = webdriver.Chrome(service=service, options=options)

action = ActionChains(driver)
time.sleep(1)


driver.get('http://www.amazon.in')
time.sleep(3)
 
firstLevelMenu = driver.find_element(By.XPATH, "//div[@class='nav-line-1-container']")
element = driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
print(element.text)

firstLevelMenu.click()
time.sleep(3)
 

signinelement = driver.find_element(By.XPATH,'//*[@id="ap_email_login"]')
signinelement.send_keys(logindata.USERNAME)
time.sleep(3)

cont = driver.find_element(By.XPATH,'//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element(By.XPATH,'//*[@id="ap_password"]')
passwordelement.send_keys(logindata.PASSWORD)
time.sleep(3)

login = driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
login.click()
time.sleep(3)

