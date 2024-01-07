import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(filename):
    """Load the dataset from a file."""
    return pd.read_csv(filename)

def preprocess_data(data):
    """Preprocess the data: clean, scale, and split."""
    # Drop non-numeric columns for simplicity
    data = data.select_dtypes(include=['float64', 'int64'])

    # Assuming the 'Fraud' column is the label
    X = data.drop('Fraud', axis=1)
    y = data['Fraud']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
