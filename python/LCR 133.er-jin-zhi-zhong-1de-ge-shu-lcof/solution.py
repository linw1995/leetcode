# Created by 林玮 (Jade Lin) at 2026/04/21 12:29
# leetgo: 1.4.15
# https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            if n & 1 == 1:
                cnt += 1

            n = n >> 1
        return cnt


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().hammingWeight(n)
    print("\noutput:", serialize(ans, "integer"))
