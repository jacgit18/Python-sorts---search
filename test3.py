def bubble_sort(A):

    for i in range(0, len(A) - 1, 1):

        for j in range(0, len(A) - 1 - i, 1):
            if A[j] > A[j + 1]:

                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
            print(A)
    return A


A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]
maxvalue = A[0]
minvalue = A[0]

list_sum = 0

for i in range(0, len(A) + 0, 1):
    # before it was len(A) - 1 that is why max and min values where off initially
    if maxvalue < A[i]:
        maxvalue = A[i]

    if minvalue > A[i]:
        minvalue = A[i]
    list_sum += A[i]
# total_sum = sum(A)
average = list_sum / len(A)


def sort0(A):
    for index in range(1, len(A)):
        value = A[index]
        i = index - 1
        while i >= 0:
            if value < A[i]:
                A[i + 1] = A[i]
                A[i] = value
                i = i - 1
            else:
                break
    return A


def median(A):
    half = len(A) // 2
    sort0(A)
    if not len(A) % 2:
        return (A[half - 1] + A[half]) / 2.0
    return A[half]


A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]
median_value = A[0]


def maximum(A):
    Max = 0
    for item in A:
     if item > Max:
         Max = item
    return Max


def mode(A):
    count = {}

    for i in A:
        if i in count.keys():
            count[i] = count[i] + 1
        else:
            count[i] = 1

    if len(A) > 0:
        listrange = maximum(count.values())
        print("Mode Value: ")

        for i in count.keys():
            if count[i] == listrange:
                print(i)


A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]

print("   ")
print("Problem 1a")
print("------------------")
print("Mean Value: ", average)
median(A)
print("Median: ", A)
print("The Median is: ", median(A))
mode(A)


print("   ")
print("Problem 1b")
print("------------------")
print("Max Value: ", maxvalue)
print("Min Value: ", minvalue)
print("   ")

print("Problem 1c Bubble Sort: ")
print("------------------")
print(A)
bubble_sort(A)


def insertion_sort(A):
    for index in range(1, len(A)):
        value = A[index]
        i = index - 1
        while i >= 0:
            if value < A[i]:
                A[i+1] = A[i]
                A[i] = value
                i = i - 1
                print(A)
            else:
                break

    return A


# how would you write code to have the list revert to default order
A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]


print(" ")
print("Problem 1d Insertion Sort: ")
print("------------------")
print(A)
insertion_sort(A)


def sort1(even):
    for index in range(1, len(A)):
        value = A[index]
        i = index - 1
        while i >= 0:
            if value < A[i]:
                A[i + 1] = A[i]
                A[i] = value
                i = i - 1
            else:
                break
    return even


def sort2(odd):
    for index in range(1, len(A)):
        value = A[index]
        i = index - 1
        while i >= 0:
            if value < A[i]:
                A[i + 1] = A[i]
                A[i] = value
                i = i - 1
            else:
                break
    return odd


def odd_even(A):

    odd = [num for num in A if num % 2 == 1]
    even = [num for num in A if num % 2 == 0]
    print(" ")

    print("Problem 2")
    print("Ordered Even Start               Ordered Odd Start")
    print("------------------               ----------------")
    print(sort1(even) + sort1(odd))

    return A


odd_even(A)


def selection_sort(A):
    for i in range(0, len(A) - 1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        if min != i:
                 A[i], A[min] = A[min], A[i]

        print(A)


A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]


def selection_sort2(A):
    for i in range(0, len(A) - 1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] > A[min]:
                min = j
        if min != i:
                 A[i], A[min] = A[min], A[i]

        print(A)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def merge_sort(mylst):
    if len(mylst) <= 1:
        return mylst

    mid = int(len(mylst)/2)
    left = merge_sort(mylst[:mid])
    right = merge_sort(mylst[mid:])
    return merge(left, right)


print("  ")
print("Problem 3 Merge sort")
print("----------------------------------")
A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]
print(merge_sort(A))


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def merge_sort(mylst):
    if len(mylst) <= 1:
        return mylst

    mid = int(len(mylst)/2)
    left = merge_sort(mylst[:mid])
    right = merge_sort(mylst[mid:])
    return merge(left, right)


A = [6, 9, 0, 4, 2, 8, 0, 0, 8, 5, 2, 1, 3, 20, -1]
print(merge_sort(A))


print(" ")
print("Problem 3 Selection sort")
print("----------------------------------")
selection_sort(A)
print(A)
print("Problem 3 Selection sort part 2")
selection_sort2(A)
print(A)
print(" ")


print("Problem 4 Palindrome")
print("----------------------------------")
A = "Abracadabra"
print(A)
A1 = A[3:6:1]
A2 = A[5:8:1]
print(A1 + "  ",  A2)


print("   ")
A = "Abracadabra"
print(A)
A = A[::-1]
print(A)
A_flip = A[5:8:]
print(A_flip)
A_flip1 = A[3:6:]
print(A_flip1)
print("   ")
if A1 == A_flip and A2 == A_flip1:
    print(" these characters are palindromes  ")
else:
    print("not palindrome")

# Mental Steps ////////////////////////////////////////////////////////////////////////////////
# start from zero index with a loop checking if the first three letters match with the first
# three letters when the word is flipped, than flip the whole word back to its original state and
# now starting from the second letter which is the first index and check for the next pair of three
# letters including that second letter and than flip the word again to checking the second index again
# continuing until you gone down the whole list of the word once after each flip comparing the three
# letters as you go down the list
#
# //////////////////////////////////////////////////////////////////////////////////////////////

# def Palindrome(A):
#    B = A[5:8:-1]

#   for i in range(0, len(A) - 1, 3):
#        for j in range(0, len(A) - 1, 3):
#          if A[3:6:1] == B:
#              print("these characters are palindromes ")

#        else:
#            print("not palindrome")


