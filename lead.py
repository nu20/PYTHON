def leaders(a , a_size):
  current = a[a_size-1]
  print(current)
  for i in range(a_size-2, -1, -1):
    if current < a[i]:
       print(a[i])
       current = a[i]
a = [4,5,7,2,1]
leaders(a,len(a))
