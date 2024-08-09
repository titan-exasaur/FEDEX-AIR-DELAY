from fedex_air_delay import logger
from fedex_air_delay.components.data_validation import DataValidation
from fedex_air_delay.config.configuration import ConfigurationManager

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Started {STAGE_NAME} <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e