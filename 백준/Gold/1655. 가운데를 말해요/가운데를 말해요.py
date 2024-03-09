import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        heapq.heappush(self.max_heap, -num)  # 최대 힙에 음수로 저장
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))  # 최대 힙의 최댓값을 최소 힙에 추가

        # 최대 힙과 최소 힙의 크기를 맞춤
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        return -self.max_heap[0]

mf = MedianFinder()

n = int(input())
for i in range(n):
    mf.addNum(int(input()))
    print(mf.findMedian())