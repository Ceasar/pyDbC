"""
Contracts for Python.

Contracts can be disabled by running the interpreter with optimization (-O)
turned on.
"""
import copy


class Contract(object):
  """A contract for a object methods."""
  def __init__(self):
    self.old = None
    self.result = None


  def __call__(self, func):
    if __debug__:
      def supplier(instance, *args, **kwargs):
        self.require(instance, *args, **kwargs)
        self.old = copy.deepcopy(instance)
        self.result = result = func(instance, *args, **kwargs)
        self.ensure(instance, *args, **kwargs)
        self.invariant(instance, *args, **kwargs)
        return result
      return supplier
    else:
      return func


  def require(self, instance, *args, **kwargs):
    pass

  def invariant(self, instance, *args, **kwargs):
    pass

  def ensure(self, instance, *args, **kwargs):
    pass
