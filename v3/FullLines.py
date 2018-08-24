# 5 by [? ? ? ? ?] -> [@ @ @ @ @]
def FullLineH(height, width, cols, probe):    
    for i  in range( height ):
      if ( len (cols[i]) == 1) and ( cols[i][0] == width):
          for j in range ( width ):
              probe[i][j] = 200
def FullLineV(height, width, rows, probe):    
    for i  in range( width ):
      if ( len (rows[i]) == 1) and ( rows[i][0] == height):
          for j in range ( height ):
              probe[j][i] = 200     
##################################################################
# 0 by [? ? ? ? ?] -> [- - - - -]
def EmptyH(height, width, cols, probe):
    for i in range ( height ):
        if (len( cols[i] ) ==0 ) or ( len(cols[i]) == 1 and cols[i][0] == 0 ):
            for j in range ( width ):
                probe[i][j] = -1

def EmptyV(height, width, rows, probe):
    for i in range ( width ):
        if (len( rows[i] ) ==0 ) or ( len(rows[i]) == 1 and rows[i][0] == 0 ):
            for j in range ( height ):
                probe[j][i] = -1
###################################################################
# [1,3] ->                -> [@ - @ @ @]
# [2,2] -> by [? ? ? ? ?] -> [@ @ - @ @]
# [3,1] ->                -> [@ @ @ - @]
def SumLineV (height, width, cols, probe):
    for i in range( height ):
        if ( len (cols[i]) > 1):
            if ( sum(cols[i]) + len(cols[i]) -1 == width ):
                lastIndex = 0
                for j in range ( len( cols[i]) ):
                    for k in range ( lastIndex , lastIndex + cols[i][j] ):
                        probe[i][k] = 200
                        lastIndex += 1
                    if ( lastIndex +1 < width ):
                        probe[i][lastIndex] = -1
                        lastIndex +=1

def SumLineH (height, width, rows, probe):
    for i in range( width ):
        if ( len (rows[i]) > 1):
            if ( sum(rows[i]) + len(rows[i]) -1 == height ):
                lastIndex = 0
                for j in range ( len( rows[i]) ):
                    for k in range ( lastIndex , lastIndex + rows[i][j] ):
                        probe[k][i] = 200
                        lastIndex += 1
                    if ( lastIndex +1 < height ):
                        probe[lastIndex][i] = -1
                        lastIndex +=1                   
 