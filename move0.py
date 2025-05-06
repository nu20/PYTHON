def move(a , a_size) :
    non = 0
    zero = 0
    while non != a_size:
        if (a[non] != 0):
          a[non] , a[zero] = a[zero] , a[non]
          zero+=1
        else:
           non+=1
a = [0 ,1 ,4 , 8 ,9]   
a_size = len(a)
print (a)
move(a , a_size) 
print(a)
