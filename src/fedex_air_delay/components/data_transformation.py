import os
import pandas as pd
from sklearn.model_selection import train_test_split

from fedex_air_delay import logger
from fedex_air_delay.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        data = data.sample(frac=0.01, random_state=234)
        data = data.dropna()
        data = data.drop_duplicates()
        
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False, header=True)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False, header=True)
        logger.info(f"train and test data split successfully")

        logger.info(data.shape)
        logger.info(train.shape)
        logger.info(test.shape)
        
        return train, test