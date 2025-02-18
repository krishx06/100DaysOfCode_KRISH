class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total_sum = 0
        
        for i in range(n):
            left_count = i + 1  
            right_count = n - i  
            total_contribution = (left_count * right_count + 1) // 2  
            
            total_sum += arr[i] * total_contribution
        
        return total_sum