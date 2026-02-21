# Created by 林玮 (Jade Lin) at 2026/02/21 21:09
# leetgo: 1.4.15
# https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(n.bit_count() in self.primes for n in range(left, right + 1))


# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().countPrimeSetBits(left, right)
    print("\noutput:", serialize(ans, "integer"))
