from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # target counters
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        
        if s1_count == s2_count: return True

        l = 0

        for r in range(len(s1), len(s2)):
            # Add count to char from the right
            s2_count[s2[r]] += 1

            # decrement count char from the left, and delete from counts
            left_char = s2[l]
            s2_count[left_char] -= 1
            if s2_count[left_char] == 0: del s2_count[left_char]
            l += 1

            # check equality
            if s1_count == s2_count: return True


        return False