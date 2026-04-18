# Created by 林玮 (Jade Lin) at 2026/04/18 21:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/mirror-distance-of-an-integer/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(int("".join(reversed(str(n)))) - n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().mirrorDistance(n)
    print("\noutput:", serialize(ans, "integer"))
