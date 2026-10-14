import os
import sys
from pathlib import Path
import urllib.request as request
import zipfile 

from src.entity.config_entity import DataIngestionConfig
from src.config.configuration import ConfigurationManager
from src.utils.utils import create_directories

from src.exception import CustomException
from src.logger import logging
logger = logging.getLogger(__name__)
    

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download with following info: \n{headers}")
        else:
            logger.info(f"File already exists at: {self.config.local_data_file}")
        
        
    def extract_zip_file(self):
        
        """Extracts if it's a zip file; otherwise skips and directly accesses the file."""
        extract_file_path = Path(self.config.local_data_file)  # artifacts/data_ingestion/data.zip
        
        # Check if the file is actually a zip file
        if zipfile.is_zipfile(extract_file_path):
            create_directories([self.config.extract_dir])
            
            with zipfile.ZipFile(extract_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.config.extract_dir)
            logger.info(f"Extracted zip contents to: {self.config.extract_dir}")
        else:
            logger.info(f"File '{extract_file_path.name}' is not a zip file. Ready for direct access at: {extract_file_path}")


