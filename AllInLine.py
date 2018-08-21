def AllInLine(width, height, cols, rows, probe):        
    for i in range( height ): 
        zeroCol = []          # [1,1]:5 если на поле 2 из 2 -> все остальные делаем пустыми
        for j in range( width ):            
            if (probe[i][j] <= 0) :
                zeroCol.append( j )        
        if (sum(cols[i]) == width - len(zeroCol)):
            for j in range ( width ):
                if j in zeroCol:                    
                    probe[i][j] = -1  
        negat = []   # [1,1]:5 если на поле 3 пустые ->заполнить оставшиеся
        for j in range ( width ):
            if (probe[i][j] == -1):
                negat.append(j)
        if (sum(cols[i]) == width - len( negat )):
            for j in range ( width ):
                if (not (j in negat) and ( (probe[i][j] >=0) and (probe[i][j] < 100))):
                    probe[i][j] = 100
                  

    for i in range( width ):
        zeroRow = []       
        for j in range( height ):
            if (probe[j][i] <= 0):
                zeroRow.append( j )
        if (sum(rows[i]) == height - len(zeroRow)):
            for j in range( height ):
                if  j in zeroRow:
                    probe[j][i] = -1 
        negat = []  
        for j in range ( height ):
            if (probe[j][i] == -1):
                negat.append(j)
        if (sum(rows[i]) == height - len( negat )):
            for j in range ( height ):
                if (not (j in negat) and ( (probe[j][i] >=0) and (probe[j][i] < 100))):
                    probe[j][i] = 100        
        


