def one_away(string1: str, string2: str):
  codes1 = [0 for _ in range(256)]
  codes2 = [0 for _ in range(256)]
  if abs(len(string1) - len(string2)) > 1:
    return False
  for char in string1:
    codes1[ord(char)] += 1
  for char in string2:
    codes2[ord(char)] += 1
  diff = [abs(codes1[i] - codes2[i]) for i in range(256)]
  if sum(diff) > 2:
    return False
  return True

one_away('pale', 'bake')