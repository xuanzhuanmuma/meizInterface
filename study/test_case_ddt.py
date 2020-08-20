# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: test_case_ddt.py
@time: 2020/8/20 16:33
"""
import unittest

import ddt

from util.handle_excel import excel_data

data = [['1', '2', '3'], ['11', '22', '33'], ['111', '222', '333']]
def get_all_data():
    return excel_data.get_excel_data()


@ddt.ddt
class TestCase01(unittest.TestCase):

    @ddt.data(*data)
    @unittest.skip
    def test_01(self, data1):
        num1, num2, num3 = data1
        print(num1, num2, num3)

    @ddt.data(*get_all_data())
    def test_02(self, data1):
        # 编号、作用、是否执行、前置条件、依赖的key、method、url、data、cookie操作、header操作、预期结果方式、预期结果、result、失败结果
        case_id, usage, is_run, condition, depend_key, method, url, request_data, cooker, header, expect_type, expect, result, result_data = data1
        
        print(data1)


if __name__ == '__main__':
    unittest.main()
