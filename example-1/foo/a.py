import foo.b

class A:
  def __init__(self, a):
    self.a = a

  def set_b(self):
    self.b = foo.b.B('my b')
