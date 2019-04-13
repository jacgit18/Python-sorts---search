
def selection_sort(numbers):

    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if numbers[j] < numbers[minpos]:
                minpos = j


                temp = numbers[i]
                numbers[i] = numbers[minpos]
                numbers[minpos] = temp

                print(numbers)


numbers = [1, 5, 9, 3, 4, 6]
selection_sort(numbers)
print(numbers)