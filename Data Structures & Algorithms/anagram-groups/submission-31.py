class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =dict()

        # assign each distinct anogram a "signature"... 
        for s in strs:
            chars = ','.join(sorted(s))
            if res.get(chars): 
                res.get(chars).append(s) # if the sig exists, simply push
            else:
                res[chars] = [s] # if the sig does not exist, create array and add the current string. 
        # return all the values in map.. ignore keys
        return list(res.values())