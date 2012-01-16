"""A collection of abstract data types."""
from collections import deque

"""While a deque can do anything a queue can do and more, by limiting the
the number of available actions we achieve two things:
  * It becomes semantically clear how we intend to use a data-structure.
  * We can strengthen the invariants.
A similiar argument can be made for using a stack in place of a list.
"""
from stack_adt import *

class Stack(object):
  """A first-in last-out data structure.
  A stack is guaranteed to always have at least 0 elements,
  and to always maintain the first-in first-out property."""
  def __init__(self):
    self._items = []

  def __len__(self):
    return len(self._items)

  @property
  def empty(self):
    return len(self) == 0

  @property
  @TopContract()
  def top(self):
    return self._items[-1]

  @PushContract()
  def push(self, item):
    '''S.push(object) -- push object on top.'''
    self._items.append(item)

  @PopContract()
  def pop(self):
    '''S.pop() -> item -- remove and return top item.
    Raises IndexError if stack is empty.
    '''
    try:
      return self._items.pop()
    except IndexError:
      raise IndexError("pop from empty stack")
