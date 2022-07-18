import heapq
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        length = len(nums)
        
        for i in range(length - 1):
            x = heapq.heappop(nums)
            
        y = heapq.heappop(nums)
        
        return (x-1)*(y-1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        for num in nums:
            if len(heap) < 2:
                heapq.heappush(heap,num)
            else:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
                
        return (heap[0] - 1) * (heap[1] - 1)