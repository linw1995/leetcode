# Created by 林玮 (Jade Lin) at 2026/04/19 13:30
# leetgo: 1.4.15
# https://leetcode.cn/problems/rearrange-spaces-between-words/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reorderSpaces(self, text: str) -> str:
        prev = " "
        words = []
        spaces = 0
        for c in text:
            if c == " ":
                spaces += 1
            elif prev == " ":
                words.append([c])
            else:
                words[-1].append(c)

            prev = c

        cnt = len(words) - 1
        ans = []
        for word in words:
            ans.append("".join(word))

        if cnt > 0:
            space = self.new_space(spaces // cnt)
            return space.join(ans) + self.new_space(spaces % cnt)
        else:
            return ans[0] + self.new_space(spaces)

    def new_space(self, size: int) -> str:
        if size == 0:
            return ""

        return "".join(" " for _ in range(size))


# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().reorderSpaces(text)
    print("\noutput:", serialize(ans, "string"))
