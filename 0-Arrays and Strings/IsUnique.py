def is_unique(theStr: str = ''):
  for i in range(1, len(theStr)):
    if theStr[i] in theStr[0:i-1]:
      return False
  return True

is_unique()

is_unique('abc')

is_unique('abca')