#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Function to collect user input for training or test set
def collect_data_set(label):
    while True:
        try:
            n = int(input(f"Enter the number of {label} samples (positive integer): "))
            if n <= 0:
                raise ValueError("Number of samples must be positive.")
            break
        except ValueError as e:
            print(e)

    data = []
    for i in range(n):
        while True:
            try:
                x = float(input(f"Enter x value for {label} sample {i + 1}: "))
                y = int(input(f"Enter y value for {label} sample {i + 1} (non-negative integer): "))
                if y < 0:
                    raise ValueError("Class label y must be a non-negative integer.")
                data.append((x, y))
                break
            except ValueError as e:
                print(e)
    
    return np.array(data)

# Collect training and test sets
print("Collecting Training Set")
train_data = collect_data_set("training")
print("Collecting Test Set")
test_data = collect_data_set("test")

# Split data into features and labels
X_train = train_data[:, 0].reshape(-1, 1)
y_train = train_data[:, 1]
X_test = test_data[:, 0].reshape(-1, 1)
y_test = test_data[:, 1]

# Ensure the number of samples is sufficient for cross-validation
if len(X_train) < 2:
    raise ValueError("Number of training samples must be at least 2 to perform cross-validation.")
if len(X_train) < 5:
    print("Warning: Number of training samples is less than the number of splits (5) for cross-validation. Adjusting cv to match sample size.")
    cv_splits = len(X_train)
else:
    cv_splits = 5

# Define the kNN model and the hyperparameter range
knn = KNeighborsClassifier()
param_grid = {'n_neighbors': list(range(1, 11))}  # k values from 1 to 10

# Perform grid search
grid_search = GridSearchCV(knn, param_grid, cv=cv_splits)
grid_search.fit(X_train, y_train)

# Get the best model and its parameters
best_k = grid_search.best_params_['n_neighbors']
best_model = grid_search.best_estimator_

# Predict and calculate accuracy on the test set
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Output the results
print(f"Best k for kNN Classifier: {best_k}")
print(f"Test set accuracy: {accuracy:.2f}")


# 

# In[ ]:




