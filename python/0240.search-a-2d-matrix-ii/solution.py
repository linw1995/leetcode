# Created by 林玮 (Jade Lin) at 2026/03/12 14:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/search-a-2d-matrix-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        end = len(matrix[0])
        for row in matrix:
            found, idx = self.binarySearch(row, end, target)
            if found:
                return True

            end = idx
        return False

    def binarySearch(self, row: List[int], end: int, target: int) -> Tuple[bool, idx]:
        begin = 0
        while begin < end:
            mid = (begin + end) // 2
            if row[mid] < target:
                begin = mid + 1
            elif row[mid] == target:
                return (True, mid)
            else:
                end = mid

        return (False, begin)


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
