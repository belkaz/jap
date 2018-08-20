import FullLines
import SumLines
import time

#     1 5 1 1 5
#   4 
# 1 1 
# 1 1
# 1 1
# 2 1 

##cols - rows
#########################################
width  = 5
heigth = 5

rows    = [[1],[5],[1], [4], [1,3]]
cols = [[1,1],
      [2,1],
      [1,1],
      [1,1],
      [3,1]
      ]
#########################################
field = []

for i in range (0 , width):
    field.append([])
    for j in range (0 , heigth):
        field[i].append('?')

while True:       
    for i in range(width):    
        print(field[i])  
    time.sleep(3) 
    print("")    
