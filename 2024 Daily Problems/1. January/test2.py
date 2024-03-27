dominance_factors = {}

def Merge(arr, Yleft, Yright, l, m, r, S):
    iL = iR = 0
    endL = len(Yleft)
    endR = len(Yright)

    right = [0] * endR

    for _ in range(endL + endR):
        if iL >= endL:
            iR += 1
        elif iR >= endR:
            iL += 1
        elif Yleft[iL][1] < Yright[iR][1]:
            dominance_factors[Yleft[iL][0]] += endR - iR
            right[iR] += 1
            iL += 1
        else:
            iR += 1

    count = 0
    for pos in range(0, endR):
        count += right[pos]
        dominance_factors[Yright[pos][0]] += count


    print(dominance_factors)
    return 

def MergeSort(towersX, towersY, l, r, S):
    if (l >= r):
        return
    else:
        m = l + (r-l)//2

        Yleft = []
        Yright = []
        for tower in towersY:
            if tower[0] <= towersX[m][0]:
                Yleft.append(tower)
            else:
                Yright.append(tower)

        MergeSort(towersX, Yleft, l, m, S)
        MergeSort(towersX, Yright, m+1, r, S)
        Merge(towersX, Yleft, Yright, l, m, r, S)

n = 8
towers = [
    (1, 7),
    (2, 2),
    (3, 6),
    (4, 5),
    (5, 1),
    (6, 8),
    (7, 3),
    (8, 4)
]

towersX = sorted(towers, key=lambda x: x[0])
towersY = sorted(towers, key=lambda x: x[1])
S = [i for i in range(n)]

for x, y in towersX:
    dominance_factors[x] = 0
 
MergeSort(towersX, towersY, 0, n-1, S)

print(dominance_factors)