#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.metrics import precision_score, recall_score


# In[2]:


def main():
    # Input number of points
    while True:
        try:
            N = int(input("Enter the number of points (positive integer): "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Initialize numpy arrays to store x (ground truth) and y (predicted) values
    x_values = np.zeros(N, dtype=int)
    y_values = np.zeros(N, dtype=int)

    # Input (x, y) points
    print("Provide the (x, y) points:")
    for i in range(N):
        while True:
            try:
                x = int(input(f"Enter x value for point {i+1} (0 or 1): "))
                if x in [0, 1]:
                    x_values[i] = x
                    break
                else:
                    print("x value must be 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")

        while True:
            try:
                y = int(input(f"Enter y value for point {i+1} (0 or 1): "))
                if y in [0, 1]:
                    y_values[i] = y
                    break
                else:
                    print("y value must be 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")

    # Compute Precision and Recall
    precision = precision_score(x_values, y_values)
    recall = recall_score(x_values, y_values)

    # Output the results
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()

    


# In[ ]:




