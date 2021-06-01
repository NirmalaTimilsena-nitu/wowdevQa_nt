from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path='C:\\chromedriver')
driver.get('http://www.google.com')