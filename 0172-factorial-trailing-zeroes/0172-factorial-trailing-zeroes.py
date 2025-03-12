class Solution:
    def trailingZeroes(self, n: int) -> int:
        def helper(n):
            if n<5:
                return 0
            return n//5 + helper(n//5)
        return helper(n)