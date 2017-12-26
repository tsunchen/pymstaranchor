#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/12/27 11:10
"""


import re
import time

import requests
from bs4 import BeautifulSoup

from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def calPlus(d):
   if '+' in d:
     #print ('+')
     ld, rd = d.split("+")
     return float(ld)+float(rd)
     #return (d[:-2])
   else:
     #print (d)
     return float(d)

def getdynamic_searchhqb_list():
    url = 'https://www.hqblicai.com/invest/index.html'
    PhantomJS_path = "E:/phantomjs-2.1.1-windows/bin"
    driver = webdriver.PhantomJS(executable_path = r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    print (driver)
    driver.get(url)
    print (driver.current_url)

    response = requests.get(url)
    print (response.status_code)
    time.sleep(1)
    #driver.save_screenshot("hqb.png")

    #print (driver.page_source)
    #ele1 = driver.find_element_by_id("products_name")
    #print (ele1)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    #print soup

    #names = soup.select('#listForm > div.secondArea > div.leftArea > div > div.title')
    names = soup.select("#show_products_short > div > ul > li.products_name") # update 201712222325
    #names = names[0:]
    #print (names)

    inbuystatus = soup.select('#show_products_short > div > ul > li.products_btn > a')
    #inbuystatus = ('#listForm > div.secondArea > div.leftArea > div > a')
    #print (inbuystatus)

    #inprogresses = soup.select('#listForm > div.secondArea > div.leftArea > div > div.result > p.totol > span')
    inprogresses = soup.select('#show_products_short > div > ul > li.products_time.clearfix > div.right') # update 201712222352
    #listForm > div.secondArea > div.leftArea > div > div.limit > div')
    #print (inprogresses)

    interests = soup.select('#show_products_short > div > ul > li.products_num')
    #print (interests)

    rangedays = soup.select('#show_products_short > div > ul > li.products_time.clearfix > div.left')
    #print (rangedays)

    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
        name = name.text.strip()
        inbuystat = inbuystat.text.strip()
        inprogress = inprogress.text.strip()
        interest = interest.text.strip().replace(u"%","")
        interest = str(calPlus(interest))
        rangeday = rangeday.text.strip().replace(u"理财期限","").replace(u"天","")

        if inbuystat == u"立即赚钱":
            # Inflation = 3%, (6.5 -> 39.16)
            rangeday2 = str(float(rangeday)/30)
            interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
            delta = str(float(interest_shadow) / float(rangeday2))
            #data = [name, inbuystat, inprogress, interest, rangeday]
            data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", delta, '\t']
            print '|'.join(data)

    time.sleep(5)
    print ("+--line of split--+")
    driver.close()
    driver.quit()









if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    getdynamic_searchhqb_list()
