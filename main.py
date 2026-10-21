import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def run_disease_pattern_detection():
    print("==================================================")
    print("   DISEASE PATTERN DETECTION SYSTEM (ML MODEL)    ")
    print("==================================================")
    
    # 1. Health-Data Analysis & Loading Dataset (Pandas)
    try:
        df = pd.read_csv('diabetes.csv')
        print(f"[Info] Dataset successfully loaded! Shape: {df.shape}")
    except FileNotFoundError:
        print("[Error] 'diabetes.csv' file sapadli nahi! Kripaya file check kara.")
        return

    print("\n--- 2. Exploratory Data Analysis (EDA) & Correlation ---")
    print(df.head())
    
    # Correlation Analysis with Outcome
    correlation = df.corr()
    print("\nTop Correlations with Diabetes Outcome:")
    print(correlation['Outcome'].sort_values(ascending=False))

    # 3. Data Preprocessing
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    # Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("\n--- 4. Patient Clustering (Unsupervised Learning) ---")
    # Applying KMeans Clustering to group patients
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    df['Patient_Cluster'] = kmeans.fit_predict(X_scaled)
    print("Patient Clusters generated successfully!")
    print(df['Patient_Cluster'].value_counts())

    print("\n--- 5. Disease Prediction (Classification Model) ---")
    # Train-Test Split (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Building Random Forest Classification Model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    print("\n--- 6. Evaluation Performance ---")
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("==================================================")

if __name__ == "__main__":
    run_disease_pattern_detection()