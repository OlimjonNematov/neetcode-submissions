class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1,-1], float("infinity")
        if len(t) > len(s): return ""
        # set up the sigT, sigWin
        sigT, sigWin = {},{}
        for letter in t:
            sigT[letter] = 1 + sigT.get(letter, 0)
        # set up checks
        have, need = 0, len(sigT)

        l = 0
        for r in range(len(s)):
            # add to window
            c = s[r]
            sigWin[c] = 1 + sigWin.get(c, 0)

            # if we meet a check, increment have
            if c in sigT and sigWin[c] == sigT[c]:
                have += 1

            # while currnet have == need
            while have == need:
                # update res if better resLength is found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r-l+1                    
                
                # remove l
                sigWin[s[l]] -= 1
                # check that removing l does not remove a check in have
                if s[l] in sigT and sigWin[s[l]] < sigT[s[l]]:
                    have -= 1
                l+=1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        