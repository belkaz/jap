import Empty
import Full
import Sum
import Towards
import Border
import IsAllSet
import CouldntSet
# rows    = [[3],[3],[4,2],[1,8,1],[2,12],[6,4],[2,3,3],[2,1,4,4],[2,3,2,1],[10,2],[9,4],[1,3,4,2,1],[2,3,2],[8],[3]]
# cols =[
#       [3,3],
#       [7],
#       [8],
#       [2,5],
#       [3,1,3,1],
#       [4,2,1],
#       [3,9],
#       [3,9],
#       [1,3,9],
#       [2,3,1,1,1,1],
#       [7,2],
#       [12],
#       [8],
#       [1,1,1],
#       [2,2,2]
#       ]

rows =      [[4], [2], [3], [3], [1]]
cols = [[2], 
        [2,1], 
        [4], 
        [1,1], 
        [1,1]]

width = len ( rows )
height = len ( cols )

probe = []
for i in range ( height ):
    probe.append ( [] )
    for j in range ( width ):
        probe[i].append( 0 )
############################################
Empty.Empty(height, width, cols, rows,  probe)
############################################
Full.Full ( height, width, cols, rows,  probe )
Sum.Sum ( height, width, cols, rows,  probe )
Towards.Towards (height, width, cols, rows,  probe)
Border.Border ( height, width, cols, rows,  probe )
IsAllSet.IsSetAll ( height, width, cols, rows,  probe )
CouldntSet.CouldntSet ( height, width, cols, rows,  probe )
############################################
for i in range ( height ):
    print ( ' '.join( map (str, probe[i]) ) )
