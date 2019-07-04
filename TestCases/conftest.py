# -*- coding: utf-8 -*-
# @Time : 2019/7/2 19:00
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : confest.py
# @Software: PyCharm Community Edition
from selenium import webdriver
from PO_V8.TestDatas import Common_data as cd
from PO_V8.Operation.Basepage import BasePage
from PO_V8.PageLocators.Login_locator import LoginPageLocator as Loginloc
from PO_V8.PageLocators.Course_loactor import CoursePageLocator as Classloc
from PO_V8.PageLocators.Text_locator import TextPageLocator as Textloc
from PO_V8.Operation.LoginPage import LoginPage
import time
import pytest

@pytest.fixture(scope='class')
def open_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.web_login_url)
            # 1.1点击登录按钮
    BasePage(driver).click_element(Loginloc.login_img, '课堂派首页——点击登录图标 ')
            # 输入账号和密码
    LoginPage(driver).login(cd.user, cd.password)
            # 1.4点击登录
    BasePage(driver).click_element(Loginloc.login_button_loc, '登录页面——确定登录')
    yield driver
    driver.quit()
@pytest.fixture
def refresh_page(open_url):
    yield
    open_url.refresh()


# 选择进入班级
@pytest.fixture
def enter_class(open_url):
    BasePage(open_url).click_element(Classloc.enter_class, '班级选择页面——进入班级')
    # 返回课堂列表
@pytest.fixture
def exit_class_list(open_url):
    BasePage(open_url).click_element(Textloc.exit_class, '作业上传页面——返回班级')
    BasePage(open_url).click_element(Textloc.change, '班级页面——切换按钮')
    time.sleep(3)
    BasePage(open_url).click_element(Textloc.class_list, '切换页面——返回班级列表')
