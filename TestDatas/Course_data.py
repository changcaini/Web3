# -*- coding: utf-8 -*-
# @Time : 2019/7/4 18:17
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : JoinClass_data.py
# @Software: PyCharm Community Edition
course_code1='4SX4VK'
course_code2='SRL7U3'
exit_sucess=[{'password':'ccn@2620','check':'课程退课成功'}]
exit_fail=[{'password':'ccn','check':'密码错误'}]

join_sucess=[{'course_code':'4SX4VK','check':'加入课堂成功'}]
join_fail=[{'course_code':'SRL7U3','check':'老师已经关闭加课'},
           {'course_code':'      ','check':'加课码不能为空'},
           {'course_code':'4SX','check':'加课验证码必须是6位字符'},
           {'course_code':'SRL7U6','check':'该加课码不存在或者已经失效'}]


if '__name__'=='main':
    mydict=exit_fail
    # type(mydict) == type({})             #检查不是字典
    # 如果是字典，再看看有没有这样的属性：
    # mydict.has_key('password')
    # print(exit_fail["password"])
    # print(exit_sucess["password"])
    # print(join_fail[0]["course_code"])
