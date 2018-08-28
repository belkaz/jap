#[2] -> [01000] -> [11000]
def CouldntSet ( height, width, cols, rows,  probe ):
    for i in range ( height ):
        negArr = []
        for j in range ( width ):
            if probe[i][j] == 1:
                negArr.append( j )        
        for j in range ( len ( negArr )):
            isAllUnk = True
            for k in range ( len ( range ( negArr[0] ))):
                if probe[i][k] != 0:
                    isAllUnk = False
            if isAllUnk :
                if len ( range ( negArr[0] )) < cols[i][0]:
                    for k in range ( len ( range ( negArr[0] ))):
                        probe[i][k] = 1
    for i in range ( width ):
        negArr = []
        for j in range ( height ):
            if probe[j][i] == 1:
                negArr.append( j )        
        for j in range ( len ( negArr )):
            isAllUnk = True
            for k in range ( len ( range ( negArr[0] ))):
                if probe[k][i] != 0:
                    isAllUnk = False
            if isAllUnk :
                if len ( range ( negArr[0] )) < rows[i][0]:
                    for k in range ( len ( range ( negArr[0] ))):
                        probe[k][i] = 1
            