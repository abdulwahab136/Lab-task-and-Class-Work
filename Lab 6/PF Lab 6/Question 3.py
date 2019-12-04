def even(x):
   for i in range (2,x+1):
    if i%2==0:
        print(i,end=(','))
    elif i%3==0:
        print(i,end=(','))
even(10)