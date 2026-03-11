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

        flags = []
        while n > 0:
            flags.append(n & 1)
            n = n >> 1

        ans = 0
        while flags:
            flag = flags.pop()
            if flag:
                flag = 0
            else:
                flag = 1

            ans = ans | flag

            if flags:
                ans = ans << 1

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().bitwiseComplement(n)
    print("\noutput:", serialize(ans, "integer"))
