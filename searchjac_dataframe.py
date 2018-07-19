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

import pymstaranchorsetting

import pandas as pd
import numpy as np

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


def get_searchjac_list(selecton, url, kyw=None, page=1):
    #print selecton
    url = url
    #url = 'https://www.juaicai.cn/product/productlist'
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
    #names = soup.select('#porductlist_li > li > div.list-item > div.item-headline > h3')
    names = soup.select(selecton[0])
    #print names

    #inbuystatus = soup.select('#porductlist_li > li > div.item-sub-btn > a')
    inbuystatus = soup.select(selecton[1])
    #print inbuystatus

    #inprogresses = soup.select('#porductlist_li > li > div.list-item > div.progress-bar > div > div > h4 > em')
    inprogresses = soup.select(selecton[2])
    #print inprogresses

    #interests = soup.select('#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt')
    #interests = soup.select(".red")
    interests = soup.select(selecton[3])
    #print interests

    #rangedays = soup.select('#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt > em')
    rangedays = soup.select(selecton[4])
    #print rangedays

    #for rngday in rangedays:
    #    print rngday.find_parent().text.encode('utf-8')

    #dataframe_conf
    arr_buffer =[]
    columns_name = ['','Name','Inbuystat','Inprogess','Interest','Rangeday','Delta','']
    arr_buffer.append(columns_name)

    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
        name = name.text
        inbuystat = inbuystat.text
        inprogress = inprogress.text.replace("\r\n","").replace("\t","")
        interest = interest.text.replace(u"%","")
        interest = str(pymstaranchorsetting.calPlus(interest))

        rangeday = rangeday.find_parent().text.replace("\t","").replace("\r\n","").replace(u"天","").replace("\n","")

        #print name.encode('utf-8')
        #print inbuystat.encode('utf-8')

        # Inflation = 3%, (6.5 -> 39.16)
        rangeday2 = str(float(rangeday)/30)
        interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
        delta = str(float(interest_shadow) / float(rangeday2))

        #print name.encode('utf-8')
        #print inbuystat.encode('utf-8')
        #if delta > '0.5':
        data = [name, inbuystat, inprogress, interest+u"%  @"+ url + " ", rangeday+u" 天", delta, '\t']
        data_o = ['',name, inbuystat, inprogress, interest+u" %@" + url + " ", rangeday, delta, '\t']
        #data = [name, inbuystat, inprogress, interest, rangeday, '\t']
        print '|'.join(data).encode('utf-8')
        #print inbuystat.text.encode('utf-8')
        arr_buffer.append(data_o)

    time.sleep(5)
    print ("+--line of split--+")
    return (arr_buffer)


'''
#https://www.juaicai.cn/activity/productlist-debt
#2018-1-2 debt project
def get_searchjac_debt_list(url, kyw=None, page=1):
    url = url
    #url = 'https://www.juaicai.cn/activity/productlist-debt'
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
                         #porductlist_li > li:nth-child(1) > div.list-item > div.item-headline > h3
    #print names

    inbuystatus = soup.select('#porductlist_li > li > div.item-sub-btn > a')
    #porductlist_li > li:nth-child(1) > div.item-sub-btn > a
    #print inbuystatus

    #inprogresses = soup.select('#porductlist_li > li > div.list-item > div.progress-bar > div > div > h4 > em')
    inprogresses = soup.select('#porductlist_li > li > div.list-item > div.progress-bar > h1')
    #print inprogresses

    #interests = soup.select('#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt')
    interests = soup.select(".red")
    #print interests

    rangedays = soup.select('#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt > em')
    #porductlist_li > li:nth-child(1) > div.list-item > div.item-rate.clearfix > dl:nth-child(2) > dt 
    #print rangedays

    #for rngday in rangedays:
    #    print rngday.find_parent().text.encode('utf-8')


    for name, inbuystat, inprogress, interest, rangeday in zip(names, inbuystatus, inprogresses, interests, rangedays):
        name = name.text
        inbuystat = inbuystat.text
        inprogress = inprogress.text.replace("\r\n","").replace("\t","")
        interest = interest.text.replace(u"%","")
        rangeday = rangeday.find_parent().text.replace("\r\n","").replace("\n","").replace("\t","").replace(u"天","")

        #print name.encode('utf-8')
        #print inbuystat.encode('utf-8')

        if (inbuystat!=u"已售罄"):
            # Inflation = 3%, (6.5 -> 39.16)
            rangeday2 = str(float(rangeday)/30)
            interest_shadow = str( (float(interest) - 3) / ((float('39.16')/float(rangeday)*365/10000 + 0.03)*100) )
            delta = str(float(interest_shadow) / float(rangeday2))

            #print name.encode('utf-8')
            #print inbuystat.encode('utf-8')

            data = [name, inbuystat, inprogress, interest+u"%", rangeday+u" 天", delta, '\t']
            #data = [name, inbuystat, inprogress, interest, rangeday, '\t']
            print '|'.join(data).encode('utf-8')
            #print inbuystat.text.encode('utf-8')

    time.sleep(5)
    print ("+--line of split--+")
'''

def get_searchjac_lists():
    #dataframe_resolve
    selecton_productlist_debt = [
      '#porductlist_li > li > div.list-item > div.item-headline > h3',
      '#porductlist_li > li > div.item-sub-btn > a',
      '#porductlist_li > li > div.list-item > div.progress-bar > h1',
      '.red',
      '#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt > em'
    ]
    arr_buffer_o1 = get_searchjac_list(selecton_productlist_debt , 'https://www.juaicai.cn/activity/productlist-debt')
    data_arr_buffer = np.array(arr_buffer_o1)
    res = pd.DataFrame(data=data_arr_buffer[1:,1:],index=data_arr_buffer[1:,0],columns=data_arr_buffer[0,1:])
    res_s = res.sort_values(by=['Delta'], ascending=False)
    #print( res_s[['Inprogess','Interest', 'Rangeday','Delta']] )
    print( res_s[['Interest', 'Rangeday','Delta']][(res_s['Delta']<'1.0')&(res_s['Delta']>'0.7')] )
    print( res_s[['Interest', 'Rangeday','Delta']][res_s['Delta']>'1.0'] )

    #
    selecton_productlist = [
      '#porductlist_li > li > div.list-item > div.item-headline > h3',
      '#porductlist_li > li > div.item-sub-btn > a',
      '#porductlist_li > li > div.list-item > div.progress-bar > div > div > h4 > em',
      '.red',
      '#porductlist_li > li > div.list-item > div.item-rate.clearfix > dl > dt > em'
    ]
    arr_buffer_o2 = get_searchjac_list(selecton_productlist , 'https://www.juaicai.cn/product/productlist')
    data_arr_buffer = np.array(arr_buffer_o2)
    res = pd.DataFrame(data=data_arr_buffer[1:,1:],index=data_arr_buffer[1:,0],columns=data_arr_buffer[0,1:])
    res_s = res.sort_values(by=['Delta'], ascending=False)
    #print( res_s[['Inprogess','Interest', 'Rangeday','Delta']] )
    print( res_s[['Interest', 'Rangeday','Delta']][(res_s['Delta']<'1.0')&(res_s['Delta']>'0.5')] )
    print( res_s[['Interest', 'Rangeday','Delta']][res_s['Delta']>'1.0'] )


def runit(t):
    get_searchjac_lists()



if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    get_searchjac_lists()
