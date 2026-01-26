# Created by 林玮 (Jade Lin) at 2026/01/26 09:45
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-absolute-difference/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        subs = []
        for i in range(len(arr) - 1):
            subs.append(arr[i + 1] - arr[i])
        target = subs[0]
        ans = []
        for i in range(len(subs)):
            item = (arr[i], arr[i + 1])
            if target > subs[i]:
                target = subs[i]
                ans = [item]
            elif target == subs[i]:
                ans.append(item)
        return ans


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumAbsDifference(arr)
    print("\noutput:", serialize(ans, "integer[][]"))
