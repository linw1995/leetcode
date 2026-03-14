# Created by 林玮 (Jade Lin) at 2026/03/14 22:17
# leetgo: 1.4.15
# https://leetcode.cn/problems/concatenation-of-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums[:] + nums[:]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getConcatenation(nums)
    print("\noutput:", serialize(ans, "integer[]"))
