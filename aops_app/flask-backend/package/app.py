# to disable TF warning log  
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import random
import numpy as np
# import tensorflow as tf
from tensorflow._api.v2.saved_model import load as tf_savedmodel_load
from tensorflow import constant as tf_constant

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
        'Algebra': -1, 
        'Combinatorics': -1, 
        'Geometry': -1, 
        'Number Theory': -1,
        }
    result_regression = {
        'Score': -1,
        'Difficulties': None,
        }

    # Regression (MATHBERT MODEL ONLY FROM HUGGING FACE)
    """
    IMPORTANT NOTE: 
        if there exist more than 1 ACTIVE regression model (EXPECTING ONLY MATHBERT FOR REGRESSION, 
        BUT MAY CONTAIN MANY VERSION OF MATHBERT) it will only take the first occurence of active model in DB
    """
    __ = sql_executer.utils_get_active_regression_model_all_column_from_models(DATABASE_NAME)
    if len(__) != 0:
        mathbert_table = __[0]
        
        MathBERTTokenizerpath = mathbert_table['vectorizer_or_tokenizer_path']
        MathBERTpath = mathbert_table['model_path']
        
        print(f"mbert_path ==> {MathBERTpath}")
        print(f"tknzr_path ==> {MathBERTTokenizerpath}")
        
        # 1. Load tokenizer first
        print("(1) status  ==> LOADING...      mathbert tokenizer")
        try:
            tokenizer = BertTokenizer.from_pretrained(MathBERTTokenizerpath, output_hidden_states=True)
        except:
            # Error is `HFValidationError` if tokenizer path is incorrect
            ...
        # 2. NO ERROR OCCUR ==> Load model
        else:
            print("(2) status  ==> SUCCESS LOADING mathbert tokenizer")
            try:
                start = perf_counter()
                MathBERT = tf_savedmodel_load(MathBERTpath)
            except:
                # Error should be `OSError` if model path is incorrect
                ...
            # 3. NO ERROR OCCUR ==> Predict
            else:
                print("(3) status  ==> SUCCESS LOADING mathbert model")
                tokenized_text_problem = tokenizer(text_problem, padding='max_length', max_length=512, truncation=True, return_tensors='tf')
                raw_regression_result = MathBERT([
                    [tokenized_text_problem['input_ids']][0], 
                    [tokenized_text_problem['attention_mask'][0]], 
                    [tokenized_text_problem['token_type_ids'][0]]
                ])
                reg_res = float(raw_regression_result[0][0])
                result_regression['Score'] = reg_res
                result_regression['Difficulties'] = discretize(reg_res)
                end = perf_counter()

                print("(4) status  ==> REGRESSION DONE!")
                print(f"TIME TAKEN to load model and do regression: {end-start:.2f}s\n")
    else: ...  # No Active regression model otherwise result set to default

    # Classification
    AVAILABLE_CLASSIFICATION_MODELS = sql_executer.utils_get_active_model_names_from_models(DATABASE_NAME, "classification")
    if selected_model in AVAILABLE_CLASSIFICATION_MODELS:
        slctd_model_path = sql_executer.SELECT_MODEL_PATH_FROM_MODELS(db, model_name=selected_model)
        
        if slctd_model_path.endswith(".pkl"):
            # sklearn model (old school models)
            print("Expecting sklearn model (Classification)...")
            vpath = sql_executer.SELECT_VECTORIZER_OR_TOKENIZER_PATH_FROM_MODELS(db, model_name=selected_model);

            try:
                loaded_vectorizer = load_pkl(vpath)
                loaded_model = load_pkl(slctd_model_path)
            except FileNotFoundError:
                # Vectorizer or Model path is not exist
                return jsonify({'classification': result_classification, 'regression': result_regression}), HTTP_200_OK                
            else:
                # Vectorizer or Model path exist
                tranformed_text = loaded_vectorizer.transform(np.array([text_problem]))
                proba_result = loaded_model.predict_proba(tranformed_text)[0]

                result_classification['Algebra'] = proba_result[0]
                result_classification['Combinatorics'] = proba_result[1]
                result_classification['Geometry'] = proba_result[2]
                result_classification['Number Theory'] = proba_result[3]
                
                return jsonify({'classification': result_classification, 'regression': result_regression}), HTTP_200_OK
        else:
            # BERT
            print("Expecting BERT-BASE-CASED (Classification)...")
            print("path is not endswith('.pkl')")

            try: 
                start = perf_counter()
                loeaded_bert_classifier = tf_savedmodel_load(slctd_model_path)
            except OSError:
                # BERT model path is not exist
                return jsonify({'classification': result_classification, 'regression': result_regression}), HTTP_200_OK
            else:
                # BERT model path exist
                proba_result = loeaded_bert_classifier(tf_constant([text_problem])).numpy()[0]
                
                result_classification['Algebra'] = float(proba_result[0])
                result_classification['Combinatorics'] = float(proba_result[1])
                result_classification['Geometry'] = float(proba_result[2])
                result_classification['Number Theory'] = float(proba_result[3])
                end = perf_counter()

                print(f"TIME TAKEN to load model and do classification w/ BERT: {end-start:.2f}s\n")
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

