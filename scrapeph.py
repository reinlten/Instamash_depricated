import time
from random import random

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from sqlalchemy import func
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://de.pornhub.com/pornstars/top?si=1")

im18 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalWrapMTubes"]/div/div/button[contains(text(), "Ich bin 18 oder älter - Eingabe")]'))).click()

stars_div_list = driver.find_elements(By.ID, "indexListContainer")

stars_list = []

f = open("stars.txt", "w")


for div in stars_div_list:
    #print(div.find_element(By.TAG_NAME, "a").text)
    #stars_list.append(div.find_element(By.TAG_NAME, "a").text)
    f.write(div.find_element(By.TAG_NAME, "a").text + "\n")

f.close()



