from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})  # This is to give our "front end access" to our API

df = pd.read_csv("../../../data/classification/imo.csv")

@app.route("/random", methods=['GET', 'POST'])
def get_random():
    n = request.args.get('n')
    contest_name = request.args.get('contest_name')
    year = request.args.get('year')
    label = request.args.get('label')
    
    result = {
        'n': n,
        'label': label,
        'contest_name': contest_name,
        'year': year,
    }
    return jsonify(result)

@app.route("/classify/classification/generate_example", methods=['GET', 'POST'])
def get_random_example_classification_problem():
    df_ = df.sample(1)
    df_ = df_.to_dict(orient='records')
    
    get = lambda col: df_[0][col] if type(df_[0][col]) == str else None
    result = {
        'no': get('no'),
        'contest_name': get('contest_name'),
        'year': get('year'),
        'link': get('link'),
        'pdf': get('pdf'),
        'post_rendered': get('post_rendered'),
        'post_canonical': get('post_canonical'),
        'label': get('label'),
    }
    return jsonify(result)
