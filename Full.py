def Full ( height, width, cols, rows,  probe ):
    for i in range ( height ):
        negArr = []
        for j in range ( width ):
            if probe[i][j] == 1:
                negArr.append ( j )
        if len ( cols[i] ) == 1 and cols[i][0] == width - len ( negArr ):
            for j in range ( width ):
                if not ( j in negArr ):
                    probe[i][j] = 2
    for i in range ( width ):
        negArr = []
        for j in range ( height ):
            if probe[j][i] == 1:
                negArr.append ( j )
        if len ( rows[i] ) == 1 and rows[i][0] == height - len ( negArr ):
            for j in range ( height ):
                if not ( j in negArr ):
                    probe[j][i] = 2