import streamlit as st
from utils.utils import load_data, load_model
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve, auc
import matplotlib.pyplot as plt

def show_model_performance():
    st.title("Model Performance")
    data = load_data()
    model = load_model()

    X = data[["sensor1", "sensor2", "sensor3"]]
    y = data["failure"]
    train_size = int(0.7 * len(data))
    X_test, y_test = X.iloc[train_size:], y.iloc[train_size:]

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    acc = (y_pred == y_test).mean()
    st.metric("Test Accuracy", f"{acc*100:.2f}%")

    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Failure", "Failure"])
    fig_cm = disp.plot(cmap="Blues", values_format="d").figure_
    st.pyplot(fig_cm)

    st.subheader("ROC Curve")
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    ax.plot([0, 1], [0, 1], "--", label="Random Chance")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend(loc="lower right")
    st.pyplot(fig)
