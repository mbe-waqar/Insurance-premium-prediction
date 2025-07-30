import pickle
import pandas as pd

# import the ML model
with open("Model/model.pkl", "rb") as f:
    model = pickle.load(f)

# MLflow
model_version = "v1.0.0"  # Example version, adjust as needed
