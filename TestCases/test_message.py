# -*- coding: utf-8 -*-
# @Time : 2019/7/4 17:44
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : test_message.py
# @Software: PyCharm Community Edition
# 私信
from PO_V8.Operation.Basepage import BasePage
from PO_V8.PageLocators.Send_mess_locator import ReplyMessageLocator as Replyloc
import time
import pytest

@pytest.mark.usefixtures("open_url")
@pytest.mark.usefixtures("enter_class")
class TestSendMessage:
    @pytest.mark.send
    def test_send_student(self, open_url):
        time.sleep(2)
        BasePage(open_url).click_element(Replyloc.students_button, '作业页面——同学按钮')
        BasePage(open_url).click_element(Replyloc.all_students, '作业页面——全部学生')
        # 4.1点击学生账号
        BasePage(open_url).click_element(Replyloc.student, '同学列表页面——选择学生')
        # 4.2点击回复按钮
        BasePage(open_url).click_element(Replyloc.reply_button, '同学列表页面——回复')
        #4.3输入回复内容
        BasePage(open_url).input_text(Replyloc.reply_mess,'同学列表页面——回复内容',"ccn test")
        #4.6点击确定按钮://a[@class="btn btn-positive disabled"]
        BasePage(open_url).click_element(Replyloc.reply_true, '同学列表页面——确定回复')
