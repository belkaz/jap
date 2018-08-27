def Reborder_H ( height, width, cols, probe) :
    for i in range ( height ):
        for j in range ( width ):
            if probe[i][j] == 200:
                isAllPrevNeg =True
                for k in range ( j ):
                    if probe[i][k] != -1:
                        isAllPrevNeg = False
                if isAllPrevNeg :
                    for k in range( j , j + cols[i][0] ):
                        probe[i][k] = 200
                    probe[i][j + cols[i][0] -1 ]
                isAllNextNeg = True
                for k in range ( j+1, width ):
                    if probe[i][k] != -1:
                        isAllNextNeg = False
                if isAllNextNeg :
                    for k in range ( j - cols[i][ len(cols[i]) -1 ] + 1 , j):
                        probe[i][k] = 200
                    probe[i][ j - len(cols[i]) - 1]  = -1     
