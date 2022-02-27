 #!/usr/bin/python
 ###
from turtle import down, left
import pytesseract 
from PIL import Image, ImageFilter
from selenium.webdriver import ActionChains  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By ### this is acyion for keyh board
from curses.textpad import Textbox
from gettext import find
from re import search
import click
from selenium import webdriver
from getpass import getpass
import time




driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome-stable"


driver = webdriver.Chrome()
driver.get("https://tms48.nepsetms.com.np/tms/client/dashboard")

#for login tms and credential
username_textbox =driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[2]/form/div[1]/input")
username_textbox.send_keys("2021022862")

password_textbox = driver.find_element_by_id('password-field')
password_textbox.send_keys("Sundar123%")

##captcha
#def get_captcha(driver, element, path):
   # location = element.location
   # size = element.size
    #driver.save_screenshot("./img/captcha2.png")
   # image = Image.open("./img/captcha.png")
   # right = location['x']
    #top = location['y'] + 140
    #right = location['x'] + size['width']
   # bottom = location['y'] + size['height'] + 140
    #image = image.crop((left, top,down, right, bottom))  # defines crop points
    #image.save(path, 'png')  # saves new cropped image

    #captcha = pytesseract.image_to_string(image) 
    #captcha = captcha.replace(" ", "").strip()
    #print(captcha)
##img = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[2]/form/div[3]/div[2]/div/img")
#get_captcha(driver, img, "captcha.png")

#driver.find_element(By.XPATH,"/html/body/app-root/app-login/div/div/div[2]/form/div[3]/div[1]/div/input").send_keys(get_captcha)

#search credincal/////
time.sleep(10)
login_button = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/form/div[4]/input').click()
time.sleep(5)

driver.find_element_by_name("filtername").send_keys("Buy/Sell undefined")
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/tms/app-menubar/aside/nav/div/form/button/i").click()

#buing element ////
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input").send_keys("ADBL")
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/typeahead-container/button[1]").click()
time.sleep(3)
achains =  ActionChains(driver)
elem1 = driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b")
achains.double_click(elem1).perform()
text = driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b").text
print(text)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input").send_keys(text)
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[3]/input").send_keys(10)
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[1]/div[2]/app-three-state-toggle/div/div/label[3]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[2]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/div/div[2]/client-order-book/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/div/span[1]/i").click()
time.sleep(2)
driver.refresh()
time.sleep(3)
achains =  ActionChains(driver)
elem2 = driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b")
achains.double_click(elem2).perform()
text1 = driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b").text
print(text1)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input").clear()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[3]/input").clear()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input").send_keys(text1)
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[2]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/div/div[2]/client-order-book/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[2]/div/span[1]/i').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/div/div[2]/client-order-book/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[2]/div/span[1]/i').click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input").clear()
time.sleep(2)
sanjay =driver.find_element(By.XPATH,'/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b').text
print(sanjay)
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[3]/input").send_keys(20)
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b').send_keys(sanjay)
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[2]/button[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/app-root/tms/main/ap-navigation/header/div/div[2]/div[3]/a/i[2]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/app-root/tms/main/ap-navigation/header/div/div[2]/div[3]/div/a[5]/span').click()








                                        