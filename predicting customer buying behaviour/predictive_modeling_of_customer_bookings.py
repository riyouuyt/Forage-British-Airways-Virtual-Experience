import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
dataset_path = 'Downloads/Dataset/customer_booking.csv'  
df = pd.read_csv(dataset_path, encoding="ISO-8859-1")

# Data Preparation and Cleaning
df['flight_day'] = df['flight_day'].map({
    "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7 # encode the flight_day into numeric
})

df['purchase_lead'] = np.log(df['purchase_lead'] + 1) # log transformation for the numeric columns 
df['length_of_stay'] = np.log(df['length_of_stay'] + 1)

# Feature Engineering
df['purchase_lead_length_of_stay_interaction'] = df['purchase_lead'] * df['length_of_stay']
df['flight_hour_bin'] = pd.cut(df['flight_hour'], bins=3, labels=['morning', 'afternoon', 'evening'])

# Scaling the Numerical Features
scaler = StandardScaler()
numeric_cols = ['purchase_lead', 'length_of_stay', 'flight_hour', 'flight_duration']
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Encoding Categorical Data
categorical_cols = ['sales_channel', 'trip_type', 'booking_origin', 'wants_extra_baggage', 'wants_preferred_seat', 'wants_in_flight_meals']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Define features (X) and target variable (y)
X = df_encoded.drop(columns=['booking_complete'])  # Features
y = df_encoded['booking_complete']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeling - Gradient Boosting Classifier
gb_model = GradientBoostingClassifier(random_state=42)
gb_model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = gb_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Gradient Boosting Classifier:")
print(f"Model Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

# Feature Importance
feature_importance = gb_model.feature_importances_
feature_names = X.columns
sorted_idx = np.argsort(feature_importance)[::-1]

top_features = 10
print("Top 10 Most Important Features:")
for i in range(top_features):
    print(f"{feature_names[sorted_idx[i]]}: {feature_importance[sorted_idx[i]]}")
