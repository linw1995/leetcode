# Created by 林玮 (Jade Lin) at 2026/03/12 15:54
# leetgo: 1.4.15
# https://leetcode.cn/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def climbStairs(self, n: int) -> int:
        # f(1) = 1
        # f(2) = 1 1, 2
        # f(3) = 1 f(2), 2 f(1)
        # f(4) = 1 f(3), 2 f(2)
        a, b = 1, 2
        while n > 1:
            a, b = b, a + b
            n -= 1

        return a


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)
    print("\noutput:", serialize(ans, "integer"))
