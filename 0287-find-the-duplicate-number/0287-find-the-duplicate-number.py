class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hashm = set()
        for num in nums:
            if num in hashm:
                return num
            hashm.add(num)
        return -1