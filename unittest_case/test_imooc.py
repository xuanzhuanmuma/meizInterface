# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: test_imooc.py
@time: 2020/8/13 10:24
"""
import HTMLTestRunner
import os
import time
import unittest


class ImoocCase(unittest.TestCase):
    def test_banner(self):
        print('测试')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase('test_banner'))
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    report_name = os.path.dirname(os.getcwd()) + '\\report\\' + now + '_result.html'
    with open(report_name, 'wb') as file:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=file,
            verbosity=2,
            title='我的测试报告',
            description='测试结果如下'
        )
        runner.run(suite)
