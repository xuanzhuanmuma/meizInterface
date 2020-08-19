# coding=utf-8
# author yanNa
# Data: 2020/8/19 21:13
'''前置条件判断'''
from util.handle_excel import HandleExcel
from jsonpath_rw import parse

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

    def get_depend_data(self, data, index):
        result_data = self.depend_data(data, index)
        matching_rule = self.split_data(data)[1]
        # data.banner.id
        json_exe = parse(matching_rule)
        print(result_data, '============', json_exe)
        madle = json_exe.find(result_data)
        print('------------', madle)
        for math in madle:
            print(math.value)

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
    # print(ConditionData().depend_data('1 > data.banner.id', 13))
    ConditionData().get_depend_data('1 > code', 13)



