from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion



import sys
if __name__=='__main__':
    logging.info("the execuation has started")
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)
        