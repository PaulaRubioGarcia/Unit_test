numbers = [10, 5, 25, 8, 17]

def largest_number(numbers):
    # Base case: 
    if len(numbers) == 1:
        return numbers[0]
    else:
        # Recursive case: 
        max_rest = largest_number(numbers[1:])
        # Return the larger of the two
        return numbers[0] if numbers[0] > max_rest else max_rest

print("Largest number of the list is:", largest_number(numbers))