import os
import yaml
import json
import pickle
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any

import sys
from src.exception import CustomException
from src.logger import logging
logger = logging.getLogger(__name__)


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns ConfigBox content."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_dirs: list, verbose: bool = True):
    """Creates a list of directories."""
    try:
        for path in path_to_dirs:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")
    except Exception as e:
        raise CustomException(e, sys)
    

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data into a JSON file."""
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")
    except Exception as e:
        raise CustomException(e, sys)
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads JSON file and returns as ConfigBox attributes."""
    try:
        with open(path, "r") as f:
            content = json.load(f)
        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)
    

@ensure_annotations
def save_obj(data: Any, path: Path):
    """Saves an object as a binary pickle file."""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:  
            pickle.dump(data, f)
        logger.info(f"binary file saved at: {path}")  
    except Exception as e:
        raise CustomException(e, sys)
    

@ensure_annotations
def load_obj(path: Path) -> Any:
    """Loads an object from a binary pickle file."""
    try:
        with open(path, "rb") as f:  
            data = pickle.load(f)    
        logger.info(f"binary file loaded from: {path}")
        return data                  
    except Exception as e:
        raise CustomException(e, sys)