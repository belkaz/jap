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
                
# [2,1] by []