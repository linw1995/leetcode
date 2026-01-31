# Created by 林玮 (Jade Lin) at 2026/01/31 10:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-smallest-letter-greater-than-target/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        for letter in letters:
            if letter <= target:
                continue
            if letter < ans or ans <= target:
                ans = letter

        return ans


# @lc code=end

if __name__ == "__main__":
    letters: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().nextGreatestLetter(letters, target)
    print("\noutput:", serialize(ans, "character"))
