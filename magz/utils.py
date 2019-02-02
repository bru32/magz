"""
General utils
Bruce Wernick
10 October 2017 15:38:10
"""

__all__ = ['counter', 'frange', 'linrange']


class Counter:
  "General purpose counter using dictionary"
  value = {}

  def __call__(self):
    return self.value

  def total(self):
    total = 0
    for k,v in list(self.value.items()):
      total += v
    return total

  def reset(self):
    "reset value to empty dict"
    self.value = {}

  def up(self, key):
    "incrementer"
    if key in self.value:
      self.value[key] += 1
    else:
      self.value[key] = 1

  def down(self, key):
    "decrementer"
    if key in self.value:
      self.value[key] -= 1
    else:
      self.value[key] = 0


# ------------------------------------------------------------------------------

def frange(start, stop, step):
  "floating point range"
  i = start
  while i < stop:
    yield i
    i += step

def linrange(start, final, count):
  "generate a linear floating point range"
  for i in range(count):
    value = start + (final-start)*float(i)/(count-1)
    yield value


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  for item in linrange(1.2, 23.5, 5):
    print (item)

