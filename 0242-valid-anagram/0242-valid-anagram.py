class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) == len(t):
        #     return sorted(s) == sorted(t)
        # else:
        #     return False

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for num in s:
            countS[num] = countS.get(num, 0) + 1
        for num in t:
            countT[num] = countT.get(num, 0) + 1
        return countS == countT