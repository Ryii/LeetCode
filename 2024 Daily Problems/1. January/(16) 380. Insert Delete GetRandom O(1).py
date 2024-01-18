import random

class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False

        self.num_map[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.num_map:
            return False

        last = self.nums[-1]
        index = self.num_map[val]

        self.num_map[last] = index
        self.nums[index] = last

        # remove the last element in the list
        self.nums.pop()

        # remove the element to be removed from the dictionary
        self.num_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()