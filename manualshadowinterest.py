#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/1/18 10:10
"""

import requests
from bs4 import BeautifulSoup

import random

def  manucalc_shadowinterest(url):
	try:
		listproxies = ['122.225.17.123:8080',
		'125.79.48.47:808',
		'219.155.10.30:8118']
		blistproxies = random.sample(listproxies, 1)
		print  blistproxies
		#proxies = {'http': '122.225.17.123:8080'}
		#proxies = {'http': '125.79.48.47:808'}
		proxies = {'http': blistproxies[0]}
		print proxies
		#url = '110.172.220.194:8080'
		response = requests.get(url, proxies=proxies)
		soup = BeautifulSoup(response.text, 'lxml')
		ip = soup.select('body > p')[0].text
		print ip
	except Exception, e:
	    print Exception, e 



if __name__=='__main__':
    #test_webpage('https://www.juaicai.cn')
    print ("+--line of split--+")
    manucalc_shadowinterest('http://icanhazip.com/')
    #219.232.165.36:8080
    #110.172.220.194:8080
    #122.225.17.123:8080

