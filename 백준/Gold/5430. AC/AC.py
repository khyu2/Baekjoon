import sys
from collections import deque
input = sys.stdin.readline

tc = int(input().rstrip())

for _ in range(tc):
  p = input().rstrip()
  n = int(input().rstrip())
  a = input().rstrip()
  dq = deque([int(num) for num in a.strip('[]').split(',') if num])
  reverse = False
  error = False

  for i in p:
    if i == 'R':
      reverse = False if reverse else True
    else:
      if not len(dq):
        error = True
        break
      if reverse:
        dq.pop()
      else:
        dq.popleft()

  if len(dq) and not error:
    print('[', end='')
    if reverse:
      while dq: print(dq.pop(), end=',' if len(dq) else ']\n')
    else:
      while dq: print(dq.popleft(), end=',' if len(dq) else ']\n')
  elif error:
    print('error')
  else:
    print('[]')