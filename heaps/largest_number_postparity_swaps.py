import heapq

class Solution:
    def largestInteger(self, num: int) -> int:
        '''
        1 2 3 4
        
        store a heap of even and odd numbers separately numbers
        evenHeap = [2, 4]
        oddHeap =  [1, 3]
        
        
        *loop through the given number (stringify it first)
            for each digit, 
                # note: we can only swap of same parity
                # so popping from the correspoding heap is more like replacing the current number with the largest of its type available
                
                if the digit is even, pop the largest even number from the correspondig heap
                if the digit is odd, pop the largest odd number from the corresponding heap
                
            return the popped results
        
        '''
        num_str = str(num)
        
        evenHeap = [-int(digit) for digit in num_str if int(digit) % 2 == 0]
        oddHeap = [-int(digit) for digit in num_str if int(digit) % 2 == 1]
        
        
        heapq.heapify(evenHeap)
        heapq.heapify(oddHeap)
        
        largest = []
        
        for num_s in num_str:
            if int(num_s) % 2 == 0:
                largest.append(str(-heapq.heappop(evenHeap)))
            else: 
                largest.append(str(-heapq.heappop(oddHeap)))
                
        return int("".join(largest))
        
        
        
