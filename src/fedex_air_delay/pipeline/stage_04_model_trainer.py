from fedex_air_delay import logger
from fedex_air_delay.components.model_trainer import ModelTrainer
from fedex_air_delay.config.configuration import ConfigurationManager

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()

if __name__ == '__main__':
    try:
        logger.info(f"***************** {STAGE_NAME} started *****************")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f"***************** {STAGE_NAME} completed *****************")
    except Exception as e:
        logger.exception(e)
        raise e