class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1,-1], float("infinity")
        if len(t)>len(s): return ""
        # pre process
        sigT, sigWin = {},{}
        for c in t:
            sigT[c] = 1 + sigT.get(c, 0)
        have, need = 0, len(sigT)
        # process
        l = 0
        for r in range(len(s)):
            # add the r char to window
            letter = s[r]
            sigWin[letter] = 1+ sigWin.get(letter,0)

            # check if we need to increment have 
            if letter in sigT and sigWin[letter] == sigT[letter]: have+=1

            # while have == need,
            while have == need:
                # check if resLen is better prev Res Len
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)

                # decrement the count on window
                sigWin[s[l]] -= 1
                
                # decrement haveif the counts in sigT are more than sigWin
                if s[l] in sigT and sigWin[s[l]] < sigT[s[l]]:
                    have -=1
                l+=1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""