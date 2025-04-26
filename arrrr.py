def arraymean(arr , arr_size):
    total_sum = 0
    for i in range(0 , arr_size):
        total_sum += arr[i]
    return float (total_sum/arr_size)

def arraymedian(arr , arr_size):
    sorted(arr)
    if arr_size % 2 !=0:
     return float(arr[int(arr_size / 2)])
    else:
       return float((arr[int((arr_size-1)/2)]+arr[int(arr_size/2)])/2)
    


arr = [ 1 , 6 , 8 , 4 , 8 , 9 , 9]
print(arraymean(arr , len (arr)))
print(arraymedian(arr , len (arr) ))