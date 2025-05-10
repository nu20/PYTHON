def kadane(a):
    n = len(a)
    max_so_far = 0
    max_ending = 0
    for i in range(0 ,n):
        max_ending = max_ending + a[i]
        if(max_ending<0):
            max_ending = 0
        if(max_so_far<max_ending):
            max_so_far = max_ending
    return max_so_far
def maxcircular(a):
    n = len(a)
    maxkadane = kadane(a)
    max_wrap = 0
    for i in range (0 , n):
        max_wrap += a[i]
        a[i] = - a[i]
    max_wrap += kadane(a)

    if  max_wrap > maxkadane:
     return  max_wrap
    else:
     return maxkadane
a = [11 ,10 ,-20 , 5 , -3, -5 ,8 ,-13 , 10]
print(maxcircular(a))

