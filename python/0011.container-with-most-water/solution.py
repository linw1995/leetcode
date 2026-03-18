# Created by 林玮 (Jade Lin) at 2026/03/18 09:20
# leetgo: 1.4.15
# https://leetcode.cn/problems/container-with-most-water/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)

        i = 0
        j = size - 1
        ans = 0
        while i < j:
            h = min(height[i], height[j])
            ans = max(ans, (j - i) * h)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(height)
    print("\noutput:", serialize(ans, "integer"))
