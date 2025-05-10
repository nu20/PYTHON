def longest_alternating_subarray(arr):

  if not arr:
    return 0

  max_length = 1
  current_length = 1
  previous_parity = arr[0] % 2

  for i in range(1, len(arr)):
    current_parity = arr[i] % 2

    if current_parity != previous_parity:
      current_length += 1
    else:
      current_length = 1

    max_length = max(max_length, current_length)
    previous_parity = current_parity

  return max_length
