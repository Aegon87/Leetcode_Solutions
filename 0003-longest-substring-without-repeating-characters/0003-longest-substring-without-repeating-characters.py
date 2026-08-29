class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = 0
        st = []
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.append(s[r])
            res = max(res, len(st))
        return res