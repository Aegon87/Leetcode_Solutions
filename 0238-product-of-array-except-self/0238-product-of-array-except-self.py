class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # #brute force:
        # answer = [] 
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if j==i:
        #             continue
        #         prod*=nums[j]
        #     answer.append(prod)
        # return answer

        #Better Solution
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        res = [0]*n

        pref[0] = suff[n-1] = 1
        # prefix:
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res