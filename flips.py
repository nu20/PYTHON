def min_flips(arr):
    n = len(arr)
    if n == 0:
        return 0

    flips_to_0 = 0
    flips_to_1 = 0

    for num in arr:
        if num == 0:
            flips_to_1 += 1
        else:
            flips_to_0 += 1
    
    return min(flips_to_0, flips_to_1)
arr1 = [0, 1, 0, 1, 0]
print(f"Minimum flips for {arr1}: {min_flips(arr1)}")  # Output: 2

arr2 = [1, 1, 1, 0]
print(f"Minimum flips for {arr2}: {min_flips(arr2)}")  # Output: 1

arr3 = [0, 0, 0]
print(f"Minimum flips for {arr3}: {min_flips(arr3)}")  # Output: 0
