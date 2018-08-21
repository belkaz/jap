def BorderElements(width, height, cols, rows, probe):
    for i in range( height ):
        if sum(cols[i]) < width:
            if  probe[i][0] == 200 :
                for j in range (0, cols[i][0]) :
                    probe[i][j] = 200
                probe[i][cols[i][0]+1] = -1
            if probe[i][width -1] == 200:
                t0 = width - cols[i][len(cols[i])-1]
                for j in range(t0, width):
                    probe[i][j] = 200
                probe[i][t0-1] = -1

    for i in range( width ):
        if sum(rows[i]) < height:
            if  probe[0][i] == 200:
                for j in range (0, rows[i][0]) :
                    probe[j][i] = 200
                probe[rows[i][0]+1][i] = -1
            if probe[height -1][i] == 200:
                t0 = height - rows[i][len(rows[i])-1]
                for j in range(t0, height):
                    probe[j][i] = 200
                probe[t0-1][i] = -1