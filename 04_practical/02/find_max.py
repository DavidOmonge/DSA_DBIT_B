

numbers = [3, 17, 9, 24, 6]

# Assume the first number is the largest to start
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(f"Largest value: {largest}")