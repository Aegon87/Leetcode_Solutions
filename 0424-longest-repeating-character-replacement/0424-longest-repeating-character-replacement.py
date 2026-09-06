class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashm = {}
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            if s[r] in hashm:
                hashm[s[r]] +=1
            else:
                hashm[s[r]] = 1
            
            maxf = max(maxf, hashm[s[r]])
            
            while ((r-l+1) - maxf) > k:
                hashm[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res