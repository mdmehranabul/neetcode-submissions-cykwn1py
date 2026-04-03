class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char ={"2": "abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}

        def dfs(i, currset):
            if len(currset)==len(digits):
                res.append(currset)
                return
            
            for c in digit_to_char[digits[i]]:
                dfs(i+1, currset+c)
        
        if digits:
            dfs(0,"")
        
        return res

        