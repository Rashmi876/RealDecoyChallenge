from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def standard_user_addtocart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Windows\chromedriver.exe')

    # 1. go to Swaglabs
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    # 2. type in a username and password
    driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')

    # 3. submit or enter the login
    driver.find_element(By.NAME, 'login-button').submit()

    # 4. assert we got a search page for puppies
    # assert 'Swag Labs' in driver.title

    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-fleece-jacket').click()

def problem_user_addtocart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Windows\chromedriver.exe')

    # 1. go to Swaglabs
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    # 2. type in a username and password
    driver.find_element(By.NAME, 'user-name').send_keys('problem_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')

    # 3. submit or enter the login
    driver.find_element(By.NAME, 'login-button').submit()

    # 4. assert we got a search page for puppies
    # assert 'Swag Labs' in driver.title

    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light').click()


def performance_glitch_user_addtocart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Windows\chromedriver.exe')

    # 1. go to Swaglabs
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    # 2. type in a username and password
    driver.find_element(By.NAME, 'user-name').send_keys('performance_glitch_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')

    # 3. submit or enter the login
    driver.find_element(By.NAME, 'login-button').submit()

    # 4. assert we got a search page for puppies
    # assert 'Swag Labs' in driver.title

    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-test.allthethings()-t-shirt-(red)').click()
    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

standard_user_addtocart()

problem_user_addtocart()

performance_glitch_user_addtocart()
