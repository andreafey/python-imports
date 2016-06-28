from example6.foo.b import B

class A:
  def __init__(self, a):
    self.a = a

  def set_b(self):
    self.b = B('my b')

