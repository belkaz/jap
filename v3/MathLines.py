# [1,1] by [@ ? ? ? @] -> [@ - - - @]
# проверка на случай, если все необходимые эмлементы уже
# установлены на поле
def Math0_H (height, width, cols, probe):
    for i in range ( height ):
        curArr = []
        unkArr = []
        for j in range ( width ):
            curArr.append(0)
        curInd = 0
        for j in range (width ):
            if probe[i][j] == 200:
                curArr[curInd] += 1
            else :
                curInd +=1
            if probe[i][j] != 200 and probe[i][j] != -1 :
                unkArr.append( j )
        curArr = [x for x in curArr if x > 0] #генератор списка
        if curArr == cols[i] :
            for j in unkArr:
                probe[i][j] = -1
def Math0_V (height, width, rows, probe):
    for i in range ( width ):
        curArr = []
        unkArr = []
        for j in range ( height ):
            curArr.append(0)
        curInd = 0
        for j in range ( height ):
            if probe[j][i] == 200:
                curArr[curInd] += 1
            else :
                curInd +=1
            if probe[j][i] != 200 and probe[j][i] != -1 :
                unkArr.append( j )
        curArr = [x for x in curArr if x > 0] #генератор списка
        if curArr == rows[i] :
            for j in unkArr:
                probe[j][i] = -1    
# [
#       [3], [2], [1]] 
#    [3] ? ?                  @@@
#    [2] ? ?              =>  @@-  
#    [1] ? ?                  @-
    
def Border_H (height, width, cols, probe):
    for i in range ( height ):
        if probe[i][0] == 200:
            for j in range(cols[i][0]):
                probe[i][j] = 200
            if cols[i][0] < width:
                probe[i][ cols[i][0] ] = -1
        if probe[i][ width - 1 ] == 200:
            for j in range( width - cols[i][ len(cols[i]) -1], width ):
                probe[i][j] = 200
            if cols[i][len(cols[i]) - 1] < width:
                probe[i][width - cols[i][ len(cols[i]) - 1] -1] = -1


def Border_V (height, width, rows, probe):
    for i in range ( width ):
        if probe[0][i] == 200:
            for j in range( rows[i][0] ):
                probe[j][i] = 200
        probe [ rows[i][0] ][i] = -1
        if probe[ width - 1 ] [i] == 200:
            for j in range( height - rows[i][ len(rows[i]) -1], height ):
                probe[j][i] = 200
            if rows[i][len(rows[i]) - 1] < height:
                probe[width - rows[i][ len(rows[i]) - 1] -1][i] = -1