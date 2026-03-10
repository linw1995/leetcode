# Created by 林玮 (Jade Lin) at 2026/03/10 17:08
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, f = -inf, 0
        for num in nums:
            f = max(f + num, num)
            ans = max(ans, f)

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))
