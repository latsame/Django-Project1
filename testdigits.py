
def triangle_number( n ):
    a = 1
    b = 1

    for i in range(1, n + 1):
        print(b, end = ' ')
        a = a + 1 
        b = b + a
        
n = 10
triangle_number(n)