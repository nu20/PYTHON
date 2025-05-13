def equilibrium(arr):
    leftsum = 0
    rightsum = 0
    n = len(arr)
    for i in range(n):
        leftsum  = 0
        rightsum = 0
        for j in range(i):
            leftsum += arr[j]
        for j in range(i + 1 ,n):
            rightsum += arr[j]
        if leftsum == rightsum:
            return i 
    return -1
arr = [2,3,6,4,1]
print("element :" , arr[equilibrium(arr)])