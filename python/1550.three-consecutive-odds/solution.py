# Created by 林玮 (Jade Lin) at 2026/04/14 20:30
# leetgo: 1.4.15
# https://leetcode.cn/problems/three-consecutive-odds/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if num % 2 == 1:
                cnt += 1
            else:
                cnt = 0

            if cnt == 3:
                return True

        return False


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeConsecutiveOdds(arr)
    print("\noutput:", serialize(ans, "boolean"))
