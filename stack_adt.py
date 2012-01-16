from contract import Contract


class StackInvariant(Contract):
  def invariant(self, instance):
    assert len(instance) >= 0
    assert instance.empty == (len(instance) == 0)


class TopContract(StackInvariant):
  """Top element."""
  def require(self, instance, *args, **kwargs):
    assert not instance.empty


class PushContract(StackInvariant):
  """Add item on top."""
  def ensure(self, instance, item):
    assert not instance.empty
    assert len(instance) == len(self.old) + 1
    assert instance.top == item


class PopContract(StackInvariant):
  """Remove top element."""
  def require(self, instance):
    assert not instance.empty

  def ensure(self, instance):
    assert len(instance) == len(self.old) - 1
    assert self.result == self.old.top
