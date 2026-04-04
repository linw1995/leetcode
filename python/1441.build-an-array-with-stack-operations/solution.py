# Created by 林玮 (Jade Lin) at 2026/04/04 14:03
# leetgo: 1.4.15
# https://leetcode.cn/problems/build-an-array-with-stack-operations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []

        s = []
        for i in range(1, n + 1):
            if s == target:
                return ops

            ops.append("Push")
            s.append(i)

            if target[len(s) - 1] != s[-1]:
                ops.append("Pop")
                s.pop()

        return ops


# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().buildArray(target, n)
    print("\noutput:", serialize(ans, "string[]"))
