# Created by 林玮 (Jade Lin) at 2026/03/12 18:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/trapping-rain-water/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        leftMax[0] = height[0]
        for i in range(1, len(height)):
            h = height[i]
            leftMax[i] = max(leftMax[i - 1], h)

        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            h = height[i]
            rightMax[i] = max(rightMax[i + 1], h)

        ans = 0
        for left, right, h in zip(leftMax, rightMax, height):
            ans += min(left, right) - h

        return ans


# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)
    print("\noutput:", serialize(ans, "integer"))
