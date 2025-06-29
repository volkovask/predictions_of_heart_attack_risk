import requests
import pandas as pd
from pathlib import Path


file_path = 'datasets/heart_test.csv'   # 'test.csv' 'heart_test.csv'
test_json = {"file_path": f"{file_path}"}
url = "http://127.0.0.1:8000/"
url_post = f"{url}predict"


def main():
    # Проверка существования файла
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")

    # 1. Загрузка CSV файла с диска
    print(f"Печатаем sample: {pd.read_csv(file_path)['id'].sample()}")

    # 2. Отправляем GET запрос
    requests.get(url)

    # 3. Отправляем POST запрос с загруженным файлом
    response = requests.post(url_post, json=test_json)

    # 4. Получаем и выводим результат
    print("JSON Response:")
    print(response.json())


if __name__ == "__main__":
    main()
