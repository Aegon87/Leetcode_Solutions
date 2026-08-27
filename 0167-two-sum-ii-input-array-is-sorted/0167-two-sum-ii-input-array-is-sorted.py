class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_ = {}
        for i, num in enumerate(numbers): 
            compliment = target - num
            if compliment in hash_:
                return hash_[compliment]+1, i+1
            hash_[num] = i
        return -1, -1

        # l, r = 0, len(numbers)-1
        # numbers.sort()
        # while l < r:
        #     if numbers[l] + numbers[r] < target:
        #         l += 1
        #     elif numbers[l] + numbers[r] > target:
        #         r -= 1
        #     else:
        #         return l+1, r+1