# -*- coding: utf-8 -*-
# @Time : 2019/7/2 20:32
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : LoginPage.py
# @Software: PyCharm Community Edition
from PO_V8.Operation.Basepage import BasePage
from PO_V8.PageLocators.Login_locator import LoginPageLocator as Loginloc

class LoginPage(BasePage):
    def login(self, user, password):
        # 输入用户名
        self.input_text(Loginloc.user_loc, '登录——输入用户名', user)
        # 输入密码
        self.input_text(Loginloc.passwd_loc, '登录——输入密码', password)
        # 点击登录
        self.click_element(Loginloc.login_button_loc, '登录——登录按钮')