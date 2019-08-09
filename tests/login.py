from selenium import webdriver

driver = webdriver.Chrome(executable_path='../chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com")
