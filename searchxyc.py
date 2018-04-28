#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/04/28 20:10
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

def getdynamic_searchxyc_list():
    url = 'http://www.xycjinfu.com/loan/list_3_1.html'
    #url = 'https://www.hqblicai.com/invest/index.html'
    PhantomJS_path = "E:/phantomjs-2.1.1-windows/bin"
    #driver = webdriver.PhantomJS(executable_path = r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver = webdriver.PhantomJS(executable_path = r'E:\dataUSB\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
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
    names = soup.find_all(class_=re.compile("ahov")) #soup.select("#starDiv > div > div > div.pro_bt.new_bt.fl > a")
    #("#show_products_short > div > ul > li.products_name") # update 201712222325
    #names = names[0:]
    #print (names)


    inbuystatus = soup.select('#starDiv > div > div > div.pro_bnt.fr > a')#('#show_products_short > div > ul > li.products_btn > a')
    #inbuystatus = ('#listForm > div.secondArea > div.leftArea > div > a')
    #print (inbuystatus)

    #inprogresses = soup.select('#listForm > div.secondArea > div.leftArea > div > div.result > p.totol > span')
    inprogresses = soup.find_all(class_=re.compile("fl ft12 pro_jds"))#('#starDiv > div > div > div.pro_jdt.fl > div > div.fl.ft12.pro_jds') #('#show_products_short > div > ul > li.products_time.clearfix > div.right') # update 201712222352
    #listForm > div.secondArea > div.leftArea > div > div.limit > div')
    #print (inprogresses)

    interests = soup.find_all(class_=re.compile("fama ft16 pr"))#soup.select('#starDiv > div > div > div.pro_lv.fl > h3')#('#show_products_short > div > ul > li.products_num')
    #print (interests)

    rangedays = soup.find_all(class_=re.compile("pro_dat fl")) #('#show_products_short > div > ul > li.products_time.clearfix > div.left')
    #print (rangedays)

    ## select the node with step = 2 
    rangedays_2 = []
    for r in range(0, len(rangedays), 2):
        rangedays_2.append(rangedays[r])
       #print rangedays[r]
    #print (rangedays_2)


    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays_2):
        name = name.text.strip()
        inbuystat = inbuystat.text.strip()
        inprogress = inprogress.text.strip().replace(u"%","")
        interest = interest.text.strip().replace(u"%","")
        interest = str(calPlus(interest))
        rangeday = rangeday.text.strip().replace("\n","").replace(u"先息后本","").replace(u"天","")#.replace(u"投资期限","").replace(u"天","")
        #print(rangeday)

        if inbuystat == u"立即投资":
            # Inflation = 3%, (6.5 -> 39.16)
            rangeday2 = str(float(rangeday)/30)
            interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
            delta = str(float(interest_shadow) / float(rangeday2))
            #data = [name, inbuystat, inprogress, interest, rangeday]
            data = [name, inbuystat, inprogress, interest+u"%", rangeday+u" 天", delta, '\t']
            print '|'.join(data)

    time.sleep(5)
    print ("+--line of split--+")
    driver.close()
    driver.quit()




def runit(t):
    getdynamic_searchxyc_list()




if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    getdynamic_searchxyc_list()
