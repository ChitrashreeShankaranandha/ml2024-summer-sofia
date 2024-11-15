#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.points = np.empty((0, 2))  # Initialize an empty array for (x, y) points

    def add_point(self, x, y):
        self.points = np.append(self.points, [[x, y]], axis=0)

    def calculate_variance(self):
        # Calculate and return the variance of y-values (labels) in the dataset
        y_values = self.points[:, 1]
        return np.var(y_values)

    def predict(self, X):
        if self.k > len(self.points):
            raise ValueError("Error: k should be less than or equal to the number of points (N).")

        # Split points into input (x-values) and output (y-values)
        x_values = self.points[:, 0].reshape(-1, 1)
        y_values = self.points[:, 1]

        # Initialize and fit the k-NN regressor
        knn_regressor = KNeighborsRegressor(n_neighbors=self.k)
        knn_regressor.fit(x_values, y_values)

        # Predict the y value for the given X
        predicted_y = knn_regressor.predict([[X]])
        return predicted_y[0]

def main():
    # Read N and k from user input
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k: "))

    knn_model = KNNRegression(k)

    # Read N points from user input
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        knn_model.add_point(x, y)

    # Calculate and display variance of y-values in the training dataset
    variance_y = knn_model.calculate_variance()
    print(f"The variance of y-values in the training data is: {variance_y}")

    # Read X value for prediction
    X = float(input("Enter the X value for prediction: "))

    # Perform k-NN regression and print the result
    try:
        predicted_y = knn_model.predict(X)
        print(f"The predicted Y value is: {predicted_y}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


# In[ ]:




