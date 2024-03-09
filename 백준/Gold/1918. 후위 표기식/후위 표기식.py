import sys
input = lambda: sys.stdin.readline().rstrip()

op = {'(' : 0, ')' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2}
a = input()
stack = []
res = []

for i in a:
  if i.isalnum(): res.append(i)
  elif i == '(': stack.append(i)
  elif i == ')': 
    while stack and stack[-1] != '(': res.append(stack.pop())
    stack.pop()
  else:
    while stack and op[i] <= op[stack[-1]]: res.append(stack.pop())
    stack.append(i)

while stack:
  res.append(stack.pop())

print(*res, sep='')
