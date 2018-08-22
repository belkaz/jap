import time

import FullLines #check full lines, empty lines, lines full without empty
import SumLines #check summs
import Borders #check border elements, 
import Towards 
##cols - rows
# 8753
#########################################
width  = 5
height = 5

rows    = [[1,1],[2,2],[3,1], [2,2], [1,1]]
cols =[[5],
      [3],
      [1],
      [1,1],
      [5]
      ]
#########################################
probe = []
field = []

for i in range (0 , width):
    probe.append([])
    field.append([])
    for j in range (0 , height):
        probe[i].append(0)
        field[i].append(" ")

FullLines.FullLine(width, height, cols, rows, probe)
SumLines.SumLines(width, height, rows, cols, probe)
Borders.Borders(width, height, cols, rows, probe) #!!!!!!!!!!!!!!
Towards.Towards(width, height, cols, rows, probe)
while True: 
    FullLines.FullLine(width, height, cols, rows, probe)
    SumLines.SumLines(width, height, rows, cols, probe)
    Borders.Borders(width, height, cols, rows, probe) #!!!!!!!!!!!!!!!!!!!

    for i in range(width):   
        
        for j in range (height):
            if probe[i][j] == 200:
                field[i][j] = "X"                
            elif probe[i][j] == -1:
                field[i][j] = "-"
    for i in range(width):
       print(''.join(field[i]))  
    time.sleep(3) 
    print("")    
