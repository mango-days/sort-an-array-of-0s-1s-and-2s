# Sort an array of 0s, 1s and 2s 

# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

array = [ 1, 0, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 0, 2, 0, 0 ]
count_2 = array.count ( 2 )
for index in range ( 0 , count_2 ) : array.remove ( 2 )
i = 0
j = len ( array ) - 1
while i <= j :
    if array [ i ] == 1 :
        if array [ j ] == 0 :
            array [ i ] = 0
            array [ j ] = 1
        else : j -= 1
    else : i += 1
for index in range ( 0 , count_2 ) : array.append ( 2 )
print ( array )
