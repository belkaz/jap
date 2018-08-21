def FullLine(width, height, cols, rows, probe):    
    for i in range(height):
        if (len(cols[i]) == 1):       
            negCount = probe[i].count(-1)        
            zeroArr = []
            if (sum(cols[i]) == width - negCount):
                for j in range(width):
                    if not (probe[i][j] == -1):
                        probe[i][j] = 200
            if (probe[i].count(200) == 1):
                for j in range( width ):
                    if not( j == probe[i].index(200)):
                        probe[i][j] = -1

    for i in range(width):
        if (len(rows[i]) == 1):
            arr = []
            for j in range(height):
                arr.append(probe[j][i])          
            negCount = arr.count(-1)        
            zeroArr = []
            if (sum(rows[i]) == height - negCount):
                for j in range(height):
                    if not (arr[j] == -1):
                        probe[j][i] = 200
            if (arr.count(200) == 1):
                for j in range( height ):
                    if not( j == arr.index(200)):
                        probe[j][i] = -1