# Created by 林玮 (Jade Lin) at 2026/03/22 16:00
# leetgo: 1.4.15
# https://leetcode.cn/problems/determine-whether-matrix-can-be-obtained-by-rotation/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        compares = [
            # x -> row [0, n)
            # y -> col [0, n)
            lambda i, j: mat[i][j] != target[i][j],
            # y -> row [0, n)
            # x -> col (n, 0]
            lambda i, j: mat[i][j] != target[j][n - 1 - i],
            # x -> row (n, 0]
            # y -> col (n, 0]
            lambda i, j: mat[i][j] != target[n - 1 - i][n - 1 - j],
            # y -> row (n, 0]
            # x -> col [0, n)
            lambda i, j: mat[i][j] != target[n - 1 - j][i],
        ]

        for compare in compares:
            is_matched = True
            for i in range(n):
                for j in range(n):
                    if compare(i, j):
                        is_matched = False
                        break

                if not is_matched:
                    break

            if is_matched:
                return True

        return False


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findRotation(mat, target)
    print("\noutput:", serialize(ans, "boolean"))
