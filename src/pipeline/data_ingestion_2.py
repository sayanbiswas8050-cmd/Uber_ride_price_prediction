import os
import sys
import pandas as pd
from dataclasses import dataclass
from pathlib import Path
from sklearn.model_selection import train_test_split

from src.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH,PARAMS_FILE_PATH
from src.utils.utils import read_yaml, create_directories
from src.exception import CustomException
from src.logger import logging

logger = logging.getLogger(__name__)


# ---------------- 1. Configuration Entity ----------------
@dataclass
class DataIngestionConfig:
    root_dir: Path
    local_source_path: Path
    raw_data_file: Path
    train_data_file: Path
    test_data_file: Path


# ------------- 2. Configuration Manager -------------
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            local_source_path=Path(config.local_source_path),
            raw_data_file=Path(config.raw_data_file),
            train_data_file=Path(config.train_data_file),
            test_data_file=Path(config.test_data_file)
        )

        return data_ingestion_config


# --------------- 3. Data Ingestion Component ---------------
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        """
        Reads local dataset, creates raw copy in artifacts,
        and splits into train and test sets.
        """
        try:
            logger.info(f"Reading dataset from local source: {self.config.local_source_path}")
            df = pd.read_csv(self.config.local_source_path)

            # Save the raw data into artifacts/data_ingestion
            df.to_csv(self.config.raw_data_file, index=False, header=True)
            logger.info(f"Raw data saved at: {self.config.raw_data_file}")

            # Train-Test Split (adjust test_size as needed)
            logger.info("Performing train-test split...")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.config.train_data_file, index=False, header=True)
            test_set.to_csv(self.config.test_data_file, index=False, header=True)

            logger.info(f"Train data saved at: {self.config.train_data_file}")
            logger.info(f"Test data saved at: {self.config.test_data_file}")

            return (
                self.config.train_data_file,
                self.config.test_data_file
            )

        except Exception as e:
            logger.error(f"Error occurred during data ingestion: {e}")



if __name__ == '__main__':
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        print(f"Data ingestion completed. Train: {train_path}, Test: {test_path}")
    except Exception as e:
        
        raise CustomException(e, sys)