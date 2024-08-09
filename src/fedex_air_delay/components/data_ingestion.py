#building the data ingestion configuration class

from pathlib import Path
from dataclasses import dataclass
from fedex_air_delay.constants import *
from fedex_air_delay.utils.common import read_yaml, create_directories
from fedex_air_delay.entity.config_entity import DataIngestionConfig
from fedex_air_delay.config.configuration import ConfigurationManager

import os
import urllib.request as request
import zipfile
from fedex_air_delay import logger
from fedex_air_delay.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):    
        if not os.path.exists(self.config.local_data_file):
            os.system(f"kaggle datasets download -d vasudevmaduri/fedexdata -p {self.config.root_dir}")
            logger.info(f"file downloaded successfully!")
        else:
            logger.info(f"{self.config.local_data_file} already exists")
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts the zip file into the data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        os.system(f"unzip {self.config.local_data_file} -d {unzip_path}")
        logger.info(f"extracted {self.config.local_data_file} into {unzip_path}")


# try:
#     config = ConfigurationManager()
#     data_ingestion_config = config.get_data_ingestion_config()
#     data_ingestion = DataIngestion(config=data_ingestion_config)
#     data_ingestion.download_file()
#     data_ingestion.extract_zip_file()
# except Exception as e:
#     raise e