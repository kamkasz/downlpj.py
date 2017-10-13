#!/usr/bin/env python2.7
# -*- coding: utf-8 -*
#importing modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import requests
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87")
 #if website is coded to check user's browser, this should make sure that it won't stop PhantomJs from working
#adress of the site on which you want to log on
baseurl = "example.com/login.aspx?" 
#login and username
username = "username"
password = "password" 
#text which will be written into forms
data="xxx"
godzina="yyy"
data2="zzz
godzina2="aaa" 
#defining of elements, like forms or buttons, which are needed to navigate the site, it will make it possible to localize them
xpaths = {  'txtUser' : "//input[@name='txtUser']",
           'txtPassword' : "//input[@name='txtPassword']",
           'submitButton' :   "//input[@name='login']",
            'submitButton2' :   "//input[@name='werwe']",
            'submitButton3' :   '//a[@id="ListOfStations"]',
            'Datef' :   "//input[@name='Datef]",
            'Hourf' :   "//input[@name='Hourf']",
            'submitButton4' :   "//input[@name='Odswiez']",
            'Datet' :   "//input[@name='Datet']",
            'Hourt' :   "//input[@name='Hourt']",
            'submitButton5' :   '//a[@id="hl_generate_excel"]'


         }
#opening PhantomJs webdriver, defining userAgent 
mydriver = webdriver.PhantomJS(desired_capabilities=dcap) 
#opening a site
mydriver.get(baseurl)
#login into website
mydriver.find_element_by_xpath(xpaths['txtUser']).clear()
mydriver.find_element_by_xpath(xpaths['txtUser']).send_keys(username)
mydriver.find_element_by_xpath(xpaths['txtPassword']).clear()
mydriver.find_element_by_xpath(xpaths['txtPassword']).send_keys(password)
mydriver.find_element_by_xpath(xpaths['submitButton']).click()
#waiting till page loads, it's probably better to use WebDriverWait
#navigating site
time.sleep(10)
mydriver.get('http://example.com/')
time.sleep(40)
mydriver.find_element_by_xpath(xpaths['submitButton3']).click()
time.sleep(30)
mydriver.find_element_by_xpath(xpaths['submitButton2']).click()
time.sleep(10)
#filling out forms
mydriver.find_element_by_xpath(xpaths['Datef']).clear()
mydriver.find_element_by_xpath(xpaths['Datef']).send_keys(data)
mydriver.find_element_by_xpath(xpaths['Hourf']).clear()
mydriver.find_element_by_xpath(xpaths['Hourf']).send_keys(godzina)
mydriver.find_element_by_xpath(xpaths['Datet']).clear()
mydriver.find_element_by_xpath(xpaths['Datet']).send_keys(data2)
mydriver.find_element_by_xpath(xpaths['Hourt']).clear()
mydriver.find_element_by_xpath(xpaths['Hourt']).send_keys(godzina2)
mydriver.find_element_by_xpath(xpaths['submitButton4']).click()
time.sleep(5)
mydriver.find_element_by_xpath(xpaths['submitButton5']).click()
#changing browser's windows
config_window = mydriver.window_handles[0]
asz=mydriver.switch_to_window(config_window)
#creating headers - they will be used is sessions
headers = {
"User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
}
s = requests.session()
s.headers.update(headers)
#getting cookies from selenium to use them in session
for cookie in mydriver.get_cookies():
    c = {cookie['name']: cookie['value']}
    s.cookies.update(c)
#downloading a file
response = s.get('http://dssp.imgw.ad/tpp/exel.aspx',stream=True)
with open("/home/kamil/Desktop/maska/euro3.xls", 'wb') as fd:

        fd.write(response.content)
mydriver.quit()

