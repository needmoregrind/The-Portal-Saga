import unittest
from stack import LinkedStack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = LinkedStack()

    def test_init(self):
        """Test that the stack is initialized correctly as empty."""
        self.assertEqual(self.stack._size, 0)
        self.assertEqual(str(self.stack), "empty stack")

    def test_push_only(self):
        """Test pushing an item onto an empty stack."""
        self.stack.push(1)
        self.assertEqual(self.stack._size, 1)
        self.assertEqual(str(self.stack), "top --> 1")

    def test_push(self):
        """Test pushing multiple items onto the stack."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack._size, 3)
        self.assertEqual(str(self.stack), "top --> 3 2 1")

    def test_peek_empty(self):
        """Test peeking an empty stack."""
        self.assertEqual(self.stack.peek(), None)
        self.assertEqual(self.stack._size, 0)
        self.assertEqual(str(self.stack), "empty stack")

    def test_peek(self):
        """Test peeking after pushing multiple items."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack._size, 3)
        self.assertEqual(str(self.stack), "top --> 3 2 1")

    def test_pop_empty(self):
        """Test popping an empty stack."""
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack._size, 0)
        self.assertEqual(str(self.stack), "empty stack")

    def test_pop(self):
        """Test popping after pushing multiple items."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack._size, 2)
        self.assertEqual(str(self.stack), "top --> 2 1")

if __name__ == '__main__':
    unittest.main()