# to disable TF warning log  
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import random
import numpy as np
import tensorflow as tf
import tensorflow_text as text  # import this to able load saved BERT tfhub model
from transformers import BertTokenizer
# import requests

# flask
from flask_cors import CORS
from flask import (Flask, jsonify, request)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# time - date
from datetime import timedelta
from utils import get_current_date
# from utils import get_current_datetime
from utils import discretize
from time import perf_counter

# database
from flask_sqlalchemy import SQLAlchemy
import sql_executer

# utils
from utils import load_pkl
from http_status_code import *


"""
Admin
    1. victorchendra, 1234abcd, Victor Chendra
    2. rickytheising, abcd1234, Ricky The Ising
    2. jacobjeshurunwarouw, jacobpassword, Jacob Jeshurun Warouw
"""
TOKEN_LIFETIME = timedelta(minutes=60)
HOME_DATA_LIFETIME = timedelta(days=1)
DATABASE_NAME = "aopsimol_artofproblemsolving"
SECRET_KEY = "SMxfWjTMu1bRLS67GseJiGWLuIogM3oVTQ"
BLACKLIST_TOKEN = set()

# http://127.0.0.1:5000/

app = Flask(__name__)

app.config["JWT_SECRET_KEY"]  = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@127.0.0.1/{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, resources={r"*": {"origins": "*"}})  # This is to give our "front end access" to our API

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Load MathBERT
# """
# IMPORTANT NOTE: 
#     if there exist more than 1 ACTIVE regression model (EXPECTING ONLY MATHBERT FOR REGRESSION, 
#     BUT MAY CONTAIN MANY VERSION OF MATHBERT) it will only take the first occurence of active model in DB
# """
# mathbert_table: dict = sql_executer.utils_get_active_regression_model_all_column_from_models(DATABASE_NAME)[0]
# MathBERTTokenizerpath = mathbert_table['vectorizer_or_tokenizer_path']
# custom_objectspath = mathbert_table['custom_objects_path']
# MathBERTpath = mathbert_table['model_path']
# start = perf_counter()
# print("Loading MathBERT...")
# tokenizer = BertTokenizer.from_pretrained(MathBERTTokenizerpath, output_hidden_states=True)
# custom_objects = load_pkl(custom_objectspath)
# MathBERT = tf.keras.models.load_model(MathBERTpath, custom_objects=custom_objects)
# print("DONE!")
# print("MathBERT loaded!")
# print(f"{perf_counter()-start:.2f}s\n")

