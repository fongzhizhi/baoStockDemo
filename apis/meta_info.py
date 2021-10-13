import baostock as bs
from apis.common import queryResult_to_DataFrame

"""
证券元信息查询相关api
"""

@queryResult_to_DataFrame()
def query_all_stock(date=None):
    """获取指定交易日期所有股票列表

    Args:
        date: 查询日期
    """
    if date is None:
        date = '2021-10-11'
    return bs.query_all_stock(date)

def get_all_stock_json(date=None):
    """获取json格式的所有股票数据
    """
    data = query_all_stock(date)
    return data.to_json(orient='records')


@queryResult_to_DataFrame()
def query_meta_info(code):
    """获取股票元数据

    Args:
        code: 股票代码
    """
    return bs.query_stock_basic(code)

def get_meta_info_json(code):
    """获取json格式的股票元数据
    """
    data = query_meta_info(code)
    return data.to_json(orient='records')