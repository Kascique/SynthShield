# This code must be executed before the EDA_and_Modeing 

import numpy as np
from faker import Faker
import random

fake = Faker()

# Define the number of samples you want
num_samples = 1000

# Initialize empty lists to hold the data for each feature
timestamps = []
amounts = []
countries = []
user_ids = []
frauds = []

# Define some parameters for the 'amount' feature
avg_amount = 70.0  # average transaction amount in your currency
std_dev_amount = 25.0  # standard deviation of the amount

# Generate the data
for _ in range(num_samples):
    # Generate a random timestamp
    timestamps.append(fake.date_time_this_year())

    # Generate a transaction amount
    amounts.append(abs(np.random.normal(avg_amount, std_dev_amount)))

    # Generate a random country
    countries.append(fake.country())

    # Generate a random user ID
    user_ids.append(fake.uuid4())

    # Randomly decide if the transaction is fraudulent or not
    frauds.append(random.choice([0, 1]))  # 0 for legitimate, 1 for fraudulent

# Combine the data into a single dataset
data = list(zip(timestamps, amounts, countries, user_ids, frauds))

# Optionally, convert the dataset to a numpy array or a pandas DataFrame
# For example, using pandas:
import pandas as pd


# Add the column titles for ease of reference during modeling
df = pd.DataFrame(data, columns=["Timestamp", "Amount", "Country", "User ID", "Fraud"])
print(df.head())  # Print the first few rows of the DataFrame

# Save the DataFrame to a CSV file
df.to_csv('synthetic_credit_card_transactions.csv', index=False)
