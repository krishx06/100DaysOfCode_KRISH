class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = [0] * len(nums)
        running_sum[0] = nums[0]
        
        for i in range(1, len(nums)):
            running_sum[i] = running_sum[i - 1] + nums[i]
        
        return running_sum