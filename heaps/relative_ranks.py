from heapq import heappush, heappop, heapify

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        
        for i in range(len(score)):
            heappush(heap,(-1*score[i],i))
            
        
        ranks = [0] * len(score)
        
        k = 1
        while heap:
            i = heappop(heap)[1]
            
            if k == 1:
                ranks[i] = "Gold Medal"
            elif k == 2:
                ranks[i] = "Silver Medal"
            elif k == 3:
                ranks[i] = "Bronze Medal"
            else:
                ranks[i] = str(k)
                
            k += 1
                
        return ranks