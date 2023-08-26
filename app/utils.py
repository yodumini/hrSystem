from sqlalchemy import create_engine


def connect_DB():
    # 資料庫參數設定
    db_settings = {
        "host": "mysql",
        "port": 3306,
        "user": "root",
        "password": "12345",
        "db": "employee",
        "charset": "utf8"
    }
    user = db_settings['user']
    passwd = db_settings['password']
    host = db_settings['host']
    db_name = db_settings['db']
    engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}:3306/{db_name}?charset=utf8mb4')
    con = engine.connect()
    return engine, con
