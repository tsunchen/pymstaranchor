
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def get_cities(url):
    list_link_text = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print (response.status_code)
    #print (soup)
    # '#js-cities-pos > div.area-city-word > div.area-line.zb > a'
    # '#js-cities-pos > div.area-city-letter > div.area-line.A > a:nth-child(2)'
    #city_links = soup.select('#js-cities-pos > div.area-city-letter > div.area-line > a')
    #'#js-cities-pos > div.area-city-word > div.area-line.zb > a:nth-child(2)'
    city_links = soup.select('a.province-item')
    for city_link in city_links:
        #print (city_link)
        list_link_text.append(city_link.text)
    return (list_link_text)


def click_cities(lst,url):
    # 获取驱动
    path = "E:\\ProgramData\\Anaconda3\\chromedriver.exe"
    # 跳转网页
    for l in lst:
        driver = webdriver.Chrome(path)
        driver.get(url)
        print(driver.title)
        print(l)
        time.sleep(4)
        # 关闭右上角
        driver.find_element_by_xpath('//*[@id="common-header-wrapper"]/div/div[1]/div[3]').click()
        time.sleep(3)
        # '#div_city > a'
        menu_ele = driver.find_element_by_css_selector("#div_city > a")
        ActionChains(driver).move_to_element(menu_ele).perform()
        # 按钮事件触发
        sub_menu_ele = driver.find_element_by_partial_link_text(l)
        time.sleep(2)
        sub_menu_ele.click()
        driver.quit()

        #driver.find_element_by_link_text(l).click()




if __name__ == '__main__':
    url = 'https://www.renrenche.com/'
    ls_link_text = get_cities(url)
    print (ls_link_text)
    click_cities(ls_link_text,url)

