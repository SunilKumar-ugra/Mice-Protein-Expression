from mice.config import ConfigurationManager
from mice.components.model_evaluation import ModelEvaluation

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_model_evaluation_config()
        evaluation = ModelEvaluation(eval_config)
        evaluation.log_into_mlflow()
