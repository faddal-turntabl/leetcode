import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i in range(len(mat)):
            heap.append((sum(mat[i]),i))
                    
        heapq.heapify(heap)
                
        ans = []
        
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
            
        return ans

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i in range(len(mat)):
            heapq.heappush(heap,(sum(mat[i]),i))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
            
        return ans