#%%
#DataExtractor

import pandas as pd
from database_utils import DatabaseConnector



class DataExtractor:
    def __init__(self):
        self.connector = DatabaseConnector()
        self.rds_engine = self.connector.init_db_engine(self.connector.creds)  
        self.table_names = self.connector.list_db_tables()
    
    def read_rds_table(self, table_name):
        df = pd.read_sql_table(table_name, self.rds_engine)
        return df

        


object = DataExtractor()
user_table = object.read_rds_table("legacy_users")
user_table.head(10)






    




# %%
