import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your dataset
data = pd.read_csv('loan_data.csv')
X = data.drop('risk', axis=1)
y = data['risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(min_samples_leaf=1, max_features='auto', random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'loan_model.pkl')