from src.logger import logging
from src.exception import InsuranceException
from src.utils import get_collection_as_dataframe
from src.entity.config_entity import DataIngestionConfig
from src.entity import config_entity
from src.entity import artifact_entity
from src.components.data_ingestion import DataIngestion 
import os,sys

# def test_logger_and_expection():
#     try:
#         logging.info("Starting the test_logger_and_exception")
#         result = 3/0
#         print(result)
#         logging.info("Stoping the test_logger_and_exception")
        
#     except Exception as e:
#        logging.debug(str(e))
#        raise InsuranceException(e, sys)
   

if __name__ == "__main__":
    # try:
    #     test_logger_and_expection()

    # except Exception as e:
    #     print(e)

    try:
    #     get_collection_as_dataframe(database_name='INSURANCE',collection_name='INSURANCE_PROJECT')
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

    except Exception as e:
        print(e)
