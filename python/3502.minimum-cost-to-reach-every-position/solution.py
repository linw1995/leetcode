# Created by 林玮 (Jade Lin) at 2026/03/28 10:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-cost-to-reach-every-position/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        return [min(cost[: i + 1]) for i in range(len(cost))]


# @lc code=end

if __name__ == "__main__":
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCosts(cost)
    print("\noutput:", serialize(ans, "integer[]"))
