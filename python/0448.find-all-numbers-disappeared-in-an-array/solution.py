# Created by 林玮 (Jade Lin) at 2026/03/19 11:28
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for num in nums:
            idx = (num - 1) % n
            nums[idx] += n

        return [i + 1 for i, num in enumerate(nums) if num <= n]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDisappearedNumbers(nums)
    print("\noutput:", serialize(ans, "integer[]"))
