from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = "C://Development/chromedriver.exe"
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

driver = webdriver.Chrome(path)

s = driver.get(url)
time.sleep(5.0)


#aa = sa.find_element_by_css_selector("button")
si = driver.find_element_by_xpath('/html/body/div[4]/a[1]')
si.click()
time.sleep(5.0)

ep = driver.find_element_by_id("username")
ps = driver.find_element_by_id("password")
ep.send_keys("burhansaydin@gmail.com")
ps.send_keys("Kerem4154!")

ent = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[3]/form/div[3]/button')
ent.send_keys(Keys.ENTER)

time.sleep(10.0)

job = driver.find_element_by_id("ember254")
job.click()

a = driver.find_element_by_xpath('//*[@id="ember654"]/span')
a.send_keys(Keys.ENTER)