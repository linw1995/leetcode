# Created by 林玮 (Jade Lin) at 2026/02/12 16:02
# leetgo: 1.4.15
# https://leetcode.cn/problems/ant-on-the-boundary/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        loc = 0
        for num in nums:
            loc += num
            if loc == 0:
                ans += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().returnToBoundaryCount(nums)
    print("\noutput:", serialize(ans, "integer"))
