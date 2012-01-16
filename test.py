import unittest

from stack import Stack


class TestStack(unittest.TestCase):
  def setUp(self):
    self.stack = Stack()

  def test_blackbox(self):
    self.stack.push(1)
    self.stack.push(5)
    self.stack.push(3)
    self.assertEqual(self.stack.top, 3)
    self.stack.pop()
    self.assertEqual(self.stack.top, 5)

if __name__ == "__main__":
  unittest.main()
