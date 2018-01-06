#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/12/25 11:10
"""


import re
import time

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib,re
import os,sys

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getdynamic_jd_list(keywords, keywordsalias):
    url = 'https://search.jd.com/'
    PhantomJS_path = "E:/phantomjs-2.1.1-windows/bin"
    driver = webdriver.PhantomJS(executable_path = r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    print (driver)
    driver.get(url)
    print (driver.current_url)

    input = driver.find_element_by_id("keyword")
    input.send_keys(keywords)
    input.send_keys(Keys.RETURN)

    time.sleep(30)

    png_name = "jd_" + keywordsalias + ".png"
    driver.save_screenshot(png_name)
    driver.close()
    driver.quit()

    #response = requests.get(url)
    #print (response.status_code)
    #time.sleep(1)



if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    getdynamic_jd_list(u"花生500g", "peanut500g")
    getdynamic_jd_list(u"牛奶1L", "milk1L")
    getdynamic_jd_list(u"酱油1.8L", "soysaurce1.8L")
