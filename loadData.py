from apis.k_data import query_k_data
from apis.meta_info import get_meta_info_json, query_all_stock, query_meta_info
from utils.connect import login
from utils.io import getRealPathRelativeToFile
import json

def update_all_stock_json(date):
    """更新所有股票元数据到本地(简版)
    """
    query_all_stock(date).to_dict(
        getRealPathRelativeToFile(__file__, '_caches/all_stock.json'),
        orient='records',
    )

def update_all_stock_meta_json(date):
    """更新所有股票元数据到本地(详尽版)
    """
    df = query_all_stock(date)
    data_dict = {}
    index = 0
    total = len(df.index)
    for row in df.itertuples():
        code = getattr(row, 'code')
        print('runing....', index / total * 100, '%')
        data_dict[code] = get_meta_info_json(code)[0]
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

def get_all_stock_csv():
    k_type = 'm'
    tup = ('date', 'code', 'open', 'high', 'low', 'close', 'preclose', 'volume',
        'amount', 'adjustflag', 'turn', 'tradestatus', 'pctChg', 'peTTM', 'pbMRQ',
        'psTTM', 'pcfNcfTTM', 'isST') if k_type == 'd' else ('date', 'code', 'open', 'high', 'low', 'close', 'volume',
        'amount', 'adjustflag', 'turn', 'pctChg')
    start = '1990-1-1'
    end = '2021-10-1'

    lask_code = None
    goOn = lask_code is None

    jsonPath = getRealPathRelativeToFile(__file__, '_caches/all_stock.json')
    index = 0
    with open(jsonPath, encoding='utf8') as f:
        all_stock = json.load(f)
        total = len(all_stock)
        for item in all_stock:
            code = item['code']
            if goOn is False and code == lask_code:
                goOn = True
            elif goOn is not True:
                index += 1
                continue
            code_name = item['code_name'].replace('*', '')
            query_k_data(code, tup, start, end, k_type).to_csv(
                getRealPathRelativeToFile(__file__, '_caches/k_datas_'+ k_type +'/' + '_'.join((code, code_name)) + '.csv'),
            )
            index += 1
            print('runing....', index / total * 100, '% -->',code_name)

@login
def run():
    print('app run...')
    # update_all_stock_json('2021-10-13')
    # get_all_stock_csv()
    update_all_stock_meta_json('2021-10-13')

run()