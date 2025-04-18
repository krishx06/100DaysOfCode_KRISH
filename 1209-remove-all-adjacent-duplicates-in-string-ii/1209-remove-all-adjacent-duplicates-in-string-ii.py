class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []  

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1  
                if stack[-1][1] == k:
                    stack.pop()  
            else:
                stack.append([char, 1])  
        
        result = ''.join(char * count for char, count in stack)
        return result