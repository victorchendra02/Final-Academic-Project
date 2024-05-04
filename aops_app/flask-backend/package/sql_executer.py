from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


def orient_record(obj):
    return [row._asdict() for row in obj]  # [{col1, col2, ...}, {}, {}, ...]

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

def is_username_exist_in_table_admins(db, username: str) -> bool:
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

def get_admin_password_by_username(db, username) -> str:
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

def insert_new_admin_into_table_admins(db, username: str, password: str, fullname: str, description: str) -> bool:
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
