# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: run_ddt.py
@time: 2020/8/20 17:20
"""
import requests
from deepdiff import DeepDiff
import json
import time
import unittest
import ddt

from util.handle_excel import excel_data
from base.base_request import request
from util.handle_ini import HandleIni
from util.handle_json import HandleJson
from util.handle_cookie import HandleCookie
from util.handler_header import HandleHeader
from util.condition_data import ConditionData
base_url = HandleIni().get_value('server', 'host')
all_data = excel_data.get_excel_data()


@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*all_data)
    def test_main_case(self, data):
        cookie = None
        get_cookie = None
        headers = None
        depend_result = None
        case_id = data[0]
        is_run = data[2]
        line_num = excel_data.get_row_number(case_id)
        if is_run == 'yes':
            is_depend = data[3]  # 前置条件(包括caseid和规则，如1>code)
            if is_depend is not None:
                '''获取依赖数据'''
                depend_result = ConditionData().get_data(is_depend, len(data))
                '''替换当前数据行中的数据为依赖数据'''
                depend_key = data[4]
                json.loads(data[7])[depend_key] = depend_result
            method = data[5]
            url = data[6]
            request_data = data[7]
            cookie_method = data[8]  # cookie操作
            is_header = data[9]  # header操作
            except_type = data[10]  # 预期结果方式
            except_result = data[11]  # 预期结果
            if cookie_method == 'yes':
                cookie = HandleCookie().get_cookie_value('app')
            if cookie_method == 'write':
                '''必须是获取到cookie'''
                get_cookie = {'is_cookie': 'app'}
            if is_header == 'yes':
                headers = HandleHeader().get_header()
            res = request.run_main(method, url, request_data, headers=headers, cookie=cookie, get_cookie=get_cookie)
            if request.get_respose_code(res) == requests.codes.ok:
                json_data = request.get_json_(res)
                # 实际code和message,跟需求写以下条件
                code = str(json_data['code'])
                message = json_data['msg']
                if except_type == 'code_message':
                    config_message = self.get_message_with_code(url, code)
                    if message == config_message:
                        excel_data.excel_write_data(line_num, 13, '成功')
                        print('测试通过')
                    else:
                        excel_data.excel_write_data(line_num, 13, '失败')
                        excel_data.excel_write_data(line_num, 14, json.dumps(json_data))
                        print('测试失败')
                if except_type == 'code':
                    # if except_result == code:
                    #     print('测试通过')
                    # else:
                    #     print('测试失败')
                    self.assertEqual(except_result, code)
                if except_type == 'message':
                    # if except_result == message:
                    #     print('测试通过')
                    # else:
                    #     print('测试失败')
                    self.assertEqual(except_result, message)
                if except_result == 'json':
                    # 项目中判断两个json发生变化，前提安装pip install deepdiff
                    if code == 1000:
                        status_str = 'success'
                    else:
                        status_str = 'error'
                    except_result_json = self.get_json_result(url, status_str)
                    result = self.handle_result_json(res, except_result_json)
                    if result:
                        print('测试通过')
                    else:
                        print('测试失败')
            else:
                print('服务器有误')

    def get_json_result(self, url, status):
        data = self.get_json_value(url)
        if data is not None:
            for i in data:
                message = i.get(status)
                if message:
                    return message
        return None

    def get_json_value(self, url):
        data = HandleJson().get_value(url, 'user_data.json')
        return data

    def get_message_with_code(self, url, code):
        data = self.get_json_value(url)
        if data is not None:
            for i in data:
                message = i.get(code)
                if message:
                    return message
        return None

if __name__ == '__main__':
    unittest.main()
