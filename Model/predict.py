import pickle
import pandas as pd

# import the ML model
with open("Model/model.pkl", "rb") as f:
    model = pickle.load(f)

# MLflow
model_version = "v1.0.0"  # Example version, adjust as needed

def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input]) 

    output = model.predict(input_df)[0]

    return output
        