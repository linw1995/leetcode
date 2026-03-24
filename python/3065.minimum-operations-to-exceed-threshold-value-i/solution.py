# Created by 林玮 (Jade Lin) at 2026/03/24 09:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i, j = 0, len(nums) - 1
        while j - i > 1:
            m = (i + j) // 2
            if nums[m] < k:
                i = m
            else:
                j = m

        if nums[i] >= k:
            return i
        else:
            return i + 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minOperations(nums, k)
    print("\noutput:", serialize(ans, "integer"))
