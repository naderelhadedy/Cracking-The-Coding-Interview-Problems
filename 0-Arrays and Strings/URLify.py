def urlify(theStr:str, length:int):
  res = theStr[:length]
  for i in range(len(res)):
    if res[i] == ' ':
      res = res[0:i]+'%20'+res[i+1:]
  return res

urlify("Mr John Smith ", 13)