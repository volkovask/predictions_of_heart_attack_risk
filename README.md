## Проект: Предсказание рисков сердечного приступа.
### Описание проекта.
В этом проекте предполагается работа с датасетом из открытого источника.<br/>
Разработана модель для предсказания риска сердечного приступа.<br/>
Предсказание осуществляется путем направления на ендпоинт "http://127.0.0.1:8000/predict" в post запросе json файла с информацией о пути где находится csv файл c тестовыми данными.

пример json файла:
```
 {"file_path": f"{FILE_PATH}"}
```


#### Ссылка на проект.
https://github.com/volkovask/predictions_of_heart_attack_risk.git

#### Автор: Андрей Волков.

#### Команды сборки проекта локально.
создать и активировать виртуальное окружение:
```
 python3 -m venv venv
 source venv/bin/activate
```
установка pip:
```
 python3 -m pip install --upgrade pip
```
установка зависимостей:
```
 pip install -r requirements.txt
```
запуск проекта:
```
 uvicorn main:app --host 0.0.0.0 --reload
```

тест test_api.py для проверки локально
запуск теста:
```
 python test_api.py
```

### Структура проекта.

```
├── README.md                   - описание проекта
├── datasets                    - датасеты
│   ├── heart_test.csv          - тестовая выборка
│   ├── heart_train.csv         - тренировочная выборка
│   ├── predictions.csv         - выборка предсказаний
│   └── test.csv                - предобработанная тестовая выборка
├── main.py                     - главный скрипт запуска приложения
├── model                       - модели
│   └── best_pipeline.joblib    - обученная модель
├── notebook.ipynb              - юпитер ноутбук предобработки и обучения модели
├── requirements.txt            - зависимости
├── settings.py                 - конфигурация и константы приложения
├── src                         - базовые классы
│   ├── csvreq.py               - сериализатор json
│   ├── dataproc.py             - загрузка и предобработка тестовых данных
│   ├── mlmodel.py              - загрузка модели и выполнение предсказания
│   └── test.py                 - тестовый скрипт модели
├── test_api.py                 - скрипт тестирования API
```