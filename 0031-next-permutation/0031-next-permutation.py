class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # finding the first decreasing number from left 
        i = len(nums)-2
        while(i>=0 and nums[i] >= nums[i+1]):
            i-=1

        #swap with the next smallest number on the subarray
        if i>=0:
            j = len(nums)-1
            while(nums[j]<=nums[i]):
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
            
        #ascending order for the right subarray -> sort/reverse
        start = i+1
        end = len(nums)-1
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
        return nums