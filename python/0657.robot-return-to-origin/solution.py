# Created by 林玮 (Jade Lin) at 2026/04/05 09:30
# leetgo: 1.4.15
# https://leetcode.cn/problems/robot-return-to-origin/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        location = [0, 0]
        for move in moves:
            if move == "U":
                location[1] += 1
            elif move == "D":
                location[1] -= 1
            elif move == "L":
                location[0] -= 1
            elif move == "R":
                location[0] += 1

        return location == [0, 0]


# @lc code=end

if __name__ == "__main__":
    moves: str = deserialize("str", read_line())
    ans = Solution().judgeCircle(moves)
    print("\noutput:", serialize(ans, "boolean"))
