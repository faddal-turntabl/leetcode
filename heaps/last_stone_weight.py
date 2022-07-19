import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        original    : sorted
        2 7 4 1 8 1 : 1 1 2 4 7 8
        pick 7 & 8
        
        2 4 1 1 1 : 1 1 1 2 4
        pick 2 & 4
        
        2 1 1 1: 1 1 1 2
        pick 1 & 2
        
        1 1 1: 1 1 1
        pick 1 & 1
        
        1
        
        return 1
        
        
        BRUTE FORCE APPROACH
        
        while the length of the array is greater than 1
            sort the array
            pop the last 2 items (those will be the 2 largest)
            
            find their difference
            if the difference is not zero, push to the heap
            
        return 0 if array is empty else return the only element left
        
        COMPLEXITY:
        O(n^2 log n) time : an outside loop sorting an array in each iteration n * nlogn
        O(1) space
            
        OPTIMIZED APPROACH (using a max heap)
    
        heapify the stones: 
        since python has only a min heap, negate all the stones before heapifying
        
        loop through while the len(stones) > 1
            pop twice for the top 2 largest
            find their difference

            if the difference is not zero push to the heap

        COMPLEXITY
        O(nlogn) time: outside loop with heapifying in each iteration n * logn
        O(n) space for the max heap stones
        
        '''
        # brute force
        while len(stones) > 1:
            stones.sort()
            
            diff = stones.pop() - stones.pop()
            
            if diff:
                stones.append(diff)
                
        return stones[0] if stones else 0
        
        # Optimized
        stones = [-stone for stone in stones]
    
        heapq.heapify(stones)
        
        while len(stones) > 1:
            diff = heapq.heappop(stones) - heapq.heappop(stones)
            
            if diff:
                heapq.heappush(stones,diff)
                
        return -1*stones[0] if stones else 0
        
        