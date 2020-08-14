# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: runcase.py
@time: 2020/8/12 16:53
"""

import os
import time
import unittest
import HTMLTestRunner


def discover():
    '''获取需要执行的测试用例脚本'''
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),  # 执行测试用例的目录，当前类和执行测试用例在同目录
        pattern='test*.py',  # 这个是匹配脚本名称的规则
        top_level_dir=None)  # 这个是顶层目录的名称，一般默认等于None就行了
    return suite

def get_time():
    '''返回当前时间格式化信息'''
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    return now

def go_runner():
    '''定义测试报告，执行测试用例脚本'''
    # report_path = os.path.dirname(os.getcwd()) + '\\report\\' + get_time() + '_result.html'
    report_path = os.path.join(os.path.dirname(os.getcwd()), 'report', get_time() + '_result.html')
    with open(report_path, 'wb') as file:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=file,
            title='自动化测试报告',
            description='自动化测试报告详细信息')
        runner.run(discover())

if __name__ == '__main__':
    go_runner()



























