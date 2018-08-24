import time

import FullLines
import MathLines
##cols - rows
# 8753
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

# rows = [[1,1], [2,2], [3,1], [2,2], [1,1]]
# cols = [[5], 
#         [3], 
#         [1], 
#         [1,1], 
#         [5]]
#########################################
probe = []
field = []

for i in range (0 , width):
    probe.append([])
    field.append([])
    for j in range (0 , height):
        probe[i].append(0)
        field[i].append(" ")

FullLines.FullLineH(height, width, cols, probe)
FullLines.FullLineV(height, width, rows, probe)
FullLines.EmptyH(height, width, cols, probe)
FullLines.EmptyV(height, width, rows, probe)
FullLines.SumLineV(height, width, cols, probe)
FullLines.SumLineH(height, width, rows, probe)

while True: 
    MathLines.Math0_H (height, width, cols, probe)
    MathLines.Math0_V (height, width, rows, probe)
    for i in range(width):           
        for j in range (height):
            if probe[i][j] == 200:
                field[i][j] = "@"                
            elif probe[i][j] == -1:
                field[i][j] = "-"
    for i in range(width):
       print(' '.join(field[i]))  
    time.sleep(3) 
    print("")    
