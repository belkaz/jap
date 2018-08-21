import time

import FullLines #заполняет столбцы и строки, полностью закрашиваемые (5 из 5 ->[11111])
import SumLines # заполняет строки и столбы в случае суммарного заполнения ([2,2] из 5 ->[11-11])
import AllInLine #заполняеи столбцы и строки в случае полного заполнения указанного диапазона ([1,1] - > [?1??1] -> [-1--1])

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
AllInLine.AllInLine(width, height, cols, rows, probe)

while True:       
    for i in range(width):    
        print(probe[i])  
    time.sleep(3) 
    print("")    
