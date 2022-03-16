from random import randint

def RandomQuickSort(L):
    n = len(L)

    if n <= 1:
        return L

    pivot_index = randint(0, n-1)
    pivot = L[pivot_index]

    left, right = [], []
    for i in [index for index in range(n) if index != pivot_index]:
        if L[i] <= pivot:
            left.append(L[i])
        else:
            right.append(L[i])

    return RandomQuickSort(left) + [pivot] + RandomQuickSort(right)
