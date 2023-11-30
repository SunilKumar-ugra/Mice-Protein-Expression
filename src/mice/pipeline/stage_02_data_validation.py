from mice.config import ConfigurationManager
from mice.components.data_validation import DataValiadtion

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
        
if __name__ == '__main__':
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
