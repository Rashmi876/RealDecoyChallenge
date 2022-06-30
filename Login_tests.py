from selenium import webdriver
from selenium.webdriver.common.by import By


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

    # 4. assert we got a search page for puppies
    assert 'Swag Labs' in driver.title

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

    # 2. submit or enter the login
    return driver.find_element(By.NAME, 'login-button').submit()

def locked_out_user():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Windows\chromedriver.exe')

    # 1. go to Swaglabs
    driver.get('https://www.saucedemo.com/')

    # 2. type in a username and password
    driver.find_element(By.NAME, 'user-name').send_keys('locked_out_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')

    # 3. submit or enter the login
    return driver.find_element(By.NAME, 'login-button').submit()


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
    return driver.find_element(By.NAME, 'login-button').submit()


standard_user()

problem_user()

locked_out_user()

performance_glitch_user()
