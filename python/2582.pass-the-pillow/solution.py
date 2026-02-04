# Created by 林玮 (Jade Lin) at 2026/02/04 15:39
# leetgo: 1.4.15
# https://leetcode.cn/problems/pass-the-pillow/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # 简单计算往返依次要 (n - 1) * 2
        idx = time % ((n - 1) * 2)
        if idx < n:
            return idx + 1
        else:
            # 反序的移动次数 idx - (n - 1)
            # ans = n - (idx - (n - 1))
            return 2 * n - 1 - idx


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    time: int = deserialize("int", read_line())
    ans = Solution().passThePillow(n, time)
    print("\noutput:", serialize(ans, "integer"))
