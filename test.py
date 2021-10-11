from apis.query_meta_info import query_all_stock
from utils.connect import login
from utils.io import getRealPathRelativeToFile

@login
def init():
    print('app init...')

def update_all_stock_json(date):
    """更新所有股票元数据到本地
    """
    query_all_stock(date).to_json(
        getRealPathRelativeToFile(__file__, '_caches/all_stock.json'),
        orient='records',
    )

init()
try:
    print('==test==')
    update_all_stock_json('2021-10-11')
except Exception as e:
    raise ValueError(e)