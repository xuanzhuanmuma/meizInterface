# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: run_main.py
@time: 2020/8/14 10:05
"""
# {
#     'password': 'R7GzdFvuSCEYDoXKs3yicQ%3D%3D',
#     'devicetoken': '9YFTbxClWA%2FPoDd6FBhauO7XXocDtnO7USL3ladWhcJrr5O%2BLAA%2FNArpdgMVNTxf',
#     'signature': '6e33e8e833c9c468ab3cd133bac688b9',
#     'version': '1.0.1',
#     'timestamp': '1597375315',
#     'account': 'mqc',
#     'sessionId': '1597129901294HWNwQrHc',
#     'os': 'android'
# }

import requests
from deepdiff import DeepDiff
import json

from util.handle_excel import excel_data
from base.base_request import request
from util.handle_ini import HandleIni
from util.handle_json import HandleJson
base_url = HandleIni().get_value('server', 'host')


class RunMain(object):
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            # openpyxl行和类分别从1开始
            data = excel_data.get_row_value(i + 2)
            is_run = data[2]
            except_type = data[8]  # 预期结果方式
            except_result = data[9]  # 预期结果
            if is_run == 'yes':
                res = request.run_main(method=data[4], url=data[5],  data=data[6])
                if request.get_respose_code(res) == requests.codes.ok:
                    json_data = request.get_json_(res)
                    # 实际code和message
                    code = str(json_data['code'])
                    message = json_data['msg']
                    if except_type == 'code_message':
                        config_message = self.get_message_with_code(data[5], code)
                        if message == config_message:
                            excel_data.excel_write_data(i + 2, 11, '成功')
                            print('测试通过')
                        else:
                            excel_data.excel_write_data(i + 2, 11, '失败')
                            excel_data.excel_write_data(i + 2, 12, json.dumps(json_data))
                            print('测试失败')
                    if except_type == 'code':
                        if except_result == code:
                            print('测试通过')
                        else:
                            print('测试失败')
                    if except_type == 'message':
                        if except_result == message:
                            print('测试通过')
                        else:
                            print('测试失败')
                    if except_result == 'json':
                        # 项目中判断两个json发生变化，前提安装pip install deepdiff
                        if code == 1000:
                            status_str = 'success'
                        else:
                            status_str = 'error'
                        except_result_json = self.get_json_result(data[5], status_str)
                        result = self.handle_result_json(res, except_result_json)
                        if result:
                            print('测试通过')
                        else:
                            print('测试失败')
                else:
                    print('服务器有误')

    def handle_result_json(self, exception_dict, result_dict):
        '''校验格式'''
        if isinstance(exception_dict) and isinstance(result_dict):
            cmp_dict = DeepDiff(exception_dict, result_dict, ignore_order=True).to_dict()
            print(cmp_dict)
            if cmp_dict.get('dictionary_item_added') or cmp_dict.get('dictionary_item_removed'):
                print('case 失败')
                return False
            else:
                print('case通过')
                return True
        else:
            return False

    def get_json_result(self, url, status):
        data = self.get_json_value(url)
        if data is not None:
            for i in data:
                message = i.get(status)
                if message:
                    return message
        return None

    def get_json_values(self):
        data = HandleJson().read_json('user_data.json')
        return data

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
    RunMain().run_case()
    # print(RunMain().get_message_with_code('api3/getbannerImage', '1001'))
    # RunMain().handle_result_json()
