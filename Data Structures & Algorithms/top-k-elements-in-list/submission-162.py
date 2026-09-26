from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count all occurances in nums
        counts = Counter(nums)
        print(counts)

        # extract top k frequent
        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)
        # format response
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res;