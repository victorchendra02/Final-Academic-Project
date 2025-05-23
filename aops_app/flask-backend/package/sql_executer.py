from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import MySQLdb


"""utils"""
def orient_record(obj):
    return [row._asdict() for row in obj]  # [{col1: row1, col2: row1, ...}, {}, {}, ...]

def utils_get_active_model_names_from_models(db_name:str, model_type: str):
    connection = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        db=db_name
    )
    cursor = connection.cursor()
    
    if model_type == "classification":
        sql = """
            SELECT model_name
            FROM models
            WHERE
                is_active=1
            AND 
                model_type='classification';
        """
    elif model_type == "regression":
        sql = """
            SELECT model_name
            FROM models
            WHERE
                is_active=1
            AND 
                model_type='regression';
        """
    elif model_type == "all_type":
        sql = """
            SELECT model_name
            FROM models
            WHERE is_active=1;
        """

    cursor.execute(sql)
    results = cursor.fetchall()
    model_names = [row[0] for row in results]

    cursor.close()
    connection.close()
    
    return model_names

def utils_get_active_regression_model_all_column_from_models(db_name: str):
    connection = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        db=db_name
    )
    cursor = connection.cursor()
    sql = """
        SELECT *
        FROM models
        WHERE
            model_type='regression'
        AND 
            is_active=1;
    """
    
    cursor.execute(sql)
    
    # Fetch the column names
    columns = [desc[0] for desc in cursor.description]
    # Fetch all rows from the executed query
    results = cursor.fetchall()
    # Convert the results to a list of dictionaries
    results_dict = [dict(zip(columns, row)) for row in results]

    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    return results_dict


"""TABLE: imo"""
def SELECT_ALL_FROM_IMO(db: SQLAlchemy, random: bool=False, limit: int|None=None):
    if random is False:
        if limit is None:
            sql = """
                SELECT 
                    *
                FROM imo;
            """
            result = db.session.execute(text(sql))
        elif type(limit) == int:
            sql = """
                SELECT 
                    *
                FROM imo
                LIMIT :limit;
            """
            result = db.session.execute(text(sql), {'limit': limit})
    elif random is True:
        if limit is None:
            sql = """
                SELECT 
                    *
                FROM imo
                ORDER BY RAND();
            """
            result = db.session.execute(text(sql))
        elif type(limit) == int:
            sql = """
                SELECT 
                    *
                FROM imo
                ORDER BY RAND()
                LIMIT :limit;
            """       
            result = db.session.execute(text(sql), {'limit': limit})

    return orient_record(result.fetchall())
    
def SELECT_ALL_FROM_IMO_WHERE_LABEL_IS_NOT_NULL(db: SQLAlchemy, random: bool=False):
    if random is False:
        sql = """
            SELECT 
                *
            FROM imo
            WHERE label IS NOT NULL;
        """
        result = db.session.execute(text(sql))
        return orient_record(result.fetchall())
    if random is True:
        sql = """
            SELECT 
                *
            FROM imo
            WHERE label IS NOT NULL
            ORDER BY RAND();
        """
        result = db.session.execute(text(sql))
        return orient_record(result.fetchall())

def SELECT_ALL_FROM_IMO_BY_LABEL(db: SQLAlchemy, label:str, random: bool=False, limit: int|None=None):
    if random is False:
        if limit is None:
            sql = """
                SELECT 
                    *
                FROM imo
                WHERE label=:label;
            """
            result = db.session.execute(text(sql), {'label': label})
        elif type(limit) == int:
            sql = """
                SELECT 
                    *
                FROM imo
                WHERE label=:label
                LIMIT :limit;
            """
            result = db.session.execute(text(sql), {'label': label, 'limit': limit})
    elif random is True:
        if limit is None:
            sql = """
                SELECT 
                    *
                FROM imo
                WHERE label=:label
                ORDER BY RAND();
            """
            result = db.session.execute(text(sql), {'label': label})
        elif type(limit) == int:
            sql = """
                SELECT 
                    *
                FROM imo
                WHERE label=:label
                ORDER BY RAND()
                LIMIT :limit;
            """       
            result = db.session.execute(text(sql), {'label': label, 'limit': limit})
 
    return orient_record(result.fetchall())

