from contract import Contract


class TopContract(Contract):
  """Top element."""
  def require(self, instance, *args, **kwargs):
    assert not instance.empty
    return True


class PushContract(Contract):
  """Add item on top."""
  def ensure(self, instance, item):
    assert not instance.empty
    assert instance.top == item
    assert len(instance) == len(self.old) + 1, "%s != %s" % (len(instance), len(self.old) + 1)
    return True


class PopContract(Contract):
  """Remove top element."""
  def require(self, instance):
    assert not instance.empty
    return True

  def ensure(self, instance):
    assert len(instance) == len(self.old) - 1
    assert self.result == self.old.top
    return True
