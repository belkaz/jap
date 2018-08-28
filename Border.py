#[3] -> [20000] ->[22200]
def Border ( height, width, cols, rows,  probe ):  
    for i in range ( height ):
        if len ( cols[i]) > 1:
            if probe[i][0] == 2:
                for j in range ( cols[i][0] ):
                    probe[i][j] = 2
                if cols[i][0] + 1 < width:
                    probe[i][cols[i][0]] = 1
            if probe[i][ len(cols[i]) ] == 2:
                print(i)
                for j in range ( width - cols[i][ len (cols[i]) -1] -1 , width ):
                    probe[i][j] = 2
                if width - cols[i][ len (cols[i]) -1] -2 > 0:
                    probe[i][width - cols[i][ len (cols[i]) -1] -2] = 1
    for i in range ( width ):
        if len (rows[0]) > 0:
            if probe[0][i] == 2:
                for j in range ( rows[i][0] ):
                    probe[j][i] = 2
                if rows[i][0] + 1 < height:
                    probe[rows[i][0] + 1][i] = 1
            if probe[ len(rows[i]) - 1 ][i] == 2:
                for j in range ( height - rows[i][ len (rows[i]) -1] -1 , height ):
                    probe[j][i] = 2
                if height - rows[i][ len (rows[i]) -1] -2 > 0:
                    probe[height - rows[i][ len (rows[i]) -1] -1][i] = 1