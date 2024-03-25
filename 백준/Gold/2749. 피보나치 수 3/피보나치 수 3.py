mod = 1000000

class Matrix:
  def __init__(self, data):
    self.data = data
  
  def __mul__(self, other):
    n = len(self.data)

    res = [[0] * n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        for k in range(n):
          res[i][j] += self.data[i][k] * other.data[k][j]
          res[i][j] %= mod
    return Matrix(res)
  
  def __mod__(self, mod):
    n = len(self.data)

    for i in range(n):
      for j in range(n):
        self.data[i][j] %= mod
    return self.data
  
  def get_fibo(self):
    return self.data[0][1]

def power(x, n):
  if n == 0: return Matrix([[1, 0], [0, 1]])
  if n == 1: return x
  half = power(x, n // 2)
  if n & 1: return half * half * x
  return half * half

a = Matrix([[1, 1], [1, 0]])
print(power(a, int(input())).get_fibo())