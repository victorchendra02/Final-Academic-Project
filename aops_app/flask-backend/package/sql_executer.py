from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


def orient_record(obj):
    return [row._asdict() for row in obj]  # [{col1: row1, col2: row1, ...}, {}, {}, ...]

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

def DELETE_ALL_FROM_HOME_DATA(db: SQLAlchemy): 
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
