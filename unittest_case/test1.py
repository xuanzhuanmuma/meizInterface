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


class LoginCase1(unittest.TestCase):
    def test_3(self):
        print('ceshi 3')


    def test_4(self):
        print('ceshi 4')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [LoginCase1('test_1'), LoginCase1('test_2')]
    suite.addTests(tests)
    unittest.TextTestRunner().run(suite)




