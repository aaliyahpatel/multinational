#DataClean
#%%
import numpy as np
import pandas as pd

class DataCleaning:
    def clean_user_data(self, df):
        users = df.copy
        # replace NULL with np.nam
        users = users.replace ('NULL', np.nan)

        # replace invalid countries to nan
        countries = ['United Kingdom', 'United States', 'Germany']
        # replace GGB to GB
        country_codes = ['GB', 'US', 'DE']
        users['country'] = users['country'].apply(lambda x: x if x in countries else np.nan)
        users['country_code'] = users['country_code'].str.replace('GGB','GB')
        # replace invalid country codes to nan
        users['country_code'] = users['country_code'].apply(lambda x: x if x in country_codes else np.nan)

        # change dates to datetime
        users['date_of_birth'] = pd.to_datetime(users['date_of_birth'], infer_datetime_format=True, errors='coerce')
        users['join_date'] = pd.to_datetime(users['join_date'], infer_datetime_format=True, errors='coerce')







# %%
