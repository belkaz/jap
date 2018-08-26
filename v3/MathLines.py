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
#    [3] @ ?                  @@@
#    [2] @ ?              =>  @@-  
#    [1] @ ?                  @-    
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
# [2] by [? - ? ? ?] => [- - ? ? ?]
# !!! частные случаи когда по одному - в строке
def Math1_H( height, width, cols, probe ):
    for i in range( height ):
        q0 = 0
        for j in range ( width ):
            if probe[i][j] == -1:
                if cols[i][0] > j :
                    for k in range (q0, j):
                        probe[i][k] = -1
                    q0 += j
                if cols[i][ len(cols[i]) -1] > width - j:
                    for k in range (j, width):
                        probe[i][k] = -1
def Math1_М( height, width, rows, probe ):
    for i in range( width ):
        q0 = 0
        for j in range ( height ):
            if probe[j][i] == -1:
                if rows[i][0] > j :
                    for k in range (q0, j):
                        probe[k][i] = -1
                    q0 += j
                if rows[i][ len(rows[i]) -1] > height - j:
                    for k in range (j, height):
                        probe[k][i] = -1
# [4] by [- @ @ @ ?] -> [- @ @ @ @]
#
def FullLine_H(height, width, cols, probe):    
    for i  in range( height ):
        negArr = []
        for j in range ( width ):
            if probe[i][j] == -1:
                negArr.append(j)
        if width - len ( negArr ) == cols[i][0] :
            for j in range ( width ):   
                if not ( j in negArr ):         
                    probe[i][j] = 200 
def FullLine_V(height, width, rows, probe):    
    for i  in range( width ):
        negArr = []
        for j in range ( height ):
            if probe[j][i] == -1:
                negArr.append(j)
        if height - len ( negArr ) == rows[i][0] :
            for j in range ( height ):   
                if not ( j in negArr ):         
                    probe[j][i] = 200  
#[2] by [? ? @ -] ->[- @ @ -]
#Reborder
def Reborder_H(height, width, cols, probe):
    for i in range( height ):       
        for j in range ( width ):
            if probe[i][j] == 200:
                t = j
                #####
                isPrevNegative = True
                for k in range (0, t):
                    if probe[i][k] != -1:
                        isPrevNegative = False
                if isPrevNegative:
                    for k in range(t, t + cols[i][0] - 1 ):
                        probe[i][k] = 200
                    probe[i][t + cols[i][0] ] = -1
                #####
                isNextNegative = True
                for k in range(t+1, width):
                    if probe[i][k] != -1:
                        isNextNegative = False
                if isNextNegative:
                    for k in range( t - cols[i][ len(cols[i]) -1 ], t + 1):
                        probe[i][k] = 200
                    probe[i][t - cols[i][ len(cols[i]) -1]] = -1

def Reborder_V(width, height, rows, probe):
    for i in range( height ):
        for j in range ( width ):
            if probe[j][i] == 200:
                t = j
                #####
                isPrevNegative = True
                for k in range (0, t):
                    if probe[k][i] != -1:
                        isPrevNegative = False
                if isPrevNegative:
                    for k in range(t+1, t + rows[i][0] - 1 ):
                        probe[k][i] = 200
                    probe[t + rows[i][0] ][i] = -1
                #####
                isNextNegative = True
                for k in range(t+1, width):
                    if probe[k][i] != -1:
                        isNextNegative = False
                if isNextNegative:
                    for k in range( t - rows[i][ len(rows[i]) -1 ], t + 1):
                        probe[k][i] = 200
                    probe[t - rows[i][ len(rows[i]) -1]][i] = -1
  
def Reb3_H ( height, width, cols, probe):
    for i in range( height ):
        for j in range (width ):
            if probe[i][j] == -1:
                isNeg = True
                for k in range (0, j):
                    if probe[i][k] != -1:
                        isNeg = False
                if isNeg :
                    for k in range (j, j + cols[i][0]):
                        probe[i][k] = 200
                    probe[i][ j + cols[i][0] ] = -1
                # isNeg = True
                # for k in range (j + 1 , width):
                #     if probe[i][k] != -1:
                #         isNeg = False
                # if isNeg :
                #     for k in range (j - cols[i][ len (cols[i]) -1], j ):
                #         probe[i][k] = 200
                #     probe[i][j - cols[i][ len (cols[i]) -1] -1 ] = -1
#[3] by [? ? ? @ ?] -> [? ? @ @ ?]
                
