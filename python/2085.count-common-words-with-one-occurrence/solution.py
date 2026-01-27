# Created by 林玮 (Jade Lin) at 2026/01/27 10:13
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-common-words-with-one-occurrence/

from typing import *
from leetgo_py import *

# @lc code=begin

from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1)
        words2 = Counter(words2)
        ans = 0
        for k in words1.keys() & words2.keys():
            if words1[k] == words2[k] == 1:
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    words1: List[str] = deserialize("List[str]", read_line())
    words2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().countWords(words1, words2)
    print("\noutput:", serialize(ans, "integer"))
