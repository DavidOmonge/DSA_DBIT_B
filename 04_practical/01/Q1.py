# Function to reverse a list
print("Function to reverse a list")
numbers = [1,2,3,4,5,6]
print(f"Not reversed: {numbers}")

def reverse_list(x):
    x.sort(reverse=True)

reverse_list(numbers)

print(f"Reversed: {numbers}")
