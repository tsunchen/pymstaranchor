#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/10/23 22:10
@upgrade: 2018/04/05 multiprocessing, threading
"""


import searchxyc
import searchjac
import searchcgtz
import searchhzjcb
import searchbym
import searchhqb
##import searchinw
import searchsx
import searchdy
import searchxj

import os
import multiprocessing
import threading



if __name__=='__main__':


	functionpool = [

            getattr(searchxyc,   'runit'),
            getattr(searchbym,   'runit'),
	    getattr(searchsx,    'runit'),
	    getattr(searchhzjcb, 'runit'),
	    
	    getattr(searchjac,   'runit'),
	    getattr(searchcgtz,  'runit'),
	    getattr(searchhqb,   'runit'),
	    
	    #getattr(searchdy,    'runit'),
	    getattr(searchxj,    'runit')

	    ]

	for f in functionpool:
		print (f)
		mf = threading.Thread(target=f, args=("",))
		mf.start()
		#mf.join()
	print ("fin--mf")



'''

	functionpool = [

	    getattr(searchjac,   'runit'),
	    getattr(searchcgtz,  'runit'),
	    getattr(searchhzjcb, 'runit'),
	    getattr(searchbym,   'runit'),
	    getattr(searchhqb,   'runit'),
	    ##getattr(searchsx,    'runit'),
	    getattr(searchdy,    'runit'),
	    ##getattr(searchxj,    'runit')

	    ]

	for f in functionpool:
		print (f)
		mp = multiprocessing.Process(target=f, args=("",))
		mp.start()
		#mp.join()

	print ("fin--mp")
'''




'''
	#searchsx.getdynamic_searchsx_lists() # 1, # 30
	searchbym.get_searchbym_list() # 53
	searchhzjcb.get_searchhzjcb_list() # 30
	searchcgtz.get_searchcgtz_list() # 40
	searchjac.get_searchjac_lists() # 60

	searchhqb.getdynamic_searchhqb_list()
	searchxj.get_searchxj_list()
    

    #searchdy.get_searchdy_list()
    ##searchinw.getdynamic_searchinw_lists()
'''


    
