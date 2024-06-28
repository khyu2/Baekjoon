import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
b = input()
st = []

for i in s:
  st.append(i)

  while len(st) >= len(b) and ''.join(st[-len(b):]) == b:
    del st[-len(b):]

if st: print(*st, sep='')
else: print('FRULA')