# -------------------- Home --------------------
@app.route("/home/home_data", methods=['GET'])
def api_for_home_page():
    def _insert_home_data(current_date):
        new_expire_date = current_date + HOME_DATA_LIFETIME
        
        algebra_problem = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, label="Algebra", random=True, limit=1)
        combin_problem = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, label="Combinatorics", random=True, limit=1)
        geomet_problem = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, label="Geometry", random=True, limit=1)
        nt_problem = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, label="Number Theory", random=True, limit=1)

        current_date_str = current_date.strftime('%Y%m%d')
        temps = [f"A{current_date_str}", f"C{current_date_str}", f"G{current_date_str}", f"NT{current_date_str}"]
        problems_combined = [algebra_problem[0], combin_problem[0], geomet_problem[0], nt_problem[0]]

        for i in range(4):
            data = {
                'id_home_data': temps[i],
                'id_key': problems_combined[i]['id_key'],
                'no': problems_combined[i]['no'],
                'contest_category': problems_combined[i]['contest_category'],
                'contest_name': problems_combined[i]['contest_name'],
                'year': problems_combined[i]['year'],
                'link': problems_combined[i]['link'],
                'pdf': problems_combined[i]['pdf'],
                'post_rendered': problems_combined[i]['post_rendered'],
                'post_canonical': problems_combined[i]['post_canonical'],
                'label': problems_combined[i]['label'],
                'day_created': current_date.strftime("%A"),
                'created_at': current_date,
                'expire_day': new_expire_date.strftime("%A"),
                'expire_on': new_expire_date,
            }
            status1 = sql_executer.INSERT_ROW_TO_TABLE_HOME_DATA(db, data)
            if status1 == False:
                status2 = sql_executer.DELETE_ALL_FROM_HOME_DATA(db)
                if status2 == False:
                    return "ERROR_WHILE_INSERT_AND_DELETE"
                return "ERROR_WHILE_INSERT"
            
        return "SUCCESS"

    current_date = get_current_date()
    current_table_home_data = sql_executer.SELECT_ALL_FROM_HOME_DATA(db)
    
    if len(current_table_home_data) != 4:
        print("=> current_table_home_data == != 4")

        if len(current_table_home_data) != 0:
            print("=> current_table_home_data != 0")
            stat = sql_executer.DELETE_ALL_FROM_HOME_DATA(db)
            if stat == False:
                return jsonify({"mgs": "Something is wrong. Back-end Error. Trying to clear table `home_data`"}), HTTP_500_INTERNAL_SERVER_ERROR
        
        status2 = _insert_home_data(current_date)
        if status2 == "SUCCESS":
            new_home_data = sql_executer.SELECT_ALL_FROM_HOME_DATA(db)
            return jsonify(new_home_data), HTTP_200_OK
        
        if status2 == "ERROR_WHILE_INSERT":
            return jsonify({"msg": status2}), HTTP_409_CONFLICT
            
        if status2 == "ERROR_WHILE_INSERT_AND_DELETE":
            return jsonify({"msg": status2}), HTTP_409_CONFLICT
        
        print("Very strange error occur!")
        return jsonify({"msg": "If this error occur, this is very strange"}), HTTP_406_NOT_ACCEPTABLE
    
    # Item has expire
    if current_date >= current_table_home_data[0]['expire_on']:
        print("Item has Expired")
        status1 = sql_executer.DELETE_ALL_FROM_HOME_DATA(db)
        if status1 == False:
            return jsonify({"mgs": "Something is wrong. Back-end Error. Trying to clear table `home_data`"}), HTTP_500_INTERNAL_SERVER_ERROR

        status2 = _insert_home_data(current_date)
        if status2 == "SUCCESS":
            new_home_data = sql_executer.SELECT_ALL_FROM_HOME_DATA(db)
            return jsonify(new_home_data), HTTP_200_OK
        
        if status2 == "ERROR_WHILE_INSERT":
            return jsonify({"msg": status2}), HTTP_409_CONFLICT
            
        if status2 == "ERROR_WHILE_INSERT_AND_DELETE":
            return jsonify({"msg": status2}), HTTP_409_CONFLICT
        
    # Item not yet expire
    else:
        print("Item not yet Expire")
        return jsonify(current_table_home_data), HTTP_200_OK
    

# -------------------- QuestionBank --------------------
@app.route("/questionbank_original/<label>", methods=['GET'])
def api_for_questionbank_page_original(label):
    result = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL(db, label=label, random=False, limit=None)
    contest_name = sql_executer.SELETC_DISTINCT_CONTEST_NAME_FROM_IMO_BY_LABEL(db, label=label)
    
    return jsonify({"problems": result, "unique_contest_name": contest_name}), HTTP_200_OK 

@app.route("/questionbank_specific_contestname/<label>", methods=['GET'])
def api_for_questionbank_page_specific(label):
    contest_name = request.args.get('contest_name')
    contest_name: list = contest_name.split(',')
    
    result = sql_executer.SELECT_ALL_FROM_IMO_BY_LABEL_AND_CONTEST_NAME(db, label=label, contest_name=contest_name)
    
    return jsonify(result), HTTP_200_OK 


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


