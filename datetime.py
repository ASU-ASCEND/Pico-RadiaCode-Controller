import utime

class datetime: # type: ignore

  def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
    self.year = year
    self.month = month
    self.day = day
    self.hour = hour
    self.minute = minute 
    self.second = second
    # ignore other args 
   
  @classmethod
  def now(cls, tz=None):
    obj = cls.__new__(cls)
    obj.load_utime()

    return obj

  def load_utime(self):
    lt = utime.localtime()
    self.year, self.month, self.day, self.hour, self.minute, self.second, _, _ = lt


class timedelta:
  def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    self.days = int(days) + int(weeks) * 7 
    self.seconds = (int(hours) * 60 + int(minutes)) * 60 + int(seconds)
    self.microseconds = int(microseconds)
    self.milliseconds = int(milliseconds)

  def total_seconds(self):
    return self.days * 86400 + self.seconds + self.milliseconds / 1_000 + self.microseconds / 1_000_000

  def __add__(self, other):
    if isinstance(other, datetime):
      return other + self
    raise TypeError("unsupported operand type(s) for +: 'timedelta' and '{}'".format(type(other)))


  def __sub__(self, other):
    if isinstance(other, timedelta):
      # naive subtraction (not normalizing)
      return timedelta(seconds=int(self.total_seconds() - other.total_seconds()))
    raise TypeError("unsupported operand for -")

  def __repr__(self):
    return "timedelta(seconds={})".format(int(self.total_seconds()))
