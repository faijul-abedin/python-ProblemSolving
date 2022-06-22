# Get the total sum of all elements in an array.

# Function declaration of get_sum.
def get_sum(numbers):
    totals = 0

# For loop in python for travel each numbers in the array.
# And add numbers in total with next element and return total continuously until the last element.
    for num in numbers:
        totals = totals + num
    return totals


# This is array of numbers.
numbers = [1, 2, 3, 4, 5, 6, 7]

# Call the function for total.
total = get_sum(numbers)

# Finally print the result.
print("The total of all elements in the array is:", total)