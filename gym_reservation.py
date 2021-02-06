from selenium import webdriver
from selenium.webdriver.common.by import By

import schedule, time

def register_latest():

    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/Users/clemens/Library/Application Support/Google/Chrome/selenium")

    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://recregister.nd.edu/")
    element = browser.find_element_by_id('loginLink')
    assert(element.is_displayed() == True)
    element.click()

    browser.implicitly_wait(10) # seconds
    login2 = browser.find_element_by_xpath("/html/body/div[5]/div[5]/div/div/div/div[2]/div[2]/div[2]/div/button")
    login2.click()


    browser.implicitly_wait(10) # seconds
    browser.find_element_by_id("okta-signin-username").send_keys("")
    browser.find_element_by_id ("okta-signin-password").send_keys("")


    login2 = browser.find_element_by_xpath("//*[@id=\"okta-signin-submit\"]")
    login2.click()

    far1 = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/a/span[1]/img")
    far1.click()

    far2 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[4]/div/div[1]/img")
    far2.click()

    reg = browser.find_elements_by_class_name("btn-primary")
    for i, element in enumerate(reg):
        if element.get_attribute('innerHTML') == "Register":
            continue
        else:
            break
    reg[i-1].click()


    far3 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/a")
    far3.click()

    far4 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/form[2]/div[2]/button[2]")
    far4.click()


    far5 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[3]/div/form/button")
    far5.click()


    far5 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[2]/button")
    far5.click()
    browser.close()

schedule.every().day.at("15:59:58").do(register_latest)

while 1:
    schedule.run_pending()
    time.sleep(1)
