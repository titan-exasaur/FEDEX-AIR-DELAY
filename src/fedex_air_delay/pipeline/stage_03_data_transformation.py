from pathlib import Path
from fedex_air_delay import logger
from fedex_air_delay.config.configuration import ConfigurationManager
from fedex_air_delay.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("assets/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Data Validation stage failed")
            
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Started {STAGE_NAME} <<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> Completed {STAGE_NAME} <<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e