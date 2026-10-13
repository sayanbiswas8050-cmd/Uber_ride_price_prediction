import os
from pathlib import Path
from logger import logging

logger = logging.getLogger(__name__)

list_of_files = [
    'src/__init__.py',
    'src/components/__init__.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/config/__init__.py',
    'src/config/configuration.py',
    'src/pipeline/__init__.py',
    'src/entity/__init__.py',
    'src/entity/config_entity.py',
    'src/constants/__init__.py',
    'config/config.yaml',
    'data'
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'exception.py',
    'logger.py',
    'setup.py',
    'requirements.txt',
    'templates/index.html'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir != '':
        PATH = os.path.join(os.getcwd(),filedir)
        os.makedirs(PATH,exist_ok= True)
        logger.info(f'Creating directory: {PATH} for the file{filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logger.info(f'Creating empty file: {filepath}')
    
    else:
        logger.info(f'{filename} is already exists' )