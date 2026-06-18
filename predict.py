import pandas as pd
from joblib import load

# Load trained model
model = load("fraud_model.pkl")

def predict_fraud(amount):

    # Create dummy values for remaining columns
    data = {
        "Time": [0]
    }

    for i in range(1, 29):
        data[f"V{i}"] = [0]

    data["Amount"] = [amount]

    df = pd.DataFrame(data)

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    if prediction == 1:
        status = "Fraud"
    else:
        status = "Legitimate"

    return status, round(probability, 4)