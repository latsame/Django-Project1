# def triangle_number(n):
    
#     for i in range(1,11):
        
#         print(triangle_number(i))
def triangular_series( n ):
    j = 1
    k = 1
     
    
    for i in range(1, n + 1):
        print(k, end = ' ')
        j = j + 1 
         
        
        k = k + j
         
# Driven Code
n = 10
triangular_series(n)