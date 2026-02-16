# Created by 林玮 (Jade Lin) at 2026/02/16 08:59
# leetgo: 1.4.15
# https://leetcode.cn/problems/reverse-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reverseBits(self, n: int) -> int:
        i = 1
        ans = 0

        for _ in range(31):
            d = (n & i) // i
            ans |= d
            ans *= 2
            i *= 2

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().reverseBits(n)
    print("\noutput:", serialize(ans, "integer"))
