def Towards(width, height, cols, rows, probe):
    for i in range ( height ):
        tempArr = []
        for j in range( width ):
                tempArr.append(0)
        if (len(cols[i]) == 1) and cols[i][0] > width/2 : 
            for k in range( cols[i][0] ) :
                tempArr[k] += 1
            for k in range (width-cols[i][0], width):
                tempArr[k] += 1
        for j in range( width ):
            if tempArr[j] == 2:
                probe[i][j] = 200
            
    for i in range ( width ):
        tempArr = []
        for j in range( height ):
                tempArr.append(0)
        if (len(rows[i]) == 1) and rows[i][0] > height/2 : 
            for k in range( rows[i][0] ) :
                tempArr[k] += 1
            for k in range (height-rows[i][0], width):
                tempArr[k] += 1
        for j in range( height ):
            if tempArr[j] == 2:
                probe[j][i] = 200