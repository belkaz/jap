import time

import FullLines
import MathLines
##cols - rows
# 19890
#########################################
width  = 15
height = 15

rows    = [[3],[3],[4,2],[1,8,1],[2,12],[6,4],[2,3,3],[2,1,4,4],[2,3,2,1],[10,2],[9,4],[1,3,4,2,1],[2,3,2],[8],[3]]
cols =[
      [3,3],
      [7],
      [8],
      [2,5],
      [3,1,3,1],
      [4,2,1],
      [3,9],
      [3,9],
      [1,3,9],
      [2,3,1,1,1,1],
      [7,2],
      [12],
      [8],
      [1,1,1],
      [2,2,2]
      ]

# rows = [[4], [2], [3], [3], [1]]
# cols = [[2], 
#         [2,1], 
#         [4], 
#         [1,1], 
#         [1,1]]
#########################################
probe = []
field = []

for i in range (0 , width):
    probe.append([])
    field.append([])
    for j in range (0 , height):
        probe[i].append(0)
        field[i].append(" ")

for i in range(width):
    print(' '.join(field[i]))  
FullLines.FullLineH(height, width, cols, probe)
FullLines.FullLineV(height, width, rows, probe)
FullLines.EmptyH(height, width, cols, probe)
FullLines.EmptyV(height, width, rows, probe)
FullLines.SumLineV(height, width, cols, probe)
FullLines.SumLineH(height, width, rows, probe)
FullLines.Towards_H (height, width, cols, probe)
FullLines.Towards_V(height, width, rows, probe)

while True: 
    time.sleep(3)
    MathLines.Math0_H (height, width, cols, probe)
    MathLines.Math0_V (height, width, rows, probe)
    MathLines.Border_H (height, width, cols, probe)
    MathLines.Border_V (height, width, rows, probe)
    MathLines.Math1_H( height, width, cols, probe )
    MathLines.Math1_М( height, width, rows, probe )
    MathLines.FullLine_H(height, width, cols, probe)
    MathLines.FullLine_V(height, width, rows, probe)
    MathLines.Reborder_H(height, width, cols, probe)
    MathLines.Reborder_V(height, width, rows, probe)
    for i in range(width):           
        for j in range (height):
            if probe[i][j] == 200:
                field[i][j] = "@"                
            elif probe[i][j] == -1:
                field[i][j] = "-"
    print('0 1 2 3 4 5 6 7 8 9 0 1 2 3 4')
    for i in range(width):        
       print(' '.join(field[i]))  
    print("-------------------------------------------")    
