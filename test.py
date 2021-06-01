
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
while True:
    driver = webdriver.Chrome(executable_path='C:\\chromedriver')
    driver.get('https://www.youtube.com')
    driver.maximize_window()
    
    sleep(3)
    driver.close()
