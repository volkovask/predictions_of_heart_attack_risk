import pandas as pd
import joblib
import logging
from pathlib import Path


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


ID = 'id'


class MLModelHandler:
    def __init__(self, model_path: str):
        self.model = None
        self.model_path = model_path
        self.__load_model()

    def __load_model(self):
        """Загрузка модели."""
        try:
            if not Path(self.model_path).exists():
                error_msg = f"Model file not found at {self.model_path}"
                logger.error(error_msg)
                raise FileNotFoundError(error_msg)

            self.model = joblib.load(self.model_path)
            logger.info(f"Model loaded successfully from {self.model_path}")

        except Exception as e:
            logger.error(f"Model loading failed: {str(e)}")
            raise

    def predict(self, data: pd.DataFrame) -> pd.DataFrame:
        """Безопасное выполнение предсказания"""
        try:
            predictions = self.model.predict(data)

            return pd.DataFrame({
                ID: data[ID],
                'prediction': predictions
            })

        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            raise
