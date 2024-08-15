from fedex_air_delay import logger
from fedex_air_delay.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from fedex_air_delay.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from fedex_air_delay.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from fedex_air_delay.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

logger.info("Welcome to Fedex Air Delay Prediction")

#########################################################

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Started {STAGE_NAME} <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()   
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

########################################################

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Started {STAGE_NAME} <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

#######################################################

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> Started {STAGE_NAME} <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

#######################################################

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> Started {STAGE_NAME} <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e