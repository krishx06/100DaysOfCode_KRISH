class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        current_sum = 0
        min_sum = 0
        
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
        
        return 1 - min_sum
