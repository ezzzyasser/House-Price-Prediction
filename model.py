import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

import joblib

df = pd.read_csv('modified_housing.csv')

X = df.drop('median_house_value', axis=1)
y = df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numeric_features = X.select_dtypes(include=['float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns


numeric_imputer = SimpleImputer(strategy='mean')
X_train_scaled = numeric_imputer.fit_transform(X_train[numeric_features])
X_test_scaled = numeric_imputer.transform(X_test[numeric_features])

categorical_encoder = OneHotEncoder()
X_train_encoded = categorical_encoder.fit_transform(X_train[categorical_features])
X_test_encoded = categorical_encoder.transform(X_test[categorical_features])

X_train_preprocessed = np.hstack((X_train_scaled, X_train_encoded.toarray()))
X_test_preprocessed = np.hstack((X_test_scaled, X_test_encoded.toarray()))

model = LinearRegression()
model.fit(X_train_preprocessed, y_train)

joblib.dump(model, 'model.pkl')

