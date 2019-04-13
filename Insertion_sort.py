def insertion_sort(numbers):
    numbers = [1, 5, 9, 3, 4, 6]
    for index in range(1, len(numbers)):
        value = numbers[index]
        i = index - 1
        while i >= 0:
            if value < numbers[i]:
                numbers[i+1] = numbers[i]
                numbers[i] = value
                i = i - 1
            else:
                break
    return numbers


number = [1, 5, 9, 3, 4, 6]
print(insertion_sort(number))