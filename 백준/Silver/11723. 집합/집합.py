import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
bit = 0
for i in range(n):
  op, *x = input().split()
  if x:
    x = int(x[0]) - 1
    if op == 'add': bit |= (1 << x)
    elif op == 'remove': bit &= ~(1 << x)
    elif op == 'toggle': bit ^= (1 << x)
    else: print(1 if (bit & (1 << x)) == (1 << x) else 0)
  elif op == 'all': bit = (1 << 20) - 1
  else: bit = 0