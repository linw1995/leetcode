# Created by 林玮 (Jade Lin) at 2026/03/11 17:19
# leetgo: 1.4.15
# https://leetcode.cn/problems/ugly-number-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [1]
        s = set(q)
        for _ in range(n):
            ans = heappop(q)

            for m in [2, 3, 5]:
                n = ans * m
                if n in s:
                    continue

                heappush(q, n)
                s.add(n)

            s.remove(ans)

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().nthUglyNumber(n)
    print("\noutput:", serialize(ans, "integer"))
