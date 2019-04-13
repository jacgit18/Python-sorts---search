position = -1


def linear_search(numbers, n):
    i = 0

    while i < len(numbers):
        if numbers[i] == n:
            globals()['position'] = i
            return True
        i = i + 1
    return False


numbers = [1, 5, 9, 3, 4, 6]
n = 9
if linear_search(numbers, n):
    print("found at ", position + 1)
else:
    print("lost")
# position = -1


# def search(list1, n):
#    i = 1

#   while i < len(list1):
#        if list1[i] == n:
#            globals()['position'] = i
#            return True
#        i = i + 1

#    return False


# list1 = [1, 5, 9, 3, 4, 6]
# n = 6

# if n in list1:
#    print("found at ", position + 1)
# # print("found")
# else:
#    print("not found")
