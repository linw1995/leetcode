# Created by 林玮 (Jade Lin) at 2026/03/31 16:35
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-palindromic-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        max_length = 1
        begin = 0

        for length in range(2, n + 1):
            for i in range(n):
                j = length + i - 1

                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and length > max_length:
                    max_length = length
                    begin = i

        return s[begin : begin + max_length]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
