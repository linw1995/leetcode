# Created by 林玮 (Jade Lin) at 2026/03/24 20:13
# leetgo: 1.4.15
# https://leetcode.cn/problems/word-search/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(
            cur: Tuple[int, int], paths: List[Tuple[int, int]], target: str
        ) -> bool:
            i, j = cur
            if board[i][j] != target[0]:
                return False

            rest = target[1:]
            if not rest:
                return True

            nexts = []

            if i > 0:
                nexts.append((i - 1, j))

            if j > 0:
                nexts.append((i, j - 1))

            if i < n - 1:
                nexts.append((i + 1, j))

            if j < m - 1:
                nexts.append((i, j + 1))

            paths.append(cur)
            for next in nexts:
                if paths and next in paths:
                    continue

                if dfs(next, paths, rest):
                    return True

            paths.pop()

            return False

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if dfs((i, j), [], word):
                    return True

        return False


# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    word: str = deserialize("str", read_line())
    ans = Solution().exist(board, word)
    print("\noutput:", serialize(ans, "boolean"))
