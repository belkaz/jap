def SumLines(width, height, rows, cols, probe):
    for i in range(height):
        if (len(cols[i]) > 1):
            if (sum(cols[i]) + len(cols[i]) - 1 == width):
                lastInd = 0
                for j in range(len(cols[i])):
                    for k in range(lastInd, lastInd + cols[i][j]):
                        probe[i][k] = 100 
                    if (lastInd + cols[i][j] < width): 
                        lastInd += cols[i][j]
                        probe[i][lastInd] = -1                     
                        lastInd += 1                                        
    for i in range(width):
        if (len(rows[i]) > 1):
            if (sum(rows[i]) + len(rows[i]) -1 == height):
                lastInd = 0
                for j in range(len(rows[i])):
                    for k in range(lastInd, lastInd + rows[i][j]):
                        probe[k][i] = 100 
                    if (lastInd + rows[i][j] < height): 
                        lastInd += rows[i][j]
                        probe[lastInd][i] = -1                     
                        lastInd += 1             
                