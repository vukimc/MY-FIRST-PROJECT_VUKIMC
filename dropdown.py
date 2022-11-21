import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.wedriver.select.import Selection
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
s=Service('E:\\Users\\vukimc\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
# set variables
# URL = 'http://bo.danieli.it:8080/BOE/BI'
URL = 'http://Danbtbi42.danieli.it:8080/BOE/OpenDocument/opendoc/openDocument.jsp?sIDType=CUID&iDocID=ARenDjNuD9tLib8v8jT2jWg'
driver.get(URL)
driver.maximize_window()
time.sleep(2)
login_user = driver.find_element(By.ID,"_id0:logon:USERNAME" )
login_user.send_keys("T80319")
login_pass = driver.find_element(By.ID, "_id0:logon:PASSWORD")
login_pass.send_keys("Cdanieli10")
log_on = driver.find_element(By.ID, "_id0:logon:logonButton").click()
# Switch to webViewFrame
def webViewFrame():
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "openDocChildFrame")))
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "webiViewFrame")))
# dropdown selection
webViewFrame()
driver.switch_to.frame(driver.find_element(By.NAME, "_iframeleftPaneW"))
time.sleep(3)
dd = Select(driver.find_element(By.ID,"PV1List"))
dd.select_by_index(1)

