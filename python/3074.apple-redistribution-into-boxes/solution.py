# Created by 林玮 (Jade Lin) at 2026/04/06 14:23
# leetgo: 1.4.15
# https://leetcode.cn/problems/apple-redistribution-into-boxes/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apple = sum(apple)

        j = 0
        while apple > 0:
            apple -= capacity[j]
            j += 1

        return j


# @lc code=end

if __name__ == "__main__":
    apple: List[int] = deserialize("List[int]", read_line())
    capacity: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumBoxes(apple, capacity)
    print("\noutput:", serialize(ans, "integer"))
