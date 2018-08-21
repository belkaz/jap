_width = 5

col = [3]

probe = [-1,0,0,0,-1]

for i in range(_width):
    if (len(col) == 1):
        negCount = probe.count(-1)        
        zeroArr = []
        if (sum(col) == _width - negCount):
           for j in range(_width):
               if not (probe[j] == -1):
                   probe[j] = 200
        
            
            

print(probe)
