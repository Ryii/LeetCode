def merge(left, right, dominance):
    merged = []
    i = j = 0
    dominance_count = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0] and left[i][1] < right[j][1]:
            dominance_count += len(left) - i
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            dominance[left[i][2]] += dominance_count
            i += 1

    while i < len(left):
        merged.append(left[i])
        dominance[left[i][2]] += dominance_count
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(towers, dominance):
    if len(towers) <= 1:
        return towers

    mid = len(towers) // 2
    left = merge_sort(towers[:mid], dominance)
    right = merge_sort(towers[mid:], dominance)

    return merge(left, right, dominance)

# def Merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m

#     L = [0] * (n1)
#     R = [0] * (n2)

#     for i in range(0, n1):
#         L[i] = arr[l + i]
 
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]

#     i = j = 0
#     k = l

#     for k in range(l, r + 1):
#         if (i > m-l):
#             arr[k] = R[j]
#             j += 1
#         elif (j > r - (m+1)):
#             arr[k] = L[i]
#             i += 1
#         elif (L[i] <= R[j]):
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1

#     return 

# def MergeSort(array, l, r):
#     if (l >= r):
#         return
#     else:
#         m = l + (r-l)//2
#         MergeSort(array, l, m)
#         MergeSort(array, m+1, r)
#         Merge(array, l, m, r)

def Merge(arr, Yleft, Yright, l, m, r, S, dominance_factors):

    print('\nStart Merge!')

    print(arr, Yleft, Yright, l, m, r, S, dominance_factors)

    S[l:r+1] = arr[l:r+1]

    i = l
    j = m + 1

    for k in range(l, r + 1):
        if (i > m):
            arr[k] = S[j]
            j += 1
        elif (j > r):
            arr[k] = S[i]
            i += 1
        elif (S[i] <= S[j]):
            arr[k] = S[i]
            i += 1
        else:
            arr[k] = S[j]
            j += 1

    iL = iR = 0
    endL = len(Yleft)
    endR = len(Yright)

    for _ in range(endL + endR):
        if iL >= endL:
            for pos in range(iL, endL):
                dominance_factors[Yleft[pos][0]] = dominance_factors.get(Yleft[pos][0], 0) + 1
                dominance_factors[Yright[iR][0]] = dominance_factors.get(Yright[iR][0], 0) + 1
            iR += 1
        elif iR >= endR:
            iL += 1
        elif Yleft[iL][1] < Yright[iR][1]:
            for pos in range(iR, endR):
                dominance_factors[Yright[pos][0]] = dominance_factors.get(Yright[pos][0], 0) + 1
                dominance_factors[Yleft[iL][0]] = dominance_factors.get(Yleft[iL][0], 0) + 1
            iL += 1
        else:
            iR += 1

    print(arr, Yleft, Yright, l, m, r, S, dominance_factors)

    return 

def MergeSort(towersX, towersY, l, r, S, dominance_factors):
    if (l >= r):
        return
    else:
        # m = l + (r-l)//2
        m = (l + r) // 2

        Yleft = []
        Yright = []
        for tower in towersY:
            if tower[0] <= towersX[m][0]:
                Yleft.append(tower)
            else:
                Yright.append(tower)

        MergeSort(towersX, Yleft, l, m, S, dominance_factors)
        MergeSort(towersX, Yright, m+1, r, S, dominance_factors)
        Merge(towersX, Yleft, Yright, l, m, r, S, dominance_factors)

# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ")

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
n = len(towers)
S = [i for i in range(n)]
dominance_factors = {}
# for x, y in towersX:
#     dominance_factors[x] = 0
 
MergeSort(towersX, towersY, 0, n-1, S, dominance_factors)

print(towers)
print(dominance_factors)


# def compute_dominance_factors(n, towers):
#     # Add index to towers for tracking dominance factor
#     indexed_towers = [(tower[0], tower[1], i) for i, tower in enumerate(towers)]
#     dominance_factors = [0] * n

#     # Sort the towers using merge sort and track dominance factor
#     merge_sort(indexed_towers, dominance_factors)

#     return dominance_factors


# # Sample input
# # n = 4
# # towers = [
# #     (3, 3),
# #     (4, 2),
# #     (5, 6),
# #     (2, 1)
# # ]

# n = 8
# towers = [
#     (1, 7),
#     (2, 2),
#     (3, 6),
#     (4, 5),
#     (5, 1),
#     (6, 8),
#     (7, 3),
#     (8, 4)
# ]

# # Compute dominance factors
# dominance_factors = compute_dominance_factors(n, towers)

# # Output the dominance factors
# print(*dominance_factors)