import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import time

# 1. Define Paths
dataset_path = 'Dataset/PhiUSIIL_Phishing_URL_Dataset.xlsx'
model_export_path = 'phishing_rf_model.pkl'

print("Loading dataset... This might take a minute.")
df = pd.read_excel(dataset_path)

# 2. Separate Features and Target
print("Separating features and target labels...")
X = df.drop(columns=['label'])
y = df['label']

# 3. Split the Data
print("Splitting data: 80% for training, 20% for testing...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set: {X_train.shape[0]} rows")
print(f"Testing set: {X_test.shape[0]} rows")

# 4. Initialize and Train the Model
# n_jobs=-1 tells the model to use all your CPU cores for faster processing
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

print("\nTraining the Random Forest model... Please wait.")
start_time = time.time()
rf_model.fit(X_train, y_train)
end_time = time.time()

print(f"Training completed in {end_time - start_time:.2f} seconds.")

# 5. Evaluate the Model
print("\nGenerating predictions on the test set...")
predictions = rf_model.predict(X_test)

print("\n--- Classification Report ---")
print(classification_report(y_test, predictions))

print("--- Confusion Matrix ---")
print(confusion_matrix(y_test, predictions))

# 6. Export the Model
print(f"\nExporting the trained model to '{model_export_path}' for the backend API...")
joblib.dump(rf_model, model_export_path)
print("Export complete. Pipeline finished successfully.")