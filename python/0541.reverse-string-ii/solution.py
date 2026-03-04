# Created by 林玮 (Jade Lin) at 2026/03/04 16:41
# leetgo: 1.4.15
# https://leetcode.cn/problems/reverse-string-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        i = 0
        while i < len(s):
            j = i + k
            ans.append("".join(reversed(s[i:j])))
            i = j + k
            ans.append(s[j:i])

        return "".join(ans)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().reverseStr(s, k)
    print("\noutput:", serialize(ans, "string"))
