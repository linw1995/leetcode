# Created by 林玮 (Jade Lin) at 2026/03/12 16:11
# leetgo: 1.4.15
# https://leetcode.cn/problems/integer-break/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def integerBreak(self, n: int) -> int:
        # f(i) = max(f(i), f(i-j) * j, (i-j) * j)
        f = [1] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                f[i] = max(f[i], f[i - j] * j, (i - j) * j)

        return f[n]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().integerBreak(n)
    print("\noutput:", serialize(ans, "integer"))
