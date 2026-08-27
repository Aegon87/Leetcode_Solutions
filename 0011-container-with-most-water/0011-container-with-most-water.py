class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        maxi = 0
        while l<r:
            length = r - l
            if height[l] <= height[r]:
                area = height[l]*length
                maxi = max(maxi, area)
                l+=1
            else:
                area = height[r]*length
                maxi = max(maxi, area)
                r-=1
        return maxi