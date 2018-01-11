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
import searchinw
import searchsx
import searchdy



if __name__=='__main__':
    searchjac.get_searchjac_lists() #searchjac.get_searchjac_debt_list()
    searchcgtz.get_searchcgtz_list()
    searchhzjcb.get_searchhzjcb_list()
    searchbym.get_searchbym_list() 
    searchhqb.getdynamic_searchhqb_list()
    searchsx.getdynamic_searchsx_lists()
    searchinw.get_searchinw_list()
    searchinw.getdynamic_searchinw_list()
    searchdy.get_searchdy_list()
    
