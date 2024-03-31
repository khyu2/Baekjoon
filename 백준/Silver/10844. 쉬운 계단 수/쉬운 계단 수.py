MOD = 10**9

n = int(input())
d = [[0 for _ in range(10)] for _ in range(n)]
for i in range(1, 10):
  d[0][i] = 1

for i in range(1, n):
  for j in range(10):
    if j == 0:
      d[i][j] = d[i-1][1]
    elif j == 9:
      d[i][j] = d[i-1][8]
    else:
      d[i][j] = d[i-1][j-1] + d[i-1][j+1]
    d[i][j] %= MOD

print(sum(d[n-1]) % MOD)