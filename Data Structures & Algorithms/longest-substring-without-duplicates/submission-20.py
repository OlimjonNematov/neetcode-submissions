class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen_set = set()
        l = 0 
        res = 0

        if not s:
            return longest
        
        for r in range(len(s)):
            while s[r] in seen_set:
                seen_set.remove(s[l])
                l+=1
            seen_set.add(s[r])
            longest = max(longest, len(seen_set))
        


        return longest;