# type: ignore
def dataclass(*, init=True, repr=True, eq=True):
  def wrap(cls):
    fields = cls.__annotations__

    if init:
      def __init__(self, **kwargs):
        for name, value in kwargs.items():
          setattr(self, name, value)

      cls.__init__ = __init__

    if repr: 
      def __repr__(self):
        values = ", ".join(f"{k}={getattr(self, k)!r}" for k in fields)
        return f"{cls.__name__}({values})"

    if eq:
      def __eq__(self, other):
        for k in fields:
          if getattr(self, k) != getattr(other, k):
            return False

        return True

  return wrap