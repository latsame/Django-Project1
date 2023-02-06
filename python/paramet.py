def fib(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('1')
    else:
        print("Iterative Approach: ", end=' ')
        print(a,b,end=' ')
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total,end=' ')
        print()
        return b
         
fib(11)