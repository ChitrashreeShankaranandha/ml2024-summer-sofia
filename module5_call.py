#!/usr/bin/env python
# coding: utf-8

# In[3]:


from module5_mod import NumberProcessor

def main():
    # Initialize the NumberProcessor instance
    processor = NumberProcessor()

    # Prompt user for the number of inputs
    try:
        n = int(input("Enter the number of elements, N (positive integer): "))
        if n <= 0:
            raise ValueError("N must be a positive integer.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return

    # Collect N numbers from the user
    print(f"Please enter {n} numbers:")
    for i in range(n):
        while True:
            try:
                number = int(input(f"Enter number {i + 1}: "))
                processor.add_number(number)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Ask for the number to search for
    try:
        x = int(input("Enter the number to search for, X: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Search for the number and print the result
    index = processor.find_number(x)
    if index == -1:
        print("-1")
    else:
        print(f"The number {x} was found at position {index}.")

if __name__ == "__main__":
    main()


# In[ ]:




