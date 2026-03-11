# Created by 林玮 (Jade Lin) at 2026/03/11 09:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/complement-of-base-10-integer/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        mask = (1 << n.bit_length()) - 1
        return n ^ mask


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().bitwiseComplement(n)
    print("\noutput:", serialize(ans, "integer"))
