import time

import FullLines #заполняет столбцы и строки, полностью закрашиваемые (5 из 5 ->[11111])
import SumLines # заполняет строки и столбы в случае суммарного заполнения ([2,2] из 5 ->[11-11])
import AllInLine #заполняеи столбцы и строки в случае полного заполнения указанного диапазона ([1,1] - > [?1??1] -> [-1--1])
import SetMathProbes #выщитываем мат вероятность заполнения
import BorderElements #заполнение боковых элементов
#  6542

##cols - rows
#########################################
width  = 5
height = 5

rows    = [[2],[3],[1], [5], [2]]
cols =[[2],
      [1,2],
      [4],
      [1,1],
      [1,1]
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
AllInLine.AllInLine(width, height, cols, rows, probe)
BorderElements.BorderElements(width, height, cols, rows, probe)


while True:      
 
    for i in range(width):    
        for j in range (height):
            if probe[i][j] == 200:
                field[i][j] = "X"
            elif probe[i][j] == -1:
                field[i][j] = "-"
    for i in range(width):
        print(field[i])  
    time.sleep(3) 
    print("")    
