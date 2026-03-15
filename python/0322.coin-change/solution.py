# Created by 林玮 (Jade Lin) at 2026/03/15 10:53
# leetgo: 1.4.15
# https://leetcode.cn/problems/coin-change/

from typing import *
from leetgo_py import *

# @lc code=begin


from math import inf
from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        @cache
        def dfs(target: int) -> int:
            if target < 0:
                return +inf

            if target == 0:
                return 0

            ans = +inf
            for coin in coins:
                ans = min(ans, dfs(target - coin) + 1)

            return ans

        ans = dfs(amount)
        return ans if ans is not +inf else -1


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    amount: int = deserialize("int", read_line())
    ans = Solution().coinChange(coins, amount)
    print("\noutput:", serialize(ans, "integer"))
