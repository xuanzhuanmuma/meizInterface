# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: handle_json.py
@time: 2020/8/14 16:46
"""
import json

class HandleJson(object):
    def read_json(self, file_path):
        with open(file_path) as file:
            data = json.load(file)
        return data

    def get_value(self, key):
        data = self.read_json()
        return data[key]