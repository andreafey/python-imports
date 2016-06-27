import example1.foo.a

class B:
  def __init__(self, b):
    self.b = b

  def set_a(self):
    self.a = example1.foo.a.A('my a')
