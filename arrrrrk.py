def reverse_and_print_array(arr):
    """Reverses an array in-place and prints it."""
    arr.reverse()
    print(arr)

# Example usage:
my_array = [1, 2, 3, 4, 5]
reverse_and_print_array(my_array)  # Output: [5, 4, 3, 2, 1]

another_array = ["apple", "banana", "cherry"]
reverse_and_print_array(another_array) # Output: ['cherry', 'banana', 'apple']
