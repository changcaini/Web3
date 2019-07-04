# -*- coding: utf-8 -*-
# @Time : 2019/7/2 19:33
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : Class_loactor.py
# @Software: PyCharm Community Edition
from selenium.webdriver.common.by import By
class CoursePageLocator:
# 点击加入课程
    add_class = (By.XPATH, '/html/body/div[3]/div[1]/div[1]')
    # 输入课程邀请码 4SX4VK
    input_code = (By.XPATH, '/html/body/div[6]/div[2]/input')
    # 点击加入
    add_button = (By.XPATH, '/html/body/div[6]/div[3]/ul/li[2]/a')
    # 退出课程操作列表
    oper_list= (By.XPATH, '//a[@class="kdmore"][1]')
    # 退出课程
    exit_button = (By.XPATH, '//*[@id="viewer-container-lists"]/dl[1]/dt/ul/li[2]/a')
   # 退课码
    exit_code=(By.XPATH, '//input[@type="password"]')
   # 确定退课
    exit_true=(By.XPATH,'//li[@class="dli2"]/a')
    # 选择进入班级
    enter_class = (By.XPATH, '//*[@id="viewer-container-lists"]/dl[1]/dt/strong/a')
    # 加课失败 提示
    fail_tips_loc=(By.XPATH,'//div[@id="error-tip"]/span')
   # 加课成功提示
    success_tips_loc=(By.XPATH,'//div[@id="show-tip"]/span')

