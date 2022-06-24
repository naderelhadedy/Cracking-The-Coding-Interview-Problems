def countWays(n: int) -> int:
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return countWays(n-1) + countWays(n-2) + countWays(n-3)

countWays(4)

countWays(3)

ways = {0:1}
def countWays_memo(n: int) -> int:
  if n < 0:
    return 0
  if n not in ways:
    ways[n] = countWays_memo(n-1) + countWays_memo(n-2) + countWays_memo(n-3)
  return ways[n]

countWays_memo(4)

countWays_memo(3)