# -------------------- Classify --------------------
@app.route("/classify", methods=['POST'])
def predict_model_classification():
    raw_body_post = request.json
    selected_model = raw_body_post.get("classifier_model")
    text_problem = raw_body_post.get("problems")

    # Store
    result_classification = {
        'Algebra': 0, 
        'Combinatorics': 0, 
        'Geometry': 0, 
        'Number Theory': 0,
        }
    result_regression = {
        'Score': 0,
        'Difficulties': None,
        }

    # Regression
    """
    IMPORTANT NOTE: 
        if there exist more than 1 ACTIVE regression model (EXPECTING ONLY MATHBERT FOR REGRESSION, 
        BUT MAY CONTAIN MANY VERSION OF MATHBERT) it will only take the first occurence of active model in DB
    """
    __ = sql_executer.utils_get_active_regression_model_all_column_from_models(DATABASE_NAME)
    if len(__) != 0:
        mathbert_table = __[0]
        if mathbert_table['is_active'] == 1:
            MathBERTTokenizerpath = mathbert_table['vectorizer_or_tokenizer_path']
            custom_objectspath = mathbert_table['custom_objects_path']
            MathBERTpath = mathbert_table['model_path']
            start = perf_counter()
            print("Loading MathBERT...")
            tokenizer = BertTokenizer.from_pretrained(MathBERTTokenizerpath, output_hidden_states=True)
            custom_objects = load_pkl(custom_objectspath)
            MathBERT = tf.keras.models.load_model(MathBERTpath, custom_objects=custom_objects)
            print("DONE!")
            print("MathBERT loaded!")
            print(f"{perf_counter()-start:.2f}s\n")

            tokenized_text_problem = tokenizer(text_problem, padding='max_length', max_length=512, truncation=True, return_tensors='tf')
            raw_regression_result = MathBERT.predict([
                [tokenized_text_problem['input_ids']], 
                [tokenized_text_problem['attention_mask']], 
                [tokenized_text_problem['token_type_ids']]
            ])
            reg_res = float(raw_regression_result[0][0])
            result_regression['Score'] = reg_res
            result_regression['Difficulties'] = discretize(reg_res)
        else:
            # MathBERT is INACTIVE otherwise result set to None
            ...
    else:
        # No Active regression model otherwise result set to None
        ...

    # Classification
    AVAILABLE_CLASSIFICATION_MODELS = sql_executer.utils_get_active_model_names_from_models(DATABASE_NAME, "classification")
    if selected_model in AVAILABLE_CLASSIFICATION_MODELS:
        temp = sql_executer.SELECT_MODEL_PATH_FROM_MODELS(db, model_name=selected_model)
        # sklearn model (old school models)
        if temp.endswith(".pkl"):
            print("Expecting sklearn model (Classification)...")
            vpath = sql_executer.SELECT_VECTORIZER_OR_TOKENIZER_PATH_FROM_MODELS(db, model_name=selected_model)
            mpath = sql_executer.SELECT_MODEL_PATH_FROM_MODELS(db, model_name=selected_model)
            
            loaded_vectorizer = load_pkl(vpath)
            loaded_model = load_pkl(mpath)

            tranformed_text = loaded_vectorizer.transform(np.array([text_problem]))
            proba_result = loaded_model.predict_proba(tranformed_text)[0]

            result_classification['Algebra'] = proba_result[0]
            result_classification['Combinatorics'] = proba_result[1]
            result_classification['Geometry'] = proba_result[2]
            result_classification['Number Theory'] = proba_result[3]
            
            print(result_regression)
            return jsonify({'classification': result_classification, 'regression': result_regression}), HTTP_200_OK
        # BERT
        else:
            print("Expecting BERT-BASE-CASED (Classification)...")
            loeaded_bert_classifier = tf.saved_model.load(sql_executer.SELECT_MODEL_PATH_FROM_MODELS(db, model_name=selected_model))
            proba_result = loeaded_bert_classifier(tf.constant([text_problem])).numpy()[0]
            
            result_classification['Algebra'] = float(proba_result[0])
            result_classification['Combinatorics'] = float(proba_result[1])
            result_classification['Geometry'] = float(proba_result[2])
            result_classification['Number Theory'] = float(proba_result[3])

            return jsonify({'classification': result_classification, 'regression': result_regression}), HTTP_200_OK
    
    # Select outside defined model OR model is INACTIVE
    else:
        return jsonify({'classification': result_classification, 'regression': result_regression}), HTTP_200_OK

@app.route("/classify/generate_example", methods=['GET'])
def generate_single_random_example_problem_for_classification():
    result = sql_executer.SELECT_ALL_FROM_IMO(db, random=True, limit=1)
    return jsonify(result[0])

@app.route("/classify/iniziate", methods=['GET'])
def classify_page_iniziator():
    AVAILABLE_CLASSIFICATION_MODELS = sql_executer.utils_get_active_model_names_from_models(DATABASE_NAME, "classification")
    return jsonify(AVAILABLE_CLASSIFICATION_MODELS), HTTP_200_OK


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

@app.route("/admin/get_admins_data", methods=['GET'])
def get_admins_data():
    result = sql_executer.SELECT_ALL_FROM_ADMINS(db)
    return jsonify(result), HTTP_200_OK

@app.route("/admin/get_imo_data", methods=['GET'])
def get_imo_data():
    result = sql_executer.SELECT_ALL_FROM_IMO(db)
    return jsonify(result), HTTP_200_OK

