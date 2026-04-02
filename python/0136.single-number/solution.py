# Created by 林玮 (Jade Lin) at 2026/04/02 11:42
# leetgo: 1.4.15
# https://leetcode.cn/problems/single-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums[1:]:
            ans ^= num
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
