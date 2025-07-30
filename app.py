from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
import pickle
import pandas as pd

# import the ML model
with open("Model/model.pkl", "rb") as f:
    model = pickle.load(f)

# MLflow
model_version = "v1.0.0"  # Example version, adjust as needed

app = FastAPI()


# Human-readable API documentation
@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}

# Machine-readable health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "version": model_version,
        "model_loaded": model is not None
    }

# Define the API endpoint for prediction
@app.post("/predict")
def predict_premium(data: UserInput):

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,  
    }])

    # Make prediction
    model_prediction = model.predict(input_df)[0]

    # Prepare response
    return JSONResponse(status_code=200, content={'predicted_premium': model_prediction}) 