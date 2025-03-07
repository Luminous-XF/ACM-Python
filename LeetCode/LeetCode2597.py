from collections import defaultdict
from typing import *


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        book = defaultdict(int)
        ans = [-1]
        self.dfs(0, ans, k, nums, book)

        return ans[0]

    def dfs(self, step: int, ans: List[int], k: int, nums: List[int], book: defaultdict) -> None:
        if step == len(nums):
            ans[0] += 1
            return

        self.dfs(step + 1, ans, k, nums, book)

        x = nums[step]
        if book[x - k] == 0 and book[x + k] == 0:
            book[x] += 1
            self.dfs(step + 1, ans, k, nums, book)
            book[x] -= 1