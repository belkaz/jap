def FullLine(width, height, cols, rows, probe):    
    for i  in range( height ):
        negArr = []
        posArr = []
        for j in range( width ):
            if probe[i][j] == -1:
                negArr.append(j)    
            elif probe[i][j] == 200:
                posArr.append(j)   
        if len(cols[i]) == 0:
            for j in range( width ):
                probe[i][j] = -1
        if len(cols[i]) == 1:                             
            if width - len(negArr) == cols[i][0]:
                for k in range( width ):
                    if not ( k in negArr): 
                        probe[i][k] = 200
            if len(posArr) == cols[i][0]:
                for k in range ( width ):
                    if not (k in posArr):
                        probe[i][k]= -1
        
    for i  in range( width ):
        negArr = []
        posArr = []
        for j in range( height ):
            if probe[j][i] == -1:
                negArr.append(j)
            elif probe[j][i] == 200:
                posArr.append(j) 
        if len(rows[i]) == 0:
            for j in range( height ):
                probe[j][i] = -1        
        if len(rows[i]) == 1:
            if height - len(negArr) == rows[i][0]:
                for k in range( height ):
                    if not ( k in negArr): 
                        probe[k][i] = 200
            if len(posArr) == rows[i][0]:
                for k in range ( height ):
                    if not (k in posArr):
                        probe[k][i] = -1