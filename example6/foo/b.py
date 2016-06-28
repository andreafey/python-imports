from example6.foo.a import A

class B:
  def __init__(self, b):
    self.b = b

  def set_a(self):
    self.a = A('my a')
