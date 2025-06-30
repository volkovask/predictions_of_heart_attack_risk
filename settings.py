ID = 'id'
BEST_PIPELINE = "model/best_pipeline.joblib"
OUTPUT_PATH = "datasets/predictions.csv"
FILE_PATH = 'datasets/heart_test.csv'
TEST_JSON = {"file_path": f"{FILE_PATH}"}
URL = "http://127.0.0.1:8000/"
URL_POST = f"{URL}predict"

# Список числовых полей.
NUM_COLUMNS = ['age',
               'bmi',
               'income',
               'cholesterol',
               'blood_sugar',
               'triglycerides',
               'systolic_blood_pressure',
               'diastolic_blood_pressure',
               'heart_rate',
               'ck_mb',
               'troponin',
               'exercise_hours_per_week',
               'sedentary_hours_per_day',
               'sleep_hours_per_day'
               ]

# Список бинарных полей.
ORD_COLUMNS = ['diabetes',
               'gender',
               'smoking',
               'alcohol_consumption',
               'family_history',
               'obesity',
               'previous_heart_problems',
               'medication_use',
               'physical_activity_days_per_week'
               ]

# Список категориальных полей.
OHE_COLUMNS = ['diet',
               'stress_level'
               ]
