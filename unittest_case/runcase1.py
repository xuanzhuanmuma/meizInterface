# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: runcase.py
@time: 2020/8/12 16:53
"""

import os
import unittest

def allTests():
    '''获取需要执行的测试用例脚本'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),  # 待执行用例的目录
        pattern='test*.py',  # 获取所有以test开头的测试文件
        top_level_dir=None)
    return suite

def run():
    unittest.TextTestRunner(verbosity=2).run(allTests())

if __name__ == '__main__':
    run()


























