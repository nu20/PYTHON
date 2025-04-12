def checksorted(a) :
    length = len(a)
    if length == 1 or length == 0 :
       return True
    return a [0] <= a [1] and checksorted(a[1:])
a = [1 , 2 ,3 , 5 ,7 ,0 ,67]
if checksorted(a) :
    print("\nyes given array is sorted")
else :
    print("\nno the array is not sorted")
    
    