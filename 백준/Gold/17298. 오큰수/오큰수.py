import sys
input = lambda: sys.stdin.readline().rstrip()

def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums) # 결과를 저장할 배열을 -1로 초기화
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i] # 현재 값이 스택의 top에 해당하는 인덱스의 다음 큰 수임을 기록
        stack.append(i) # 현재 인덱스를 스택에 추가
    
    return result

n = int(input())
a = list(map(int, input().split()))

print(' '.join(map(str, next_greater_element(a))))