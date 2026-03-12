# Created by 林玮 (Jade Lin) at 2026/03/12 10:47
# leetgo: 1.4.15
# https://leetcode.cn/problems/lru-cache/

from typing import *
from leetgo_py import *

# @lc code=begin
from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)

        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    capacity: int = deserialize("int", constructor_params[0])
    obj = LRUCache(capacity)

    for i in range(1, len(ops)):
        match ops[i]:
            case "get":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.get(key))
                output.append(ans)
            case "put":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                value: int = deserialize("int", method_params[1])
                obj.put(key, value)
                output.append("null")

    print("\noutput:", join_array(output))
