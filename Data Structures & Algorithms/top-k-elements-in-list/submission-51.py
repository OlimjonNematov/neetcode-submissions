class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict();

        # iterate through nums
        for num in nums:
            if count.get(num)is not None:
                count[num]+=1;    
            else:
                count[num]=1

        # sort by values
        sf = sorted(count, key=count.get);
        i=len(sf)-1
        res = []
        # while i<k return key in a list
        while i>=0 and len(res)<k:
            print(sf[i])
            res.append(sf[i])
            i-=1

        return res