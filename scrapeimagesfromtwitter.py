import os
import wget
import time
from random import random

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.chrome.service import Service
from sqlalchemy import func
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

dirList = os.listdir("website/static/imgdir")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.twitter.com/")

twitter_count = 0

insta_links = []
twitter_links = []
onlyfans_links = []
pornhub_links = []
errors = 0

for i in range(0, len(dirList)):
    f = open("website/static/imgdir/" + dirList[i] + "/social.txt", "r")
    links = f.readlines()
    f.close()
    for link in links:

        if link.find("twitter") != -1:
            twitter_count += 1
            try:
                driver.get(link.rstrip("\n") + "/photo")

                time.sleep(3)

                try:
                    twitter_div_container = driver.find_element(By.XPATH,
                                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/img')

                except:
                    print("error finding profile pic")
                    try:
                        twitter_div_container = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div[1]/div/div/div/div/div/img')
                    except:
                        print("error findin profil pic (2)")

                twitter_link = twitter_div_container.get_attribute("src")


                wget.download(twitter_link, "website/static/imgdir/" + dirList[i])


            except:
                print("some error with twitter link 1 occured")
                errors += 1

    print("progress: " + str((i / len(dirList)) * 100) + "%")
    print("errors/all  " + str(errors) + "/" + str(twitter_count))
