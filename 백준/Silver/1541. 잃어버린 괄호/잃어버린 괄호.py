# (-) 인데 값이 온 경우 tmp 에 누적
# (-) 아닌데 값이 온 경우 answer 에 누적
# (-) 인데 다시 - 가 오거나 끝나는 경우 answer 에 누적
# 50-(50+30)-40 = -70

s = input()
s += '+' 
str_tmp = ""
answer = 0
tmp = 0
minus = False
for i in s:
  if i.isnumeric():
    str_tmp += i
    continue

  x = int(str_tmp)
  str_tmp = ""
  # print(x, answer, tmp)

  if i == '+':
    if minus:
      tmp -= x
    else:
      answer += x
  else:
    if minus:
      tmp -= x
    else:
      minus = True
      answer += x

answer += tmp
print(answer)
