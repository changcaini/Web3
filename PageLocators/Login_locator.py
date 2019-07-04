# -*- coding: utf-8 -*-
# @Time : 2019/6/23 10:03
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : login_page_locator.py
# @Software: PyCharm Community Edition
from selenium.webdriver.common.by import By
class LoginPageLocator:
    # 登录图标
    login_img=(By.XPATH,'//a[@class="login"]')
    # 用户名
    user_loc=(By.XPATH,'//input[@name="account"]')
    # 密码
    passwd_loc=(By.XPATH,'//input[@name="pass"]')
    # 登录按钮
    login_button_loc=(By.XPATH,'//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')
