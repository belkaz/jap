def Sum ( height, width, cols, rows,  probe ):
    for i in range ( height ):
        negArr = []
        for j in range ( width ):
            if probe[i][j] == 1:
                negArr.append ( j )        
        if len ( cols[i] ) > 1 :
            if sum ( cols[i] ) + len ( cols[i] ) -1 == width - len ( negArr ):
                    lastInd = 0
                    for j in range ( len ( cols[i] )):
                        for k in range ( lastInd, lastInd + cols[i][j] ):
                            probe[i][k] = 2
                        lastInd += cols[i][j]
                        if lastInd < width:
                            probe[i][ lastInd ] = 1
                            lastInd += 1
    for i in range ( width ):
        negArr = []
        for j in range ( height ):
            if probe[j][i] == 1:
                negArr.append ( j )        
        if len ( rows[i] ) > 1 :
            if sum ( rows[i] ) + len ( rows[i] ) -1 == height - len ( negArr ):
                    lastInd = 0
                    for j in range ( len ( rows[i] )):
                        for k in range ( lastInd, lastInd + rows[i][j] ):
                            probe[k][i]= 2
                        lastInd += rows[i][j]
                        if lastInd < height:
                            probe[ lastInd ][i] = 1
                            lastInd += 1

