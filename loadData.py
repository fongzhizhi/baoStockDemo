from apis.k_data import query_k_data
from apis.meta_info import get_meta_info_json, query_all_stock, query_meta_info
from utils.connect import login
from utils.io import getRealPathRelativeToFile
import json

def update_all_stock_json(date):
    """更新所有股票元数据到本地(简版)
    """
    query_all_stock(date).to_json(
        getRealPathRelativeToFile(__file__, '_caches/all_stock.json'),
        orient='records',
    )

def update_all_stock_meta_json(date):
    """更新所有股票元数据到本地(详尽版)
    """
    df = query_all_stock(date)
    data_dict = {}
    index = 0
    for row in df.itertuples():
        code = getattr(row, 'code')
        print('runing....', index / 5000 * 100, '%')
        data_dict[code] = get_meta_info_json(code)
        index += 1
    filePath = getRealPathRelativeToFile(__file__, '_caches/all_stock_meta.json')
    out_file = open(filePath, "w")
    json.dump(data_dict, out_file) 
    out_file.close()
    

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
    # update_all_stock_json('2020-10-13')
    # get_all_stock_csv('sh.000001', '2020-10-1', '2021-10-1')
    update_all_stock_meta_json('2020-10-13')

run()