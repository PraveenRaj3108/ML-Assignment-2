import streamlit as st
import pandas as pd
import joblib
import os

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

st.set_page_config(
    page_title="Income Classification Models",
    page_icon="📊",
    layout="wide"
)

st.title("Income Classification Models")

# Model Selection
model_choice = st.selectbox(
    "Select Model",
    [
        "Logistic",
        "Decision Tree",
        "KNN",
        "Naive Bayes",
        "SVM"
    ]
)

# Model Paths
paths = {
    "Logistic": "logistic.pkl",
    "Decision Tree": "dt.pkl",
    "KNN": "knn.pkl",
    "Naive Bayes": "nb.pkl",
    "SVM": "svm.pkl"
}

# Check model file exists
model_path = paths[model_choice]

if not os.path.exists(model_path):
    st.error(f"Model file not found: {model_path}")
    st.write("Available Files:", os.listdir())
    st.stop()

# Load Model
model = joblib.load(model_path)

st.success(f"{model_choice} model loaded successfully")

# Upload Test CSV
uploaded_file = st.file_uploader(
    "Upload Test CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")
    st.dataframe(df.head())

    # Target column
    target_column = "Target"

    if target_column not in df.columns:
        st.error(
            "Target column not found. Please upload a CSV containing a 'Target' column."
        )
        st.stop()

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Prediction
    y_pred = model.predict(X)

    # Metrics
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    mcc = matthews_corrcoef(y, y_pred)

    # AUC
    try:
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X)[:, 1]
            auc = roc_auc_score(y, y_prob)
        elif hasattr(model, "decision_function"):
            y_score = model.decision_function(X)
            auc = roc_auc_score(y, y_score)
        else:
            auc = "Not Available"
    except:
        auc = "Not Available"

    st.subheader("Evaluation Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Accuracy", round(accuracy, 4))
    col2.metric("Precision", round(precision, 4))
    col3.metric("Recall", round(recall, 4))

    col4, col5, col6 = st.columns(3)

    col4.metric("F1 Score", round(f1, 4))
    col5.metric("MCC", round(mcc, 4))

    if auc != "Not Available":
        col6.metric("AUC", round(auc, 4))
    else:
        col6.metric("AUC", "N/A")

    # Confusion Matrix
    st.subheader("Confusion Matrix")

    cm = confusion_matrix(y, y_pred)

    cm_df = pd.DataFrame(
        cm,
        index=["Actual 0", "Actual 1"],
        columns=["Predicted 0", "Predicted 1"]
    )

    st.dataframe(cm_df)

    # Classification Report
    st.subheader("Classification Report")

    report = classification_report(
        y,
        y_pred,
        output_dict=True
    )

    report_df = pd.DataFrame(report).transpose()

    st.dataframe(report_df)
