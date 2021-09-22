from os import abort, path
import baostock as bs
import pandas as pd
from Utils.io import getRealPathRelativeToFile
from Utils.connect import login

@login
def query_history():
    # 获取数据
    res = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close",
    start_date='2017-07-01', end_date='2017-07-11',
    frequency="d", adjustflag="3")

    if res.error_code != '0':
        raise ValueError(res.error_msg)
    
    # 数据格式转换
    data_list = []
    while (res.error_code == '0') & res.next():
        data_list.append(res.get_row_data())
    data = pd.DataFrame(data_list, columns=res.fields)

    # 数据导出
    exportFile = getRealPathRelativeToFile(__file__, r'caches\history_k_data.json')
    data.to_json(exportFile, indent=2)

# main
if __name__ == '__main__':
    try:
        query_history()
    except Exception as e:
        print('=>', e, '<=')
    