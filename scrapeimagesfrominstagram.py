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

for i in range(len(dirList)):
    print(str(i)+dirList[i])

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


insta_links_count = 0

insta_links = []
twitter_links = []
onlyfans_links = []
pornhub_links = []
errors = 0

for i in range(676, len(dirList)):
    f = open("website/static/imgdir/"+ dirList[i] +"/social.txt","r")
    links = f.readlines()
    f.close()
    for link in links:
        if link.find("instagram") != -1:
            try:
                driver.get(link.rstrip("\n"))

                time.sleep(5)

                try:
                    insta_div_container = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div')

                except:
                    print("xpath error (1)")
                    try:
                        insta_div_container = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div')
                    except:
                        print("xpath error (2)")
                        try:
                            insta_div_container = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[4]/article/div[1]/div')
                        except:
                            print("xpath error (3)")
                #    try:
                insta_img_container = insta_div_container.find_elements(By.TAG_NAME, "a")
                #        try:
                img_links_container = []

                for img in insta_img_container:
                    img_links_container.append(img.find_element(By.TAG_NAME, "img").get_attribute("srcset"))

                for link in img_links_container:
                    link_split_container = link.split(" ")
                    link_split = [link_split_container[0]]
                    print(link_split)
                    for k in range(len(link_split_container)-2):
                        print(link_split_container[k+1])
                        link_split.append(link_split_container[k+1].split(",")[1])

                    for j in range(len(link_split)):
                        print(link_split[j])
                        wget.download(link_split[j], "website/static/imgdir/"+dirList[i])

                print(img_links_container)

            except:
                print("some error with a insta link occured")
                errors += 1



            insta_links.append(link)
            insta_links_count += 1



        if link.find("twitter") != -1:
            twitter_links.append(link)
        if link.find("onlyfans") != -1:
            twitter_links.append(link)

    print("progress: " + str((i/len(dirList))*100) +"%")
    print("errors/all  " + str(errors) +"/"+str(insta_links_count))

#print(insta_links)










#f = open("srces.txt", "r")
#images = f.readlines()
#f.close()

#path = os.getcwd()
#path = os.path.join(path, "website\static\img")

#print(path)
#print(images[0])

#for i in range(round(len(images)/2)):
#    wget.download(images[2*i+1], os.path.join(path, images[2*i].rstrip("\n") + ".jpg"))


