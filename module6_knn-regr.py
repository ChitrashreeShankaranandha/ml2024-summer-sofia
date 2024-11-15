#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.spatial import distance

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.points = np.empty((0, 2))  

    def add_point(self, x, y):
        self.points = np.append(self.points, [[x, y]], axis=0)

    def predict(self, X):
        if self.k > len(self.points):
            raise ValueError("Error: k should be less than or equal to the number of points (N).")

        # Calculate distances from X to each x-coordinate in points
        distances = distance.cdist([[X]], self.points[:, [0]], 'euclidean').flatten()
        
        # Get indices of the k-nearest neighbors
        nearest_indices = distances.argsort()[:self.k]
        
        # Get the y-values of the k-nearest neighbors and calculate the mean
        y_values = self.points[nearest_indices, 1]
        return np.mean(y_values)

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




