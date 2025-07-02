numbers = [3, 17, 9, 24, 6]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print(f"smallest value is: {smallest}")