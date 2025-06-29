import logging
from src.csvreq import CSVRequest
from src.dataproc import DataProcessor
from fastapi import FastAPI, HTTPException
from src.mlmodel import MLModelHandler
from settings import BEST_PIPELINE, OUTPUT_PATH

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


# Инициализация обработчика модели
try:
    model_handler = MLModelHandler(BEST_PIPELINE)
except Exception as error:
    logger.critical(f"Failed to initialize model handler: {str(error)}")
    raise


@app.post("/predict")
async def predict_req(request: CSVRequest):
    try:
        logger.info(f"Received prediction request for file: {request.file_path}")

        # Загрузка и предобработка данных
        data = DataProcessor.load_and_preprocess(
            request.file_path
        )

        # Получение предсказаний
        predictions = model_handler.predict(data)

        # Сохраняем результат в CSV
        predictions.to_csv(OUTPUT_PATH, index=False)
        logger.info(f"Save predictions to {OUTPUT_PATH} file.")

        # Формирование ответа
        response = {
            "status": "success",
            "stats": {"processed_rows": len(data)},
            "predictions": predictions.to_dict(orient="records")
        }

        logger.info(f"Prediction successful. Processed {len(data)} rows.")

        return response

    except FileNotFoundError as not_found:
        logger.error(f"File not found: {str(not_found)}")
        raise HTTPException(status_code=404, detail=str(not_found))
    except ValueError as value_error:
        logger.error(f"Validation error: {str(value_error)}")
        raise HTTPException(status_code=400, detail=str(value_error))
    except Exception as exc:
        logger.error(f"Unexpected error: {str(exc)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(exc)}")


@app.get("/")
def health_check():
    return {"status": "ready"}
