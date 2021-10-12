from apis.meta_info import get_all_stock_json, get_meta_info_json
from utils.connect import login
from apis.k_data import get_k_data_json
from flask import Flask, request

@login
def init():
    print('app init...')

init()
app = Flask(__name__)

@app.route('/get_k_data_json', methods=["POST"])
def _get_k_data_json():
    """
    查询k线数据(支持多股查询)
    """
    data = request.get_json()
    codes = None
    # 多股
    if 'codes' in data:
        codes = data['codes']
    # 单股
    else:
        codes = [data['code']]
    start = data['start']
    end = data['end']
    frequency = data['frequency'] if ('frequency' in data) else None
    res = {}
    for code in codes:
        res[code] = get_k_data_json(code, start, end, frequency)
    return res


@app.route('/get_all_stock_json/<date>', methods=["GET"])
def _get_all_stock_json(date):
    """
    获取指定日期json格式的所有股票元数据
    """
    return get_all_stock_json(date)

@app.route('/get_meta_info/<code>', methods=["GET"])
def _get_meta_info(code):
    """
    查询证券元信息
    """
    return get_meta_info_json(code)
