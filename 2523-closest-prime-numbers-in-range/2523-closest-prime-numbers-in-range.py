class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        MAX = right + 1
        is_prime = [True] * MAX
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(MAX ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX, i):
                    is_prime[j] = False

        primes_in_range = [i for i in range(left, right + 1) if is_prime[i]]

        if len(primes_in_range) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(1, len(primes_in_range)):
            diff = primes_in_range[i] - primes_in_range[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [primes_in_range[i - 1], primes_in_range[i]]

        return result