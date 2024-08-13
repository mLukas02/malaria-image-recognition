import sys
from cnnRecognition import logger
from cnnRecognition.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnRecognition.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnRecognition.pipeline.stage_03_training import ModelTrainingPipeline
from cnnRecognition.pipeline.stage_04_evaluation import EvaluationPipeline

def run_stage(stage_name):
    if stage_name == "data_ingestion":
        STAGE_NAME = "Data Ingestion stage"
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            data_ingestion = DataIngestionTrainingPipeline()
            data_ingestion.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e

    elif stage_name == "prepare_base_model":
        STAGE_NAME = "Prepare base model"
        try:
            logger.info(f"*******************")
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            prepare_base_model = PrepareBaseModelTrainingPipeline()
            prepare_base_model.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e

    elif stage_name == "training":
        STAGE_NAME = "Training"
        try:
            logger.info(f"*******************")
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            model_trainer = ModelTrainingPipeline()
            model_trainer.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e

    elif stage_name == "evaluation":
        STAGE_NAME = "Evaluation stage"
        try:
            logger.info(f"*******************")
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            model_evalution = EvaluationPipeline()
            model_evalution.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e

    else:
        logger.error(f"Unknown stage: {stage_name}")
        print(f"Unknown stage: {stage_name}. Please choose from 'data_ingestion', 'prepare_base_model', 'training', 'evaluation'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main_pipeline.py <stage_name>")
        print("Available stages: 'data_ingestion', 'prepare_base_model', 'training', 'evaluation'")
        sys.exit(1)

    stage_name = sys.argv[1]
    run_stage(stage_name)
