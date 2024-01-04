from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
            
        answer = []
            
        while dic:
            arr = []
            for key, item in dic.copy().items():
                arr.append(key)
                if item == 1:
                    dic.pop(key)
                else:
                    dic[key] = item - 1
                    
            answer.append(arr)
                    
        return answer