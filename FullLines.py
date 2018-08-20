def FullLine(width, height, cols, rows, probe):
    for i in range(height):
        if (len(cols[i]) == 1):
            if (cols[i][0] == width):
                for j in range (width):
                    probe[i][j] = 100
    for i in range(width):
        if (len(rows[i]) == 1):
            if (rows[i][0] == height):
                for j in range (height):
                    probe[j][i] = 100