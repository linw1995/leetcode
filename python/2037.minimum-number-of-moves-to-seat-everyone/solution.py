# Created by 林玮 (Jade Lin) at 2026/03/25 15:06
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))


# @lc code=end

if __name__ == "__main__":
    seats: List[int] = deserialize("List[int]", read_line())
    students: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minMovesToSeat(seats, students)
    print("\noutput:", serialize(ans, "integer"))
