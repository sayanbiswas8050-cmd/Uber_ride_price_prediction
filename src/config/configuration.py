from src.constants import *
from src.utils.utils import read_yaml,create_directories
from src.entity.config_entity import DataIngestionConfig

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