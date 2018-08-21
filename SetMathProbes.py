def SetMathProbes(width, height, cols, rows, probe):   
    for i in range( height ):        
        empCount = [] # ! -1
        setCount = []# 200
        for j in range( width ):
            if ( probe[i][j] == 200):
                setCount.append( j )
            elif ( probe[i][j] == -1):
                empCount.append( j )
        for j in range( width ):
            if (not ( j in empCount )) and (not (j in setCount)):
                q0 = sum(cols[i]) - len(setCount) #сколько еще надо расставить
                q1 = width - len(empCount) - len(setCount) #сколько свободных
                probe[i][j] += int(q0 / q1 *100)

    for i in range( width ):        
        empCount = [] # ! -1
        setCount = []# 200
        for j in range( height ):
            if ( probe[j][i] == 200):
                setCount.append( j )
            elif ( probe[j][i] == -1):
                empCount.append( j )
        for j in range( height ):
            if (not ( j in empCount )) and (not (j in setCount)):
                q0 = sum(rows[i]) - len(setCount) #сколько еще надо расставить
                q1 = height - len(empCount) - len(setCount) #сколько свободных
                probe[j][i] += int(q0 / q1 *100)
        