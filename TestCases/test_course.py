# -*- coding: utf-8 -*-
# @Time : 2019/7/2 21:16
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : test_upload.py
# @Software: PyCharm Community Edition

from PO_V8.Operation.Basepage import BasePage
from PO_V8.PageLocators.Course_loactor import CoursePageLocator as Courseloc
from PO_V8.TestDatas import Course_data as Course_data
from PO_V8.Operation.CoursePage import CoursePage
import time
import pytest
@pytest.mark.usefixtures("open_url")
@pytest.mark.usefixtures("refresh_page")
class TestOperateCourse:
        # 1退出班级
        # 1.1退出班级——失败
        pytestmark = pytest.mark.course
        @pytest.mark.exit_wrong
        @pytest.mark.parametrize("data",Course_data.exit_fail)
        def test_exit_class_fail(self, open_url,data):
            # 点击课程操作列表
            time.sleep(3)
            BasePage(open_url).click_element(Courseloc.oper_list, '选择课程页面——操作列表')
            # 选择退课
            BasePage(open_url).click_element(Courseloc.exit_button, '选择课程页面——退课')
            # 输入登录密码退课
            BasePage(open_url).input_text(Courseloc.exit_code, '退课页面——输入登录密码',data["password"])
            # 确定退课
            BasePage(open_url).click_element(Courseloc.exit_true, '退课页面——退课')
            assert CoursePage(open_url).fail_tips()==data["check"]
        # 1.2退出班级——成功
        @pytest.mark.exit_success
        @pytest.mark.parametrize("data", Course_data.exit_sucess)
        def test_exit_class_success(self, open_url,data):
            # 点击课程操作列表
            time.sleep(3)
            BasePage(open_url).click_element(Courseloc.oper_list, '选择课程页面——操作列表')
            # 选择退课
            BasePage(open_url).click_element(Courseloc.exit_button, '选择课程页面——退课')
            # 输入登录密码退课
            BasePage(open_url).input_text(Courseloc.exit_code, '退课页面——输入邀请码',data["password"])
            # 确定退课
            BasePage(open_url).click_element(Courseloc.exit_true, '退课页面——退课')
            assert CoursePage(open_url).success_tips() == data["check"]

        # 加入班级——失败
        @pytest.mark.wrongJoin
        @pytest.mark.parametrize("data", Course_data.join_fail)
        def test_join_class_fail(self, open_url,data):
            #  点击加入课程
            BasePage(open_url).click_element(Courseloc.add_class, '选择课程页面——选择课程')
            # #输入课程邀请码 4SX4VK
            BasePage(open_url).input_text(Courseloc.input_code, '选择课程页面——输入邀请码',data["course_code"])
            # 点击加入
            BasePage(open_url).click_element(Courseloc.add_button, '选择课程页面——确定加入')
            assert CoursePage(open_url).fail_tips()==data["check"]


        # 加入班级——成功
        @pytest.mark.successJoin
        @pytest.mark.parametrize("data", Course_data.join_sucess)
        def test_join_class_success(self, open_url,data):
            #  点击加入课程
            BasePage(open_url).click_element(Courseloc.add_class, '选择课程页面——选择课程')
            # #输入课程邀请码 4SX4VK
            BasePage(open_url).input_text(Courseloc.input_code, '选择课程页面——输入邀请码', data["course_code"])
            # 点击加入
            BasePage(open_url).click_element(Courseloc.add_button, '选择课程页面——确定加入')
            assert CoursePage(open_url).success_tips()==data["check"]





