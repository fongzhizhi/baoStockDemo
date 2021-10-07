from utils.connect import login
from analyze.priceIndex import get_k_data_json
from flask import Flask, request

@login
def init():
    print('init...')

init()
app = Flask(__name__)

@app.route('/get_k_data_json', methods=["POST"])
def user():
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
    res = {}
    for code in codes:
        res[code] = get_k_data_json(code, start, end)
    return res