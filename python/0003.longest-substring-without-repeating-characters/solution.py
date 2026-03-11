# Created by 林玮 (Jade Lin) at 2026/03/11 16:56
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = length = 0
        bound = ord("a")
        prev_idxs = [-1] * 128
        for i, c in enumerate(s):
            prev_idx = prev_idxs[ord(c) - bound]
            if prev_idx < 0 or i - prev_idx > length:
                length += 1
            else:
                ans = max(ans, length)
                length = i - prev_idx

            prev_idxs[ord(c) - bound] = i

        return max(ans, length)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
