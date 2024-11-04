class NumberProcessor:
    def __init__(self):
        """Initializes an empty list to store numbers."""
        self.numbers = []

    def add_number(self, number):
        """Adds a number to the list."""
        self.numbers.append(number)

    def find_number(self, x):
        """Finds the index (1-based) of number x in the list.
        
        Args:
            x (int): The number to find.
        
        Returns:
            int: The 1-based index if found, or -1 if not found.
        """
        try:
            # Find the 0-based index and convert it to 1-based
            index = self.numbers.index(x) + 1
            return index
        except ValueError:
            # Return -1 if the number is not in the list
            return -1