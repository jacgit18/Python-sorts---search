position = -1


def binary_search(numbers, n):

    lower = 0  # lower bound
    upper = len(numbers) - 1  # upper bound

    while lower <= upper:
        mid = (lower+upper) // 2

        if numbers[mid] == n:
            globals()['position'] = mid
            return True
        else:
            if numbers[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1


numbers = [10, 50, 94, 30, 45, 69]
# number must be ordered in binary search algo
# in this example you would,nt be able to find anything past 94
n = 50

if binary_search(numbers, n):
    print("found at ", position + 1)
else:
    print("lost")
