import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd


class DatabaseConnector:
    def __init__(self):
        self.creds = self.read_db_creds()
        self.engine = self.init_db_engine(self.creds)

    def read_db_creds(self):
        with open('../Multinational Retail Data Centralisation/db_creds.yaml' , 'r') as db_creds_file:
            db_creds = yaml.safe_load(db_creds_file)
        return db_creds
        

    def init_db_engine(self, db_creds):
        engine = create_engine(f"{db_creds['DATABASE_TYPE']}+{db_creds['DBAPI']}://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}")
        engine.connect()
        return engine

    def list_db_tables(self):
        #engine = self.init_db_engine()
        inspector = inspect(self.engine)
        table_names = inspector.get_table_names()
        return table_names






















