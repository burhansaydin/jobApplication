from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

path = "C://Development/chromedriver.exe"
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

driver = webdriver.Chrome(path)

site = driver.get(url)
time.sleep(5.0)

sign_in = driver.find_element_by_xpath('/html/body/div[4]/a[1]')
sign_in.click()
time.sleep(5.0)

email = driver.find_element_by_id("username")
pswrd = driver.find_element_by_id("password")
email.send_keys("example@gmail.com")
pswrd.send_keys("example123.")

ent = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[3]/form/div[3]/button')
ent.send_keys(Keys.ENTER)

time.sleep(10.0)

job = driver.find_element_by_xpath('//*[@id="ember248"]/div/div')
job.click()
time.sleep(5.0)

apply = driver.find_element_by_xpath('//*[@id="ember603"]')
apply.click()
time.sleep(5.0)

countries = driver.find_element_by_id("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2358505345,9,phoneNumber~country)")
countries.click()
phone = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2358505345,9,phoneNumber~country)"]/option[230]')

number = driver.find_element_by_id("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2358505345,9,phoneNumber~nationalNumber)")
number.clear()
number.send_keys("6970548924")

last_apply = driver.find_element_by_id("ember1025")