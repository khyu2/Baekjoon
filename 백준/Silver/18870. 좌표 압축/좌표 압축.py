import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
b = {}

cp_a = list(set(a))
cp_a.sort()

for i in range(len(cp_a)):
  if cp_a[i] not in b:
    b[cp_a[i]] = i

for i in a:
  print(b[i], end=' ')