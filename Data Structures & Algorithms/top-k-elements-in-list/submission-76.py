class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # count occur of all nums 
        for num in nums:
            count[num] = count.get(num,0)+1

        # sort all
        arr = []
        for n, c in count.items():
            arr.append([c,n])
        arr.sort();

        # pop top k
        ans=[]
        for i in range(0,k):
            ans.append(arr.pop()[1])

        return ans;