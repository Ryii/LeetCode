class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows * cols
        curStep = 2
        curPos = (rStart, cStart)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        output = [curPos]

        while len(output) != total:
            for stepSize in range(1, curStep // 2 + 1):
                newPos = dirs[(curStep + 2) % 4] * stepSize
                curPos = (curPos[0]+newPos[0], curPos[1]+newPos[1])
                if curPos[0] >= 0 and curPos[0] < rows and curPos[1] >= 0 and curPos[1] < cols:
                    output.append(curPos)
            curStep += 1

        return output