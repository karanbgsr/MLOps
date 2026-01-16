import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:

    """
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    """
    client = None

    def __init__(self,database_name=DATABASE_NAME)->None:
        mongo_db_url = os.getenv(MONGODB_URL_KEY)
        MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
        self.client =  MongoDBClient.client
        self.database = self.client[self.client]
        self.database_name = database_name

   