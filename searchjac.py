#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/10/20 22:10
"""

import urllib

import re
import time

import requests
from bs4 import BeautifulSoup

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


def get_searchjac_list(kyw=None, page=1):
    #url = 'http://www.mailiangwang.com/biz/list'
    url = 'https://www.juaicai.cn/product/productlist'
    payload = {'keyword': kyw, 'pageid': page}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.14'}
    response = requests.get(url, headers=headers)
    #response = requests.get(url, params = payload)
    print response.url
    print response.status_code
    soup = BeautifulSoup(response.text, 'lxml')
    #print soup
    #names = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n1 > a')
    #print names
    names = soup.select('#porductlist_li > li > div.list-item > div.item-headline > h3')
    #print names

    inbuystatus = soup.select('#porductlist_li > li > div.item-sub-btn > a')
    #print inbuystatus

    inprogresses = soup.select('#porductlist_li > li > div.list-item > div.progress-bar > div > div > h4 > em')
    #print inprogresses

    #interests = soup.select('#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt')
    interests = soup.select(".red")
    #print interests

    rangedays = soup.select('#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt > em')
    #print rangedays

    #for rngday in rangedays:
    #    print rngday.find_parent().text.encode('utf-8')


    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
        name = name.text
        inbuystat = inbuystat.text
        inprogress = inprogress.text
        interest = interest.text.replace(u"%","")
        rangeday = rangeday.find_parent().text.replace(u"天","")

        #print name.encode('utf-8')
        #print inbuystat.encode('utf-8')

        # Inflation = 3%, (6.5 -> 39.16)
        rangeday2 = str(float(rangeday)/30)
        interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
        delta = str(float(interest_shadow) / float(rangeday2))

        #print name.encode('utf-8')
        #print inbuystat.encode('utf-8')

        data = [name, inbuystat, inprogress, interest, rangeday, rangeday2,  interest_shadow, delta, '\t']
        #data = [name, inbuystat, inprogress, interest, rangeday, '\t']
        print '|'.join(data).encode('utf-8')
        #print inbuystat.text.encode('utf-8')

    time.sleep(5)
    print ("+--line of split--+")





if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')

    get_searchjac_list()
