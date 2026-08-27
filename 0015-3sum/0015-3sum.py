class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(tmp))
        # return [list(i) for i in res]

        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                target = a + nums[l] + nums[r]
                if target < 0:
                    l+=1
                elif target > 0:
                    r-=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res