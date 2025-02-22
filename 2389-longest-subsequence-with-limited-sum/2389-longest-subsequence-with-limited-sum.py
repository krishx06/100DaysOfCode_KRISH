class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        
        prefix_sums = [0] * len(nums)
        prefix_sums[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i]
        
        def binary_search(target):
            low, high = 0, len(prefix_sums) - 1
            result = -1  
            while low <= high:
                mid = (low + high) // 2
                if prefix_sums[mid] <= target:
                    result = mid  
                    low = mid + 1
                else:
                    high = mid - 1
            return result

        answer = []
        for q in queries:
            index = binary_search(q)
            answer.append(index + 1)
        
        return answer

