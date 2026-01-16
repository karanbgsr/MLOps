from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
import pandas as pd
import sys
import os
import numpy as np


class US_VISA:

    def __init__(self):
        #creating a object of MongoDB client
        self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
    
    def export_collection_as_dataframe(self,collection_name:str)->pd.DataFrame:
        collection = self.mongo_client.database[collection_name]
        df = pd.DataFrame(list(collection.find()))
        if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
        df.replace({"na":np.nan},inplace=True)
        return df
    
