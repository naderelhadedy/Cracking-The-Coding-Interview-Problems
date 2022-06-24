map = {0:0, 1:1}
def fib(n):
  if n not in map:
    map[n] = fib(n-1) + fib(n-2)
  return map[n]

fib(5)