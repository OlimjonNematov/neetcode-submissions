from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1>len_s2: return False

        win_s1, win_s2 = Counter(s1), Counter(s2[:len_s1])

        if win_s1 == win_s2: return True

        l = 0 
        # enter the for loop 
        for r in range(len_s1, len_s2):
            # add r to win_s2
            win_s2[s2[r]] += 1

            # remove l from win_s2, move l
            win_s2[s2[l]] -= 1
            if win_s2[s2[l]] == 0: del win_s2[s2[l]]
            l+=1

            # check if win_s1 == win_s2
            if win_s1 == win_s2: return True

        return False
