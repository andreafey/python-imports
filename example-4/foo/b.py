class B:
  def __init__(self, b):
    self.b = b

  def set_a(self):
    import foo.a as a
    self.a = a.A('my a')
