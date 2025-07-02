import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("user_data_copy.csv")

data['registration_date'] = pd.to_datetime(data['registration_date'])
min_date = data['registration_date'].min()
data['days_since_start'] = (data['registration_date'] - min_date).dt.days

X = data[['user_id']].values
y = data['days_since_start'].values

model = LinearRegression()
model.fit(X, y)

def predict_registration_date(user_id):
    days_since_start = model.predict(np.array([[user_id]]))[0]
    predicted_date = min_date + pd.to_timedelta(days_since_start, unit='days')
    return predicted_date

predicted_date = predict_registration_date(434161633)
print(f"Predicted registration date for user_id 434161633: {predicted_date}")