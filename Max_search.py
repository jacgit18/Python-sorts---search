#def max_search(numbers, maxvalue, minvalue, i):
numbers = [1, 5, 9, 3, 4, 6, 45]

maxvalue = numbers[0]
minvalue = numbers[0]

for i in range(0, len(numbers), 1):
    if maxvalue < numbers[i]:
        maxvalue = numbers[i]

    if minvalue > numbers[i]:
        minvalue = numbers[i]

print(maxvalue)
print(minvalue)