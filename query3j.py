#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/10/23 22:10
"""

import searchjac
import searchcgtz
import searchhzjcb
import searchbym
import searchhqb
##import searchinw
import searchsx
import searchdy
import searchxj



if __name__=='__main__':
	#searchsx.getdynamic_searchsx_lists()
	searchbym.get_searchbym_list()
	searchhzjcb.get_searchhzjcb_list()
	searchjac.get_searchjac_lists() #searchjac.get_searchjac_debt_list()
	searchcgtz.get_searchcgtz_list()   
	searchhqb.getdynamic_searchhqb_list()
	searchxj.get_searchxj_list()
    #searchdy.get_searchdy_list()
    ##searchinw.getdynamic_searchinw_lists()
    
