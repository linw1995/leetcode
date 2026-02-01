# Created by 林玮 (Jade Lin) at 2026/02/01 09:41
# leetgo: 1.4.15
# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        costs = sorted(nums[1:3])
        for num in nums[3:]:
            costs.append(num)
            costs = sorted(costs)[:2]

        return sum(costs) + nums[0]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(nums)
    print("\noutput:", serialize(ans, "integer"))
