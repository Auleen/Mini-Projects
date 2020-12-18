import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import sys
import time

driver=webdriver.Chrome("C:\\Program Files (x86)\\chromedriver\\chromedriver.exe")

url=pyperclip.paste()

print("Source link : "+url)

list1=url.split("=")

print(list1)

watchlink=list1[1]

print(watchlink)

list2=["https://ytmp3.com/download/",watchlink]

target_url="".join(list2)

print(target_url)

req=requests.get(target_url)
print(str(req.headers))

print(target_url)

driver.get(target_url)
wait=WebDriverWait(driver,10)

try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"done")))
    driver.find_element_by_class_name("done").click()
except:
    print("Task Failed.Try Again Later")



sys.exit(0)
