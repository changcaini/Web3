# -*- coding: utf-8 -*-
# @Time : 2019/7/4 17:46
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : Send_mess_locator.py
# @Software: PyCharm Community Edition
from selenium.webdriver.common.by import By
class ReplyMessageLocator:
# 4、点击同学：
    students_button = (By.XPATH,'//a[@href="/StudentsV2/index/courseid/MDAwMDAwMDAwMLOsvZeIuauv.html"]')
    # 点击全部学生：
    all_students= (By.XPATH, '//li[@class="all"]')
    # 4.1点击学生账号
    student=(By.XPATH,'//p[@title="1502"]')
    # 4.2点击回复按钮
    reply_button=(By.XPATH,'//li[@data-id="MDAwMDAwMDAwMLOGz5SGz6tqhdtyoQ"]/a')
    #4.3输入回复内容
    reply_mess =(By.XPATH,'//*[@id="dvm"]/div[3]/textarea')
    #4.6点击确定按钮://a[@class="btn btn-positive disabled"]
    reply_true=(By.XPATH,'//*[@id="dvm"]/div[3]/div[2]/a')