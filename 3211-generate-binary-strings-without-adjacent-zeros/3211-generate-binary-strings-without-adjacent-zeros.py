class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        s = ['0'] * n
        
        def backtrack(index, flag):
            if index == n:
                res.append(''.join(s))
                return
            if not flag:
                backtrack(index + 1, True)
            s[index] = '1'
            backtrack(index + 1, False)
            s[index] = '0'

        backtrack(0, False)
        return res