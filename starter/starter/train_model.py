import os
import pickle
import sys

import pandas as pd
from ml.data import process_data
from ml.model import compute_model_metrics, inference, train_model
from sklearn.model_selection import train_test_split
from slicing import slice_metrics

# Add the necessary imports for the starter code.
file_dir = os.path.dirname(__file__)
sys.path.insert(0, file_dir)

# Add code to load in the data.
data = pd.read_csv(os.path.join(file_dir, "../data/clean_census.csv"))

# train-test split.
train, test = train_test_split(data, test_size=0.2, random_state=42)

cat_features = [
    "workclass",
    "education",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native_country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Process the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

# Train and save a model.
model = train_model(X_train, y_train)

# Ensure the model directory exists
model_dir = os.path.join(file_dir, "../model")
os.makedirs(model_dir, exist_ok=True)

# Save artifacts
pickle.dump(model, open(os.path.join(model_dir, "model.pkl"), "wb"))
pickle.dump(encoder, open(os.path.join(model_dir, "encoder.pkl"), "wb"))
pickle.dump(lb, open(os.path.join(model_dir, "label_binarizer.pkl"), "wb"))


# Inference and evaluation.
train_pred = inference(model, X_train)
test_pred = inference(model, X_test)
precision, recall, f_one = compute_model_metrics(y_test, test_pred)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1: {f_one}")

# Slicing
slice_metrics(model, encoder, lb, data, "workclass", categorical_features=cat_features)
