import os
from datetime import datetime

DATABASE_NAME = 'US_VISA'
COLLECTION_NAME = "VISA_DATA"
MONGODB_URL_KEY = "MONGODB_URL"

PIPLELINE_NAME:str = "usvisa"
ARTIFACT_DIR:str = "artifact"

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

FILE_NAME = 'EasyVisa.csv'
MODEL_FILE_NAME = "model_pkl"
"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
