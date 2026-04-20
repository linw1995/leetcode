# Created by 林玮 (Jade Lin) at 2026/04/20 21:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/two-furthest-houses-with-different-colors/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left = [-1] * 101
        for idx, color in enumerate(colors):
            if left[color] == -1:
                left[color] = idx

        n = len(colors)
        right = [-1] * 101
        for idx, color in enumerate(reversed(colors)):
            if right[color] == -1:
                right[color] = idx

        ans = -1
        for i, l in enumerate(left):
            for j, r in enumerate(right):
                if l == -1 or r == -1:
                    continue

                if i != j:
                    ans = max(ans, n - 1 - r - l)

        return ans


# @lc code=end

if __name__ == "__main__":
    colors: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDistance(colors)
    print("\noutput:", serialize(ans, "integer"))
