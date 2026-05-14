# Created by 林玮 (Jade Lin) at 2026/05/14 21:51
# leetgo: 1.4.15
# https://leetcode.cn/problems/check-if-array-is-good/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        nums.sort()
        for a, b in zip(range(1, len(nums)), nums):
            if a != b:
                return False

        return nums[-1] == len(nums) - 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isGood(nums)
    print("\noutput:", serialize(ans, "boolean"))
