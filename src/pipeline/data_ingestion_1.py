import os
import sys
from dataclasses import dataclass
from os import path, sysconf
from pathlib import Path
import urllib.request as request
import zipfile 
from numpy import extract

from src.constants import *
from utils.utils import read_yaml,create_directories
from exception import CustomException
from logger import logging
logger = logging.getLogger(__name__)

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file: Path
    extract_dir: Path
    
class ConfigurationManager:
    def __init__(self,
                config_filepath = CONFIG_FILE_PATH,
                schema_filepath = SCHEMA_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH):
        
        # 1. Assign filepaths
        self.config_filepath = config_filepath
        self.schema_filepath = schema_filepath
        self.params_filepath = params_filepath
        
        # 2. Read yaml files
        self.config = read_yaml(self.config_filepath)
        self.schema = read_yaml(self.schema_filepath)
        self.params = read_yaml(self.params_filepath)
        
        # 3. Create root artifacts directory
        create_directories([self.config.artifacts_root])
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        # create artifacts/data_ingestion 
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            extract_dir = config.extract_dir
            )
        
        return data_ingestion_config
    

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename}")
        else:
            logger.info(f"File already exists at: {self.config.local_data_file}")
        
        """Extracts if it's a zip file; otherwise skips and directly accesses the file."""
        local_file = Path(self.config.local_data_file)
        
        # Check if the file is actually a zip file
        if zipfile.is_zipfile(local_file):
            create_directories([self.config.extract_dir])
            
            with zipfile.ZipFile(local_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.extract_dir)
            logger.info(f"Extracted zip contents to: {self.config.extract_dir}")
        else:
            logger.info(f"File '{local_file.name}' is not a zip file. Ready for direct access at: {local_file}")
        
        # # Find the extracted CSV file
        # extracted_files = os.listdir(EXTRACTED_DATA_FILE_PATH)
        # csv_files = [f for f in extracted_files if f.endswith('.csv')]
        
        # if len(csv_files) == 0:
        #     raise FileNotFoundError('No CSV file found in the extracted_data folder')
        # if len(csv_files) > 1:
        #     raise ValueError("Multiple CSV files found. Please spacify wchich one to use.")
        
        # # Read the CSV into a DataFrame
        # csv_file_path = os.path.join(EXTRACTED_DATA_FILE_PATH,csv_files[0])
        # df = pd.read_csv(csv_file_path)
        
        # return df

if __name__ == '__main__':
    try:
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        raise CustomException(e, sys)