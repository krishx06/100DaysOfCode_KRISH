class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n > 0:
            while n % 4 == 0:
                n //= 4

        return(True if n == 1 else False)