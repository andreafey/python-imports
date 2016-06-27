class A:
  def __init__(self, a):
    self.a = a

  def set_b(self):
    import example4.foo.b as b
    self.b = b.B('my b')
