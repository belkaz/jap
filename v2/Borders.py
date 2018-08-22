def Borders(width, height, cols, rows, probe):
    for i in range ( height ):
        if probe [i][0] == 200:
            for j in range ( cols[i][0] ):
                probe[i][j] = 200
        if probe [i][width - 1] == 200:
            for j in range (width - cols[i][len(cols[i])-1], width -1):
                probe[i][j] = 200