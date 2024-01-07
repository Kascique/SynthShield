# Synthetic Data-Driven Fraud Detection Model

## Overview

This project aims to demonstrate a machine learning approach to detect fraudulent transactions using a synthetic dataset. It includes scripts for generating synthetic data, preprocessing this data, training a machine learning model, and evaluating its performance.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or later
- Pip (Python package installer)

## Installation

**Clone the Repository:**
```bash
git clone https://github.com/Kascique/SynthShield
cd SynthShield
```

## Set Up a Virtual Environment (Optional but recommended):

**For Unix or MacOS::**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows::**
```bash
python -m venv venv
venv\Scripts\activate
```

**For Windows::**
```bash
pip install -r requirements.txt
```

## Generating the Synthetic Dataset


**generate_data.py::**
```bash
python generate_data.py
```

This will create a file named synthetic_credit_card_transactions.csv in the data/ directory.

## Running the Analysis


**1. Start Jupyter Notebook::**
```bash
jupyter notebook
```

2. Navigate to the notebooks/ directory and open EDA_and_Modeling.ipynb.

3. Run the cells in the notebook to perform the following:

Load and preprocess the data.
Conduct exploratory data analysis (EDA).
Train the machine learning model.
Evaluate the model's performance.