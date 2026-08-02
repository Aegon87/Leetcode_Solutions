class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binSearch(nums,target, True)
        right = self.binSearch(nums,target, False)
        return [left,right]

    def binSearch(self,nums,target,leftBias):
        l ,r = 0, len(nums)-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                res = mid
                if leftBias:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return res
        
                                    

    