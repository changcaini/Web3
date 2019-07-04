# -*- coding: utf-8 -*-
# @Time : 2019/6/23 10:03
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : login_page_locator.py
# @Software: PyCharm Community Edition
from selenium.webdriver.common.by import By
class TextPageLocator:
    # 作业上传
    # 选择上传作业
    text_loc=(By.XPATH,'//*[@id="homework-page"]/div[2]/div/div/div/div[2]/div[2]/a')
    # 更新提交
    update_button=(By.XPATH,'//*[@id="viewer-handup"]/div[1]/div[1]/a[2]')
    # 确定更新提交
    update_true=(By.XPATH,'//*[@id="update-pop"]/div[2]/a[2]')

    # 删除已提交的
    delete_upload=(By.XPATH,'//*[@id="viewer-handup"]/div[2]/div[1]/ul/li/div/a')
    # 上传文件
    upload_doc=(By.XPATH,'//*[@id="viewer-handup"]/div[1]/div[1]/a[1]')
    #选择本地文件上传
    file_path=(By.XPATH,"D:\Python15\class_web_20190601\ccnTestUploadFile.docx")
    # # 点击更新提交
    upload_true=(By.XPATH,'//*[@id="viewer-handup"]/div[1]/div[1]/a[3]')
    # 关闭提示
    know=(By.XPATH,'//a[@class="weui_btn_dialog primary"]')
    # 返回上级
    exit_class=(By.XPATH,'//a[@id="return-course"]')
    # 切换
    change=(By.XPATH,'//img[@src="/Public/Common/img/ktp1_09.png"]')
    # 返回课堂列表
    class_list=(By.XPATH,'//a[@class="leftnavclass"]')
    # 作业状态
    text_status=(By.XPATH,'//a[@class="view-work"]')

    # 讨论
    discuss=(By.XPATH,'//a[@href="/Discuss/index/homeworkid/MDAwMDAwMDAwMLSGx5eG36to.html"]')
    # 留言输入框
    leftMess_input=(By.XPATH,'//div[@class="input-click clearfix"]')
    # 留言内容
    leftMess=(By.XPATH,'//textarea[@class="comment-txt"]')
    # 确定发送留言
    send_true=(By.XPATH,'//a[@class="sure active"]')