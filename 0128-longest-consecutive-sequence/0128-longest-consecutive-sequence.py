class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        for num in numSet:
            #check if start of a sequence
            if num-1 not in numSet:
                cnt = 1
                while num+cnt in numSet:
                    cnt += 1
                longest = max(longest, cnt)
        return longest