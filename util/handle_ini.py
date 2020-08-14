# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: handle_ini.py
@time: 2020/8/14 10:10
"""
import configparser
import os


class HandleIni(object):
    def __init__(self, file_name=None):
        if file_name is None:
            # 默认路径
            file_name = os.path.dirname(os.getcwd()) + r'\config\server.ini'
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf

    def get_value(self, node, key):
        try:
            data = self.cf.get(node, key)
        except Exception:
            print('没有获取到值')
            data = None
        return data
