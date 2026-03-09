# Created by 林玮 (Jade Lin) at 2026/03/09 21:14
# leetgo: 1.4.15
# https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/

from typing import *
from leetgo_py import *

# @lc code=begin

from heapq import heappushpop, heapify


class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        q = [-s for s in stock[:cnt]]
        heapify(q)

        for s in stock[cnt:]:
            heappushpop(q, -s)

        return [-s for s in q]


# @lc code=end

if __name__ == "__main__":
    stock: List[int] = deserialize("List[int]", read_line())
    cnt: int = deserialize("int", read_line())
    ans = Solution().inventoryManagement(stock, cnt)
    print("\noutput:", serialize(ans, "integer[]"))
