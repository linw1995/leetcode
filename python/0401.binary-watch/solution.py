# Created by 林玮 (Jade Lin) at 2026/02/17 10:45
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-watch/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # minutes: ["0:01","0:02","0:04","0:08","0:16","0:32"]
        # 可能会超过 59
        # hours: ["1:00","2:00","4:00","8:00"]
        return self.turnOn(0, [False] * 10, turnedOn)

    def turnOn(self, idx: int, lights: List[bool], turnedOn: int) -> List[str]:
        ans = []

        if turnedOn == 0:
            rv = self.formatWatch(lights)
            if rv is not None:
                ans.append(rv)
        elif idx < 10:
            ans.extend(self.turnOn(idx + 1, lights[:], turnedOn))
            lights[idx] = True
            ans.extend(self.turnOn(idx + 1, lights[:], turnedOn - 1))

        return ans

    def formatWatch(self, lights: List[bool]) -> Optional[str]:
        minutes = 0
        step = 1
        for i in range(6):
            if lights[i]:
                minutes += step

            step = step << 1

        if minutes > 59:
            return None

        hours = 0
        step = 1
        for i in range(4):
            if lights[i + 6]:
                hours += step

            step = step << 1

        if hours >= 12:
            return None

        return f"{hours}:{minutes:02d}"


# @lc code=end

if __name__ == "__main__":
    turnedOn: int = deserialize("int", read_line())
    ans = Solution().readBinaryWatch(turnedOn)
    print("\noutput:", serialize(ans, "string[]"))