def SELECT_DISTINCT_YEAR_FROM_IMO(db: SQLAlchemy, sort: str="DESC") -> list[int]:
    sql = """
        SELECT 
            DISTINCT(year) AS `years` 
        FROM 
            `imo` 
        ORDER BY 
            `years`
        :sort_type;
    """
    raw_result = db.session.execute(text(sql), {"sort_type": sort.upper()})
    result = orient_record(raw_result.fetchall())
    return [i['years'] for i in result]

def SELETC_DISTINCT_CONTEST_NAME_FROM_IMO(db: SQLAlchemy) -> list[str]:
    sql = """
        SELECT 
            DISTINCT(contest_name) AS unique_contest_name
        FROM 
            imo
        ORDER BY
            `unique_contest_name`
        ASC;
    """
    raw_result = db.session.execute(text(sql))
    result = orient_record(raw_result.fetchall())
    return [i['unique_contest_name'] for i in result]

def SELETC_DISTINCT_CONTEST_NAME_FROM_IMO_BY_LABEL(db: SQLAlchemy, label: str) -> list[str]:
    sql = """
        SELECT 
            DISTINCT(contest_name) AS unique_contest_name
        FROM 
            imo
        WHERE 
            label=:label
        ORDER BY
            `unique_contest_name`
        ASC;
    """
    raw_result = db.session.execute(text(sql), {'label': label})
    result = orient_record(raw_result.fetchall())
    return [i['unique_contest_name'] for i in result]

def SELECT_ALL_FROM_IMO_BY_LABEL_AND_CONTEST_NAME(db: SQLAlchemy, label: str, contest_name: str | list):
    if isinstance(contest_name, str):
        sql = """
            SELECT *
            FROM imo
            WHERE label=:label
            AND contest_name=:contest_name;
        """
        params = {'label': label, 'contest_name': contest_name}
    elif isinstance(contest_name, list):
        placeholders = ', '.join([':contest_name_' + str(i) for i in range(len(contest_name))])
        sql = f"""
            SELECT *
            FROM imo
            WHERE label=:label
            AND contest_name IN ({placeholders});
        """
        params = {'label': label}
        params.update({f'contest_name_{i}': val for i, val in enumerate(contest_name)})

    result = db.session.execute(text(sql), params)
    return orient_record(result.fetchall())

def INSERT_INTO_IMO(db: SQLAlchemy, data: dict) -> bool:
    sql = """
        INSERT INTO `imo`(
            no,
            contest_category,
            contest_name,
            year,
            link,
            pdf,
            post_rendered,
            post_canonical,
            label
        )
        VALUES(
            :no,
            :contest_category,
            :contest_name,
            :year,
            :link,
            :pdf,
            :post_rendered,
            :post_canonical,
            :label
        );
    """

    try:
        db.session.execute(
            text(sql),
            {
                "no": data['no'],
                "contest_category": data['contest_category'],
                "contest_name": data['contest_name'],
                "year": data['year'],
                "link": data['link'],
                "pdf": data['pdf'],
                "post_rendered": data['post_rendered'],
                "post_canonical": data['post_canonical'],
                "label": data['label'],
            }
        )
        return True
    except:
        print("Error while inserting row to `imo` table!")
        return False
    
def UPDATE_ROW_TABLE_IMO(db: SQLAlchemy, id_key: int, updated_data: dict) -> bool:
    sql = """
        UPDATE
            `imo`
        SET
            `no`=:no,
            `contest_category`=:contest_category,
            `contest_name`=:contest_name,
            `year`=:year,
            `link`=:link,
            `pdf`=:pdf,
            `post_rendered`=:post_rendered,
            `post_canonical`=:post_canonical,
            `label`=:label
        WHERE
            `imo`.`id_key`=:id_key;
    """
    
    try:
        db.session.execute(
            text(sql),
            {
                "id_key": id_key,
                "no": updated_data['no'],
                "contest_category": updated_data['contest_category'],
                "contest_name": updated_data['contest_name'],
                "year": updated_data['year'],
                "link": updated_data['link'],
                "pdf": updated_data['pdf'],
                "post_rendered": updated_data['post_rendered'],
                "post_canonical": updated_data['post_canonical'],
                "label": updated_data['label'],
            }
        )
        return True
    except:
        try:
            print(f"Error while UPDATING row WHERE id_key=`{id_key}` in `imo` table!")
        except:
            print(f"Error while UPDATING row WHERE id_key=<UNKNOWN> in `imo` table!")
        finally:
            return False

