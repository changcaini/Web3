# -*- coding: utf-8 -*-
# @Time : 2019/7/4 19:06
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : course.py
# @Software: PyCharm Community Edition

from PO_V8.Operation.Basepage import BasePage
from PO_V8.PageLocators.Course_loactor import CoursePageLocator as Courseloc
class CoursePage(BasePage):
    def fail_tips(self):
        loc=Courseloc.fail_tips_loc
        self.wait_eleVisible(loc,'加课/退课失败提示')
        tips=self.get_element_text(loc,'加课/退课失败提示')
        return tips
    def success_tips(self):
        loc = Courseloc.success_tips_loc
        self.wait_eleVisible(loc,'加课/退课成功提示')
        tips=self.get_element_text(loc,'加课/退课成功提示')
        return tips


