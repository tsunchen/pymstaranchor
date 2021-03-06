#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/1/1 10:10
"""


import re
import time

import requests
from bs4 import BeautifulSoup

from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import types


def calMonthDay(d):
   #.replace(u"个月","").replace(u"天","")
   if u"个月" in d:
     #print ('Month')
     dd = int(d.replace(u"个月","")) * 30
     return (dd)
   elif u"天" in d:
     #print ('Day')
     return (d.replace(u"天",""))
   else:
        return ("1")



def calPlus(d):
   if '+' in d:
     #print ('+')
     ld, rd = d.split("+")
     return float(ld)+float(rd)
     #return (d[:-2])
   else:
     #print (d)
     return float(d)





def get_searchdy_list(kyw=None, page=1):
    url = 'https://www.51duoying.com/gushou/list'
    payload = {'keyword': kyw, 'pageid': page}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.14'}
    #Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
    response = requests.get(url, headers=headers)
    #request = urllib2.Request(url)
    #response = urllib2.urlopen(request)
    #print (response.getcode())
    #response = requests.get(url, params = payload)
    print (response.url)
    print (response.status_code)

    soup = BeautifulSoup(response.text, 'lxml')
    #print soup

    time.sleep(5)


    names = soup.select('body > div.gray_bg.main_warp.pad_bot_1 > div > div.right_main > div > div.products > ul > li > div > div.tit.clear > h4 > a')
    #body > div.main > div:nth-child(3) > div > div:nth-child(3) > p
    #print (names)

    inbuystatus = soup.select('body > div.gray_bg.main_warp.pad_bot_1 > div > div.right_main > div > div.products > ul > li > div > div.btn_warp.single > a')
    #print (inbuystatus)

    inprogresses = soup.select('body > div.gray_bg.main_warp.pad_bot_1 > div > div.right_main > div > div.products > ul > li > div > div.pro_info > div')
                               #body > div.gray_bg.main_warp.pad_bot_1 > div > div.right_main > div > div.products > ul > li > div > div.pro_info > div > div.text
    #body > div.main > div:nth-child(3) > div > div:nth-child(3) > ul > li.progress > span
    #print (inprogresses)

    interests = soup.select("body > div.gray_bg.main_warp.pad_bot_1 > div > div.right_main > div > div.products > ul > li > div > div.pro_info > p.pct")
    ##interests = soup.find_all(class_=re.compile("red big"))
    #body > div.main > div > div > div > div.fl > ul > li > p > span
    #print (interests)

    rangedays = soup.select('body > div.gray_bg.main_warp.pad_bot_1 > div > div.right_main > div > div.products > ul > li > div > div.pro_info > p.day')
    #print len(rangedays)
    #soup.find_all("a", text="Elsie")
    #rangedays = soup.find_all(re.compile("投资期限"))
    rangedays_li3 = []
    for rx in range(2, len(rangedays), 4): 
        #print rangedays[rx]
        rangedays_li3.append(rangedays[rx])
   
    datalist1 = []
    datalist2 = []
    dicdata = []
    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
    #for name, inprogress, interest, rangeday in zip(names, inprogresses, interests, rangedays):
        name = name.text.strip().replace("\n","")
        inbuystat = inbuystat.text.strip()
        inprogress = inprogress.text.strip()
        interest = interest.text.strip().replace("%","") # .replace("\n", "") #.replace(u"年化收益","")
        #rangeday = rangeday.text.strip()+u"天"
        rangeday = rangeday.text.strip().replace(u"天","")

        ##test mode
        #data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", '\t']
        #print '|'.join(data).encode('utf-8')


        if inbuystat != u"":
            # Inflation = 3%, (6.5 -> 39.16)
            rangeday2 = str(float(rangeday)/30)
            interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
            delta = str(float(interest_shadow) / float(rangeday2))

            #print name.encode('utf-8')
            #print inbuystat.encode('utf-8')
            #data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", '\t']
            data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", delta, '\t']
            #datalist1.append(rangeday.replace(u"天",""))
            #datalist2.append(data)
            #dictdata = dict(zip(rangeday,data))
            #data = [name, inprogress, interest, rangeday]
            print '|'.join(data).encode('utf-8')
    #print datalist1
    #print datalist2
    #dicdata = zip(datalist1,datalist2)
    #print dicdata

    #sortedDictValues2(dicdata)
    #for k in keys:
    #    print k
    time.sleep(5)
    print ("+--line of split--+")





'''
def getdynamic_searchdy_list(url,kyw=None, page=1):
    #url = 'https://www.suoxing.vip/index/standard/list2/3/0'
    url = url
    #driver = webdriver.PhantomJS(executable_path = r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver = webdriver.PhantomJS(executable_path = r'E:\dataUSB\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    print (driver)
    driver.get(url)
    print (driver.current_url)
    #print (driver.page_source)

    #payload = {'keyword': kyw, 'pageid': page}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.14'}
    #Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
    response = requests.get(url, headers=headers)
    #request = urllib2.Request(url)
    #response = urllib2.urlopen(request)
    #print (response.getcode())
    #response = requests.get(url, params = payload)
    #print (response.url)
    print (response.status_code)

    #soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    #print soup

    time.sleep(5)

    names = soup.select('#tab > ul > li.title.clearfix > p')
    #print (names)

    inbuystatus = soup.select('#tab > ul > li.five.fl > a > span')
    ##hms_timer0
    ##tab > ul:nth-child(1) > li.five.fl > a
    #print (inbuystatus)

    inprogresses = soup.select('#tab > ul > li.five.fl > p')
    #print (inprogresses)

    interests = soup.select('#tab > ul > li.one.fl > div.bid_number')
    #interests = soup.find_all(class_=re.compile("red big"))
    #body > div.main > div > div > div > div.fl > ul > li > p > span
    #print (interests)

    rangedays = soup.select('#tab > ul > li.three.fl > p.f30.gray6.arial.lh30')
    #print len(rangedays)
    #soup.find_all("a", text="Elsie")
    #rangedays = soup.find_all(re.compile("投资期限"))
    rangedays_li3 = []
    for rx in range(2, len(rangedays), 4): 
        #print rangedays[rx]
        rangedays_li3.append(rangedays[rx])
   
    datalist1 = []
    datalist2 = []
    dicdata = []

    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
    #for name, inprogress, interest, rangeday in zip(names, inprogresses, interests, rangedays):
        name = name.text.strip()
        inbuystat = inbuystat.text.strip()
        inprogress = inprogress.text.strip().replace("\n", "")
        interest = interest.text.strip().replace("\r\n", "").replace("\t","").replace("%","")
        interest = str(calPlus(interest))
        rangeday = rangeday.text.strip()  #.replace(u"个月","").replace(u"天","")
        rangeday = str(calMonthDay(rangeday))

        #test mode
        #data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", '\t']
        #print '|'.join(data).encode('utf-8')


        if inbuystat != u"还款中":            
            #print (rangeday)
            #print type(rangeday)
            # Inflation = 3%, (6.5 -> 39.16)
            rangeday2 = str(float(rangeday)/30)
            interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
            delta = str(float(interest_shadow) / float(rangeday2))
            #print name.encode('utf-8')
            #print inbuystat.encode('utf-8')
            #data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", '\t']
            data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", delta, '\t']
            #datalist1.append(rangeday.replace(u"天",""))
            #datalist2.append(data)
            #dictdata = dict(zip(rangeday,data))
            #data = [name, inprogress, interest, rangeday]
            print '|'.join(data).encode('utf-8')

    #time.sleep(5)
    #print ("+--line of split--+")
'''    





def sortedDictValues2(adict): 
    adict.sort(key=lambda x:x[0]) 
    for item in adict:
        print item
    #keys = adict.keys() 
    #keys.sort() 
    #return [dict[key] for key in keys] 

'''
def getdynamic_searchdy_lists():
    getdynamic_searchdy_list('https://www.51duoying.com/gushou/list', kyw=None, page=1)
    #getdynamic_searchdy_list('https://www.suoxing.vip/index/standard/list2/1/0', kyw=None, page=1)
    #getdynamic_searchdy_list('https://www.suoxing.vip/index/standard/list2/7/7', kyw=None, page=1)
'''

if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    #'https://www.suoxing.vip/index/standard/list2/3/0'
    #getdynamic_searchsx_list('https://www.suoxing.vip/index/standard/list2/3/0', kyw=None, page=1)
    get_searchdy_list()
    #getdynamic_searchdy_lists()
