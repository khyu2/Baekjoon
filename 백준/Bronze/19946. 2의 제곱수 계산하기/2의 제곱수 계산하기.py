def cal(idx):
  res = 1
  for i in range(64):
    res <<= 1
    if i == idx: res -= 1
  return res

x = int(input())

for i in range(65):
  if cal(i-1) == x: print(i)