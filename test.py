from apis.meta_info import query_all_stock
from loadData import update_all_stock_json
from utils.connect import login
from utils.io import getRealPathRelativeToFile

@login
def init():
    print('app init...')

init()
try:
    print('==test==')
    update_all_stock_json('2021-10-11')
except Exception as e:
    raise ValueError(e)