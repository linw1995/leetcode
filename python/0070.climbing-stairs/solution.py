# Created by 林玮 (Jade Lin) at 2026/03/19 09:45
# leetgo: 1.4.15
# https://leetcode.cn/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for _ in range(n - 1):
            a, b = b, a + b
        return a


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)
    print("\noutput:", serialize(ans, "integer"))
