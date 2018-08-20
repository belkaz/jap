import time

import FullLines
import SumLines
#     1 5 1 1 5
#   4 
# 1 1 
# 1 1
# 1 1
# 2 1 

##cols - rows
#########################################
width  = 5
height = 5

rows    = [[1],[5],[1], [1], [5]]
cols =[[4],
      [1,1],
      [1,1],
      [1,1],
      [2,1]
      ]
#########################################
probe = []

for i in range (0 , width):
    probe.append([])
    for j in range (0 , height):
        probe[i].append(0)

FullLines.FullLine(width, height, cols, rows, probe)
SumLines.SumLines(width, height, rows, cols, probe)

while True:       
    for i in range(width):    
        print(probe[i])  
    time.sleep(3) 
    print("")    
