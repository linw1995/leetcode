# Created by 林玮 (Jade Lin) at 2026/04/10 22:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-distance-between-three-equal-elements-i/

from typing import *
from leetgo_py import *

# @lc code=begin

from math import isinf, inf


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1

        ans = +inf
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue

                for k in range(j + 1, n):
                    if nums[j] != nums[k]:
                        continue

                    ans = min(ans, abs(i - j) + abs(j - k) + abs(k - i))

        if isinf(ans):
            return -1

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumDistance(nums)
    print("\noutput:", serialize(ans, "integer"))
