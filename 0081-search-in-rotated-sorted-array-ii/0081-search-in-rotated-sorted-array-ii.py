class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <=r:
            mid = (l+r)//2
            if target==nums[mid]:
                return True
            elif nums[l]==nums[mid]==nums[r]:
                l += 1
                r -= 1
                continue
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False
