from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2: return False

        win_s1, win_s2 = Counter(s1), Counter(s2[:len_s1])
        
        if win_s1 == win_s2: return True

        l = 0 
        for r in range(len_s1, len_s2):

            # add the new char
            win_s2[s2[r]] +=1

            # remove the l char
            # decrement (and maybe remove from wins2 if value is 0)
            win_s2[s2[l]] -= 1
            if win_s2[s2[l]] == 0:
                del win_s2[s2[l]]

            # move l
            l+=1

            # check
            if win_s1 == win_s2: return True

        return False

