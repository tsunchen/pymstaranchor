# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 获取驱动
path = "E:\\ProgramData\\Anaconda3\\chromedriver.exe"
driver = webdriver.Chrome(path)

# 跳转网页
driver.get("https://home.51cto.com/index")
print(driver.title)

# 睡眠时间
driver.implicitly_wait(4)

# 登录框
login_ele = driver.find_element_by_css_selector("#login-wechat > div.userPassLogin.back_account > a")
# 触发点击事件
ActionChains(driver).click(login_ele).perform()


# 查找输入框，输入帐号密码，输入框提前清理
try:
    logpassword = WebDriverWait(driver, 4, 0.1).until(EC.presence_of_element_located((By.ID, "loginform-password")))
    logpassword.clear()
    logpassword.send_keys("")
    print ("password资源加载成功")
except:
    print ("password资源加载失败，发送告警邮件或短信")
finally:
    print ("无论是否加载成功，都将响应用于password资源清理")

try:
    #logform-username
    logusername = WebDriverWait(driver, 5 ,0.5).until(EC.presence_of_element_located((By.ID, "loginform-username")))
    logusername.clear()
    logusername.send_keys("")
    print ("username资源加载成功")
except:
    print("username资源加载失败，发送告警邮件或短信")
finally:
    print("无论是否加载成功，都将响应用于username资源清理")


# 查找登陆按钮并点击
button = driver.find_element_by_css_selector("#login-form > div.clearfix.zxfDl > input.loginbtn.fl")
button.click()

#
driver.implicitly_wait(4)

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
    print("login pass")
else:
    print("login fail")

driver.quit()
