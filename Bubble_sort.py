def bubble_sort(numbers):
    for i in range(0, len(numbers) - 1, 1):
        for j in range(0, len(numbers) - 1 - i, 1):
            if numbers[j] < numbers[j + 1]:

                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
        print(numbers)


numbers = [1, 5, 9, 3, 4, 6]
print(numbers)
bubble_sort(numbers)
print(numbers)