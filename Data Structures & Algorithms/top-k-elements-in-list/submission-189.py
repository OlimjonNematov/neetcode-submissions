from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counts = Counter(nums)
        heap = []

        for num in counts:
            heapq.heappush(heap, [counts[num], num])
            if len(heap)>k:
                heapq.heappop(heap)
            
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans