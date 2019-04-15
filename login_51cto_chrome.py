# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 获取驱动
path = "E:\\ProgramData\\Anaconda3\\chromedriver.exe"
driver = webdriver.Chrome(path)

# 跳转网页
driver.get("https://home.51cto.com/index")
print(driver.title)

# 睡眠时间
#sleep(2)
driver.implicitly_wait(5)

# 登录框
login_ele = driver.find_element_by_css_selector("#login-wechat > div.userPassLogin.back_account > a")

# 触发点击事件
ActionChains(driver).click(login_ele).perform()

# 查找输入框，输入帐号密码，输入框提前清理
driver.find_element_by_css_selector("#loginform-username").clear()
driver.find_element_by_css_selector("#loginform-username").send_keys("username")

driver.find_element_by_css_selector("#loginform-password").clear()
driver.find_element_by_css_selector("#loginform-password").send_keys("password")

# 查找登陆按钮并点击
button = driver.find_element_by_css_selector("#login-form > div.clearfix.zxfDl > input.loginbtn.fl")
button.click()

#sleep(1)
driver.implicitly_wait(5)

# 处理最上层弹框 body > div:nth-child(20) > a:nth-child(2)
driver.find_element_by_css_selector("body > div:nth-child(20) > a:nth-child(2)").click()

# hover事件#login_status > ul > li.hovercur > a
# community_element = driver.find_element_by_css_selector("#login_status > ul > li.hovercur > a")
# ActionChains(driver).move_to_element(community_element).perform()

# 验证登陆元素
# login_status > ul > li:nth-child(1) > a:nth-child(1)
# login_status > ul > li:nth-child(1) > a:nth-child(1) > strong
user_name_element = driver.find_element_by_css_selector("#login_status > ul > li:nth-child(1) > a:nth-child(1)")
print(user_name_element.text)
name = user_name_element.text
if u"TSUNx" == name:
    print("login okay")
else:
    print("login fail")

driver.quit()
