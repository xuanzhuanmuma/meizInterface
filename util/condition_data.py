# coding=utf-8
# author yanNa
# Data: 2020/8/19 21:13
'''前置条件判断'''
from util.handle_excel import HandleExcel
from jsonpath_rw import parse
import json

class ConditionData(object):
    def split_data(self, data):
        # 1 > data.banner.id
        case_id = data.split('>')[0].strip()
        rule_data = data.split('>')[1].strip()
        return case_id, rule_data

    def depend_data(self, data, index):
        '''根据前置条件中的编号，获取依赖数据'''
        case_id = self.split_data(data)[0]
        handle_excel = HandleExcel()
        row_num = handle_excel.get_row_number(case_id)
        # row_values = handle_excel.get_row_values(row_num)
        value = handle_excel.get_cell_value(row_num, index)
        return value

    def get_depend_data(self, result_data, matching_rule):
        '''获取依赖字段'''
        json_exe = parse(matching_rule)
        madle = json_exe.find(result_data)
        print('返回结果：', result_data)
        print('匹配条件：', matching_rule)
        return [math.value for math in madle]

    def get_data(self, data, index):
        # data.bizId
        # result_data = {
        # "code": 200,
        # "msg": "success",
        # "data": {
        #             "bizId": "28ed792b15be407a9fef260fb57e437f",
        #             "procInsId": "8e794944d85445859271ae92f40c6701",
        #             "nodeId": "7393db094e5c48fb8823f4a1875438d7",
        #             "workId": "1b4d9a1df3024971b805a1a6bcb50946"
        #      }
        # }
        # matching_rule = 'data.bizId'
        # result_data = eval(self.depend_data(data, index))
        result_data = json.loads(self.depend_data(data, index))
        matching_rule = self.split_data(data)[1]
        return self.get_depend_data(result_data, matching_rule)

'''
def get_row_num(key, id):
    # 根据id编号获取行号
    num = -1
    lists = HandleExcel().get_colums_value(key)
    for i in range(len(lists)):
        if str(lists[i]) == id:
            num = i + 1
    return num
'''

if __name__ == '__main__':
    print(ConditionData().get_data("1 > code", 14))



