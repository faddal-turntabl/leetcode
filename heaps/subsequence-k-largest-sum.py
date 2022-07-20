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


# someones solutions

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tuple_heap = [] # Stores (value, index) as min heap
        for i, val in enumerate(nums):
            if len(tuple_heap) == k:
                heappushpop(tuple_heap, (val, i)) # To prevent size of heap growing larger than k
            else:
                heappush(tuple_heap, (val, i))
		# heap now contains only the k largest elements with their indices as well.
        tuple_heap.sort(key=lambda x: x[1]) # To get the original order of values. That is why we sort it by index(x[1]) & not value(x[0])
        ans = []
        for i in tuple_heap:
            ans.append(i[0])
        return ans


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Heap to keep track of max values, and map to output ordering by index
        pq = []
        heapq.heapify(pq)
        indexes = {}
        for index, num in enumerate(nums):
            # Add all values to heap and map
            heapq.heappush(pq, (num, index))
            indexes[index] = num
            # If we have more values than can be returned, remove the smallest from both the heap and the map
            if len(pq) > k:                
                del indexes[heapq.heappop(pq)[1]]
        # Return the values in the map, which represent the answers ordered in this case
        return indexes.values()