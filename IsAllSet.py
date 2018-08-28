# [1,1] -> [20002] -> [21112]
def IsSetAll ( height, width, cols, rows,  probe ):
    for i in range ( height ):
        if sum( cols[i]) == probe[i].count ( 2 ):
            for j in range( width ):
                if probe[i][j] == 0:
                    probe[i][j] = 1
    
    for i in range ( width ):
        vertArr = []
        for j in range ( height ):
            vertArr.append( probe[j][i])
        if sum( rows[i]) == vertArr.count ( 2 ):
            for j in range( height ):
                if probe[j][i] == 0:
                    probe[j][i] = 1