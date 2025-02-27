class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset = [[]]
        for val in nums:
            subset += [ [val] + curr for curr in subset]
        
        return subset