@app.route("/admin/insert_new_data_imo", methods=['POST'])
def insert_new_data_imo():
    data = request.json
    label = data.get('label').strip()
    try:
        temp = {
            "no": data.get('no').strip(),
            "contest_category": data.get('contest_category').strip(),
            "contest_name": data.get('contest_name').strip(),
            "year": int(data.get('year').strip()),
            "link": data.get('link').strip(),
            "pdf": data.get('pdf').strip(),
            "post_rendered": data.get('post_rendered').strip(),
            "post_canonical": data.get('post_canonical').strip(),
            "label": None if label == "None" else label,
        }
    except:
        print("ERROR: UNCOMPLETE BODY POST OR TYRING TO INT(year)")
        return jsonify({'msg': 'UNCOMPLETE BODY POST OR TYRING TO INT(year)', 'status': False}), HTTP_400_BAD_REQUEST
    
    data = temp
    stat = sql_executer.INSERT_INTO_IMO(db, data)

    if stat is True:
        return jsonify({"msg": "Insert row success", "status": True}), HTTP_200_OK
    if stat is False:
        return jsonify({"msg": "Insert row failed", "status": False}), HTTP_406_NOT_ACCEPTABLE
    
@app.route("/admin/update_row_imo", methods=['POST'])
def update_row_imo():
    data = request.json
    if type(data.get('year')) == int:
        year = data.get('year')
    if type(data.get('year')) == str:
        year = data.get('year').strip()
    
    label = data.get('label').strip()
    try:
        temp = {
            "id_key": data.get('id_key'),  # should be AUTO INT from front-end
            "no": data.get('no').strip(),
            "contest_category": data.get('contest_category').strip(),
            "contest_name": data.get('contest_name').strip(),
            "year": int(year),
            "link": data.get('link').strip(),
            "pdf": data.get('pdf').strip(),
            "post_rendered": data.get('post_rendered').strip(),
            "post_canonical": data.get('post_canonical').strip(),
            "label": None if label == "None" else label,
        }
    except:
        print("ERROR: UNCOMPLETE BODY POST OR TYRING TO INT(year)")
        return jsonify({'msg': 'UNCOMPLETE BODY POST OR TYRING TO INT(year)', 'status': False}), HTTP_400_BAD_REQUEST
    
    data = temp
    stat = sql_executer.UPDATE_ROW_TABLE_IMO(db, id_key=int(data.get('id_key')), updated_data=data)
    
    if stat is True:
        return jsonify({"msg": "Update row success", "status": True}), HTTP_200_OK
    if stat is False:
        return jsonify({"msg": "Update row failed", "status": False}), HTTP_406_NOT_ACCEPTABLE

@app.route("/admin/delete_row_imo", methods=['POST'])
def delete_row_imo():
    data = request.json
    try:
        id_key = data.get('id_key')
    except:
        print("Error can't get `id_key` from BODY POST")
        return jsonify({"msg": "ERROR `id_key` MISSING BODY POST"}), HTTP_400_BAD_REQUEST

    stat = sql_executer.DELETE_FROM_IMO_WHERE_ID_KEY(db, id_key)
    
    if stat is True:
        return jsonify({"msg": "Delete row success", "status": True}), HTTP_200_OK
    if stat is False:
        return jsonify({"msg": "Delete row failed", "status": False}), HTTP_406_NOT_ACCEPTABLE

@app.route("/admin/add_new_admin", methods=['POST'])
def add_new_admin():
    raw_body_post = request.json

    username = raw_body_post.get("username").replace(" ", "").lower()
    password = generate_password_hash(raw_body_post.get("password").strip())
    full_name = raw_body_post.get("full_name").strip()
    description = raw_body_post.get("description").strip()
    
    # username =  "jacobjeshurunwarouw"
    # password =  generate_password_hash("jacobpassword")
    # full_name =  "Jacob Jeshurun Warouw"
    # description =  "This is the third admin"

    username_already_exist = sql_executer.is_username_exist_in_table_admins(db, username)
    if username_already_exist:
        print("Username already taken!")
        return jsonify({"msg": "Username already taken!", "status": False}), HTTP_400_BAD_REQUEST
    else:
        print("Username is UNIQUE!")
        insert_new_admin_success = sql_executer.insert_new_admin_into_table_admins(db, username, password, full_name, description)
        if insert_new_admin_success:
            print("New admin has been added!")
            return jsonify({"msg": "Insert row success", "status": True}), HTTP_200_OK
        else:
            print("Fail to add new admin!")
            return jsonify({"msg": "Insert row failed (make sure username is unique)", "status": True}), HTTP_406_NOT_ACCEPTABLE

