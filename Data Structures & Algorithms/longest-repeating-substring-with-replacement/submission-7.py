from collections import defaultdict

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # hash map of counts for all letters
        counts = defaultdict(int)
        l =0 
        maxf = 0

        for r in range(len(s)):
            # increment occurence
            counts[s[r]] = 1 + counts[s[r]]
            # get current max char
            maxf = max(maxf, counts[s[r]])
            
            # while we have more replacements than non maxf letters in a window
            while (r-l + 1) - maxf > k:
                # decrement count of left
                counts[s[l]] -= 1

                # move the sliding window
                l += 1
            res = max(res, r-l+1)

                
        return res