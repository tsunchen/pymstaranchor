#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/11/11 10:10

check > copy selector

"""


import re
import time

import requests
from bs4 import BeautifulSoup




def calPlus(d):
   if '+' in d:
     #print ('+')
     ld, rd = d.split("+")
     return float(ld)+float(rd)
     #return (d[:-2])
   else:
     #print (d)
     return float(d)




def get_searchcgtz_list(kyw=None, page=1):
    #url = 'http://www.mailiangwang.com/biz/list'
    #url = 'https://www.cgtz.com/projects.html'
    url = 'https://www.cgtz.com/project/'
    payload = {'keyword': kyw, 'pageid': page}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.14'}
    response = requests.get(url, headers=headers)
    #request = urllib2.Request(url)
    #response = urllib2.urlopen(request)
    #print (response.getcode())
    #response = requests.get(url, params = payload)
    print (response.url)
    print (response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    #print soup

    #time.sleep(5)

    names = soup.select('body > section.container.clearfix > div > div.mainCon.clearfix > div.floatRight > ul > li > div.saleHave > div > span > a')
                        #
                        #body > section > div > article > div > dl > dt > a
                        #'body > section > div > article > div > dl > dt > a'
                        
    #print (names)

    inbuystatus = soup.select('body > section.container.clearfix > div > div.mainCon.clearfix > div.floatRight > ul > li > div.saleHave > ul > li.lastLi > a')
                               #
                               #body > section > div > article > div > dl > dd > div > div > div.view
                               #body > section > div > article > div > dl > dd > div > div > div.view > a
                               #body > section > div > article > div > dl > dd > div > div > div.view
    #print inbuystatus

    inprogresses = soup.select('body > section.container.clearfix > div > div.mainCon.clearfix > div.floatRight > ul > li > div.saleHave > div > span.fSpan')
                                #
                                #body > section > div > article > div > dl > dd > div > div > div > em
                                #body > section > div > article > div > dl > dd > div > div > div
    #print (inprogresses)

    interests = soup.find_all(text=re.compile("%"))
                            #soup.select('body > section.container.clearfix > div > div.mainCon.clearfix > div.floatRight > ul > li > div.saleHave > ul > li ')
                            #soup.select('.longLi > em')
                            #body > section.container.clearfix > div > div.mainCon.clearfix > div.floatRight > ul > li > div.saleHave > ul > li > em
                            #body > section > div > article > div > dl > dd > div.fl.w2 > div > span.fcDeepRed
                            #'body > section > div > article > div > dl > dd > div.fl.w2 > div > span')
                            #body > section:nth-child(5) > div > article > div > dl:nth-child(8) > dd > div.fl.w2 > div > span.fcDeepRed
                            #body > section:nth-child(5) > div > article > div > dl:nth-child(9) > dd > div.fl.w2 > div > span.fcDeepRed
    #print (interests)

    rangedays = soup.select('em[style]')
                            #
                            #soup.find_all(style=re.compile("#333"))
                            #em[style]
                            #body > section.container.clearfix > div > div.mainCon.clearfix > div.floatRight > ul > li > div.saleHave > ul > li > em
                            #body > section > div > article > div > dl > dd > div.fl.w3 > div > span.fcRed > em
    #print (rangedays)

    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
    #for name, inprogress, interest, rangeday in zip(names, inprogresses, interests, rangedays):
        name = name.text.strip()
        inbuystat = inbuystat.text.strip()
        inprogress = inprogress.text.strip()
        interest = interest.strip().replace("%","")
        interest = str(calPlus(interest))
        rangeday = rangeday.find_parent().text.strip().replace("\n","").replace(" ","").replace(u"投资期限","").replace(u"天","")

        #print name.encode('utf-8')
        #print inbuystat.encode('utf-8')

        # Inflation = 3%, (6.5 -> 39.16)
        rangeday2 = str(float(rangeday)/30)
        interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
        delta = str(float(interest_shadow) / float(rangeday2))


        #data = [name, inbuystat, inprogress, interest, rangeday,'\t']
        data = [name, inbuystat, inprogress, interest, rangeday, rangeday2,  interest_shadow, delta, '\t']
        #data = [name, inprogress, interest, rangeday]
        print '|'.join(data).encode('utf-8')


    time.sleep(5)
    print ("+--line of split--+")






if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    get_searchcgtz_list()
    #print calPlus("15")
    #print calPlus("9 + 2.2")
