def arr_min_max(arr , arrsize):
    maximum = arr[0]
    minimum = arr[0]
    for i in range(len(arr)):
        if arr[i]>maximum:
           maximum = arr[i]

    for i in range(len(arr)):
        if arr[i]<minimum:
           minimum = arr[i]
    print("maximum is " , maximum)
    print("minimum is " , minimum)
arr = [1,3,5,7,8]
arr_min_max(arr , len(arr))