def DELETE_FROM_IMO_WHERE_ID_KEY(db: SQLAlchemy, id_key: int) -> bool:
    sql = """
        DELETE FROM 
            `imo` 
        WHERE 
            `imo`.`id_key`=:id_key
    """
    try:
        try:
            int(id_key)
        except:
            print(f"Error trying to INT(id_key) => `{id_key}` - {type(id_key)}")
            return False
        
        db.session.execute(text(sql), {'id_key': int(id_key)})
        return True
    except:
        print(f"Error while DELETE WHERE id_key=`{id_key}`")
        return False


"""TABLE: admins"""
def SELECT_ALL_FROM_ADMINS(db: SQLAlchemy):
    sql = """
        SELECT *
        FROM admins;
    """
    
    raw_result = db.session.execute(text(sql))
    result = orient_record(raw_result.fetchall())
    return result

def is_username_exist_in_table_admins(db: SQLAlchemy, username: str) -> bool:
    sql = """
        SELECT
        COUNT(*) AS
            'is_username_exist'
        FROM
            admins
        WHERE
            username=:username
    """
    raw_result = db.session.execute(text(sql), {'username' : username})
    result = orient_record(raw_result.fetchall())[0]['is_username_exist']
    return True if result == 1 else (False if result == 0 else -99999)

def get_admin_password_by_username(db: SQLAlchemy, username) -> str:
    sql = """
        SELECT 
            password
        FROM
            admins
        WHERE
            username=:username
    """
    raw_result = db.session.execute(text(sql), {'username': username})
    result = orient_record(raw_result.fetchall())[0]['password']
    return result

def insert_new_admin_into_table_admins(db: SQLAlchemy, username: str, password: str, fullname: str, description: str) -> bool:
    """
    NOTE: 
        BEFORE USING THIS FUNCTION, CHECK IF USERNAME ALREADY EXIST/TAKEN
        USING `is_username_exist_in_table_admins` FUNCTION.
    """
    
    sql = """
        INSERT INTO admins(
            username, 
            password, 
            full_name, 
            created_at, 
            is_active,
            description
        ) 
        VALUES(
            :username, 
            :password, 
            :full_name, 
            CURRENT_TIMESTAMP, 
            TRUE,
            :description
        );
    """
    try:
        db.session.execute(text(sql), {'username': username, 'password': password, 'full_name': fullname, 'description': description})
        return True
    except:
        return False


"""TABLE: models"""
def SELECT_ALL_FROM_MODELS(db: SQLAlchemy):
    sql = """
        SELECT *
        FROM models;
    """
    raw_result = db.session.execute(text(sql))
    result = orient_record(raw_result.fetchall())
    return result

def SELECT_ALL_FROM_MODELS_BY_MODEL_NAME(db: SQLAlchemy, model_name: str):
    sql = """
        SELECT *
        FROM models
        WHERE model_name=:mn
    """
    raw_result = db.session.execute(text(sql), {"mn": model_name})
    result = orient_record(raw_result.fetchall())
    return result

def SELECT_MODEL_PATH_FROM_MODELS(db: SQLAlchemy, model_name: str) -> str:
    sql = """
        SELECT model_path AS _
        FROM models
        WHERE 
            model_name=:model_name;
    """
    raw_result = db.session.execute(text(sql), {"model_name": model_name})
    result = orient_record(raw_result.fetchall())
    return result[0]['_']

def SELECT_VECTORIZER_OR_TOKENIZER_PATH_FROM_MODELS(db: SQLAlchemy, model_name: str) -> str:
    sql = """
        SELECT vectorizer_or_tokenizer_path AS _
        FROM models
        WHERE 
            model_name=:model_name;
    """
    raw_result = db.session.execute(text(sql), {"model_name": model_name})
    result = orient_record(raw_result.fetchall())
    return result[0]['_']
 
def get_all_active_model_names(db: SQLAlchemy, model_type:None|str=None) -> list[str]:
    if isinstance(model_type, None):
        sql = """
            SELECT model_name AS model_name
            FROM models
            WHERE is_active=1;
        """
        raw_result = db.session.execute(text(sql))
        result = orient_record(raw_result.fetchall())
        return [i['model_name'] for i in result]
    
    if isinstance(model_type, str):
        sql = """
            SELECT model_name AS model_name
            FROM models
            WHERE
                is_active=1
            AND 
                model_type=:model_type;
        """
        raw_result = db.session.execute(text(sql), {'model_type': model_type})
        result = orient_record(raw_result.fetchall())
        return [i['model_name'] for i in result]
 

