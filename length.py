def find_list_length(my_list):
    length = 0
    for _ in my_list:
        length += 1
    return length
my_list = [10, 20, 30, 40, 50]
list_length = find_list_length(my_list)
print("Length of the list:", list_length)
