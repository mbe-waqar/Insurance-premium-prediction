from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from Model.predict import predict_output, model, model_version


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

    user_input = {
        'bmi': data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,  
    }

    try:
        # Make prediction
        model_prediction = predict_output(user_input)
        # Prepare response
        return JSONResponse(status_code=200, content={'predicted_premium': model_prediction}) 
    
    except Exception as e:
        # Return error response
        return JSONResponse(status_code=500, content={'error': str(e)})