# Created by 林玮 (Jade Lin) at 2026/02/22 10:20
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-gap/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        left_match = False
        length = 0
        while n > 0:
            t = n & 1
            if t:
                if left_match:
                    if length > ans:
                        ans = length
                else:
                    left_match = True

                length = 0

            length += 1

            n = n >> 1

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().binaryGap(n)
    print("\noutput:", serialize(ans, "integer"))
