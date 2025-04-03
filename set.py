def printpowerset(set , setsize) :
    powersetsize = 2**setsize
    outer = 0
    inner = 0
    for outer in range(0 , powersetsize) :
        for inner in range(0 , setsize) :
            if(outer&(1 << inner)) > 0 :
                print(set[inner] , end ="")
        print("")
set =[1,5,3]
size = len(set)
printpowerset(set , size)
    