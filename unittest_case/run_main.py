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

from util.handle_excel import excel_data
from base.base_request import request
from util.handle_ini import HandleIni
from util.handle_json import HandleJson
base_url = HandleIni().get_value('server', 'host')


class RunMain(object):
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_row_value(i + 2)
            is_run = data[2]
            if is_run == 'yes':
                res = request.run_main(data[4], data[5], data[6])
                print(request.get_text(res))
                print(request.get_content(res))
                print(request.get_json_(res))
                print(request.get_respost_encoding(res))
                print(request.get_respose_code(res) == requests.codes.ok)
                print(request.get_respost_head(res))
                if request.get_respose_code(res) == requests.codes.ok:
                    json_data = request.get_json_(res)
                    print(json_data['code'])
                else:
                    print('服务器有误')

    def get_json_values(self):
        data = HandleJson().read_json('user_data.json')
        return data

    def get_json_value(self, url):
        data = HandleJson().get_value(url, 'user_data.json')
        return data

    def get_message_with_code(self, url, code):
        data = self.get_json_value(url)
        for i in data:
            message = i.get(code)
            # TODO

if __name__ == '__main__':
    # RunMain().run_case()
    print(RunMain().get_message_with_code('api3/getbannerImage', ))
