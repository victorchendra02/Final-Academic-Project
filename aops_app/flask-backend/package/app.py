import random
import numpy as np

from flask_cors import CORS
from flask import (Flask, jsonify, request)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

import sql_executer
from utils import load_pkl, get_current_time
from http_status_code import *

"""
Admin
    1. victorchendra, 1234abcd, Victor Chendra
    2. rickytheising, abcd1234, Ricky The Ising
    2. jacobjeshurunwarouw, jacobpassword, Jacob Jeshurun Warouw
"""
TOKEN_LIFETIME = timedelta(minutes=60)
DATABASE_NAME = "aopsimol_artofproblemsolving"
SECRET_KEY = "e23d7c4c7d545bff40817a7c28351544e14397aa6c72096a1405474c97dfd39ac11bdd31a6b25a31"
BLACKLIST_TOKEN = set()


# http://127.0.0.1:5000/

app = Flask(__name__)

app.config["JWT_SECRET_KEY"]  = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@127.0.0.1/{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, resources={r"*": {"origins": "*"}})  # This is to give our "front end access" to our API

db = SQLAlchemy(app)
jwt = JWTManager(app)


SVCvectorizer = load_pkl("../../../models/saved_models/classification/SupportVectorMechine/vectorizer.pkl")
SVCmodel = load_pkl("../../../models/saved_models/classification/SupportVectorMechine/model.pkl")

MNBvectorizer = load_pkl("../../../models/saved_models/classification/MultinomialNB/vectorizer.pkl")
MNBmodel = load_pkl("../../../models/saved_models/classification/MultinomialNB/model.pkl")


# -------------------- Home --------------------
def api_for_home_page():
    ...


# -------------------- QuestionBank --------------------
def api_for_questionbank_page():
    ...


# -------------------- Random --------------------
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
            temp = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Algebra', random=True, limit=dict_label['Algebra'])
            for _ in temp: result.append(_)
        elif selected_label == 'Combinatorics':
            temp = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Combinatorics', random=True, limit=dict_label['Combinatorics'])
            for _ in temp: result.append(_)
        elif selected_label == 'Geometry':
            temp = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Geometry', random=True, limit=dict_label['Geometry'])
            for _ in temp: result.append(_)
        elif selected_label == 'Number Theory':
            temp = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, 'Number Theory', random=True, limit=dict_label['Number Theory'])
            for _ in temp: result.append(_)
    
    random.shuffle(result)
    return jsonify(result)


# -------------------- Classification --------------------
@app.route("/classify/classification", methods=['GET'])
def predict_model_classification():
    text_problem = request.args.get('problem')
    
    tranformed_text = SVCvectorizer.transform(np.array([text_problem]))
    proba_result = SVCmodel.predict_proba(tranformed_text)[0]
    result = {
        'Algebra': proba_result[0], 
        'Combinatorics': proba_result[1], 
        'Geometry': proba_result[2], 
        'Number Theory': proba_result[3]
        }
    
    return jsonify(result)

@app.route("/classify/classification/generate_example", methods=['GET'])
def generate_single_random_example_problem_for_classification():
    result = sql_executer.SELECT_ALL_FROM_IMO(db, random=True, limit=1)
    return jsonify(result[0])


# -------------------- Regression --------------------
@app.route("/classify/regression/generate_example", methods=['GET'])
def generate_single_random_example_problem_for_regression():
    result = sql_executer.SELECT_ALL_FROM_IMO(db, random=True, limit=1)
    return jsonify(result[0])


# -------------------- About --------------------
def api_for_about_page():
    ...


# -------------------- Admin --------------------
@app.route("/admin/login", methods=['POST'])
def admin_login():
    # http://127.0.0.1:5000/admin/login
    
    data = request.json
    if len(data.keys()) > 2: return jsonify({'message': 'Wrong HTTP body!', 'status': False}), HTTP_400_BAD_REQUEST
    
    try:
        username = data.get('username').strip()
    except:
        return jsonify({'message': 'MISSING_USERNAME', 'status': False}), HTTP_400_BAD_REQUEST
    try:
        password = data.get('password').strip()
    except:
        return jsonify({'message': 'MISSING_PASSWORD', 'status': False}), HTTP_400_BAD_REQUEST
    
    username_exist: bool = sql_executer.is_username_exist_in_table_admins(db, username)
    if username_exist:
        fetched_pass: str = sql_executer.get_admin_password_by_username(db, username)
        password_match = check_password_hash(fetched_pass, password)
        
        if password_match:
            token = create_access_token(identity=username, expires_delta=TOKEN_LIFETIME)
            return jsonify({'message': 'PASSWORD_MATCH', 'status': HTTP_200_OK, 'token': token, 'username': username}), HTTP_200_OK
        else:
            return jsonify({'message': 'WRONG_PASSWORD', 'status': HTTP_401_UNAUTHORIZED}), HTTP_401_UNAUTHORIZED
    else:
        return jsonify({'message': 'NO_SUCH_USERNAME', 'status': HTTP_404_NOT_FOUND}), HTTP_404_NOT_FOUND
    
@app.route("/admin/logout", methods=['POST'])
@jwt_required()
def admin_logout():
    token: str = request.headers.get("Authorization") # "Bearer eyJhbGciOiJ..."
    BLACKLIST_TOKEN.add(token)
    return jsonify({'message': 'Logout successful', 'status': True}), HTTP_200_OK

@app.route("/admin/is_authorized", methods=['GET'])
@jwt_required()
def is_authorized():
    current_user = get_jwt_identity()
    
    if request.headers.get("Authorization") in BLACKLIST_TOKEN:
        return jsonify({"message": 'Token invalid'}), HTTP_401_UNAUTHORIZED
    
    return jsonify({"message": 'Token still valid'}), HTTP_200_OK


# @app.route("/admin/add_new_admin", methods=['GET'])
def add_new_admin():
    username =  "jacobjeshurunwarouw"
    password =  generate_password_hash("jacobpassword")
    full_name =  "Jacob Jeshurun Warouw"
    description =  "This is the third admin"

    username_already_exist = sql_executer.is_username_exist_in_table_admins(db, username)
    if username_already_exist:
        print("Username already taken!")
    else:
        print("Username is UNIQUE!")
        insert_new_admin_success = sql_executer.insert_new_admin_into_table_admins(db, username, password, full_name, description)
        if insert_new_admin_success:
            print("New admin has been added!")
        else:
            print("Fail to add new admin!")

    return jsonify({"Testing": True})


