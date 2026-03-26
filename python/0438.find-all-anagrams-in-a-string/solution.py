# Created by 林玮 (Jade Lin) at 2026/03/26 19:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(p)
        p = Counter(p)
        w = Counter(s[:size])

        ans = []
        for i in range(len(s) - size):
            if p == w:
                ans.append(i)

            k = s[i]
            w[k] = w[k] - 1
            if w[k] == 0:
                del w[k]

            k = s[i + size]
            w[k] = w[k] + 1

        if p == w:
            ans.append(len(s) - size)

        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().findAnagrams(s, p)
    print("\noutput:", serialize(ans, "integer[]"))
