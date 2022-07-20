from heapq import heappush, heapify, heappop

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        '''
        sorting + heaps approach
        [-1,-2,3,4]
        
        1. store [index,num] of nums in a list 
           [ [0,-1]  [1,-2]  [2,3] [3,4] ]
           
        2. sort in descending order of num (so that first K are the largest)
            [ [3,4] [2,3] [0,-1] [1,-2] ]
        
        3. slice to get first K
            [ [3,4] [2,3] [0,-1] ]
            
        4. heapify into minHeap
        
        5. pop out and pick num in an iteration loop (the pop would return the pair with the smallest index each time)
        
        
        purely heaps approach
        
        1. store each number and its index as a pair in a maxheap : [num, index]
           (this ensures that, when the first k pairs get popped, they are the largest)
           
        2. pop out first K into a minHeap in the format [index,num]
           the [index, num] format ensures minHeap pops out the pair with the least index
           
        3. pop min heap into a final answer array, picking only num
        
        
        '''
        #step 1
        pairs = []
        
        for i in range(len(nums)):
            heappush(pairs,[-1*nums[i],i])
            
        #step 2
        top_k = []
        
        while len(top_k) < k:
            val, i = heappop(pairs)
            heappush(top_k,[i,val])
            
        #step 3
        final = []
        
        while top_k:
            final.append(heappop(top_k)[1] * -1)
            
        return final

        # modified
         #step 1
        pairs = []
        
        for i in range(len(nums)):
            heappush(pairs,[-nums[i],i])
            
        #step 2
        top_k = []
        
        while len(top_k) < k:
            val, i = heappop(pairs)
            heappush(top_k,i)
            
        #step 3
        final = []
        
        while top_k:
            index = heappop(top_k)
            final.append(nums[index])
            
        return final
    
            
        
            
#         pairs = []
        
#         for i in range(len(nums)):
#             pairs.append((i,nums[i]))
            
        
#         pairs.sort(key=lambda x:x[1], reverse=True)
        
        
#         pairs = pairs[:k]
        
        
#         heapify(pairs)
        
#         final = []
        
#         while pairs:
#             final.append(heappop(pairs)[1])
            
#         return final