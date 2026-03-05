# Created by 林玮 (Jade Lin) at 2026/03/05 14:32
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-changes-to-make-alternating-binary-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minOperations(self, s: str) -> int:
        # 00
        #   10 -> 1
        #   01 -> 1
        # 01
        #   01 -> 0
        #   10 -> 2
        # 000
        #   010 -> 1
        #   101 -> 2
        # 010
        #   010 -> 0
        #   101 -> 3
        ans = sum(int(c) != i % 2 for i, c in enumerate(s))
        return min(ans, len(s) - ans)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minOperations(s)
    print("\noutput:", serialize(ans, "integer"))
