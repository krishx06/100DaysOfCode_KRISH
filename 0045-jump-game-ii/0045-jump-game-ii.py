class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] == 0:
            return -1
        
        max_reach = nums[0]  
        steps = nums[0] 
        jumps = 1  
        
        for i in range(1, n):
            if i == n - 1:
                return jumps
            
            max_reach = max(max_reach, i + nums[i])
            steps -= 1
            
            if steps == 0:
                jumps += 1
                if i >= max_reach:
                    return -1
                steps = max_reach - i
        
        return -1


