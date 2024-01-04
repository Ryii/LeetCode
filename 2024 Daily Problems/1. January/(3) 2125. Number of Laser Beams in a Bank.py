from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0

        for n in bank:
            num = n.count("1")
            if num == 0:
                continue
            total += num * prev
            prev = num

        return total