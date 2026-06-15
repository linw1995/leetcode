# Created by 林玮 (Jade Lin) at 2026/06/15 22:38
# leetgo: 1.4.15
# https://leetcode.cn/problems/take-gifts-from-the-richest-pile/

from typing import *
from leetgo_py import *

# @lc code=begin

from math import floor, sqrt
from heapq import heapify, heappop, heappush


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-t for t in gifts]
        heapify(gifts)
        for _ in range(k):
            t = -heappop(gifts)
            t = int(floor(sqrt(t)))
            heappush(gifts, -t)

        return sum(-t for t in gifts)


# @lc code=end

if __name__ == "__main__":
    gifts: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().pickGifts(gifts, k)
    print("\noutput:", serialize(ans, "long"))
