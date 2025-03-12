class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"
        
        while len(word) < k:
            new_word = ''.join(chr(((ord(c) - ord('a') + 1) % 26) + ord('a')) for c in word)
            word += new_word
        
        return word[k-1]
