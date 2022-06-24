def ispermutation(string: str):
  codes = [0 for _ in range(256)]
  lower_str = string.lower()
  for char in lower_str:
    codes[ord(char)] += 1

  codes[ord(' ')] = 0
  count = 0
  for val in codes:
    if val % 2:
      count += 1
      if count > 1:
        return False
  return True

ispermutation('Able was I ere I saw Elba')

ispermutation('Tact Coa')