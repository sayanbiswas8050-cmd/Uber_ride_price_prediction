from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file: Path
    extract_dir: Path