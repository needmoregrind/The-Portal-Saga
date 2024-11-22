class MyList:

    def __init__(self, initial_capacity=4):
        # Initialize an empty list with an initial capacity
        self.capacity = initial_capacity  # Initial capacity of the list
        self.size = 0  # Number of elements in the list
        self.array = [None] * self.capacity  # Create an array with the initial capacity

    def insert(self, data, index=None):  # Set index=None as the default
    # Handle insertion at the end if no index is provided
        if index is None or index < 0:
            index = self.size  # Set index to the end of the list
        # If index is greater than the size, set it to size (add to the end)
        if index > self.size:
            index = self.size

        if self.size == self.capacity:
            self._expand_capacity()

        # Shift elements to the right to make space for the new element
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = data
        self.size += 1

    def _expand_capacity(self):
        # Double the capacity
        self.capacity *= 2
        # Create a new array with the updated capacity
        new_array = [None] * self.capacity
        # Copy elements from the old array to the new one
        for i in range(self.size):
            new_array[i] = self.array[i]
        # Replace the old array with the new array
        self.array = new_array

    def is_empty(self):
        return self.size == 0
    
    def delete(self, index):
        if self.is_empty() or index < 0 or index >= self.size:
            return None  # Return None if the list is empty or index is invalid
        
        value = self.array[index]  # Store the value to return
        self._remove_at_index(index)  # Remove the element at the specified index
        return value  # Return the removed value
    
    def remove(self, data):
        for i in range(self.size):
            if self.array[i] == data:
                self._remove_at_index(i)  # Remove the first instance of data
                return  # Exit after removing the first occurrence
        # If data isn’t found, do nothing
    
    def _remove_at_index(self, index):
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

    def peek(self, index):
        """Return the data at the specified index. Return None if index is invalid."""
        if index < 0 or index >= self.size:
            return None
        return self.array[index]
    
    def find(self, data):
        """Return the index of the first instance of data, or -1 if not found.
        
    The runtime of this method is O(n), where n is the number of elements in the list.
    This is because, in the worst-case scenario, we must check each element in the list 
    until we find the target data or reach the end of the list. 
    Thus, the time taken grows linearly with the size of the list.
    """
        for i in range(self.size):
            if self.array[i] == data:
                return i  # Return the index of the first match
        return -1  # Return -1 if the data is not found
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.is_empty():
            return "empty list"
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"

    def count(self, data):
        """Return the number of times data appears in the list."""
        count = 0
        for i in range(self.size):
            if self.array[i] == data:
                count += 1
        return count
    
