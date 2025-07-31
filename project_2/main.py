import pickle
import pandas as pd

# Now we have to Load model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Sample input (must match encoded feature columns)
sample = {
    'Year': 2019,
    'Kilometers_Driven': 40000,
    'Mileage': 18,
    'Engine': 1500,
    'Power': 120,
    'Seats': 5,
    'Brand_Toyota': 1,
    'Fuel_Type_Petrol': 1,
    'Transmission_Manual': 1,
    'Owner_Type_Second': 1,
    # set other dummies to 0
}

# Convert to DataFrame and fill missing dummies with 0
sample_df = pd.DataFrame([sample])
for col in X.columns:
    if col not in sample_df.columns:
        sample_df[col] = 0

# Predict
predicted_price = model.predict(sample_df)[0]
print("Predicted Price:", int(predicted_price))
