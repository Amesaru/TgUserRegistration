import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('user_data_copy.csv')

df['registration_date'] = pd.to_datetime(df['registration_date'])

plt.figure(figsize=(10, 6))
plt.scatter(df['user_id'], df['registration_date'], color='blue')

plt.xlabel('User ID')
plt.ylabel('Registration Date')
plt.title('User Registration Dates')

plt.show()