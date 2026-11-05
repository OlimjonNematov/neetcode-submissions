from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the counts
        ans = []
        counts = Counter(nums) # {values: count}
        heap = []

        # build the min heap
        for num in counts:
            heapq.heappush(heap, [counts[num], num])
            # maintain main heap
            if len(heap) > k:
                heapq.heappop(heap)

        # populate ans
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans