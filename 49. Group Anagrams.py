from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)

        for word in strs:
            hashMap[tuple(sorted(word))].append(word)

        return hashMap.values()



        # hashMap = defaultdict(list)

        # for word in strs:

        #     wordDict = [0] * 26
        #     for c in word:
        #         wordDict[ord(c) - ord('a')] += 1

        #     hashMap[tuple(wordDict)].append(word)

        # return hashMap.values()