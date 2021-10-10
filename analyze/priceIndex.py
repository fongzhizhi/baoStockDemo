"""
价格指数
价格指数是在股票投资中，以某个时期为基期，
以后各个时期股票平均价格同基期价格相比计算出的百分数。
反映股票价格水平变化的指数。
"""
from datasApi.query_k_data import query_k_data

def getPriceIndex(basePrice: float, nowPrice: float, format_str = '.2f'):
    """获取价格指数

    Args:
        basePrice: 基期价格
        nowPrice: 当前价格
        format_str: 格式转换码
    """
    return format(100 * (nowPrice / basePrice), format_str)

def getPriceIndexs(price_list: list, basePrice: float = None):
    """获取价格指数列表

    Args:
        price_list: 价格指数
    """
    basePrice = price_list[0] if basePrice is None else basePrice
    priceIndexs = []
    for price in price_list:
        priceIndexs.append(getPriceIndex(basePrice, price))
    return priceIndexs

def get_k_data_json(code: str, start: str, end: str):
    """获取json格式的K线数据
    """
    data = query_k_data(code, ('code', 'date', 'open', 'close', 'high', 'low'), start, end)
    return data.to_json(orient='records', double_precision = 2)