def Borders(width, height, cols, rows, probe):
    for i in range ( height ):
        if probe [i][0] == 200:
            for j in range ( cols[i][0] ):
                probe[i][j] = 200

        if probe [i][width - 1] == 200:
            for j in range (width - cols[i][len(cols[i])-1], width -1):
                probe[i][j] = 200
   

    for i in range ( width ):
        if probe [0][i] == 200:
            for j in range ( rows[i][0] ):
                probe[j][i] = 200
 
        if probe[height - 1][i] == 200:   
            q0 = height -2        
            for j in range (height - rows[i][len(rows[i]) - 1], height -1):
                probe[j][i] = 200
                q0 -= 1
            probe[q0][i] = -1
            

# план - проверка на отталкивание от стены