#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/10/23 11:10
"""


import re
import time

import requests
from bs4 import BeautifulSoup

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


def get_searchhzjcb_list(kyw=None, page=1):
    url = 'https://www.hzjcb.com/borrow/listNew.do'
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

    #names = soup.select('#listForm > div.secondArea > div.leftArea > div > div.title')
    names = soup.select(".title") # update 201712222325
    names = names[1:]
    #print (names)

    inbuystatus = soup.select('#listForm > div.secondArea > div.leftArea > div > a')
    #inbuystatus = ('#listForm > div.secondArea > div.leftArea > div > a')
    #print (inbuystatus)

    #inprogresses = soup.select('#listForm > div.secondArea > div.leftArea > div > div.result > p.totol > span')
    inprogresses = soup.select('#listForm > div.secondArea > div.leftArea > div > div.result > p.totol > span.progressNum') # update 201712222352
    #listForm > div.secondArea > div.leftArea > div > div.limit > div')
    print (inprogresses)

    interests = soup.select('#listForm > div.secondArea > div.leftArea > div > div.Profit')
    #print (interests)

    rangedays = soup.select('#listForm > div.secondArea > div.leftArea > div > div.limit > p.term > span')
    #print (rangedays)

    
    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
    #for name, inprogress, interest, rangeday in zip(names, inprogresses, interests, rangedays):
        name = name.text.strip()
        inbuystat = inbuystat.text.strip()
        inprogress = inprogress.text.strip().replace("\t","").replace("\r\n","")
        #interest = interest.text.strip().replace("\n", "").replace(u"年化收益","").replace(u"%","").replace(" ","")
        interest = interest.text.strip().replace("\r\n", "").replace(u"年化收益率","").replace("\t","").replace(u"%","").replace("\n","")  # update 201712222336
        rangeday = rangeday.text.strip().replace(u"天","")

        if (rangeday != '7'):
            # Inflation = 3%, (6.5 -> 39.16)
            rangeday2 = str(float(rangeday)/30)
            interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
            delta = str(float(interest_shadow) / float(rangeday2))
            #print name.encode('utf-8')
            #print inbuystat.encode('utf-8')
            #data = [name, inbuystat, inprogress, interest, rangeday, '\t']
            data = [name, inbuystat, inprogress, interest+u"%", rangeday+u"天", delta, '\t']
            #data = [name, inprogress, interest, rangeday]
            print '|'.join(data).encode('utf-8')
       
    time.sleep(5)
    print ("+--line of split--+")




if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    get_searchhzjcb_list()
