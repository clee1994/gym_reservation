import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import schedule, time
import pause, datetime

#https://selenium-python.readthedocs.io/waits.html

def register_latest(target_time):

    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/Users/clemens/Library/Application Support/Google/Chrome/selenium")

    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://recregister.nd.edu/")

    browser.implicitly_wait(5)
    element = browser.find_element_by_id('loginLink')
    #assert(element.is_displayed() == True)
    element.click()


    #browser.implicitly_wait(5) # seconds
    success = None
    while success is None:
        try:
            #browser.implicitly_wait(3)
            login2 = browser.find_element_by_xpath("/html/body/div[5]/div[5]/div/div/div/div[2]/div[2]/div[2]/div/button")
            login2.click()
            success = True
        except:
            pass


    #browser.implicitly_wait(10) # seconds
    success = None
    while success is None:
        try:
            browser.implicitly_wait(10)
            browser.find_element_by_id("okta-signin-username").send_keys("")
            browser.find_element_by_id ("okta-signin-password").send_keys("")
            login2 = browser.find_element_by_xpath("//*[@id=\"okta-signin-submit\"]")
            login2.click()
            success = True
        except:
            pass


    success = None
    while success is None:
        try:
            browser.implicitly_wait(3)
            far1 = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/a/span[1]/img")
            far1.click()
            success = True
        except:
            pass

    # wait till 5pm sharp 
    pause.until(datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, target_time[0], target_time[1],target_time[2] ))

    #t_now = time.localtime() datetime.timedelta(hours=17, minutes=00, seconds=00)
    #time.sleep()

    success = None
    while success is None:
        try:
            far2 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[4]/div/div[1]/img")
            far2.click()
            success = True
        except:
            pass

    success = None
    while success is None:
        try:
            browser.implicitly_wait(3)
            reg = browser.find_elements_by_class_name("btn-primary")
            for i, element in enumerate(reg):
                if element.get_attribute('innerHTML') == "Register":
                    continue
                else:
                    break
            reg[i-1].click()
            success = True
        except:
            pass


    success = None
    while success is None:
        try:
            browser.implicitly_wait(3)
            far3 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/a")
            far3.click()
            success = True
        except:
            pass

    success = None
    while success is None:
        try:
            browser.implicitly_wait(3)
            far4 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/form[2]/div[2]/button[2]")
            far4.click()
            success = True
        except:
            pass

    success = None
    while success is None:
        try:
            browser.implicitly_wait(3)
            far5 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[3]/div/form/button")
            far5.click()
            success = True
        except:
            pass

    success = None
    while success is None:
        try:
            browser.implicitly_wait(3)
            far5 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[2]/button")
            far5.click()
            success = True
        except:
            pass


    browser.close()

register_latest((13,24,45))

schedule.every().day.at("16:56:00").do(register_latest,(17,0,0))

while 1:
    schedule.run_pending()
    time.sleep(1)
