#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Ask the user for input N (positive integer)
N = int(input("Enter a positive integer N: "))


# In[2]:


# Step 2: Read N numbers from the user
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)


# In[5]:


# Step 3: Ask the user for input X (integer)
X = int(input("Enter an integer X: "))


# In[6]:


# Step 4: Check if X is in the list of numbers and output the result
if X in numbers:
    # Output the 1-based index (index + 1)
    print(numbers.index(X) + 1)
else:
    # Output -1 if X is not found
    print("-1")


# In[ ]:




