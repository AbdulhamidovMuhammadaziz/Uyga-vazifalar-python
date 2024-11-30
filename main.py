# row = 5
# col = 5

# ortaRow = row//2
# ortaCol = col//2


# Masala 1
# for i in range(row) :
#     for j in range(col) :
#         print("*" , end=" ")
#     print()
# print()

# Masala 2
# for i in range(row) :
#     for j in range(col) :
#         if j==0 :
#             print("#" , end=" ")
#         else :
#             print("*" , end=" ")
#     print()
# print()

# Masala 3
# for i in range(row) :
#     for j in range(col) :
#         if j==0 or i ==0 :
#             print("#" , end=" ")
#         else :
#             print("*" , end=" ")
#     print()
# print()


# Masala 4 
# for i in range(row) :
#     for j in range(col) :
#         if i==0 or j==0 or j==col-1 :
#             print("#" , end=" ") 
#         else :
#             print("*" , end=" ")
#     print()
# print()


# Masala 5
# for i in range(row) :
#     for j in range(col) :
#         if i==0 or j==0 or j==col-1 or i==row-1 :
#             print("#" , end=" ") 
#         else :
#             print("*"  , end=" ")
#     print()
# print()


# Masala 6
# for i in range(row) :
#     for j in range(col) :
#         if i==0 or j==0 or i==row-1 or j==col-1 or i==ortaRow :
#             print("#" , end=" ")
#         else:
#             print("*" , end=" ") 
#     print()
# print()

# Masala 7 
# for i in range(row) :
#     for j in range(col) :
#         if i==0 or j==0 or i==row-1 or j==col-1 or i==ortaRow or j==ortaCol :
#             print("#" , end=" ")
#         else :
#             print("0" , end=" ") 
#     print()
# print()


# Masala 8
# for i in range(row) :
#     for j in range(col) :
#         if i==j :
#             print("0" , end=" ") 
#         else :
#             print("*" , end=" ")
#     print()
# print()


# Masala 9
# for i in range(row) :
#     for j in range(col) :
#         if i>=j :
#             print("0" , end=" ")
#         else :
#             print("*" , end=" ")
#     print()
# print()


# Masala 10
# for i in range(row) :
#     for j in range(col) :
#         if (i+j) % 2 == 0  :
#             print("0" , end=" ")
#         else:
#             print("1" , end=" ")
#     print()
# print()

# Masala 11
# for i in range(row) :
#     for j in range(col) :
#         if i==j or i+j==col-1 :
#             print("0" , end=" ") 
#         else :
#             print("1" , end=" ")
#     print()
# print()


# Masala 12
# for i in range(row) :
#     for j in range(col) :
#         if i==j or j+i==col-1 or i==0 or j==0  or i==row-1 or j==col-1:
#             print("0", end=" ")
#         else :
#             print("1" , end=" ")
#     print()
# print()


# Masala 13
# for i in range(row) :
#     for j in range(col) :
#         print(chr(65+i), end=" " )
#     print()
# print()


# Masala 14
# num = 1
# for i in range (1 , row+1) :
#     for j in range(1 , col+1) :
#         print(num, end=" ")
#         num+=1
#     print()
# print()

# Masala 15 
# num = 1
# for i in range(row) :
#     for j in range(col) :
#         print(num , end=" ")
#         num+=2
#     print()
# print()

# Masala 17
# num = 1
# count = 0
# for i in range(row) :
#     for j in range(col) :
#         print(num , end=" ")
#         if j==0 or j==col-1 :
#            count+=num
#         num+=1
#     print()
# print()
# print(count)


# Masala 18
# num = 1 
# count = 0 
# for i in range (row) :
#     for j in range(col) :
#         print(num , end=" ")
#         if j==0 or j==col-1 or i==ortaRow :
#             count+=num
#         num+=1
#     print()
# print()
# print(count)
     

# Masala 19
# num = 1 
# count = 0 
# for i in range (row) :
#     for j in range(col) :
#         print(num , end=" ")
#         if j==0 or j==col-1 or i==ortaRow or j==ortaCol :
#             count+=num
#         num+=1
#     print()
# print()
# print(count)
    

# Masala 20
# num = 1 
# count = 0 
# for i in range (row) :
#     for j in range(col) :
#         print(num, end=" ")
#         if j<=i :
#             count+=num
#         num+=1
#     print()
# print()
# print(count)

# Masala 21 
# num = 1
# count = 0


# for i in range(row ) :
#     for j in range(col) :
#         print(num , end=" ")
#         if i+j!=col-1 and j <=i :
#             count+=num
#         num+=1
#     print()
# print()

# print(count)

# Masala 22
# num  = 1
# count = 0

# for i in range(row) :
#     for j in range(col) :
#         print(num , end=" ")
#         if i==j or j+i==col-1 :
#             count+=num
#         num+=1
#     print()
# print()
# print(count)

# Masala 23
# for i in range(row) :
#     for j in range(col) :
#         if j<=i :
#             print("*" , end=" ")
#         else :
#             print(" " , end=" ")
#     print()
# print()


# Masala 24
# for i in range(1 , row+1) :
#     for j in range(1 , col+1) :
#         if j<=i :
#             print(j , end=" ")
#         else :
#             print(" " , end=" ")
#     print()
# print()

# Masala 25
# for i in range(1 , row+1) :
#     for j in range(1 , col+1) :
#         if j<=i :
#             print(i , end=" ")
#         else :
#             print(" " , end=" ")
#     print()
# print()

#   M harifi 

# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#          ( j == 1 or j == input_column)
#             or (i == j and j <= input_column // 2+1 and i <= input_row // 2+1)
#             or ( j == (input_column - i + 1) and i <= input_row // 2+1 )
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()  

# SET MAVZUSI 

mayset = {'azizbek','ulugbek', 'azamat', 'lochinbek'}
mayset.add('Ali')
print(mayset)