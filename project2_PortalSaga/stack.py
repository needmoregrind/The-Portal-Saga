class Node:
    def __init__(self, data=None, next_node=None):
        self._data = data
        self._next = next_node

class LinkedStack:
    def __init__(self):
        self._top = None  # The top node in the stack
        self._size = 0  # Size of the stack

    def push(self, data):
        """Push a new element onto the stack"""
        '''
        Places an item on top of the stack.

        Runtime Analysis:
        -----------------
        The runtime of this push operation is O(1) (constant time).
        - The operation involves creating a new node (which takes constant time, O(1)).
        - The new node is inserted at the start of the linked list, which is O(1), as the linked list maintains a reference to the first node.
        - No traversal of the list is required to add the node, because the stack is implemented in a way that always inserts at the head (top of the stack).
        
        Thus, every step in the push method takes constant time, leading to an overall O(1) runtime.
        
        '''
        new_node = Node(data, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """Pop the top element off the stack and return its value"""
        if self.isEmpty():
            return None
        data = self._top._data
        self._top = self._top._next
        self._size -= 1
        return data

    def peek(self):
        """Return the top element without removing it"""
        if self.isEmpty():
            return None
        return self._top._data

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def isEmpty(self):
        """Check if the stack is empty"""
        return self._size == 0

    def isFull(self):
        """For a linked stack, the stack is never full."""
        return False

    def __str__(self):
        """Return a string representation of the stack"""
        if self.isEmpty():
            return "empty stack"
        
        result = "top --> "
        current = self._top
        while current is not None:
            result += str(current._data) + " "
            current = current._next
        return result.strip()
    
# p= LinkedStack()
# p.push('A')
# p.push('B')
# p.push('C')

# print(p)