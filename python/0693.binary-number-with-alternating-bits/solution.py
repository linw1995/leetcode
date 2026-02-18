# Created by 林玮 (Jade Lin) at 2026/02/18 22:44
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-number-with-alternating-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 0:
            return False

        expect = not bool(n & 1)
        while n > 0:
            n = n >> 1

            if bool(n & 1) != expect:
                return False

            expect = not expect
        
        return True


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().hasAlternatingBits(n)
    print("\noutput:", serialize(ans, "boolean"))
