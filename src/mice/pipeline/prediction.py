import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
from mice import logger


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        
    def predict(self, data):
        prediction = self.model.predict(data)
        logger.info(prediction)
        if(prediction==0):                      # 'c-CS-m': 0,
            pred="c-CS-m: Control Mice, Stimulated To Learn, Injected With Memantine (10 mice)"
            logger.info(pred)
        elif(prediction==1):                    #  'c-CS-s': 1
            pred="c-CS-s: Control Mice, Stimulated To Learn, Injected With Saline (9 mice)"
            logger.info(pred)
        elif(prediction==2):                    #  'c-SC-m': 2,
            pred="c-SC-m: Control Mice, Not Stimulated To Learn, Injected With Memantine (10 mice)"
            logger.info(pred)
        elif(prediction==3):                    #  'c-SC-s': 3,
            pred="c-SC-s: Control Mice, Not Stimulated To Learn, Injected With Saline (9 mice)"
            logger.info(pred)
        elif(prediction==4):                    #  't-CS-m': 4
            pred="t-CS-m: Trisomy Mice, Stimulated To Learn, Injected With Memantine (9 mice)"
            logger.info(pred)
        elif(prediction==5):                    #  't-CS-s': 5,
            pred="t-CS-s: Trisomy Mice, Stimulated To Learn, Injected Withh Saline (7 mice)"
            logger.info(pred)
        elif(prediction==6):                    #  't-SC-m': 6,
            pred="t-SC-m: Trisomy Mice, Not Stimulated To Learn, Injected With Memantine (9 mice)"
            logger.info(pred)
        elif(prediction==7):                    #  't-SC-s': 7
            pred="t-SC-s: Trisomy Mice, Not Stimulated To Learn, Injected With Saline (9 mice)"
            logger.info(pred)
        else:
            pred="UNKNOWN"
            logger.info(pred)
        return pred