@app.route("/admin/delete_homedata", methods=['GET'])
def delete_homedata():
    try:
        secret_parameter = request.args.get("eR9j07LCQkEwXkTH")  # value should be: uacibxzt
    except:
        secret_parameter = -99999
        
    if secret_parameter != -99999:
        if secret_parameter == "uacibxzt":
            status = sql_executer.DELETE_ALL_FROM_HOME_DATA(db)
            if status is False:
                return jsonify({"msg": "Fail to delete `home_data` (Error while trying to delete `home_data`)", "status": False}), HTTP_500_INTERNAL_SERVER_ERROR

            return jsonify({"msg": "Delete ALL `home_data` success", "status": True}), HTTP_200_OK
    else:
        return jsonify({"msg": "Bad request (missing or invalid parameters)", "status": False}), HTTP_400_BAD_REQUEST
    
@app.route("/admin/get_homedata", methods=['GET'])
def get_homedata():
    result = sql_executer.SELECT_ALL_FROM_HOME_DATA(db)
    return jsonify(result)


# -------------------- models --------------------
@app.route("/admin/get_models", methods=['GET'])
def get_models():
    result = sql_executer.SELECT_ALL_FROM_MODELS(db)
    return jsonify(result)

@app.route("/admin/insert_new_data_models", methods=['POST'])
def add_new_model():
    data = request.json
    
    try:
        model_type = data.get('model_type').strip()
        model_name = data.get('model_name').strip()
        model_path = data.get('model_path').strip()
        vectorizer_or_tokenizer_path = data.get('vectorizer_or_tokenizer_path').strip()
        custom_objects_path = data.get('custom_objects_path') if data.get('custom_objects_path') == None else data.get('custom_objects_path').strip()
        is_active = int(data.get('is_active'))
    except:
        print("Error INCOMPLETE BODY POST or something error trying to get data from BODY POST")
        return jsonify({"msg": "ERROR MISSING BODY POST"}), HTTP_400_BAD_REQUEST
    
    insert_new_model_sucess = sql_executer.insert_new_mode_into_table_models(
        db, 
        model_type,
        model_name,
        model_path,
        vectorizer_or_tokenizer_path,
        custom_objects_path,
        is_active,
    )
    if insert_new_model_sucess:
        print("New model has been added!")
        return jsonify({"msg": "Insert row success", "status": True}), HTTP_200_OK
    else:
        print("Fail to add new model!")
        return jsonify({"msg": "Insert row failed (make sure model_name is unique)", "status": True}), HTTP_406_NOT_ACCEPTABLE
    
@app.route("/admin/update_row_models", methods=['POST'])
def update_row_models():
    data = request.json
    
    try:
        id_model = data.get('id_model')
        model_type = data.get('model_type').strip()
        model_name = data.get('model_name').strip()
        model_path = data.get('model_path').strip()
        vectorizer_or_tokenizer_path = data.get('vectorizer_or_tokenizer_path').strip()
        custom_objects_path = data.get('custom_objects_path') if data.get('custom_objects_path') == None else data.get('custom_objects_path').strip()
        is_active = int(data.get('is_active'))
    except:
        print("Error INCOMPLETE BODY POST or something error trying to get data from BODY POST")
        return jsonify({"msg": "ERROR MISSING BODY POST"}), HTTP_400_BAD_REQUEST
    
    updated_data = {
        'id_model': id_model,
        'model_type': model_type,
        'model_name': model_name,
        'model_path': model_path,
        'vectorizer_or_tokenizer_path': vectorizer_or_tokenizer_path,
        'custom_objects_path': custom_objects_path,
        'is_active': is_active,
    }
    
    updated_row_models_success = sql_executer.update_row_table_models(db, id_model, updated_data)
    if updated_row_models_success:
        print("New model has been added!")
        return jsonify({"msg": "Update row success", "status": True}), HTTP_200_OK
    else:
        print("Fail to add new model!")
        return jsonify({"msg": "Update row failed", "status": True}), HTTP_406_NOT_ACCEPTABLE
    
@app.route("/admin/delete_row_models", methods=['POST'])
def delete_row_models():
    data = request.json
    
    try:
        id_model = data.get('id_model')
    except:
        print("Error can't get `id_model` from BODY POST")
        return jsonify({"msg": "ERROR `id_model` MISSING BODY POST"}), HTTP_400_BAD_REQUEST
    
    delete_row_success = sql_executer.delete_row_table_models(db, id_model)
    if delete_row_success:
        return jsonify({"msg": "Delete row success", "status": True}), HTTP_200_OK
    else:
        return jsonify({"msg": "Delete row failed", "status": False}), HTTP_406_NOT_ACCEPTABLE


# print("################# Flask API ready #################")
