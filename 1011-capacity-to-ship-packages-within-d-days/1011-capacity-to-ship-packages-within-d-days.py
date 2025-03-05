class Solution:
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(capacity):
            
            total_weight = 0
            required_days = 1  
            
            for weight in weights:
                if total_weight + weight > capacity:
                    required_days += 1
                    total_weight = 0  
                total_weight += weight 
            
            return required_days <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid  
            else:
                left = mid + 1 
        
        return left  
