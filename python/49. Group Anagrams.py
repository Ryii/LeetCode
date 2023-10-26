from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

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