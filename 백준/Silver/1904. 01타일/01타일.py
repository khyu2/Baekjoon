n = int(input())
d = [0 for _ in range(n+10)]
MOD = 15746

d[1], d[2] = 1, 2
for i in range(3, n + 1):
  d[i] = (d[i-1] + d[i-2]) % MOD
print(d[n])