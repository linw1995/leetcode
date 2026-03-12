# Created by 林玮 (Jade Lin) at 2026/03/12 13:32
# leetgo: 1.4.15
# https://leetcode.cn/problems/the-skyline-problem/

from typing import *
from leetgo_py import *

# @lc code=begin

from heapq import heappush, heappop


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        length = len(buildings)
        buildings.sort(key=lambda x: x[0])

        points = []
        for left, right, _ in buildings:
            points.append(left)
            points.append(right)

        ans = []
        heights = []
        idx = 0
        for point in sorted(points):
            while idx < length and buildings[idx][0] <= point:
                (_, right, height) = buildings[idx]
                heappush(heights, (-height, right))
                idx += 1

            while heights and heights[0][1] <= point:
                heappop(heights)

            height = -heights[0][0] if heights else 0
            if not ans or ans[-1][1] != height:
                ans.append((point, height))

        return ans


# @lc code=end

if __name__ == "__main__":
    buildings: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getSkyline(buildings)
    print("\noutput:", serialize(ans, "integer[][]"))
