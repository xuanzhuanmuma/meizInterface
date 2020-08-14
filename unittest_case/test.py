# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: test.py
@time: 2020/8/10 17:11
"""
import requests
import hashlib
import json
import unittest
from base.base_request import request

host = 'http://www.imooc.com'
data = {
    'username': '111',
    'password': '1234'
}
class LoginCase(unittest.TestCase):

    def test_2(self):
        # 如果满足给定条件，那么就跳过当前case
        request.run_main('get', host, data)
        print('ceshi 2')

    @unittest.skipIf(host != 'https://www.imooc.com', '暂时不执行')
    def test_1(self):
        print('ceshi 1')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginCase('test_1'))
    suite.addTest(LoginCase('test_2'))
    unittest.TextTestRunner().run(suite)




