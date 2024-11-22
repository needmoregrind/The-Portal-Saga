from mylist import MyList

class LinkedQueue:
    """
    Linked Queue ADT with MyList as the underlying data structure.
    """
    def __init__(self):
        self._items = MyList()  # Using MyList for dynamic storage.
        
    def enqueue(self, data):
        """Add an item to the end of the queue."""
        self._items.insert(data)  # Insert at the end (default behavior).
    
    def dequeue(self):
        """Remove and return the front item of the queue."""
        return self._items.delete(0)  # Remove the first item (index 0).
    
    def peek(self):
        """Return the front item without removing it."""
        return self._items.peek(0)  # Peek at the first item (index 0).
    
    def is_empty(self):
        """Return True if the queue is empty, otherwise False."""
        return len(self._items) == 0
    
    def __len__(self):
        """Return the number of items in the queue."""
        return len(self._items)
    
    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "empty queue"
        
        contents = " ".join(str(self._items.peek(i)) for i in range(len(self._items)))
        return f"front --> {contents} <-- back"

