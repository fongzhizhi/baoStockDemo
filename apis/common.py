"""
公共方法
"""

import functools
from typing import Tuple
import pandas as pd

def queryResult_to_DataFrame(number_fields: Tuple = None):
    """查询数据转为 DataFrame 数据

        Args:
        queryFun 查询方法
        number_fields 需要转换为数字的列
    """
    def f(queryFun):
        @functools.wraps(queryFun)
        def formate(*args, **kwargs):
            #查询诗句
            query_data = queryFun(*args, **kwargs)
            # 数据校验
            if query_data is None:
                raise ValueError('Query data is None!')
            if query_data.error_code != '0':
                raise ValueError(query_data.error_msg)
            # 转换为 DataFrame
            data_list = []
            columns = query_data.fields
            # 记录需要转换为数字的项
            convert2FloatIndex = []
            if number_fields is not None:
                for i, v in enumerate(columns):
                    if v in number_fields:
                        convert2FloatIndex.append(i)
            
            while (query_data.error_code == '0') & query_data.next():
                row = query_data.get_row_data()
                for index in convert2FloatIndex:
                    try:
                        row[index] = float(row[index])
                    except Exception as e:
                        print(e, '=>', row[index])
                data_list.append(row)
            return pd.DataFrame(data_list, columns=columns)
        return formate
    return f