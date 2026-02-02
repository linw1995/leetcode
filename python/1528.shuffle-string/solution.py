# Created by 林玮 (Jade Lin) at 2026/02/02 09:34
# leetgo: 1.4.15
# https://leetcode.cn/problems/shuffle-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = list(s[:])
        for src, dst in enumerate(indices):
            ans[dst] = s[src]

        return "".join(ans)
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    indices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().restoreString(s, indices)
    print("\noutput:", serialize(ans, "string"))
