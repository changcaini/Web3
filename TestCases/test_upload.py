# -*- coding: utf-8 -*-
# @Time : 2019/7/2 21:16
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : test_upload.py
# @Software: PyCharm Community Edition
from PO_V8.Operation.upload_file import upload
from PO_V8.Operation.Basepage import BasePage
from PO_V8.PageLocators.Text_locator import TextPageLocator as Textloc
from PO_V8.TestDatas import Common_data as cd
import time
import pytest

@pytest.mark.usefixtures("open_url")
@pytest.mark.usefixtures("enter_class")
class TestUpload:
        @pytest.mark.upload
        def test_upload_Doc(self, open_url):
            # 选择作业
            BasePage(open_url).click_element(Textloc.text_loc, '作业页面——选择作业')
            # 更新提交
            BasePage(open_url).click_element(Textloc.update_button, '作业页面——更新作业')
            # 确定更新提交
            BasePage(open_url).click_element(Textloc.update_true, '作业页面——确定要更新 ')
            # 删除已提交的
            BasePage(open_url).click_element(Textloc.delete_upload, '作业页面——删除已提交')
            # 上传文件
            BasePage(open_url).click_element(Textloc.upload_doc, '作业页面——上传文件')
            # 选择本地文件上传
            time.sleep(5)
            file_path = "D:\Python15\class_web_20190601\ccnTestUploadFile.docx"
            upload(file_path)
            # # 点击更新提交
            time.sleep(5)
            BasePage(open_url).click_element(Textloc.upload_true, '作业页面——确定提交')

        # @pytest.mark.usefixtures("exit_class_list")
        @pytest.mark.discuss
        def test_discuss(self, open_url):
            BasePage(open_url).click_element(Textloc.discuss, '作业页面——讨论')
            BasePage(open_url).click_element(Textloc.leftMess_input, '作业讨论页面——点击留言框')
            BasePage(open_url).input_text(Textloc.leftMess, '作业讨论页面——输入留言内容',cd.leftMessage)
            BasePage(open_url).click_element(Textloc.send_true, '作业讨论页面——确定发送留言')

            # 查看作业状态
        def test_text_status(self,open_url):
            # BasePage(open_url).click_element(Textloc.exit_class, '作业上传页面——返回班级')
            status=BasePage(open_url).get_element_text(Textloc.text_status,'作业页面——查看作业状态')
            print("作业状态",status)









