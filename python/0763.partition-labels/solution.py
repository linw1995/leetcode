# Created by 林玮 (Jade Lin) at 2026/03/08 11:56
# leetgo: 1.4.15
# https://leetcode.cn/problems/partition-labels/

import enum
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lefts = []
        rights = []
        ans = []
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                continue

            seen.add(c)

            j = self.findEnd(s, i, len(s) - 1)
            lefts.append(i)
            rights.append(j)

            if not ans:
                ans.append((i, j))
            else:
                last = ans[-1]
                if j < last[1]:
                    continue
                elif i < last[1]:
                    ans[-1] = (last[0], j)
                else:
                    ans.append((i, j))

        return [s[1] - s[0] + 1 for s in ans]

    def findEnd(self, s: str, i: int, j: int) -> int:
        while i < j:
            if s[i] == s[j]:
                return j

            j -= 1
        return j


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partitionLabels(s)
    print("\noutput:", serialize(ans, "integer[]"))
