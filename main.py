from fedex_air_delay import logger
from fedex_air_delay.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Welcome to Fedex Air Delay Prediction")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Started {STAGE_NAME} <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()   
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e