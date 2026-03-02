# Created by 林玮 (Jade Lin) at 2026/03/02 11:14
# leetgo: 1.4.15
# https://leetcode.cn/problems/type-of-triangle/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"

        unified = set(nums)
        size = len(unified)
        if size == 1:
            return "equilateral"
        elif size == 2:
            return "isosceles"
        else:
            return "scalene"


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().triangleType(nums)
    print("\noutput:", serialize(ans, "string"))
