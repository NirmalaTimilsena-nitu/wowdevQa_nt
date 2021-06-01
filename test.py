
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
while True:
    driver = webdriver.Chrome(executable_path='C:\\chromedriver')
    driver.get('https://www.twitter.com')
    driver.maximize_window()
    # driver.getCurrentUrl()
    sleep(5)
    email=driver.find_elements_by_name("session[username_or_email]")
    password=driver.find_elements_by_name("session[password]")

    sleep(10)
    driver.close()

