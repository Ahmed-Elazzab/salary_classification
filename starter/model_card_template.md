## Model Details
The model used for this project is a `RandomForestClassifier` with default hyperparameters.

## Intended Use
The model is used classifying whether employees salary is above $50,000 or not.

## Training Data
The data utilized for training this model came from the Census Bureau  https://archive.ics.uci.edu/ml/datasets/census+income


## Evaluation Data
The original dataset is first pre-processed and then split into training (80%) and evaluation data (20%).

## Metrics
Precision, recall, and F_beta score were used as metrics for evaluating the model's performance. The model achieves the following result:
* Precision: 0.7321428571428571
* Recall: 0.6431372549019608
* F_beta: 0.6847599164926931


## Limitations
The model may not generalize well to populations outside the original census data. It may reflect biases present in the data.

## Ethical Considerations
Predictions should not be used for decisions that could negatively impact individuals without further human review.

## Model Version
Version: 1.0  
Date: 2025-05-31

## Authors
Developed by Ahmed ELazab.