from typing import List


class Solution(object):
    MAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        ans = []
        self.dfs(0, [], digits, ans)

        return ans

    def dfs(self, step: int, s: List, digits: str, ans: List[str]) -> None:
        if step == len(digits):
            ans.append("".join(s))
            return

        num = int(digits[step])
        for c in list(self.MAP[num]):
            s.append(c)
            self.dfs(step + 1, s, digits, ans)
            s.pop()
