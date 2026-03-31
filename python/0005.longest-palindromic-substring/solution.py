# Created by 林玮 (Jade Lin) at 2026/03/31 16:35
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-palindromic-substring/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        for m in range(n):
            i = m - 1
            j = m + 1
            candidate = s[m]

            while i >= 0 and j < n and s[i] == s[j]:
                candidate = s[i : j + 1]
                j += 1
                i -= 1

            if len(candidate) > len(ans):
                ans = candidate

            i = m - 1
            j = m
            candidate = ""

            while i >= 0 and j < n and s[i] == s[j]:
                candidate = s[i : j + 1]
                j += 1
                i -= 1

            if len(candidate) > len(ans):
                ans = candidate

        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
