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