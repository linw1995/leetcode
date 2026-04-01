# Created by 林玮 (Jade Lin) at 2026/04/01 21:35
# leetgo: 1.4.15
# https://leetcode.cn/problems/search-a-2d-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m * n
        while j - i > 1:
            mid = (j + i) // 2
            c = matrix[mid // n][mid % n]
            if c == target:
                return True
            elif c < target:
                i = mid
            else:
                j = mid

        return matrix[i // n][i % n] == target


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
