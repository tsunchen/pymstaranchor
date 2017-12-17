#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/10/23 12:10
"""


import re
import time

import requests
from bs4 import BeautifulSoup

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


def get_searchbym_list(kyw=None, page=1):
    url = 'https://www.baiyimao.com/wgtz/Product/productCategory!getProductByCondition.action'
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

    names = soup.select('body > div.main > div > div > div > p > a')
    #print (names)

    inbuystatus = soup.select('body > div.main > div > div > div > ul > li > a')
    #print (inbuystatus)

    inprogresses = soup.select('body > div.main > div > div > div > ul > li.progress > span')
    #body > div.main > div:nth-child(3) > div > div:nth-child(3) > ul > li.progress > span
    #print (inprogresses)

    #interests = soup.select("[class~=big]")
    interests = soup.find_all(class_=re.compile("red big"))
    #body > div.main > div > div > div > div.fl > ul > li > p > span
    #print (interests)

    rangedays = soup.select('body > div.main > div > div > div > div.fl > ul > li > p > span')
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
    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays_li3):
    #for name, inprogress, interest, rangeday in zip(names, inprogresses, interests, rangedays):
        name = name.text.strip()
        inbuystat = inbuystat.text.strip()
        inprogress = inprogress.text.strip()
        interest = interest.text.strip() # .replace("\n", "") #.replace(u"年化收益","")
        
        #rangeday = rangeday.text.strip()+u"天"
        rangeday = rangeday.text.strip()

        # Inflation = 3%, (6.5 -> 39.16)
        rangeday2 = str(float(rangeday)/30)
        interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
        delta = str(float(interest_shadow) / float(rangeday2))

        #print name.encode('utf-8')
        #print inbuystat.encode('utf-8')

        data = [name, inbuystat, inprogress, interest, rangeday, rangeday2,  interest_shadow, delta, '\t']
        datalist1.append(rangeday.replace(u"天",""))
        datalist2.append(data)
        #dictdata = dict(zip(rangeday,data))
        #data = [name, inprogress, interest, rangeday]
        print '|'.join(data).encode('utf-8')



    #print datalist1
    #print datalist2
    dicdata = zip(datalist1,datalist2)
    #print dicdata

    #sortedDictValues2(dicdata)


    #for k in keys:
    #    print k
    time.sleep(5)
    print ("+--line of split--+")






def sortedDictValues2(adict): 
    adict.sort(key=lambda x:x[0]) 
    for item in adict:
        print item
    #keys = adict.keys() 
    #keys.sort() 
    #return [dict[key] for key in keys] 


if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    get_searchbym_list()
