import requests
import pandas as pd
from pathlib import Path
from settings import FILE_PATH, TEST_JSON, URL, URL_POST


def main():
    # Проверка существования файла
    if not Path(FILE_PATH).exists():
        raise FileNotFoundError(f"Файл {FILE_PATH} не найден")

    # 1. Загрузка CSV файла с диска
    print(f"Печатаем sample: {pd.read_csv(FILE_PATH)['id'].sample()}")

    # 2. Отправляем GET запрос
    requests.get(URL)

    # 3. Отправляем POST запрос с загруженным файлом
    response = requests.post(URL_POST, json=TEST_JSON)

    # 4. Получаем и выводим результат
    print("JSON Response:")
    print(response.json())


if __name__ == "__main__":
    main()
