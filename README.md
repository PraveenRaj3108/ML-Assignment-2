Machine Learning Assignment 2
Problem Statement

The objective of this project is to build and compare multiple machine learning classification models to predict whether an individual's annual income exceeds $50,000 per year based on demographic and employment-related information.

Five machine learning classification algorithms were implemented, trained, evaluated, and deployed using Streamlit Community Cloud. The deployed application allows users to upload test data, select a model, and view performance metrics without retraining the models.

Dataset Description
Dataset Name

Adult Income Dataset

Source

UCI Machine Learning Repository

Problem Type

Binary Classification

Target Variable

Income

Classes:

<=50K

50K

Dataset Statistics
Attribute	ValueNumber of Records	48,842
Number of Features	14
Target Classes	2
Learning Type	Supervised Classification
Features

The dataset contains demographic and employment-related features such as:

Age
Workclass
Education
Education Number
Marital Status
Occupation
Relationship
Race
Sex
Capital Gain
Capital Loss
Hours per Week
Native Country
Fnlwgt
GitHub Repository Link

Replace with your actual repository URL

https://github.com/PraveenRaj3108/ML-Assignment-2
Streamlit Application Link

https://your-app-name.streamlit.app](https://ml-assignment-2-emewiakt5ko7pmpfvroyzr.streamlit.app/)
Models Used

The following classification models were implemented using Scikit-Learn:

Logistic Regression
Decision Tree Classifier
K-Nearest Neighbors (KNN)
Naive Bayes Classifier
Support Vector Machine (SVM)
Model Performance Comparison
ML Model Name	Accuracy	AUC	Precision	Recall	F1 Score	MCCLogistic Regression	0.8212	0.8595	0.7347	0.4648	0.5694	0.4830
Decision Tree	0.8130	0.7557	0.6306	0.6391	0.6349	0.5092
KNN	0.8210	0.8593	0.7629	0.4296	0.5497	0.4775
Naive Bayes	0.7971	0.8589	0.7038	0.3491	0.4667	0.3922
Support Vector Machine	0.8210	0.8593	0.7629	0.4296	0.5497	0.4775
Observations on Model Performance
ML Model Name	Observation about Model PerformanceLogistic Regression	Achieved the highest AUC score and strong overall classification performance. It provided a good balance between precision and accuracy.
Decision Tree	Produced the highest recall and F1-score among the evaluated models. It was capable of identifying more positive instances but had a lower AUC score.
KNN	Demonstrated competitive accuracy and precision. Its performance was close to Logistic Regression but depended heavily on feature scaling and neighborhood selection.
Naive Bayes	Fastest model to train and evaluate. However, it achieved lower recall and F1-score compared to other models due to the strong independence assumptions.
Support Vector Machine	Achieved performance comparable to Logistic Regression with excellent AUC score and high precision. It performed well on the classification task.
Overall Winner	Logistic Regression and SVM achieved the strongest overall performance in terms of Accuracy and AUC. Decision Tree achieved the highest Recall and F1-Score.
Streamlit Application Features

The developed application includes the following functionalities:

Dataset Upload

Users can upload a CSV test dataset for evaluation.

Model Selection

Users can select any of the following trained models:

Logistic Regression
Decision Tree
KNN
Naive Bayes
SVM
Evaluation Metrics

The application calculates and displays:

Accuracy
Precision
Recall
F1 Score
AUC Score
Matthews Correlation Coefficient (MCC)
Confusion Matrix

Displays the confusion matrix for the selected model.

Classification Report


Conclusion

In this project, five machine learning classification algorithms were implemented and compared on the Adult Income Dataset. The models were evaluated using Accuracy, Precision, Recall, F1 Score, AUC Score, and MCC. Logistic Regression and Support Vector Machine demonstrated the strongest overall predictive performance, while Decision Tree achieved the best Recall and F1 Score.

A web-based Streamlit application was successfully developed and deployed, enabling interactive evaluation of the trained models using uploaded test datasets. This project demonstrates a complete machine learning workflow consisting of data preprocessing, model development, evaluation, deployment, and real-world inference.
