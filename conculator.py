row = 12
col = 8

for i in range(row + 1):
    for j in range(col + 1):
        
        if i == 0 or j == 0 or i == row or j == col:
            print('*', end=' ')
        
        elif i == 2 and 2 <= j <= 6:
            print('*', end=' ')
        elif i == 4 and j in [2,3,4,5,6] or (i == 3 and j in [2,6]):
            print('*', end=' ')
        elif i == 6 and j in [2, 4, 6]:  
            print(7 + (j // 2 - 1), end=' ')
        elif i == 8 and j in [2, 4, 6]: 
            print(4 + (j // 2 - 1), end=' ')
        elif i == 10 and j in [2, 4, 6]:  
            print(1 + (j // 2 - 1), end=' ')
        else:
            print(' ', end=' ')
    print()
