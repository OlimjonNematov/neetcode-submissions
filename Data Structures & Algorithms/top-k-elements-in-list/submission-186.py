from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create heap
        heap = []
        ans = []
        counts = Counter(nums) #[value, count]

        # for num 
        for num in counts:
            # keep track of [count, value]
            heapq.heappush(heap, [counts[num], num])
            # clean up the heap
            if len(heap)>k:
                heapq.heappop(heap)
        
        # create the ans list
        while heap:
            ans.append(heapq.heappop(heap)[1])

        # return ans
        return ans