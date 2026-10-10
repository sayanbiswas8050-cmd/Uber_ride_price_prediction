import logging
import os
from datetime import datetime

# Create folder
logs_path = os.path.join(os.getcwd(), 'logs') ## current_path, logs folder
os.makedirs(logs_path,exist_ok= True)

# Create log file names 
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    filemode= 'a',
    format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s : %(message)s',
    level= logging.INFO
)