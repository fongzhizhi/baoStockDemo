import baostock as bs
from apis.common import queryResult_to_DataFrame

"""
k线查询相关api
"""
@queryResult_to_DataFrame(('open','close', 'high', 'low', 'preclose', 'volume', 'amount'))
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
    return bs.query_history_k_data_plus(code, ','.join(fields), start, end, frequency, adjustflag)

def get_k_data_json(code: str, start: str, end: str, frequency: str = 'd'):
    """获取json格式的K线数据
    """
    data = query_k_data(code, ('code', 'date', 'open', 'close', 'high', 'low'), start, end, frequency)
    return data.to_json(orient='records', double_precision = 2)