"""TABLE: home_data"""
def SELECT_ALL_FROM_HOME_DATA(db: SQLAlchemy):
    sql = """
        SELECT 
            * 
        FROM 
            home_data
    """
    raw_result = db.session.execute(text(sql))
    result = orient_record(raw_result.fetchall())
    return result

def DELETE_ALL_FROM_HOME_DATA(db: SQLAlchemy) -> bool: 
    sql = """
        DELETE FROM home_data;
    """
    try:
        db.session.execute(text(sql))
        return True
    except:
        return False

def INSERT_ROW_TO_TABLE_HOME_DATA(db: SQLAlchemy, data: dict) -> bool:
    sql = """
        INSERT INTO home_data(
            id_home_data,
            id_key,
            no,
            contest_category,
            contest_name,
            year,
            link,
            pdf,
            post_rendered,
            post_canonical,
            label,
            day_created,
            created_at,
            expire_day,
            expire_on
        )
        VALUES(
            :id_home_data,
            :id_key,
            :no,
            :contest_category,
            :contest_name,
            :year,
            :link,
            :pdf,
            :post_rendered,
            :post_canonical,
            :label,
            :day_created,
            :created_at,
            :expire_day,
            :expire_on
        );
    """

    try:
        db.session.execute(
            text(sql),
            {
                "id_home_data": data['id_home_data'],
                "id_key": data['id_key'],
                "no": data['no'],
                "contest_category": data['contest_category'],
                "contest_name": data['contest_name'],
                "year": data['year'],
                "link": data['link'],
                "pdf": data['pdf'],
                "post_rendered": data['post_rendered'],
                "post_canonical": data['post_canonical'],
                "label": data['label'],
                "day_created": data['day_created'],
                "created_at": data['created_at'],
                "expire_day": data['expire_day'],
                "expire_on": data['expire_on']
            }
        )
        return True
    except:
        print("Error while inserting row to `home_data` table!")
        return False


"""TABLE: models"""
def insert_new_model_into_table_models(
    db: SQLAlchemy, 
    model_type:str, 
    model_name:str, 
    model_path:str, 
    vectorizer_or_tokenizer_path:str, 
    is_active: int) -> bool:
    
    sql = """
        INSERT INTO models(
            model_type, 
            model_name, 
            model_path, 
            vectorizer_or_tokenizer_path,
            is_active
        ) 
        VALUES(
            :model_type, 
            :model_name, 
            :model_path, 
            :vectorizer_or_tokenizer_path,
            :is_active
        );
    """
    try:
        db.session.execute(
            text(sql), 
            {
                'model_type': model_type, 
                'model_name': model_name, 
                'model_path': model_path, 
                'vectorizer_or_tokenizer_path': vectorizer_or_tokenizer_path, 
                'is_active': is_active
            })
        return True
    except:
        return False

def update_row_table_models(db: SQLAlchemy, id_model: int, updated_data: dict):
    sql = """
        UPDATE
            `models`
        SET
            `id_model`=:id_model,
            `model_type`=:model_type,
            `model_name`=:model_name,
            `model_path`=:model_path,
            `vectorizer_or_tokenizer_path`=:vectorizer_or_tokenizer_path,
            `is_active`=:is_active
        WHERE
            `models`.`id_model`=:id_model;
    """
    
    try:
        db.session.execute(
            text(sql),
            {
                "id_model": int(id_model),
                "model_type": updated_data['model_type'],
                "model_name": updated_data['model_name'],
                "model_path": updated_data['model_path'],
                "vectorizer_or_tokenizer_path": updated_data['vectorizer_or_tokenizer_path'],
                "is_active": updated_data['is_active'],
            }
        )
        return True
    except:
        try:
            print(f"Error while UPDATING row WHERE id_key=`{id_model}` in `models` table!")
        except:
            print(f"Error while UPDATING row WHERE id_key=<UNKNOWN> in `models` table!")
        finally:
            return False
        
def delete_row_table_models(db: SQLAlchemy, id_model: int) -> bool:
    sql = """
        DELETE FROM 
            `models` 
        WHERE 
            `models`.`id_model`=:id_model;
    """
    try:
        try:
            int(id_model)
        except:
            print(f"Error trying to INT(id_model) => `{id_model}` - {type(id_model)}")
            return False
        
        db.session.execute(text(sql), {'id_model': int(id_model)})
        return True
    except:
        print(f"Error while DELETE WHERE id_model=`{id_model}`")
        return False
    
    