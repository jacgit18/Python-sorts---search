
def quick_sort(B):
    if len(B) < 2:
        return B
    else:
        pivot = B[0]
        del(B[0])
        rightside = []
        leftside = []

        for A in B:
            if A < pivot:
                leftside.append(A)
            else:
                rightside.append(A)
        return quick_sort(leftside) + [pivot] + quick_sort(rightside)


A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]
print("Problem 3 Quick sort")
print("----------------------------------")
print(quick_sort(A))


def quick_sort(B):
    if len(B) < 2:
        return B
    else:
        pivot = B[0]
        del(B[0])
        rightside = []
        leftside = []

        for A in B:
            if A > pivot:
                leftside.append(A)
            else:
                rightside.append(A)
        return quick_sort(leftside) + [pivot] + quick_sort(rightside)


A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]
print(quick_sort(A))




