class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        workers = sorted(worker, reverse=True)
        jobs = sorted(zip(profit, difficulty), reverse=True)
        profit, difficulty = zip(*jobs)
        pos = 0
        worker = 0
        ans = 0

        print(workers)
        print(difficulty, profit)
        
        while worker < len(workers) and pos < len(difficulty):
            if workers[worker] >= difficulty[pos]:
                ans += profit[pos]
                worker += 1
            else:
                pos += 1
            

        return ans