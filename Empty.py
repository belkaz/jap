def Empty ( height, width, cols, rows,  probe):
    for i in range ( height ):
        if len (cols[i] ) == 0  or ( len ( cols[i]) == 1 and cols[i][0] == 0) :
            for j in range ( width ):
                probe[i][j] = 1
    for i in range ( width ):
        if len ( rows[i] ) == 0  or ( len ( rows[i] ) == 1 and rows[i][0] == 0) :
            for j in range ( height ):
                probe [j][i] = 1
                 