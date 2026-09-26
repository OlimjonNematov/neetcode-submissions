from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return a list
        ans = []
        counts = Counter(nums)

        # loop through and keep track of top frequent
        heap = []
        for num in counts:
            heapq.heappush(heap, [counts[num],num])
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)

        while heap:
            ans.append(heapq.heappop(heap)[1])

        # return ans
        return ans;
