from apis.k_data import query_k_data
from apis.meta_info import query_all_stock
from utils.connect import login
from utils.io import getRealPathRelativeToFile

def update_all_stock_json(date):
    """更新所有股票元数据到本地
    """
    query_all_stock(date).to_json(
        getRealPathRelativeToFile(__file__, '_caches/all_stock.json'),
        orient='records',
    )

def update_all_stock_csv(date):
    """更新所有股票元数据到本地
    """
    query_all_stock(date).to_csv(
        getRealPathRelativeToFile(__file__, '_caches/all_stock('+date+').csv'),
    )

def get_all_stock_csv(code, start, end, type='d'):
    tup = ('date', 'code', 'open', 'high', 'low', 'close', 'preclose', 'volume',
        'amount', 'adjustflag', 'turn', 'tradestatus', 'pctChg', 'peTTM', 'pbMRQ',
        'psTTM', 'pcfNcfTTM', 'isST')
    query_k_data(code, tup, start, end, type).to_csv(
        getRealPathRelativeToFile(__file__, '_caches/k_data_('+code+'['+start+', '+end+']).csv'),
    )

@login
def run():
    print('app run...')
    get_all_stock_csv('sh.000001', '2020-10-1', '2021-10-1')

run()