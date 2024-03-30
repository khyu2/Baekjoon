n = int(input())
for i in range(31):
  if n == (1 << i):
    print(1)
    exit(0)
print(0)