import time
from random import random

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from sqlalchemy import func
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget

f = open("stars.txt", "r")

girls = f.readlines()

f.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")

cookies = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='aOOlW  bIiDR  ']"))).click()

username = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys("feef_he")
password.send_keys("ELoTRiXHDx1")
time.sleep(2)
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Jetzt nicht')]"))).click()

not_now2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Jetzt nicht')]"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Suchen']")))

g = open("srces.txt", "w")
i=0
for girl in girls:
    time.sleep(1)
    i += 1
    try:
        searchbox.clear()
        searchbox.send_keys(girl)
        time.sleep(2)
        try:
            # pic_addr_wait = WebDriverWait(driver, 21).until(
            #    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[1]/div/span')))

            pic_addr_span = driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[1]/div/span')

            g.write(girl + pic_addr_span.find_element(By.TAG_NAME, "img").get_attribute("src") + "\n")

            print("progress: " + str((i / len(girls)) * 100) + "%")
        except NoSuchElementException:
            print("FAILURE")
    except StaleElementReferenceException:
        print("searchbox error")


time.sleep(5)
#searchbox.send_keys(Keys.ENTER)
#print("enter1")
#searchbox.send_keys(Keys.ENTER)
#print("enter2")
#time.sleep(5)














def getabos():
    get_abos = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))).click()

    time.sleep(2)
    print("trying to access list")

    driver.execute_script("window.scrollTo(0,250)")

    followers = driver.find_element(By.CLASS_NAME, "isgrP")
    try:
        print(followers.find_element(By.CLASS_NAME, "jSC57  _6xe7A"))
    except NoSuchElementException:
        print("no jsc57")

    try:
        print(followers.find_element(By.CLASS_NAME, "PZuss"))
    except NoSuchElementException:
        print("no Pzuss")

    try:
        print(followers.find_elements(By.TAG_NAME, "li"))
    except NoSuchElementException:
        print("no li")

    try:
        followers_li = followers.find_elements(By.TAG_NAME, "li")
        for li in followers_li:
            print(li.find_element(By.TAG_NAME, "a").get_attribute("href"))
    except NoSuchElementException:
        print("no li")

    print(followers)

    # followers = driver.find_elements(By.CLASS_NAME, "RnEpo  Yx5HN      ")

    # print(followers)

    # followers = [follower.get_attribute("href") for follower in followers]

    # print(followers)

    # for i in range(0, 10):

    # followers_it = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[1]/div[
    # 2]/div[1]/span/a/span")

    # print(followers_it)
    # xpath = "//div[@css='position: relative; z-index: 1;']/div/div[2]/div/div[1]"

    # popup = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # dialog = driver.find_element("/html/body/div[2]/div/div[2]/div/div[2]")

    # for i in range(0, 100):
    #    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
    #    time.sleep(random.randint(500,1000)/1000)
    #    print("Extract friends %", round((i/(100/2)*100),2) ,"from","%100")

    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",popup)

    # driver.execute_script("window.scrollTo(0,100)")

    # persons = driver.find_element()
    time.sleep(20)
    print("kein bock mehr")
