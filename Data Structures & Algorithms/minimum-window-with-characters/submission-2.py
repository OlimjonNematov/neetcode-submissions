class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1,-1], float("infinity")

        if len(t) > len(s): return ""

        sigT, window = {}, {}

        for letter in t:
            sigT[letter] = 1 + sigT.get(letter, 0)
        
        have, need = 0, len(sigT)

        l=0
        for r in range(len(s)):
            # add to our window
            c = s[r]
            window[c] = 1 + window.get(c,0)

            # does the window have the exact number of occurences needed for c
            if c in sigT and window[c] == sigT[c]:
                have +=1

            #  while we match the sig, start moving l
            while have == need:
                # update the result set, if it is shorter
                if  (r-l+1)< resLen:
                    res = [l, r]
                    resLen = r-l+1

                # check that we do not accidentaly remove a required letter
                window[s[l]] -=1
                if s[l] in sigT and window[s[l]] < sigT[s[l]]:
                    have -= 1
                l +=1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""