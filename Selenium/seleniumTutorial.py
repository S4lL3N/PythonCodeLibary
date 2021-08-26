#import selenium

from selenium import webdriver

username = ''
password = ''

url = "www.google.com"

driver = webdriver.Chrome("C:\\Users\\S4lL3\\Documents\\My_VS_Code\\Python\\SeleniumChromeDriver\\chromedriver_win32\\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("userId").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath('//*[@id="bodycontent"]/olblogin-app/div/section/form[1]/fieldset/div[4]/button').click()


"""

Instructions for chrome driver:
https://chromedriver.chromium.org/downloads/version-selection


79.0.3945.88 my version of chrome
79.0.3945.36 latest selenium chromedriver

https://chromedriver.storage.googleapis.com/LATEST_RELEASE_79.0.3945.88

https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/  used this one to download
"""