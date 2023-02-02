import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd




def read_db_cred():
    with open('../Multinational Retail Data Centralisation/db_creds.yaml' , 'r') as db_creds_file:
        db_creds = yaml.safe_load(db_creds_file)
    return db_creds

def init_db_engine():
    db_creds = read_db_creds()
    engine = create_engine(f"{db_creds['DATABASE_TYPE']}+{db_creds['DBAPI']}://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}")
    return engine

def list_db_tables():
    engine = init_db_engine()
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    return table_names

read_db_cred()
init_db_engine()
list_db_tables()

