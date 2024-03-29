class Solution:
    def kthGrammar(self, N, K):
        
        # Think of the base case, already given here though
        if N == 1:
            return 0
        
        # We need to do some observation here:
        # 1 - Calculate the length of every row which is as below
        mid = (2 ** (N-1))//2
        
        # If the K lies in the first half, it is actually same as prev row
        if K <= mid:
            return self.kthGrammar(N-1, K)
        
        else:
            # Else it subtract the first half and then it is same as 
            # complement of the prev row
            return 1 - self.kthGrammar(N-1, K-mid)
# 