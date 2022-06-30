from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def standard_user():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Windows\chromedriver.exe')

    # 1. go to Swaglabs
    driver.get('https://www.saucedemo.com/')

    # 2. type in a username and password
    driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')

    # 3. submit or enter the login
    driver.find_element(By.NAME, 'login-button').submit()

    time.sleep(3)

    #4. Click on the footer links
    driver.find_element(By.CSS_SELECTOR, "[href='https://twitter.com/saucelabs']").click()
    driver.find_element(By.CSS_SELECTOR, "[href='https://www.facebook.com/saucelabs']").click()
    driver.find_element(By.CSS_SELECTOR, "[href='https://www.linkedin.com/company/sauce-labs/']").click()

    # driver.close()


def problem_user():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Windows\chromedriver.exe')

    # 1. go to Swaglabs
    driver.get('https://www.saucedemo.com/')

    # 2. type in a username and password
    driver.find_element(By.NAME, 'user-name').send_keys('problem_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')

    # 3. submit or enter the login
    driver.find_element(By.NAME, 'login-button').submit()

    time.sleep(3)

    #4. Click on the footer links
    driver.find_element(By.CSS_SELECTOR, "[href='https://twitter.com/saucelabs']").click()
    driver.find_element(By.CSS_SELECTOR, "[href='https://www.facebook.com/saucelabs']").click()
    driver.find_element(By.CSS_SELECTOR, "[href='https://www.linkedin.com/company/sauce-labs/']").click()


def performance_glitch_user():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Windows\chromedriver.exe')

    # 1. go to Swaglabs
    driver.get('https://www.saucedemo.com/')

    # 2. type in a username and password
    driver.find_element(By.NAME, 'user-name').send_keys('performance_glitch_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')

    # 3. submit or enter the login
    driver.find_element(By.NAME, 'login-button').submit()

    time.sleep(3)

    # 4. Click on the footer links
    driver.find_element(By.CSS_SELECTOR, "[href='https://twitter.com/saucelabs']").click()
    driver.find_element(By.CSS_SELECTOR, "[href='https://www.facebook.com/saucelabs']").click()
    driver.find_element(By.CSS_SELECTOR, "[href='https://www.linkedin.com/company/sauce-labs/']").click()


standard_user()

problem_user()

performance_glitch_user()
