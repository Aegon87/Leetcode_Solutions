class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # hashm = set()
        # for num in nums:
        #     if num in hashm:
        #         return True
        #     hashm.add(num)
        # return False

        if len(nums) != len(set(nums)):
            return True
        return False