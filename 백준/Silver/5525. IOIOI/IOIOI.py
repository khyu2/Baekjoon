n = int(input())
m = int(input())
s = input()

ans = 0
combo = 0
i = 0
while i < m - 2:
  if s[i:i+3] == 'IOI':
    combo += 1
    i += 1

    if combo == n:
      combo -= 1
      ans += 1
  else: combo = 0
  i += 1

print(ans)