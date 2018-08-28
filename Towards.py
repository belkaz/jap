# [4] -> [00000] -> [02220]
# [2] -> [11000] -> [11020]
def Towards (height, width, cols, rows,  probe):    
    for i in range ( height ):
        if len ( cols[i] ) == 1:
            tempArr = []
            for j in range ( width ):
                tempArr.append( 0 )
            for j in range ( cols[i][0] ):
                tempArr[j] += 1
            for j in range ( width - cols[i][0], width):
                tempArr[j] += 1 
            for j in range ( width ):
                if tempArr[j] == 2:
                    probe[i][j] = 2           
    for i in range ( width ):
        if len ( rows[i] ) == 1:
            tempArr = []
            for j in range ( height ):
                tempArr.append( 0 )
            for j in range ( rows[i][0] ):
                tempArr[j] += 1
            for j in range ( height - rows[i][0], height):
                tempArr[j] += 1 
            for j in range ( height ):
                if tempArr[j] == 2:
                    probe[j][i] = 2
     