import baostock as bs
import pandas as pd

def query_k_data(code: str, fields: tuple, start: str = None, end: str = None, frequency: str="d", adjustflag: str='3'):
    """查询K线数据

    Args:
        code: 股票代码
        fields: 参数列表
            date: 交易日期
            code: 证券代码
            open: 开盘价
            close: 收盘价
            high: 最高价
            low: 最低价
            preclose: 前收盘价
            volume: 成交量(股)
            amount: 成交额(元)
            adjustflag: 复权状态
            turn: 换手率
            tradestatus: 交易状态(1: 正常 | 0: 停牌)
            pctChg: 涨跌幅(百分比)
            peTTM: 滚动市盈率
            pbMRQ: 市净率
            psTTM: 	滚动市销率
            pcfNcfTTM: 滚动市现率
            isST: 是否ST股，1是，0否
        start: 开始日期，为空时取2015-01-01
        end: 结束日期，为空时取最近交易日期
        frequency: k线类型。默认日k。d(日) | w(周) | m(月) | 5(5min) | 15(15min) | 30(30min) | 60(60min)
        adjustflag: 复权类型。默认不复权。1(后赋权) | 2(前复权) | 3(不复权)
    """
    # 获取数据
    k_data = bs.query_history_k_data_plus(code, ','.join(fields), start, end, frequency, adjustflag)
    if k_data is None:
        raise ValueError('Query data is None!')
    if k_data.error_code != '0':
        raise ValueError(k_data.error_msg)
    # 转换为 DataFrame
    data_list = []
    columns = k_data.fields
    # 记录需要转换为数字的项
    number_fields = ('open','close', 'high', 'low', 'preclose', 'volume', 'amount')
    convert2FloatIndex = []
    for i, v in enumerate(columns):
        if v in number_fields:
            convert2FloatIndex.append(i)
    
    
    while (k_data.error_code == '0') & k_data.next():
        row = k_data.get_row_data()
        for index in convert2FloatIndex:
            row[index] = float(row[index])
        data_list.append(row)
    return pd.DataFrame(data_list, columns=columns)