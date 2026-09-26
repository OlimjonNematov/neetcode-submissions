class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # "abaaaacuqioadkja"
        window = set()
        l = 0
        res = 0

        if not s:
            return res

        for r in range(len(s)):
            
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, len(window))
        
        return res;