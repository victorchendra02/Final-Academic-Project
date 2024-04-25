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

