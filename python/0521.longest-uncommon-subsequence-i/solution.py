# Created by 林玮 (Jade Lin) at 2026/02/26 13:51
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-uncommon-subsequence-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            return max(len(a), len(b))

        return -1


# @lc code=end

if __name__ == "__main__":
    a: str = deserialize("str", read_line())
    b: str = deserialize("str", read_line())
    ans = Solution().findLUSlength(a, b)
    print("\noutput:", serialize(ans, "integer"))