@app.route("/admin/get_all_active_classifier_models_name", methods=['GET'])
def get_all_active_classifier_models_name():
    AVAILABLE_CLASSIFICATION_MODELS = sql_executer.utils_get_active_model_names_from_models(DATABASE_NAME, "classification")
    return jsonify(AVAILABLE_CLASSIFICATION_MODELS), HTTP_200_OK

@app.route("/admin/classify_problem", methods=['POST'])
def admin_classify():
    raw_body_post = request.json
    selected_model = raw_body_post.get("classifier_model")
    text_problem = raw_body_post.get("problems")
    
    result_classification = {
        'Algebra': -1, 
        'Combinatorics': -1, 
        'Geometry': -1, 
        'Number Theory': -1,
        }

    AVAILABLE_CLASSIFICATION_MODELS = sql_executer.utils_get_active_model_names_from_models(DATABASE_NAME, "classification")
    if selected_model in AVAILABLE_CLASSIFICATION_MODELS:
        slctd_model_path = sql_executer.SELECT_MODEL_PATH_FROM_MODELS(db, model_name=selected_model)
        if slctd_model_path.endswith(".pkl"):
            # sklearn model (old school models)
            print("(ADMIN) Expecting sklearn model (Classification)...")
            vpath = sql_executer.SELECT_VECTORIZER_OR_TOKENIZER_PATH_FROM_MODELS(db, model_name=selected_model);

            try:
                loaded_vectorizer = load_pkl(vpath)
                loaded_model = load_pkl(slctd_model_path)
            except FileNotFoundError:
                # Vectorizer or Model path is not exist
                return jsonify({"msg": f"FileNotFoundError:\nIncorrect model or vectorizer path: `{selected_model}`"}), HTTP_404_NOT_FOUND
            else:
                # Vectorizer or Model path exist
                tranformed_text = loaded_vectorizer.transform(np.array([text_problem]))
                proba_result = loaded_model.predict_proba(tranformed_text)[0]

                result_classification['Algebra'] = proba_result[0]
                result_classification['Combinatorics'] = proba_result[1]
                result_classification['Geometry'] = proba_result[2]
                result_classification['Number Theory'] = proba_result[3]
                
                return jsonify({'classification': result_classification, "label": max(result_classification, key=result_classification.get)}), HTTP_200_OK
        else:
            # BERT
            print("(ADMIN) Expecting BERT-BASE-CASED (Classification)...")
            print("(ADMIN) path is not endswith('.pkl')")

            try: 
                start = perf_counter()
                loeaded_bert_classifier = tf_savedmodel_load(slctd_model_path)
            except OSError:
                # BERT model path is not exist
                return jsonify({"msg": f"OSError:\nIncorrect model path: `{selected_model}`"}), HTTP_404_NOT_FOUND
            else:
                # BERT model path exist
                proba_result = loeaded_bert_classifier(tf_constant([text_problem])).numpy()[0]
                
                result_classification['Algebra'] = float(proba_result[0])
                result_classification['Combinatorics'] = float(proba_result[1])
                result_classification['Geometry'] = float(proba_result[2])
                result_classification['Number Theory'] = float(proba_result[3])
                end = perf_counter()
                print(f"(ADMIN) TIME TAKEN to load model and do classification w/ BERT: {end-start:.2f}s\n")

                return jsonify({'classification': result_classification, "label": max(result_classification, key=result_classification.get)}), HTTP_200_OK
    
    # Select outside defined model OR model is INACTIVE
    else:
        return jsonify({"msg": f"Exception:\nSomething error can't be explained: `{selected_model}`"}), HTTP_404_NOT_FOUND
        

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
        is_active = int(data.get('is_active'))
    except:
        print("Error INCOMPLETE BODY POST or something error trying to get data from BODY POST")
        return jsonify({"msg": "ERROR MISSING BODY POST"}), HTTP_400_BAD_REQUEST
    
    insert_new_model_sucess = sql_executer.insert_new_model_into_table_models(
        db, 
        model_type,
        model_name,
        model_path,
        vectorizer_or_tokenizer_path,
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
