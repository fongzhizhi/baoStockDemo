from utils.connect import login
from analyze.priceIndex import get_k_data_json
from flask import Flask, request

@login
def init():
    print('init...')

init()
app = Flask(__name__)

@app.route('/get_k_data_json')
def user():
    data = request.get_json()
    code = data['code']
    start = data['start']
    end = data['end']
    res = get_k_data_json(code, start, end)
    return res