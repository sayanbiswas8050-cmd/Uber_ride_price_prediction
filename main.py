from src.pipeline.data_ingestion_1 import DataIngestionTrainingPipeline

import sys
from src.exception import CustomException
from src.logger import logging
logger = logging.getLogger(__name__)

try:
    logger.info(f"Data Ingestion stage start now")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'Data Ingestion stage Completed')
except Exception as e:
    raise CustomException(e, sys)