from example2.foo import b

class A:
  def __init__(self, a):
    self.a = a

  def set_b(self):
    self.b = b.B('my b')

