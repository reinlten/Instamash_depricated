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
import wget
import os
import wget

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://de.pornhub.com/")
im18 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                   '//*[@id="modalWrapMTubes"]/div/div/button[contains(text(), "Ich bin 18 oder älter - Eingabe")]'))).click()

f = open("phlinks.txt", "r")
urls = f.readlines()
f.close()

for url in urls:

    driver.get(url)

    time.sleep(3)
    try:
        nameClass = driver.find_element(By.CLASS_NAME, "name")
        name = nameClass.find_element(By.TAG_NAME, "h1").text
        try:
            socialClass = driver.find_element(By.XPATH,
                                              '/html/body/div[4]/div[2]/div[5]/div/section/div[3]/div[1]/div[2]/section/ul')
        except NoSuchElementException:
            try:
                socialClass = driver.find_element(By.XPATH,
                                                  '/html/body/div[5]/div[2]/div[5]/div/section/div[3]/div[1]/div[2]/section/ul')
            except NoSuchElementException:
                try:
                    socialClass = driver.find_element(By.XPATH,
                                                      '/html/body/div[6]/div[2]/div[5]/div/section/div[3]/div[1]/div[2]/section/ul')
                except NoSuchElementException:
                    try:
                        socialClass = driver.find_element(By.XPATH,
                                                          '/html/body/div[7]/div[2]/div[5]/div/section/div[3]/div[1]/div[2]/section/ul')
                    except NoSuchElementException:
                        try:
                            socialClass = driver.find_element(By.XPATH,
                                                              '/html/body/div[8]/div[2]/div[5]/div/section/div[3]/div[1]/div[2]/section/ul')
                        except NoSuchElementException:
                            print("Following sociallinks could not be found: " + name)

        socialLinksContainer = socialClass.find_elements(By.TAG_NAME, "a")

        socialLinks = []

        for link in socialLinksContainer:
            socialLinks.append(link.get_attribute("href"))

        print(socialLinks)
        phPicLink = driver.find_element(By.ID, "getAvatar").get_attribute("src")

        os.mkdir("website/static/imgdir/" + name)

        f = open("website/static/imgdir/" + name + "/social.txt", "w")

        f.write(url)

        for link in socialLinks:
            f.write(link + "\n")

        f.close()

        wget.download(phPicLink, "website/static/imgdir/" + name + "/" + name.rstrip("\n") + ".jpg")

    except:
        print("some other error occured with url: " + url)
