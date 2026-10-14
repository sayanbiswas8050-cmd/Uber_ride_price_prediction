from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion

import sys
from src.exception import CustomException
from src.logger import logging
logger = logging.getLogger(__name__)


class DataIngestionTrainingPipeline():
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        

if __name__ == "__main__":
    try:
        logger.info(f"Data Ingestion stage start now")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'Data Ingestion stage Completed')
    except Exception as e:
        raise CustomException(e, sys)