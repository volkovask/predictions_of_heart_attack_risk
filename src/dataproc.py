import logging
import numpy as np
import pandas as pd
import re
from pathlib import Path
from settings import OHE_COLUMNS, ORD_COLUMNS


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataProcessor:
    @staticmethod
    def load_and_preprocess(file_path: str) -> pd.DataFrame:
        """Загрузка и предобработка данных"""
        try:
            # Проверка существования файла
            if not Path(file_path).exists():
                raise FileNotFoundError(f"CSV file not found at {file_path}")

            # Чтение CSV с проверкой
            df = pd.read_csv(file_path)
            logger.info(f"Data loaded successfully. Shape: {df.shape}")

            # Обработка датафрейма
            # Приведение полей к змеиному формату.
            df.rename(columns=DataProcessor.__prepare_columns(df), inplace=True)
            logger.info(
                "Let's convert the column names in accordance with the snake register.")

            # Преобразование поля в бинарное.
            DataProcessor.__gender_to_binary(df)
            logger.info("Converting a field 'gender' to binary.")

            # Удалим пропуски
            df.dropna(inplace=True)
            logger.info("Removing the gaps.")

            # Преобразование типа поля в int.
            DataProcessor.__convert_float_to_int(df)
            logger.info("Converting a type fields to int.")

            return df

        except Exception as exc:
            logger.error(f"Data loading failed: {str(exc)}")
            raise

    @staticmethod
    def __to_snake_case(column_name: str) -> str:
        """Приведение полей к змеиному формату."""
        # Заменяем пробелы, дефисы и двоеточия на подчёркивания.
        value = re.sub(r'[\s\-:]', '_', column_name)
        # Вставляем подчёркивание между заглавной и строчной буквой (для camelCase).
        value = re.sub(r'([a-z])([A-Z])', r'\1_\2', value)
        # Заменяем множественные подчёркивания на одинарные.
        value = re.sub(r'_+', '_', value)
        # Приводим к нижнему регистру
        return value.lower()

    @staticmethod
    def __prepare_columns(data: pd.DataFrame) -> dict:
        """Подготовка списка колонок."""
        columns_dict = {}
        columns = data.columns.tolist()

        for col in columns:
            columns_dict[col] = DataProcessor.__to_snake_case(col)

        return columns_dict

    @staticmethod
    def __gender_to_binary(data: pd.DataFrame) -> None:
        """Преобразование поля в бинарное."""
        data['gender'] = (np.where(data['gender'] == 'Male', '1.0', data['gender']))
        data['gender'] = (np.where(data['gender'] == 'Female', '0.0', data['gender']))
        data['gender'] = data['gender'].astype('float64').astype('int64')

    @staticmethod
    def __convert_float_to_int(data: pd.DataFrame) -> pd.DataFrame:
        """Преобразование типа поля в int."""
        data[ORD_COLUMNS] = data[ORD_COLUMNS].astype('int64')
        data[OHE_COLUMNS] = data[OHE_COLUMNS].astype('int64')
