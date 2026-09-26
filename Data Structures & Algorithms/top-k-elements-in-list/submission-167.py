from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count all occoruances
        counts = Counter(nums)
        print(counts)

        # extract k most frequent occs
        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)

        # format and return res
        res = []    
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
