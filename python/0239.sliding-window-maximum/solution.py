# Created by 林玮 (Jade Lin) at 2026/03/11 22:13
# leetgo: 1.4.15
# https://leetcode.cn/problems/sliding-window-maximum/

from collections import deque
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]

        q = deque(maxlen=k)

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

        ans = []
        for idx, num in enumerate(nums[k:], start=k):
            ans.append(nums[q[0]])

            while q and q[0] <= idx - k:
                q.popleft()

            while q and nums[q[-1]] < num:
                q.pop()

            q.append(idx)

        ans.append(nums[q[0]])
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSlidingWindow(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
