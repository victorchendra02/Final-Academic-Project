from flask import Flask, request, jsonify
from flask_cors import CORS
import random

from db import *

app = Flask(__name__)
database_name = "aopsimol_artofproblemsolving"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@127.0.0.1/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, resources={r"*": {"origins": "*"}})  # This is to give our "front end access" to our API
db = SQLAlchemy(app)


@app.route("/algebra", methods=['GET'])
def get_all_algebra():
    result = SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Algebra', random=True, limit=1)
    return jsonify(result)
    
@app.route("/random", methods=['GET'])
def get_random():
    n = request.args.get('n')
    labels = request.args.get('label')
    
    n = max(1, min(int(n), 50))
    labels: list = labels.split(',')
    if len(labels) > n: labels = random.sample(labels, n)
    
    len_label = len(labels)
    mod = n % len_label
    
    dict_label = {
        'Algebra': None,
        'Combinatorics': None,
        'Geometry': None,
        'Number Theory': None,
    }
    if mod == 0 :
        for _ in labels:
            dict_label[_] = n//len_label
    else:
        for _ in labels:        
            dict_label[_] = n//len_label
        if mod > 1:
            copy_label = labels
            random.shuffle(copy_label)
            for i in range(mod):
                dict_label[copy_label[i]] += 1
        else:
            dict_label[random.choice(labels)] += mod
    
    result = []
    for selected_label in labels:
        if selected_label == 'Algebra':
            temp = SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Algebra', random=True, limit=dict_label['Algebra'])
            for _ in temp: result.append(_)
        elif selected_label == 'Combinatorics':
            temp = SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Combinatorics', random=True, limit=dict_label['Combinatorics'])
            for _ in temp: result.append(_)
        elif selected_label == 'Geometry':
            temp = SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Geometry', random=True, limit=dict_label['Geometry'])
            for _ in temp: result.append(_)
        elif selected_label == 'Number Theory':
            temp = SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Number Theory', random=True, limit=dict_label['Number Theory'])
            for _ in temp: result.append(_)
    
    random.shuffle(result)
    return jsonify(result)

@app.route("/classify/classification/generate_example", methods=['GET'])
def generate_single_random_example_problem_for_classification():
    result = SELECT_ALL_FROM_IMO(db, random=True, limit=1)
    return jsonify(result[0])

@app.route("/classify/regression/generate_example", methods=['GET'])
def generate_single_random_example_problem_for_regression():
    result = SELECT_ALL_FROM_IMO(db, random=True, limit=1)
    return jsonify(result[0])
