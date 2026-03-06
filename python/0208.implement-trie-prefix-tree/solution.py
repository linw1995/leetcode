# Created by 林玮 (Jade Lin) at 2026/03/06 22:00
# leetgo: 1.4.15
# https://leetcode.cn/problems/implement-trie-prefix-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


class Trie:
    def __init__(self):
        self.root = [None] * 26

    def insert(self, word: str) -> None:
        p = None
        root = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if root[idx] is None:
                root[idx] = (False, [None] * 26)

            p = root
            root = root[idx][1]

        p[idx] = (True, p[idx][1])

    def search(self, word: str) -> bool:
        p = None
        root = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if root[idx] is None:
                return False

            p = root[idx]
            root = root[idx][1]

        return p and p[0]

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if root[idx] is None:
                return False

            root = root[idx][1]

        return root is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Trie()

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                obj.insert(word)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                ans = serialize(obj.search(word))
                output.append(ans)
            case "startsWith":
                method_params = split_array(params[i])
                prefix: str = deserialize("str", method_params[0])
                ans = serialize(obj.startsWith(prefix))
                output.append(ans)

    print("\noutput:", join_array(output))
