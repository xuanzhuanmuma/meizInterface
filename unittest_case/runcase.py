# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: runcase.py
@time: 2020/8/12 16:53
"""

import unittest

from unittest_case.test import LoginCase
from unittest_case.test1 import LoginCase1


def simple_run():
    case1 = unittest.TestLoader().loadTestsFromTestCase(LoginCase)
    case2 = unittest.TestLoader().loadTestsFromTestCase(LoginCase1)
    suites = unittest.TestSuite([case1, case2])
    unittest.TextTestRunner().run(suites)




























