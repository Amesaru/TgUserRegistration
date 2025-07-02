import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('user_data_copy.csv')

# Convert the 'registration_date' column to datetime format
df['registration_date'] = pd.to_datetime(df['registration_date'])

# Plot the graph
plt.figure(figsize=(10, 6))
plt.scatter(df['user_id'], df['registration_date'], color='blue')

# Add labels and title
plt.xlabel('User ID')
plt.ylabel('Registration Date')
plt.title('User Registration Dates')

# Display the plot
plt.show()