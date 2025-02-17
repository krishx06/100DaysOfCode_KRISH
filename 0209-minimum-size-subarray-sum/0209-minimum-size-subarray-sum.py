class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        

        n = len(nums)
        min_length = n + 1  
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if min_length == n + 1:
            return(0)
        else:
            return(min_length)
            