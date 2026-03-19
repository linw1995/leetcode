# Created by 林玮 (Jade Lin) at 2026/03/19 11:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallerNumbersThanCurrent(nums)
    print("\noutput:", serialize(ans, "integer[]"))
