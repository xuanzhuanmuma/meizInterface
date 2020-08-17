# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: handle_json.py
@time: 2020/8/14 16:46
"""
import json
import os

class HandleJson(object):
    def read_json(self, file_name=None):
        base_path = os.path.dirname(os.getcwd())
        if file_name is None:
            file_path = base_path + r'\config\user_data.json'
        else:
            file_path = base_path + '\\config\\' + file_name
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_value(self, key, file_name=None):
        data = self.read_json(file_name)
        return data.get(key)

    def write_value(self, file_name, data):
        base_path = os.path.dirname(os.getcwd())
        file_path = base_path + '\\config\\' + file_name
        with open(file_path, 'w') as file:
            file.write(json.dumps(data))

if __name__ == '__main__':
    data = {
        "app": {
            "ada": "adafds"
        }
    }
    HandleJson().write_value('cookie.json', data)
