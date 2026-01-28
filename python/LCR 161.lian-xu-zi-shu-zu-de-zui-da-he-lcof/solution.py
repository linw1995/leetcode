# Created by 林玮 (Jade Lin) at 2026/01/28 10:52
# leetgo: 1.4.15
# https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSales(self, sales: List[int]) -> int:
        max_streak = streak = sales[0]
        for sale in sales[1:]:
            streak = max(streak + sale, sale)
            max_streak = max(max_streak, streak)

        return max_streak


# @lc code=end

if __name__ == "__main__":
    sales: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSales(sales)
    print("\noutput:", serialize(ans, "integer"))
