# Created by 林玮 (Jade Lin) at 2026/03/19 11:28
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(range(1, len(nums) + 1))
        for num in nums:
            s.discard(num)
        return sorted(s)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDisappearedNumbers(nums)
    print("\noutput:", serialize(ans, "integer[]"))
