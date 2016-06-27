import foo.a

class B:
  def __init__(self, b):
    self.b = b

  def set_a(self):
    self.a = foo.a.A('my a')
