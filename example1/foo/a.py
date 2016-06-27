import example1.foo.b

class A:
  def __init__(self, a):
    self.a = a

  def set_b(self):
    self.b = example1.foo.b.B('my b')

