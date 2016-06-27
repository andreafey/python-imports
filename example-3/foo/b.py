import foo.a as a

class B:
  def __init__(self, b):
    self.b = b

  def set_a(self):
    self.a = a.A('my a')
