from collections import defaultdict
from typing import *


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1

        ans, k = 0, 0
        for num in nums:
            k ^= num
            ans += cnt[k]
            cnt[k] += 1

        return ans
